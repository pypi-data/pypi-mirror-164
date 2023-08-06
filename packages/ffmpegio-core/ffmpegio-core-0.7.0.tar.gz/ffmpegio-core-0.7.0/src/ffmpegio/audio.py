"""Audio Read/Write Module
"""

from . import ffmpegprocess, utils, configure, FFmpegError, probe, plugins, analyze
from .utils import filter as filter_utils, log as log_utils
import logging

__all__ = ["create", "read", "write", "filter", "detect"]


def _run_read(
    *args, sample_fmt_in=None, ac_in=None, ar_in=None, show_log=None, **kwargs
):
    """run FFmpeg and retrieve audio stream data
    :param *args ffmpegprocess.run arguments
    :type *args: tuple
    :param sample_fmt_in: input sample format if known but not specified in the ffmpeg arg dict, defaults to None
    :type sample_fmt_in: str, optional
    :param ac_in: number of input channels if known but not specified in the ffmpeg arg dict, defaults to None
    :type ac_in: int, optional
    :param ar_in: input sampling rate if known but not specified in the ffmpeg arg dict, defaults to None
    :type ar_in: int, optional
    :param show_log: True to show FFmpeg log messages on the console,
                     defaults to None (no show/capture)
                     Ignored if stream format must be retrieved automatically.
    :type show_log: bool, optional
    :param **kwargs ffmpegprocess.run keyword arguments
    :type **kwargs: tuple
    :return: [description]
    :rtype: [type]
    """
    """

    :param show_log: True to show FFmpeg log messages on the console, 
                     defaults to None (no show/capture)
                     Ignored if stream format must be retrieved automatically.
    :type show_log: bool, optional
    :rtype: (int, str)
    """

    dtype, ac, rate = configure.finalize_audio_read_opts(
        args[0], sample_fmt_in, ac_in, ar_in
    )

    if dtype is None or ac is None or rate is None:
        configure.clear_loglevel(args[0])

        out = ffmpegprocess.run(*args, capture_log=True, **kwargs)
        if show_log:
            print(out.stderr)
        if out.returncode:
            raise FFmpegError(out.stderr)

        info = log_utils.extract_output_stream(out.stderr)

        ac = info.get("ac", None)
        rate = info.get("ar", None)
    else:
        out = ffmpegprocess.run(
            *args,
            capture_log=None if show_log else True,
            **kwargs,
        )
        if out.returncode:
            raise FFmpegError(out.stderr, show_log)

    return rate, plugins.get_hook().bytes_to_audio(
        b=out.stdout, dtype=dtype, shape=(ac,), squeeze=False
    )


def create(
    expr,
    *args,
    progress=None,
    show_log=None,
    t_in=None,
    ar=None,
    ac=None,
    sample_fmt=None,
    af=None,
    **kwargs,
):
    """Create audio data using an audio source filter

    :param expr: name of the source filter or full filter expression
    :type expr: str
    :param \\*args: filter arguments
    :type \\*args: tuple, optional
    :param progress: progress callback function, defaults to None
    :type progress: callable object, optional
    :param show_log: True to show FFmpeg log messages on the console,
                     defaults to None (no show/capture)
                     Ignored if stream format must be retrieved automatically.
    :type show_log: bool, optional
    :param t_in: duration of the video in seconds, defaults to None
    :type t_in: float, optional
    :param ar: sampling rate in samples/second, defaults to None
    :type ar: int, optional
    :param ac: number of channels, defaults to None
    :type ac: int, optional
    :param sample_fmt: sample format, defaults to None
    :type sample_fmt: str, optional
    :param af: additional filter, defaults to None
    :type af: FilterGraph or str, optional
    :param \\**options: FFmpeg options (see :doc:`options`)
    :type \\**options: dict, optional
    :return: sampling rate and audio data
    :rtype: tuple[int, object]

    .. note:: Either `duration` or `nb_samples` filter options must be set.

    See https://ffmpeg.org/ffmpeg-filters.html#Audio-Sources for available video source filters

    ouptut data object is determined by the selected `bytes_to_audio` hook

    """

    url, (ar_in, ac_in) = filter_utils.compose_source("audio", expr, *args, **kwargs)

    if sample_fmt is None:
        sample_fmt = "dbl"

    # need_t = ("mandelbrot", "life")
    # if t_in is None and any((expr.startswith(f) for f in need_t)):
    #     raise ValueError(f"Some sources {need_t} must have t_in specified")

    ffmpeg_args = configure.empty()
    inopts = configure.add_url(ffmpeg_args, "input", url, {"f": "lavfi"})[1][1]
    outopts = configure.add_url(ffmpeg_args, "output", "-", {})[1][1]

    if t_in:
        inopts["t"] = t_in

    for k, v in zip(
        ("ar", "ac", "sample_fmt", "filter:a"),
        (ar or ar_in, ac or ac_in, sample_fmt, af),
    ):
        if v is not None:
            outopts[k] = v

    return _run_read(
        ffmpeg_args,
        sample_fmt_in=sample_fmt,
        ac_in=ac_in,
        ar_in=ar_in,
        show_log=show_log,
        progress=progress,
    )


def read(url, progress=None, show_log=None, **options):
    """Read audio samples.

    :param url: URL of the audio file to read.
    :type url: str
    :param progress: progress callback function, defaults to None
    :type progress: callable object, optional
    :param show_log: True to show FFmpeg log messages on the console,
                     defaults to None (no show/capture)
                     Ignored if stream format must be retrieved automatically.
    :type show_log: bool, optional
    :param \\**options: FFmpeg options, append '_in' for input option names (see :doc:`options`)
    :type \\**options: dict, optional
    :return: sample rate in samples/second and audio data object specified by `bytes_to_audio` plugin hook
    :rtype: tuple(float, object)

    .. note:: Even if :code:`start_time` option is set, all the prior samples will be read.
        The retrieved data will be truncated before returning it to the caller.
        This is to ensure the timing accuracy. As such, do not use this function
        to perform block-wise processing. Instead use the streaming solution,
        see :py:func:`open`.


    """

    sample_fmt = options.get("sample_fmt", None)
    ac_in = ar_in = None
    if sample_fmt is None:
        try:
            # use the same format as the input
            info = probe.audio_streams_basic(url, 0)[0]
            sample_fmt = info["sample_fmt"]
            ac_in = info.get("ac", None)
            ar_in = info.get("ar", None)
        except:
            sample_fmt = "s16"

    input_options = utils.pop_extra_options(options, "_in")
    url, stdin, input = configure.check_url(
        url, False, format=input_options.get("f", None)
    )

    ffmpeg_args = configure.empty()
    configure.add_url(ffmpeg_args, "input", url, input_options)[1][1]
    configure.add_url(ffmpeg_args, "output", "-", options)[1][1]

    return _run_read(
        ffmpeg_args,
        stdin=stdin,
        input=input,
        sample_fmt_in=sample_fmt,
        ac_in=ac_in,
        ar_in=ar_in,
        progress=progress,
        show_log=show_log,
    )


def write(
    url,
    rate_in,
    data,
    progress=None,
    overwrite=None,
    show_log=None,
    extra_inputs=None,
    **options,
):
    """Write a NumPy array to an audio file.

    :param url: URL of the audio file to write.
    :type url: str
    :param rate_in: The sample rate in samples/second.
    :type rate_in: int
    :param data: input audio data object, converted to bytes by `audio_bytes` plugin hook .
    :type data: object
    :param progress: progress callback function, defaults to None
    :type progress: callable object, optional
    :param overwrite: True to overwrite if output url exists, defaults to None
                      (auto-select)
    :type overwrite: bool, optional
    :param show_log: True to show FFmpeg log messages on the console,
                     defaults to None (no show/capture)
    :type show_log: bool, optional
    :param extra_inputs: list of additional input sources, defaults to None. Each source may be url
                         string or a pair of a url string and an option dict.
    :type extra_inputs: seq(str|(str,dict))
    :param \\**options: FFmpeg options, append '_in' for input option names (see :doc:`options`)
    :type \\**options: dict, optional
    """

    url, stdout, _ = configure.check_url(url, True)
    input_options = utils.pop_extra_options(options, "_in")

    ffmpeg_args = configure.empty()
    configure.add_url(
        ffmpeg_args,
        "input",
        *configure.array_to_audio_input(rate_in, data=data, **input_options),
    )

    # add extra input arguments if given
    if extra_inputs is not None:
        for input in extra_inputs:
            if isinstance(input, str):
                configure.add_url(ffmpeg_args, "input", input)
            else:
                configure.add_url(ffmpeg_args, "input", *input)

    configure.add_url(ffmpeg_args, "output", url, options)

    out = ffmpegprocess.run(
        ffmpeg_args,
        input=plugins.get_hook().audio_bytes(obj=data),
        stdout=stdout,
        progress=progress,
        overwrite=overwrite,
        capture_log=None if show_log else True,
    )
    if out.returncode:
        raise FFmpegError(out.stderr, show_log)


def filter(expr, input_rate, input, progress=None, sample_fmt=None, **options):
    """Filter audio samples.

    :param expr: SISO filter graph.
    :type expr: str
    :param input_rate: Input sample rate in samples/second
    :type input_rate: int
    :param input: input audio data, accessed by `audio_info()` and `audio_bytes()` plugin hooks.
    :type input: object
    :param progress: progress callback function, defaults to None
    :type progress: callable object, optional
    :param \\**options: FFmpeg options, append '_in' for input option names (see :doc:`options`)
    :type \\**options: dict, optional
    :return: output sampling rate and audio data object, created by `bytes_to_audio` plugin hook
    :rtype: tuple(int, object)

    """

    input_options = utils.pop_extra_options(options, "_in")

    ffmpeg_args = configure.empty()
    configure.add_url(
        ffmpeg_args,
        "input",
        *configure.array_to_audio_input(input_rate, data=input, **input_options),
    )
    outopts = configure.add_url(ffmpeg_args, "output", "-", options)[1][1]
    outopts["sample_fmt"] = sample_fmt
    outopts["filter:a"] = expr

    return _run_read(
        ffmpeg_args,
        input=plugins.get_hook().audio_bytes(obj=input),
        progress=progress,
    )


def detect(
    url,
    *features,
    ss=None,
    t=None,
    to=None,
    start_at_zero=False,
    time_units=None,
    progress=None,
    show_log=None,
    **options,
):
    """detect audio stream features

    :param url: audio file url
    :type url: str
    :param \*features: specify features to detect:

        ============  ================  =========================================================
        feature       FFmpeg filter     description
        ============  ================  =========================================================
        'silence'     `silencedetect`_  Detect silence in an audio stream
        ============  ================  =========================================================

        defaults to include all the features
    :type \*features: tuple, a subset of ('silence',), optional
    :param ss: start time to process, defaults to None
    :type ss: int, float, str, optional
    :param t: duration of data to process, defaults to None
    :type t: int, float, str, optional
    :param to: stop processing at this time (ignored if t is also specified), defaults to None
    :type to: int, float, str, optional
    :param start_at_zero: ignore start time, defaults to False
    :type start_at_zero: bool, optional
    :param time_units: units of detected time stamps (not for ss, t, or to), defaults to None ('seconds')
    :type time_units: 'seconds', 'frames', 'pts', optional
    :param progress: progress callback function, defaults to None
    :type progress: callable object, optional
    :param show_log: True to show FFmpeg log messages on the console,
                     defaults to None (no show/capture)
    :type show_log: bool, optional
    :param \**options: FFmpeg detector filter options. For a single-feature call, the FFmpeg filter options
        of the specified feature can be specified directly as keyword arguments. For a multiple-feature call,
        options for each individual FFmpeg filter can be specified with <feature>_options dict keyword argument.
        Any other arguments are treated as a common option to all FFmpeg filters. For the available options
        for each filter, follow the link on the feature table above to the FFmpeg documentation.
    :type \**options: dict, optional
    :return: detection outcomes. A namedtuple is returned for each feature in the order specified.
        All namedtuple fields contain a list with the element specified as below:

        .. list-table::
           :header-rows: 1
           :widths: auto

           * - feature
             - named tuple field
             - element type
             - description
           * - 'silence'
             - 'interval'
             - (numeric, numeric)
             - (only if mono=False) Silent interval
           * - 
             - 'chX'
             - (numeric, numeric)
             - (only if mono=True) Silent interval of channel X (multiple)

    :rtype: tuple of namedtuples

    Examples
    --------

    .. code-block::python

        ffmpegio.audio.detect('audio.mp3', 'silence')

    .. _silencedetect: https://ffmpeg.org/ffmpeg-filters.html#silencedetect

    """

    all_detectors = {
        "silence": analyze.SilenceDetect,
    }

    if not len(features):
        features = [*all_detectors.keys()]

    # pop detector-specific options
    det_options = [options.pop(f"{k}_options", None) for k in features]

    # create loggers
    try:
        loggers = [all_detectors[k](**options) for k in features]
    except:
        raise ValueError(f"Unknown feature(s) specified: {features}")

    # add detector-specific options
    for l, o in zip(loggers, det_options):
        if o is not None:
            l.options.update(**o)

    # exclude unspecified input options
    input_opts = {k: v for k, v in zip(("ss", "t", "to"), (ss, t, to)) if v is not None}

    # run analysis
    analyze.run(
        url,
        *loggers,
        start_at_zero=start_at_zero,
        time_units=time_units,
        progress=progress,
        show_log=show_log,
        **input_opts,
    )

    return tuple((l.output for l in loggers))

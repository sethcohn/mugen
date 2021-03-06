### Globals ###
debug = False
music_video_name = None
music_video_dimensions = None
music_video_crf = '18'
allow_repeats = False

### GENERAL ###
VERSION = "1.0"
HELP = " Please review supported inputs and values on the help menu via --help"

FILE_TYPE_AUDIO = 'audio'
FILE_TYPE_VIDEO = 'video'
FILE_TYPE_SPEC = 'spec'

### VIDEO ###
WIDESCREEN_ASPECT_RATIO = 16/float(9)

MOVIEPY_FPS = 24
MOVIEPY_CODEC = 'libx264'
MOVIEPY_AUDIO_BITRATE = '320K'
ESSENTIA_BITRATE = 320

MIN_EXTREMA_RANGE = 30
DURATION_PRECISION = 17

RS_TYPE_REPEAT = 'repeat'
RS_TYPE_SCENE_CHANGE = 'scene_change'
RS_TYPE_TEXT_DETECTED = 'text_detected'
RS_TYPE_SOLID_COLOR = 'solid_color'

### TRACKS ###

AUDIO_TRACK_BEAT_LOCATIONS = 'beat_locations'
SUBS_TRACK_SEGMENT_NUMBERS = 'segment_numbers'
SUBS_TRACK_SEGMENT_DURATIONS = 'segment_durations'
SUBS_TRACK_SPEC = 'spec'

### PATHS ###
TEMP_PATH_BASE = 'temp/'
TEMP_MOVIEPY_AUDIOFILE = TEMP_PATH_BASE + 'moviepy_temp_audio.mp3'

OUTPUT_PATH_BASE = 'output/'
MUSIC_VIDEO_NAME_DEFAULT = 'music_video'
VIDEO_OUTPUT_EXTENSION = '.mkv'
SUBTITLES_EXTENSION = '.srt'
SPEC_EXTENSION = '.json'
ESSENTIA_ONSETS_AUDIO_EXTENSION = '.wav'

SEGMENTS_PATH_BASE = OUTPUT_PATH_BASE + 'segments/'
RS_PATH_BASE = OUTPUT_PATH_BASE + 'rejected_segments/'
RS_PATH_REPEAT = RS_PATH_BASE + RS_TYPE_REPEAT + '/'
RS_PATH_SCENE_CHANGE = RS_PATH_BASE + RS_TYPE_SCENE_CHANGE + '/'
RS_PATH_TEXT_DETECTED = RS_PATH_BASE + RS_TYPE_TEXT_DETECTED + '/'
RS_PATH_SOLID_COLOR = RS_PATH_BASE + RS_TYPE_SOLID_COLOR + '/'
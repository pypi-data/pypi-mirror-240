## IMPORTS
if 'Imports':

    if 'Standard Python Library':
        import os                           # local file operations, mainly os.path.join
        import platform                     # returns operating system information
        from pathlib import Path as Dir     # handles various local dir operations

######## GLOBAL VARIABLES #######################
if 'Global Variables':                                      # HIDE VARS
    OS_VERSION = platform.system()                          # OS VERSION
    USER_DIR = Dir.home()                                   # USER DIR
    APP_NAME = 'podRacer'                                   # APP NAME
    APP_DIR = os.path.join(USER_DIR, APP_NAME)              # APP DIR
    if OS_VERSION == 'Darwin':                              # MAC LIB
        LIB_DIR = os.path.join(USER_DIR, 'Library', APP_NAME)
    elif OS_VERSION == 'Windows':                           # WIN LIB
        LIB_DIR = os.path.join(USER_DIR, 'AppData', 'Roaming', APP_NAME)
    else:                                                   # LIN LIB
        LIB_DIR = os.path.join(APP_DIR, 'Data')
    PROFILE_DIR = os.path.join(LIB_DIR, 'profile')          # PROFILE DIR
    PROCESS_DIR = os.path.join(LIB_DIR, 'process')          # PROCESS DIR
###############################################

## LIBRARY INFO
info = dict(
    app_name = APP_NAME,
    os_version = OS_VERSION,
)

## DIRECTORIES
dirs = dict(
    user_dir = USER_DIR,
    app_dir = APP_DIR,
    lib_dir = LIB_DIR,
    process_dir = PROCESS_DIR
)

## PODCAST RSS FEED URL'S
podcast_links = dict(
    wyrbw = "https://feeds.megaphone.fm/PARA9654630519",
    radiolab = "https://www.wnycstudios.org/feeds/series/podcasts?premiumtier=vipers&include_owner=true&audio_suffix=%26delivery=premium&audio_only=true&limit=10000",
    stiff_socks = "https://www.patreon.com/rss/stiffsockspod?auth=3q3EX1Vu6AuS2YQQyc-laMU6NIKgkA--",
    mwmh = "https://www.patreon.com/rss/murderwithmyhusband?auth=jklhka0Qz-bMO3FBJIuNl8ryfo8cwPtg"
)
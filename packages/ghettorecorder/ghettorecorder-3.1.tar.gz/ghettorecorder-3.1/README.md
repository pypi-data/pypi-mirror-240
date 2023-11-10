# GhettoRecorder
Grab hundreds of radio stations simultaneously.

## Overview
This repository shows the source code of a multiprocessor capable recorder app.

A documented [example](https://github.com/44xtc44/eisenmp_examples) runs on my [eisenmp framework](https://github.com/44xtc44/eisenmp).

* Class implementation [__init__.py](https://github.com/44xtc44/GhettoRecorder/blob/dev/ghettorecorder/__init__.py) allows external modules (e.g. blacklist) to manipulate instances
* Blacklist module [ghetto_blacklist.py](https://github.com/44xtc44/GhettoRecorder/blob/dev/ghettorecorder/ghetto_blacklist.py) JSON records can be merged with my [EisenRadio](https://github.com/44xtc44/EisenRadio) DB dump
* Threaded HTTP server [__main__.py](https://github.com/44xtc44/GhettoRecorder/blob/dev/ghettorecorder/__main__.py) is switching the Backend and feeds the Frontend to run a show
* AAC files cut from stream are repaired on the fly with my [aacRepair](https://github.com/44xtc44/aacRepair)

<table>
  <tbody>
    <tr>
      <td>
        <img src="https://github.com/44xtc44/GhettoRecorder/raw/dev/.github/ghetto_cmd.PNG" alt="menu options on command line" style="width:460px"/> 
      </td>
    </tr>
    <tr>
      <td>
        <img src="https://github.com/44xtc44/GhettoRecorder/raw/dev/.github/ghetto_py_http.PNG" alt="custom python multithreading http server" style="width:460px"/>
      </td>
    </tr>
    <tr>
      <td>
        <img src="https://github.com/44xtc44/GhettoRecorder/raw/dev/.github/screenshot_mobile.png" alt="mobile Android" style="height:460px"/>
      </td>
    </tr>
    <tr>
      <td>
        <a href="https://github.com/44xtc44/Ghetto-Android">
            <img src="https://github.com/44xtc44/GhettoRecorder/raw/dev/.github/ghetto-android.png" alt="mobile Android" style="height:460px"/>
        </a>
      </td>
    </tr>
  </tbody>
</table>




## Import

    from ghettorecorder import GhettoRecorder

    ghetto_raid = GhettoRecorder(radio, url)  # use different URLs to test SSL
    ghetto_raid.com_in = mp.Queue(maxsize=1)  # eval exec communication
    ghetto_raid.com_out = mp.Queue(maxsize=1)  # response; exec ok is "None"
    ghetto_raid.audio_out = mp.Queue(maxsize=1)  # current HTTP response buffer
    ghetto_raid.start()  # wants a loop in main() to keep the show alive


## Snapcraft package

    $ sudo snap install ghettorecorder

<img src="https://github.com/44xtc44/GhettoRecorder/raw/dev/.github/ghetto_url_no_rotation.png" alt="ghetto desktop icon" style="width:46px"/> 


Desktop icon for the click addicted.

    $ ghettorecorder.url  # Ghetto HTTP threaded server
    $ ghettorecorder.cmd  # command line with menu

## Python package

    $ pip3 install ghettorecorder
 
    $ pip3 show ghettorecorder  # prep removal
    $ pip3 uninstall ghettorecorder  # del custom dirs of recorder in ... /python3.x/site-packages
 
    # command line
    $ ghetto_cmd  # Python executable 'beside' /python3.x/site-packages in /python3.x/Scripts
    $ python3 -m ghettorecorder.cmd
 
    # browser
    $ ghetto_url or
    $ python3 -m ghettorecorder


## Links

* PYPI: https://pypi.org/project/GhettoRecorder
* Snap: https://snapcraft.io/ghettorecorder
* GitHub: https://github.com/44xtc44/GhettoRecorder
* Issues to fix: https://github.com/44xtc44/GhettoRecorder/issues
* ReadTheDocs: https://ghettorecorder.readthedocs.io/ (see module index)

## Configuration File

'Settings.ini' is the config file for GhettoRecorder.
INI files consist of sections to divide different settings.::

    [STATIONS]
    anime_jp = http://streamingv2.shoutcast.com/japanimradio-tokyo

    [GLOBAL]
    blacklist_enable = True
    save_to_dir = f:\54321


[STATIONS] custom radio name and radio connection information (can be pls or m3u playlist)

[GLOBAL] blacklist status and the *custom* parent directory location

## Usage

### Main Menu

    menu 'Main'
    1 -- Record (local listen option)
    2 -- Change parent record path
    3 -- Enable/disable blacklists
    4 -- Set path to config, settings.ini
    5 -- aac file repair
    6 -- Exit


### Record Menu

    0 	>> aacchill             <<
    1 	>> 80ies_nl             <<
    2 	>> anime_jp             <<
    3 	>> blues_uk             <<
    4 	>> br24                 <<
    ...
    Enter to record -->:

    Write the leading Number (list index) into the input field . Hit 'Enter'.
    OR
    Write or copy/paste the radio name into the input field. Hit 'Enter'.
    Add as many radios as you like.
    Hit 'Enter' without input to start grabbing.
    Listen to the first selected radio via local streaming ``http://localhost:1242/``

### Change parent record path Menu

    option 'Change record parent path'
    1 -- New parent path for recorded radios. Write to config.
    2 -- Back to Main Menu
    Enter your choice: 1

        Write a new path to store files
    ..settings.ini [GLOBAL] section: {'blacklist_enable': 'True', 'save_to_dir': 'f:\\31'}
    Enter a new path, OS syntax (f:\10 or /home ) -->:

The default path is the directory of the module.
In most cases you want to store grabbed files somewhere else.

### Blacklist Menu

    Write a new blacklist option to settings.ini file
    ..settings.ini [GLOBAL] section: {'blacklist_enable': 'True', 'save_to_dir': 'f:\\31'}
    1 -- blacklist on (don't write title if already downloaded)
    2 -- blacklist off
    3 -- Back to Main Menu
    Enter your choice: 1

    	blacklist is ON: settings.ini file
    	Existing titles are not recorded again and again.
    file name is "blacklist.json" in the same folder as "settings.ini"
    ..settings.ini [GLOBAL] section: {'blacklist_enable': 'True', 'save_to_dir': 'f:\\31'}
    Hit Enter to leave -->:

    Blacklist writing can be switched on/off.
    Titles are listed for each of the radios and can be deleted to 'unlist' them.
    File name is ``blacklist.json`` and always in the same folder as 'settings.ini'.


### Set path to config

    Write Path to settings.ini and blacklist.json file
    Enter a new path, OS syntax (f:\10 or /home ) -->: F:\44
    	created: F:\44
    ..settings.ini [GLOBAL] section: {'blacklist_enable': 'True'}
    Hit Enter to leave -->:

    You can store your config file 'settings.ini' somewhere on the file system.
    Default place for grabbed files is the mentioned folder.
    If a custom save path is written to config, this path is used.


### aac file repair

    Write a path to aac files. Only aac files will be touched.
    ..settings.ini [GLOBAL] section: {'blacklist_enable': 'True', 'save_to_dir': 'f:\\31'}
    Enter a path, OS syntax (f:\10 or /home ) -->:f:\6aac
    	created: f:\6aac
    	f:\6aac\aac_repair created
    [ COPY(s) in f:\6aac\aac_repair ]
    ----- 1 file(s) failed -----
    f:\6aac\Sergey Sirotin & Golden Light Orchestra - Around The World.aacp
    ValueError non-hexadecimal number found in fromhex() arg at position 5438113
    ----- 97 file(s) repaired -----
    f:\6aac\111_Slovo_Original_Mix.aac; cut(bytes): [330]
    f:\6aac\351 Lake Shore Drive - You Make My Day.aacp; cut(bytes): [389]

    The repair option uses a folder name as input.
    Repaired files are stored in 'aac_repair' sub folder.
    Cut bytes count is shown at the end of the line.
    Repair can fail if the file is corrupted not only at start or end.

### GhettoRecorder Class

Communicate with the instance

       ========= ================= =========================================================
       port      action            description
       ========= ================= =========================================================
       com_in    commands input    tuple (radio, [str 'eval' or 'exec'], str 'command')
       com_out   status, err msg   (radio, [str 'eval' or 'exec'], response)
       audio_out copy of html resp a local HTTP server can loop through to a browser or app
       ========= ================= =========================================================

Feature attributes to switch on/off

       ========================== ==================================================================================
       attribute                  description
       ========================== ==================================================================================
       runs_meta                  periodic metadata call to create path for named rec out; False: unnamed rec file
       runs_record                disables writing to recorder file at all
       recorder_file_write        allow dump 'current' recorder file; need 'runs_meta'; makes rec blacklist possible
       runs_listen                disable write to audio_out queue; 3rd party can write into queue; listen blacklist
       ========================== ==================================================================================

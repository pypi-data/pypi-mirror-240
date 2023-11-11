from .deezer.deezer import *
from .soundcloud.soundcloud import *
from .youtube.youtube import *
from .youtube.ytm import *

import logging, shutil, os, atexit
from sys import exit
__name__ == 'music-helper'
__version__ = '2.0.0'


class DummyClass:    
    def __getattr__(self, name):
        def dummy_method(*args, **kwargs):
            raise ValueError('This provider has not been configured.')
        return dummy_method


class MusicHelper(object):
    def __init__(self, deezer_arl:str=None,sc_data:tuple=None, ytm_oauth:str="", debug:bool=False, ffmpeg_path:str="./") -> None:
        atexit.register(self.save)
        
        self.deezer_status = False
        self.ytm_status = False
        self.yt_status = True
        self.sc_status = False
        self.debug = debug
        self.root_path = os.path.dirname(os.path.abspath(__file__))
        if ffmpeg_path:
            self.ffmpeg_path = shutil.which(ffmpeg_path)
        else:
            self.ffmpeg_path = shutil.which('ffmpeg')

        if self.ffmpeg_path is None:
            if debug: logging.critical('Could not find ffmpeg.' )
            exit('Could not find ffmpeg' if not debug else 1)
       


        #### INIT DEEZER
        if deezer_arl:
            self.deezer = Deezer(deezer_arl, debug)
            self.deezer_status = True
            if debug: logging.info("Deezer status: Running")
        else: self.deezer = DummyClass()

        #### INIT YOUTUBE
        self.youtube = YouTube(debug, self.ffmpeg_path)
        self.yt_status = True
        if debug: logging.info("YouTube status: Running")

        #### INIT YOUTUBE MUSIC
        if ytm_oauth:
            self.ytm = YouTubeMusic(oauth = ytm_oauth, debug = self.debug)
            self.ytm_status = True
            if debug: logging.info("YouTube Music status: Running")
        else: self.ytm = DummyClass()

        #### INIT SoundCloud
        if sc_data:
            self.soundcloud = SoundCloud(client_id=sc_data[0],auth_token=sc_data[1], 
                                         debug = self.debug)
            self.sc_status = True
            if debug: logging.info("SoundCloud status: Running")
        else: self.soundcloud = DummyClass()



    def save(self):
        ...
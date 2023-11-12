from os import path
from random import choice
import time
from enum import StrEnum
import threading
from typing import List

from just_playback import Playback

class ALLOWEDPOSTIONS(StrEnum):
    START = "start"
    END = "end"
    NEXT = "next"
    

class Playlist():
    """
    A class that handles audio playlists.
    """
    def __init__(self):
        self.playback = Playback()
        self.seekpos = 0
        self.duration = 0
        self.volume = 1.0
        self.playback.set_volume(self.volume)
        
        self.times_looped_playlist = 0
        self.times_looped_song = 0
        
        self.loop_at_end_of_song = False
        self.loop_at_end_of_playlist = True
        self.shuffle = False
        self.pause_after_each_song = 0.5
        
        self.index = {"numerical_index" : 0, "filename" : ""}
        self.is_playing = True
        self.playlist = []

        
    def load_files(self, path_to_files : List[str]) -> None:
        """
        Load multiple files into a playlist, to be played by just_playback.
        
        Args:
            path_to_files: The absolute or relative path to the audio file

        Throws a FileNotFoundError if any audio file is not found
        """
        
        for i in path_to_files:
            if not path.exists(i):
                raise FileNotFoundError(f'File "{i}" was not found!')
        self.playlist = path_to_files
    
    def add_files(self, path_to_files : List[str] | str, postion : str) -> None:
        """
        Add multipule (or one) files to a playlist.
        
        Args:
            path_to_files: A list of files or a single file
            position: Where to add the file. Accepted values are: Start, End, Next
        """
            
        try:
            postion = ALLOWEDPOSTIONS(postion.lower())
        except ValueError as e:
            raise ValueError(f"{postion} is not a valid positon.\nValid postions are Start, End, Next")
        
        if postion == "start":
            self.playlist.insert(path_to_files, 0)
            return
        if postion == "end":
            self.playlist.append(path_to_files, 0)
            return
        if postion == "next":
            self.playlist.insert(path_to_files, self.index["numerical_index"] + 1)
            return
    
    def del_files(self, index : int | None = None, filename : str | None = None) -> None:
        """
        Delete a file from the playlist.
        
        Args:
            index: The index of the file to delete
            filename: The name of the file to delete
        """
        if index is not None:
            del self.playlist[index]
        elif filename is not None:
            self.playlist.remove(filename)
    
    def play(self) -> None:
        """
        Plays the playlist, starting from first file.
        """
        self.playing = True
        if self.is_playing == True:
            selfless = threading.Thread(target = self._playlist_host)
            selfless.name = "Playlist host"
        selfless.start()
        
    def resume(self) -> None:
        """
        Resmumes paused playback.
        """
        self.playback.resume()
    
    def pause(self) -> None:
        """
        Pauses playing playback.
        """
        
        self.playback.pause()
    
    def stop(self) -> None:
        """
        Completely stops playback.
        """
        self.playback.stop()
    
    def seek(self, pos : float) -> None: 
        """
        Seek to a point in the currently playing file.
        
        Arguments:
            pos: The position in seconds that you want to seek to. Decimal points allowed.
        """

        self.playback.seek(pos)
    
    def set_volume(self, volume : float) -> None:
        """
        Set the volume.
        
        Arguments:
            volume: The volume, an float between 0 and 1.
        """
        self.volume = volume
        self.playback.set_volume(volume)
    
    def config(self, arg) -> None:
        """
        Configure various options
        
        Arguments:
        
             arg: A dictionary containing {"Key of thing you want to set" : Value (bool or int)}
        
        Keys:
            loop_at_end_of_song -> bool
            loop_at_end_of_playlist -> bool
      
        """
        if not type(arg['loop_at_end_of_song']) == bool or type(arg['loop_at_end_of_playlist']) == bool:
            return -1
        
        self.loop_at_end_of_song = arg['loop_at_end_of_song']
        self.loop_at_end_of_playlist = arg['loop_at_end_of_playlist']
    
    def _playlist_host(self):
        """
        Internal function that handles the playlist. Do not use!
        """
        
        if threading.current_thread() == threading.main_thread():
            return
        self.playlist_is_over = False
        self.is_playing = False
        choices = list(range(len(self.playlist)))
        if self.shuffle:
            chosen = choice(choices)
            choices.remove(chosen)
        else:
            chosen = 0
        
        self.playback.load_file(self.playlist[chosen])
        self.index = {"index" : chosen, "filename" : self.playlist[chosen]}
        self.playback.play()
        
        while not self.playlist_is_over:
            self.duration = self.playback.duration
            while not self.playback.curr_pos >= self.playback.duration - 0.1: # next comment ⌄
                self.seekpos = self.playback.curr_pos
                
                if not threading.main_thread() in threading.enumerate():
                    self.playback.stop()
                    self.is_playing = True
                    return
                
            time.sleep(max(0.1, self.pause_after_each_song)) # cursorpos never equals duration, so we have to account for that
            
            if self.loop_at_end_of_song:
                self.times_looped_song += 1
                self.playback.play()
                continue
            
            if self.shuffle:
                chosen = choice(choices)
                choices.remove(chosen)
            else:
                chosen = self.index["index"] + 1
                
            self.times_looped_song = 0
            self.index["index"] = chosen
            
            if self.index["index"] == len(self.playlist): # check for if the playlist is over, and if it should loop
                if self.loop_at_end_of_playlist:
                    self.times_looped_playlist += 1
                    self.index["index"] = 0
                else:
                    self.playlist_is_over = True
                    break
                
            self.index["filename"] = self.playlist[self.index["index"]]
            self.playback.load_file(self.index["filename"])
            self.playback.play()
            
        self.playing = False
        self.is_playing = True

        
    def joinThreads(self):
        for i in threading.enumerate():
            if i == threading.main_thread() and not i.name == "Playlist host":
                continue
            i.join()
        return            


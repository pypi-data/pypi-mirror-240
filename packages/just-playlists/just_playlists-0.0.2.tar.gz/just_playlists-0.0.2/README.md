# Just Playlists
### A simple playlist manager for Just Playback

Just Playlists is a simple playlist manager for Just Playback. It allows you to create a list of songs, then play them sequentially (or randomly).

It supports every file format which just playback supports.


## Installation
### Preqrequisites
- Python 3.6 or higher
- Just Playback 0.1.7 or higher

### Installing

`pip install just_playlists`

## Usage

### Creating a playlist

```python
playlist = Playlist()
songs = [
    "C:/Users/Me/Music/My Song.mp3",
    "/test.wav",
    "/music-files/another-song.ogg",
    "great-song.mp3"
]

playlist.load_files(songs)

playlist.play()

while playlist.is_playing:
    time.sleep(1) # hold the main thread open so the songs can keep playing

```
You can even add and delete songs from the playlist while it's playing:
```python
songs = [
    "C:/Users/Me/Music/My Song.mp3",
    "/test.wav",
    "/music-files/another-song.ogg",
    "great-song.mp3"
]
playlist.add_file(songs, next) # append the list of songs to play next.
playlist.del_files("great-song.mp3") # you can only delete one song at a time
playlist.del_files(1) # you can also delete by index ( if both are provided, index is used)
```
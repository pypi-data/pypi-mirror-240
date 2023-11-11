from youtubesearchpython.__future__ import VideosSearch
import io, asyncio, os
from ..util import sanitize_string, apply_tags_to_audio
from ..deezer.util import create_folders
from pytube import YouTube as pYouTube
import ytmusicapi, os, logging, asyncio


FFMPEG_PATH = ""
class YouTube:
    def __init__(self, debug:bool, ffmpeg:str) -> None:
        global FFMPEG_PATH
        self.debug = debug
        FFMPEG_PATH = ffmpeg

    async def search(self, query:str, limit:int=10, clear_result:bool=False):
        search_result = VideosSearch(query, limit = limit)
        search_result = await search_result.next()
        if clear_result:
            temp_list = []
            for item in search_result['result']:
                time_parts = item.get('duration', "1:10").split(':')
                if len(time_parts) == 2: 
                    minutes, seconds = map(int, time_parts)
                    total_seconds = (minutes * 60) + seconds
                elif len(time_parts) == 3:  
                    hours, minutes, seconds = map(int, time_parts)
                    total_seconds = (hours * 3600) + (minutes * 60) + seconds
                
                if total_seconds < 360:
                    video_title = item.get('title', "unknown")
                    video_user = item.get('channel', {}).get('name', "unknown")

                    video_title, video_channelname = await sanitize_string(video_title, video_user)
                    temp_list.append({
                        'trackID': item['id'],
                        'title': video_title,
                        'artist': video_channelname,
                        'album': video_title,
                        'cover': item.get('thumbnails', [])[0].get('url', '')
                    })
            
            search_result['result'] = temp_list

        return search_result
    
    @staticmethod
    async def download_audio(video_id:str, download_dir:str=None, tags:dict=None):

        a = pYouTube(f"https://youtu.be/{video_id}", 
                        use_oauth=True,
                        allow_oauth_cache=True)
        if not tags:
            tags = {
                'artist': a.author,
                'title': a.title,
                'album': a.title,
                'cover': a.thumbnail_url
            }
        if download_dir:
            create_folders(download_dir)
            artist, title = await sanitize_string(tags.get('artist', ''), tags.get('title'), True)
            filename = f"{artist} - {title}.mp3"
            filepath = os.path.join(download_dir, filename)

        audio_stream = a.streams.filter(only_audio=True, file_extension='mp4').first()
        audio_length = a.length
        tags.update({'cover': a.thumbnail_url})

        start = 0
        end = audio_length - 1
        cmd = [
            FFMPEG_PATH, "-ss", str(start), "-i", audio_stream.url,
            "-t", str(end - start + 1), "-acodec", "libmp3lame",
            "-f", "mp3", filepath if download_dir else '-'
        ]
        proc = await asyncio.create_subprocess_exec(
            *cmd,
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.PIPE
        )
        mp3_data, _ = await proc.communicate()
        if proc.returncode == 0:
            if not download_dir:
                audio_io_data = io.BytesIO(mp3_data)

                audio_io_data = await apply_tags_to_audio(
                    audio = audio_io_data, 
                    tags = tags, 
                    return_bytes = True)
                
                return audio_io_data
            else:
                await apply_tags_to_audio(
                    audio = filepath, 
                    tags = tags, 
                    return_bytes = False)
                
                return filepath





class YouTubeMusic:
    def __init__(self, oauth:str, debug:bool) -> None:
        self.debug = debug
        self.oauth = oauth
        try:
            if os.path.exists(self.oauth):
                self.ytm = ytmusicapi.YTMusic(self.oauth)
            else:
                ytmusicapi.setup_oauth(self.oauth)
                self.ytm = ytmusicapi.YTMusic(self.oauth)
        except Exception as ytm_exception:
            raise ytm_exception


    async def __search(self, query:str, filter:str, scope:str, 
                       limit:int, ignore_spelling:bool):
        data = self.ytm.search(query = query, filter = filter, scope = scope, 
                               limit = limit, ignore_spelling = ignore_spelling)
        return data 
    async def search(self, query:str, filter:str=None, scope:str=None, 
                       limit:int=20, ignore_spelling:bool=False):
        """
        Search YouTube music
        Returns results within the provided category.

        :param query: Query string, i.e. 'Oasis Wonderwall'
        :param filter: Filter for item types. Allowed values: ``songs``, ``videos``, ``albums``, ``artists``, ``playlists``, ``community_playlists``, ``featured_playlists``, ``uploads``.
          Default: Default search, including all types of items.
        :param scope: Search scope. Allowed values: ``library``, ``uploads``.
            For uploads, no filter can be set! An exception will be thrown if you attempt to do so.
            Default: Search the public YouTube Music catalogue.
        :param limit: Number of search results to return
          Default: 20
        :param ignore_spelling: Whether to ignore YTM spelling suggestions.
          If True, the exact search term will be searched for, and will not be corrected.
          This does not have any effect when the filter is set to ``uploads``.
          Default: False, will use YTM's default behavior of autocorrecting the search.
        :return: List of results depending on filter.
          resultType specifies the type of item (important for default search).
          albums, artists and playlists additionally contain a browseId, corresponding to
          albumId, channelId and playlistId (browseId=``VL``+playlistId)

          Example list for default search with one result per resultType for brevity. Normally
          there are 3 results per resultType and an additional ``thumbnails`` key::

            [
              {
                "category": "Top result",
                "resultType": "video",
                "videoId": "vU05Eksc_iM",
                "title": "Wonderwall",
                "artists": [
                  {
                    "name": "Oasis",
                    "id": "UCmMUZbaYdNH0bEd1PAlAqsA"
                  }
                ],
                "views": "1.4M",
                "videoType": "MUSIC_VIDEO_TYPE_OMV",
                "duration": "4:38",
                "duration_seconds": 278
              },
              {
                "category": "Songs",
                "resultType": "song",
                "videoId": "ZrOKjDZOtkA",
                "title": "Wonderwall",
                "artists": [
                  {
                    "name": "Oasis",
                    "id": "UCmMUZbaYdNH0bEd1PAlAqsA"
                  }
                ],
                "album": {
                  "name": "(What's The Story) Morning Glory? (Remastered)",
                  "id": "MPREb_9nqEki4ZDpp"
                },
                "duration": "4:19",
                "duration_seconds": 259
                "isExplicit": false,
                "feedbackTokens": {
                  "add": null,
                  "remove": null
                }
              },
              {
                "category": "Albums",
                "resultType": "album",
                "browseId": "MPREb_9nqEki4ZDpp",
                "title": "(What's The Story) Morning Glory? (Remastered)",
                "type": "Album",
                "artist": "Oasis",
                "year": "1995",
                "isExplicit": false
              },
              {
                "category": "Community playlists",
                "resultType": "playlist",
                "browseId": "VLPLK1PkWQlWtnNfovRdGWpKffO1Wdi2kvDx",
                "title": "Wonderwall - Oasis",
                "author": "Tate Henderson",
                "itemCount": "174"
              },
              {
                "category": "Videos",
                "resultType": "video",
                "videoId": "bx1Bh8ZvH84",
                "title": "Wonderwall",
                "artists": [
                  {
                    "name": "Oasis",
                    "id": "UCmMUZbaYdNH0bEd1PAlAqsA"
                  }
                ],
                "views": "386M",
                "duration": "4:38",
                "duration_seconds": 278
              },
              {
                "category": "Artists",
                "resultType": "artist",
                "browseId": "UCmMUZbaYdNH0bEd1PAlAqsA",
                "artist": "Oasis",
                "shuffleId": "RDAOkjHYJjL1a3xspEyVkhHAsg",
                "radioId": "RDEMkjHYJjL1a3xspEyVkhHAsg"
              }
            ]


        """
        task = await asyncio.get_event_loop().run_in_executor(None, 
                        lambda: self.__search(query = query, filter = filter, 
                                             scope = scope, limit = limit, 
                                             ignore_spelling = ignore_spelling))
        
        
        task_result = await task
        return task_result 
    
    
    async def __search_by_id(self, videoID:str, signatureTimestamp:int):
        data = self.ytm.get_song(videoId=videoID, signatureTimestamp=signatureTimestamp)
        return data
    async def search_by_id(self, videoID:str, signatureTimestamp:int = None):
        task = await asyncio.get_event_loop().run_in_executor(None, 
                        lambda: self.__search_by_id(videoID = videoID, signatureTimestamp = signatureTimestamp))
        
        
        task_result = await task
        return task_result
    

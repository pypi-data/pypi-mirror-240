from soundcloud import SoundCloud as Sound_Cloud
from soundcloud.resource.track import Track
from soundcloud.resource.user import User
from soundcloud.resource.playlist import AlbumPlaylist
from soundcloud import Media, Transcoding, Format, Badges, CreatorSubscription, Product, Visual, Visuals

import json, datetime, itertools, math, aiohttp, asyncio
from typing import Union

class CustomEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime.datetime):
            return obj.strftime('%Y-%m-%dT%H:%M:%SZ')
        if isinstance(obj, Track):
            return obj.__dict__
        if isinstance(obj, Media):
            return obj.__dict__
        if isinstance(obj, Transcoding):
            return obj.__dict__
        if isinstance(obj, User):
            return obj.__dict__
        if isinstance(obj, Format):
            return obj.__dict__
        if isinstance(obj, Badges):
            return obj.__dict__
        if isinstance(obj, CreatorSubscription):
            return obj.__dict__
        if isinstance(obj, Product):
            return obj.__dict__
        if isinstance(obj, Visuals):
            return obj.__dict__
        if isinstance(obj, Visual):
            return obj.__dict__
        return super().default(obj)

class SoundCloud:
    def __init__(self, client_id:str, auth_token:str, debug:bool) -> None:
        self.debug = debug
        self.available_filters = ['track', 'user', 'album', 'playlist']
        self.methods = [
            'get_track',
            'download',
            'get_track_url'
        ]


        self.sc_client = Sound_Cloud(client_id = client_id, 
                                    auth_token = auth_token)

    async def __search_api_query(self, query:str,  filter:str, limit:int) -> Union[Track, User, AlbumPlaylist]:
        if filter == "track":
            data = self.sc_client.search_tracks(query = query)
        elif filter == "user":
            data = self.sc_client.search_users(query = query)
        elif filter == "album":
            data = self.sc_client.search_albums(query = query)
        elif filter == "playlist":
            data = self.sc_client.search_playlists(query = query)

        limited_data = itertools.islice(data, limit)
        return limited_data
    async def __api_query(self, method:str, **kwargs):
        data = None
        if method in self.methods:
            if method == 'get_track':
                data = self.sc_client.get_track(kwargs.get('track_id', 0))
            
            elif method == 'get_track_url':
                track_id = kwargs.get('track_id', 0)
                track = await self.get_track(track_id)
            
                download_url = None
                if track.downloadable:
                    download_url = self.sc_client.get_track_original_download(track.id, track.secret_token)


                if download_url is None:
                    aac_transcoding = None
                    mp3_transcoding = None
                    
                    for t in track.media.transcodings:
                        if t.format.protocol == "hls" and "aac" in t.preset:
                            aac_transcoding = t
                        elif t.format.protocol == "hls" and "mp3" in t.preset:
                            mp3_transcoding = t

                    transcoding = None

                    if aac_transcoding:
                        transcoding = aac_transcoding
                    elif mp3_transcoding:
                        transcoding = mp3_transcoding


                    if not transcoding:
                        return None
                    
                    if self.logger: self.logger.info(f'[SC-DL] [{track_id}]: Download link generation..')
                    url = transcoding.url
                    bitrate_KBps = 256 / 8 if "aac" in transcoding.preset else 128 / 8
                    total_bytes = bitrate_KBps * transcoding.duration
                    
                    min_size = 0
                    max_size = math.inf
                    
                    if not min_size <= total_bytes <= max_size:
                        return None
                    
                    if url is not None:
                        headers = self.sc_client.get_default_headers()
                        if self.sc_client.auth_token:
                            headers["Authorization"] = f"OAuth {self.sc_client.auth_token}"

                        async with aiohttp.ClientSession(headers=headers) as session:
                            async with session.get(url, params={"client_id": self.sc_client.client_id}) as response:
                                download_url = await response.json()   
                                download_url = download_url.get('url', "")

                return download_url
            
        return data
    async def __search_api_query(self, query:str,  filter:str, limit:int) -> Union[Track, User, AlbumPlaylist]:
        if filter == "track":
            data = self.sc_client.search_tracks(query = query)
        elif filter == "user":
            data = self.sc_client.search_users(query = query)
        elif filter == "album":
            data = self.sc_client.search_albums(query = query)
        elif filter == "playlist":
            data = self.sc_client.search_playlists(query = query)

        limited_data = itertools.islice(data, limit)
        return limited_data
    async def get_track_url(self, track_id:int, **kwargs) -> Track:
        """
            Getting information from a track by its ID

            :param track_id: Track ID on SoundCloud

            :return: SoundCloud.BasicTrack 
        """
        task = await asyncio.get_event_loop().run_in_executor(None, 
                    lambda: self.__api_query(
                                    method='get_track_url',
                                    track_id = track_id,**kwargs))
        
        
        task_result = await task
        return task_result
    async def get_track(self, track_id:int, **kwargs) -> Track:
        """
            Getting information from a track by its ID

            :param track_id: Track ID on SoundCloud

            :return: SoundCloud.BasicTrack 
        """
        task = await asyncio.get_event_loop().run_in_executor(None, 
                    lambda: self.__api_query(
                                    method='get_track',
                                    track_id = track_id,**kwargs))
        
        
        task_result = await task
        return task_result
    async def serialize_to_json(self, tracks:list):
        res = []
        for x in tracks:
            d = json.dumps(x, cls=CustomEncoder)
            res.append(json.loads(d))
        return res
    async def search(self, query:str, filter:str='track', limit:int=10, json_dump:bool=False):
        """
            Soundcloud search


            :param query: Search string
            :param filter: Filter for item types. Allowed values: ``track``, ``user``, ``album``, ``playlist``.
            Default: ``track``
            :param limit: Limit Results
            Default: ``10``

            :return: Generator limited by ``limit``
        """
        
        if filter not in self.available_filters:
            filter = self.available_filters[0]
        
        task = await asyncio.get_event_loop().run_in_executor(None, lambda: self.__search_api_query(query, filter, limit))
        task_result = await task
        if json_dump:
            task_result = await self.serialize_to_json(list(task_result))
        
        return task_result
    async def __search_by_link(self, link:str):
        return self.sc_client.resolve(link)
    async def search_by_link(self, link:str, json_dump:bool=False):
        task = await asyncio.get_event_loop().run_in_executor(None, lambda: self.__search_by_link(link))
        task_result = await task
        if json_dump:
            task_result = await self.serialize_to_json(list(task_result))
        
        return task_result




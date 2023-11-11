from mutagen.mp3 import MP3, HeaderNotFoundError
from mutagen.id3 import ID3, APIC, TIT2, TPE1, TALB
from typing import Union
import io, aiohttp, unidecode, re
from .deezer.constants.networking_settings import HTTP_HEADERS

SANITIZE_PARTS = ["lyric","lyrics", "(music video)","(official music video)", "feat.", "f."]

@staticmethod
async def sanitize_string(string_line:str, other_string_line:str="", _unidecode:bool=False):
    if _unidecode: string_line = unidecode.unidecode_expect_nonascii(string_line) 
    string_line = re.sub(r'[^\w\s.-]', '', string_line)

    if other_string_line:
        string_line = string_line.replace(other_string_line, "")
        if _unidecode:other_string_line = unidecode.unidecode_expect_nonascii(other_string_line) 
        other_string_line = re.sub(r'[^\w\s.-]', '', other_string_line)

    string_line = string_line.replace("-", "")

    for part in SANITIZE_PARTS:
        if string_line.lower().find(part) != -1:
            string_line = string_line.replace(part, "")

        if other_string_line:
            if other_string_line.lower().find(part) != -1:
                other_string_line = other_string_line.replace(part, "")

    

    if other_string_line:
        return (string_line.strip(), other_string_line.strip())

    
    return string_line.strip()  
@staticmethod
async def apply_tags_to_audio(audio:Union[str, io.BytesIO], tags:dict) -> Union[str, io.BytesIO]: 
    if tags:
        try:
            audio_file = MP3(audio, ID3=ID3)
        except HeaderNotFoundError:
            audio = io.BytesIO(audio.getvalue())
            try:
                audio_file = MP3(audio, ID3=ID3)
            except HeaderNotFoundError:
                return None
    if not audio_file.tags:
            audio_file.tags = ID3()

    audio_file.tags.add(TPE1(encoding=3, text=tags.get('artist', "unknown")))  
    audio_file.tags.add(TALB(encoding=3, text=tags.get('album', "unknown")))   
    audio_file.tags.add(TIT2(encoding=3, text=tags.get('title', "unknown"))) 


    track_cover = tags.get("cover", None)
    if track_cover is None:
        track_cover = tags.get("_albumart", None)


    if track_cover:
        if isinstance(track_cover, bytes):
            audio_file.tags.add(
                APIC(
                    encoding=3,
                    mime="image/jpeg",
                    type=3,
                    desc=u"cover",
                    data=track_cover
                )
                )
        elif isinstance(track_cover, str):
            try:
                async with aiohttp.ClientSession(headers=HTTP_HEADERS) as session:
                    async with session.get(track_cover) as response:
                        cover_data = await response.read()

                audio_file.tags.add(
                    APIC(
                        encoding=3,
                        mime="image/jpeg",
                        type=3,
                        desc=u"cover",
                        data=cover_data
                    )
                )
            except (aiohttp.ClientConnectorError, aiohttp.ClientConnectorSSLError, aiohttp.ServerTimeoutError):
                ...

    if isinstance(audio, io.BytesIO):
        return io.BytesIO(audio.getvalue())
    elif isinstance(audio, str):
        audio_file.save()
        return audio
    else:
        return '????'
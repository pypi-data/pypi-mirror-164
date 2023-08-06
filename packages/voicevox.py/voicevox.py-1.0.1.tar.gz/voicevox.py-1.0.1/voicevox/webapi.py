import requests
import urllib
import urllib.request
from asyncio import run, gather

class webapi:

    @staticmethod
    def run(apikey, text, sound):
        params = {'apikey': apikey,
                  'text': text,
                  'sound': sound,
                  }
        post = requests.get(f"https://api.su-shiki.com/v2/voicevox/audio/?key={apikey}&speaker={sound}&pitch=0&intonationScale=1&speed=1&text={text}")
        with open("voice.wav", "wb") as fp:
            fp.write(post.content)
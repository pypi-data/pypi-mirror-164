import json
import requests
import wave
import subprocess
import asyncio
import urllib.request
import platform


class voiceclient:

    @staticmethod
    def app(exepass):
        subprocess.Popen(exepass)

    @staticmethod
    def run(text, speaker, filename):
        query_payload = {"text": text, "speaker": speaker}
        r = requests.post("http://localhost:50021/audio_query", 
        params=query_payload, timeout=(10.0, 300.0))
        query_data = r.json()
        synth_payload = {"speaker": speaker}    
        r = requests.post("http://localhost:50021/synthesis", params=synth_payload, data=json.dumps(query_data))
        with open(filename, "wb") as fp:
            fp.write(r.content)

    @staticmethod
    def vbox_dl():
        pf = platform.system()
        if pf == 'Windows':
            url = "https://github.com/VOICEVOX/voicevox/releases/download/0.13.1/VOICEVOX.Web.Setup.0.13.1.exe"
            urllib.request.urlretrieve(url, 'voicevox.exe')
            subprocess.run("voicevox.exe")
        elif pf == 'Darwin':
            url = "https://github.com/VOICEVOX/voicevox/releases/download/0.13.1/VOICEVOX.0.13.1.dmg"
            urllib.request.urlretrieve(url, 'voicevox.dmg')
            subprocess.run("voicevox.dmg", shell=True)
        elif pf == 'Linux':
            url = "https://voicevox.hiroshiba.jp/static/5a524c78055a8eb31039f9d8e9462623/linuxInstallNvidia.sh"
            urllib.request.urlretrieve(url, 'voicevox.sh')
            subprocess.run("voicevox.sh", shell=True)

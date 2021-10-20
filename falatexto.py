import subprocess
from ibm_watson import SpeechToTextV1
from ibm_watson.websocket import RecognizeCallback, AudioSource
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

# extraindo o Audio

command = 'ffmpeg -i aiml.mkv -ab 160k -ar 44100 -vn audio.wav'
subprocess.call(command, shell=True)

# Configurando serviço STT

apikey = ''
url = ''
# Setup service
authenticator = IAMAuthenticator(apikey)
stt = SpeechToTextV1(authenticator=authenticator)
stt.set_service_url(url)

#Abrir fonte de áudio e converter

with open('audio.wav', 'rb') as f:
    res = stt.recognize(audio=f, content_type='audio/wav', model='en-AU_NarrowbandModel', continuous=True).get_result()

#Processar Resultados
len(res['results'])

text = [result['alternatives'][0]['transcript'].rstrip() + '.\n' for result in res['results']]
#Imprimindo Resultados
text = [para[0].title() + para[1:] for para in text]
transcript = ''.join(text)
with open('output.txt', 'w') as out:
    out.writelines(transcript)


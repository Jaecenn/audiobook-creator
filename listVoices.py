"""Lists the available voices."""
from google.cloud import texttospeech
from google.cloud.texttospeech import enums
client = texttospeech.TextToSpeechClient()

# Performs the list voices request
voices = client.list_voices()

for voice in voices.voices:
    # Display the voice's name. Example: tpc-vocoded
    print('Name: {}'.format(voice.name))
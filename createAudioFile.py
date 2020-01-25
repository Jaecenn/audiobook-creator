

def synthesize_text(text):
    """Synthesizes speech from the input string of text."""
    from google.cloud import texttospeech
    client = texttospeech.TextToSpeechClient()

    input_text = texttospeech.types.SynthesisInput(text=text)

    # Note: the voice can also be specified by name.
    # Names of voices can be retrieved with client.list_voices().
    voice = texttospeech.types.VoiceSelectionParams(
        language_code='en-US',
        name='en-US-Wavenet-E')
        #name='en-US-Standard-E')
        #ssml_gender=texttospeech.enums.SsmlVoiceGender.FEMALE)

    audio_config = texttospeech.types.AudioConfig(
        audio_encoding=texttospeech.enums.AudioEncoding.MP3)

    response = client.synthesize_speech(input_text, voice, audio_config)

    return response.audio_content


import io
filename="The Empire of Ashes - Anthony Ryan_35_41.txt"
maxChars = 5000
import re

import os
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = r'd:\Dokumenty\Programming\textToAudio\AudiobookCreator-efe46d1d9039.json'
# with open(filename, 'r') as infile:
#     words = 0
#     characters = 0
#     block = ""
#     fileID = 1
#     fileList = enumerate(infile, 1) 
#     atLeastOnce = False

#     for lineno, line in fileList:
#         wordslist = line.split()
#         words += len(wordslist)
#         characters += sum(len(word) for word in wordslist)
        
#         if (characters > maxChars):
#             atLeastOnce = True
#             block = block.strip()
#             block = re.sub("\s\s+", " ", block)
#             print("***************BLOCK"+ str(fileID))
#             print(block)
#             outAudio = synthesize_text(block)
#             fileName = 'output'+ str(fileID) + ".mp3"
#             # The response's audio_content is binary.
#             with open(fileName, 'wb') as out:
#                 out.write(outAudio)
#                 print('Audio content written to file: ' + fileName)
#             block = ""
#             fileID = fileID + 1
#             words = 0
#             characters = 0
#         block = block + line   
#     if atLeastOnce == False:
#         block = block.strip()
#         block = re.sub("\s\s+", " ", block)
#         print("***************BLOCK"+ str(fileID))
#         print(block)
#         outAudio = synthesize_text(block)
#         fileName = 'output'+ str(fileID) + ".mp3"
#         # The response's audio_content is binary.
#         with open(fileName, 'wb') as out:
#             out.write(outAudio)
#             print('Audio content written to file: ' + fileName)
#         block = ""
#         fileID = fileID + 1
#         words = 0
#         characters = 0

# print(lineno)
# print(words)
# print(characters)


with open(filename, 'r', encoding="utf-8", errors='ignore') as infile:
    #print(infile.read())
    fileContent = infile.read(maxChars - 1)
    #infile.seek(maxChars - 1,0)
    fileID = 1
    lastPart = ""

    while (fileContent != ""):

        fileContent = re.sub("\s\s+", " ", fileContent)
        if fileID > 1:
            pos = fileContent.find(lastPart)
            fileContent = fileContent[(pos + len(lastPart)):]

        lastPart = fileContent[-10:]

        # print("********************* BLOCK" + str(fileID))
        # print(fileContent)
        outAudio = synthesize_text(fileContent)
        outfileName = os.path.splitext(filename)[0] + '_part'+ str(fileID).zfill(4) + ".mp3"
        # The response's audio_content is binary.
        with open(outfileName, 'wb') as out:
            out.write(outAudio)
            print('Audio content written to file: ' + outfileName)
        
        infile.seek(((maxChars - 1)*fileID))
        fileID = fileID + 1;
        fileContent = infile.read(maxChars - 1)

#     #more precise concatenation
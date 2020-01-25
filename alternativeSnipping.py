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
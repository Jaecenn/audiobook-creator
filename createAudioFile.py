
import synthetizer, io, re, os
import config as cfg

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = cfg.googleAuthTokenPath


with open(cfg.inputTxtFilePath, 'r', encoding="utf-8", errors='ignore') as infile:
    #print(infile.read())
    fileContent = infile.read(cfg.maxCharsInBatch - 1)
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
        outfileName = os.path.splitext(cfg.inputTxtFilePath)[0] + '_part'+ str(fileID).zfill(4) + ".mp3"
        # The response's audio_content is binary.
        with open(outfileName, 'wb') as out:
            out.write(outAudio)
            print('Audio content written to file: ' + outfileName)
        
        infile.seek(((cfg.maxCharsInBatch - 1)*fileID))
        fileID = fileID + 1;
        fileContent = infile.read(cfg.maxCharsInBatch - 1)

#     #more precise concatenation
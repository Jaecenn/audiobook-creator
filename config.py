#!/usr/bin/env python

inputTxtFilePath = "testData\\2. CEH v9 Certified Ethical Hac - Zamzar.txt"

destinationFolder = inputTxtFilePath

synthetizerSetup = {
    'language_code': 'en-US',
    'name': 'en-US-Wavenet-E',
    #'name': 'en-US-Standard-E',
    'maxCharsInBatch': '5000',
    'limitNuOfBatches': '2'
}

googleAuthTokenPath = r"d:\Dokumenty\Programming\textToAudio\AudiobookCreator-efe46d1d9039.json"
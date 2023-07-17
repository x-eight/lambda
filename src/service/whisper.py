import subprocess
import os
import json
#import whisperx


def getJsonByWhisper(fileName, folderPath):
    try:
        filePath = os.path.join(folderPath, fileName + ".mp3")
        outputFilePath = os.path.join(folderPath, fileName + ".json")
        comando = f'whisperx {filePath} --compute_type float32 -o {folderPath} --output_format json'
        #subprocess.run(comando, shell=True, check=True)

        #with open(outputFilePath, "r") as jsonFile:
        #    contenidoArchivo = json.load(jsonFile)
        
        #return contenidoArchivo
        return {}

    except subprocess.CalledProcessError as e:
        raise Exception("whisperx was unable to transcribe the video")
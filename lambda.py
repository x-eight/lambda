import subprocess
import whisperx
import os

def handler(event, context):
    print("ffmpeg ffmpeg")
    print(os.system("ffmpeg -version"))
    print("whisperx whisperx")
    print(os.system("whisperx -version"))
    return {"Hello": "World"}


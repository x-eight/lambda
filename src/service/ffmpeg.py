import subprocess
import shutil
import os

def convertToMP3(fileName, dirPath, videoUrl):
    mp3Path = os.path.join(dirPath, fileName + ".mp3")
    ffmpeg_command = ["ffmpeg", "-i", videoUrl, "-f", "mp3", mp3Path]

    try:
        subprocess.run(ffmpeg_command, check=True)
        return mp3Path
    except subprocess.CalledProcessError as e:
        raise Exception("ffmpeg could not convert to mp3")
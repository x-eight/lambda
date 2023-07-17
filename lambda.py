import subprocess

def handler(event, context):
    ffmpeg_command = ["whisperx", "--version"]
    subprocess.run(ffmpeg_command, check=True)
    return {"Hello": "World"}


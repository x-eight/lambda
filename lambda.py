import subprocess

def handler(event, context):
    ffmpeg_command = ["ffmpeg", "--version"]
    subprocess.run(ffmpeg_command, check=True)
    return {"Hello": "World"}


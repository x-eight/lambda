import io
import os
import json
from tempfile import TemporaryDirectory
from pydantic import BaseModel
from fastapi import APIRouter
from service.ffmpeg import convertToMP3
from service.whisper import getJsonByWhisper
import subprocess
import logging

class ApiError(Exception):
    pass

class TranslabeBody(BaseModel):
    url: str
    file_name: str

router = APIRouter()

@router.get("/status")
async def status():
    return {"running":"ok"}

@router.post("/translabe")
async def translabe():#body: TranslabeBody
    fileName = "original"#body.file_name
    videoUrl = "https://dev-drawify-v3.s3.eu-west-3.amazonaws.com/video/original.mp3"#body.url
    tempDir = os.path.join(os.path.dirname(__file__), "service/folder")
    datosJSON = {}
    with TemporaryDirectory(dir=tempDir,prefix="temp-") as temp_dir:
        mp3Path = convertToMP3(fileName, temp_dir, videoUrl)
        if mp3Path:
            print("Conversion completed in MP3")
        else:
            raise Exception("The conversion failed.")

        try:
            datosJSON = getJsonByWhisper(fileName, temp_dir)
        except ApiError as e:  
            raise Exception(str(e))

    return datosJSON

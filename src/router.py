#from . import translabe, error
from error import register_error_handlers
from translabe import router
from fastapi import FastAPI, Request, status
from fastapi.encoders import jsonable_encoder
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from pydantic import BaseModel

def create_app():
    app = FastAPI()

    register_error_handlers(app)
    app.include_router(router, prefix="/api")

    return app
from fastapi import FastAPI, Request, status
from fastapi.exceptions import RequestValidationError, HTTPException
from fastapi.responses import JSONResponse

def register_error_handlers(app: FastAPI):
    @app.exception_handler(status.HTTP_404_NOT_FOUND)
    async def exception_not_found(request: Request, exc: RequestValidationError):
        return JSONResponse(
            status_code=status.HTTP_404_NOT_FOUND,
            content={
                'error': 'Page not found',
                'message': 'The requested URL does not exist'
            },
        )

    @app.exception_handler(status.HTTP_405_METHOD_NOT_ALLOWED)
    async def generic_exception_handler(request, exc):
        message = str(exc.args[0]) if exc.args else "Server error has occurred"
        return JSONResponse(
            status_code=500,
            content={
                'error': 'Internal Server Error',
                'message': message
            }
        )

    @app.exception_handler(status.HTTP_500_INTERNAL_SERVER_ERROR)
    async def generic_exception_handler(request, exc: RequestValidationError):
        message = str(exc.args[0]) if exc.args else "Server error has occurred"
        return JSONResponse(
            status_code=500,
            content={
                'error': 'Internal Server Error',
                'message': message
            }
        )
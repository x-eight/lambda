from dotenv import load_dotenv
import os
import uvicorn
from router import create_app

load_dotenv()

port = int(os.environ.get("PORT"))
host = os.environ.get("APP_HOST")

app = create_app()


if __name__ == "__main__":
    uvicorn.run(app, host=host, port=port)

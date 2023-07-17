from mangum import Mangum
from src import main

handler = Mangum(main.create_app())


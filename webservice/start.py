import uvicorn
from app.app import app
from app.routes import *
from config import WebServer


if __name__ == "__main__":
    uvicorn.run(app, host=WebServer.host, port=WebServer.port)
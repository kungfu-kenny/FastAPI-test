from fastapi import FastAPI
from models.models import engine, Base, session_value

Base.metadata.create_all(bind=engine)
app = FastAPI()
db = session_value()

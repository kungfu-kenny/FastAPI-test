from datetime import datetime
from sqlalchemy import (create_engine, 
                        Column, 
                        Integer,
                        String, 
                        DateTime)
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from config import PostgreSQL

engine = create_engine(PostgreSQL.url)#TODO change here if it is neccessary

session_value = sessionmaker(bind=engine, autocommit=False, autoflush=False,)

Base = declarative_base()

class EventGameBasic(Base):
    __tablename__ = 'events'
    id = Column(Integer, primary_key=True)
    datetime = Column(DateTime, default=datetime.now())
    app_id = Column(String(50), default='casino')
    account_id = Column(Integer, nullable=False)
    session_id = Column(Integer, nullable=False)
    signature = Column(String(150))
    event = Column(String(100), nullable=False)
    character_id = Column(String(50))
    comment = Column(String(150), default='None')
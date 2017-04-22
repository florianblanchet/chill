from flask import Flask
import requests
import os
import urllib.request
from bs4 import BeautifulSoup
from sqlalchemy.orm import sessionmaker
import time
import schedule
from sqlalchemy import *
SQLALCHEMY_DATABASE_URI = os.environ.get('HEROKU_POSTGRESQL_PUCE_URL')
token = os.environ.get('FB_ACCESS_TOKEN')
engine = create_engine(SQLALCHEMY_DATABASE_URI)
engine.echo = False
metadata = MetaData(engine)
users = Table('user', metadata, autoload=True)
news = Table('news', metadata, autoload=True)

Session = sessionmaker(bind=engine)
session = Session()

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

if __name__ == '__main__':
    app.run()

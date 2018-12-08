from bottle import route, run, view
from datetime import datetime as dt
from random import random
from horoscope import generate_prophecies
import os

shablon = os.getcwd() + os.sep + 'views' + os.sep + 'shablon1.tpl'
@route("/")
@view(shablon)
def index():
  now = dt.now()
  pr = generate_prophecies(6, 2)
  return {
    "date": f"{now.year}-{now.month}-{now.day}",
    "predictions": pr,
  }

@route("/api/forecasts")
def api_forecasts():
  pr = generate_prophecies(6, 2)
  return {"prophecies": pr }

run(
  host="localhost",
  port=8080,
  autoreload=True
)
from bottle import route, run, view, static_file
from datetime import datetime as dt
from random import random
from horoscope import generate_prophecies
import os

# фишка из 6го модуля чтобы шаблон видел файлы js и css
@route("/static/<filename:path>")
def send_static(filename):
    return static_file(filename, root="static")

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
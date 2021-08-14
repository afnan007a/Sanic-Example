
from sanic import Sanic
from sanic.response import json, html, text
import os

app = Sanic(__name__)

@app.route('/')
def index(request):
  template = open(os.getcwd() + "/templates/index.html")
  return html(template.read())

app.run(host='0.0.0.0', port=4044)

from flask import Flask
import requests

app = Flask(__name__)

@app.route("/buy")
def buy():
    res = requests.get("http://billing:8000")
    return res.text
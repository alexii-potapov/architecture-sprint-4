from flask import Flask
import requests

app = Flask(__name__)

@app.route("/")
def pay():
    res = requests.get("http://order:8002")
    return "Payed"+res.text

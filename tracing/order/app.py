from flask import Flask
import random
import time

app = Flask(__name__)

@app.route("/")
def order():
    random_order_number = random.randint(1, 500)
    time.sleep(random_order_number*0.001) #задержка
    return str(random_order_number)
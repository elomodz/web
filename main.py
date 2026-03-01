from flask import Flask, render_template
from threading import Thread
from bot import run_bot
import os

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")

def run_web():
    port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=port)

def run_all():
    t1 = Thread(target=run_web)
    t1.start()

    t2 = Thread(target=run_bot)
    t2.start()

if __name__ == "__main__":
    run_all()

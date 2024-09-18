from flask import Flask

app = Flask(__name__)

@app.route("/health")
def health():
    return "ok", 200

@app.route("/ping")
def ping():
    return "pong!", 200
import time

import flask
from flask import Flask, render_template
app = Flask(__name__)


@app.route("/")
def serve():
    return render_template("index.html", version=flask.__version__)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000)

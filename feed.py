from flask import Flask, render_template, url_for
from feeders import hackernews

app = Flask(__name__)


@app.route("/", methods=["GET"])
def feed():
    return render_template('feed.html')


@app.route("/hn", methods=["GET"])
def hn():
    return hackernews.get_top()


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)

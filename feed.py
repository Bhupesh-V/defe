from flask import Flask, render_template, url_for
from feeders import hackernews, devto

app = Flask(__name__)


@app.route("/", methods=["GET"])
def feed():
    return render_template('feed.html')


@app.route("/hn", methods=["GET"])
def hn():
    stories = hackernews.get_top()
    return render_template('hackernews.html', stories=stories)


@app.route("/devto", methods=["GET"])
def dev_to():
    data = devto.get_articles()
    return render_template('dev.html', data=data)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)

from flask import Flask, render_template, url_for

app = Flask(__name__)


@app.route("/", methods=["GET"])
def feed():
    return render_template('feed.html')


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)

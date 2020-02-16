from flask import Flask, render_template, jsonify, request
from feeders import devto, reddit, feeder

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def feed():
    if request.method == "GET":
        data = feeder.all_feed()
        return render_template("feed.html", allfeed=data)
    else:
        service = request.json
        print(service)
        if service["feed"] == "dev":
            data = devto.get_articles()
            return jsonify(data)
        elif service["feed"] == "reddit":
            data = reddit.subreddit(service["sub"], service["sort"])
            return jsonify(data)
        else:
            data = feeder.feed(service["feed"])
            return jsonify(data)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)

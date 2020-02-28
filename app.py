from flask import Flask, render_template, jsonify, request
from feeders import feeder

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def feed():
    if request.method == "GET":
        data = feeder.all_feed(True)
        data_keys = feeder.read_data("general")
        data_keys = [item["name"] for item in data_keys]
        return render_template("feed.html", allfeed=data, feeder_sites=data_keys)
    else:
        service = request.json
        print(service)
        data = feeder.feed(service["feed"])
        return jsonify(data)


@app.route("/news", methods=["GET"])
def news_feed():
    data = feeder.news_feed(True)
    data_keys = feeder.read_data("news")
    data_keys = [item["name"] for item in data_keys]
    return render_template("news.html", news_feed_data=data, feeder_sites=data_keys)


@app.route("/podcasts", methods=["GET"])
def podcast():
    data = feeder.podcasts_feeds(True)
    data_keys = feeder.read_data("podcast")
    data_keys = [item["name"] for item in data_keys]
    return render_template("podcast.html", podcast_feed=data, feeder_sites=data_keys)


@app.route("/newsletters", methods=["GET"])
def newsletter():
    data = feeder.newsletters_feeds(True)
    data_keys = feeder.read_data("newsletter")
    data_keys = [item["name"] for item in data_keys]
    return render_template(
        "newsletter.html", newsletter_feed=data, feeder_sites=data_keys
    )


@app.route("/feeders")
def feeder_sites_info():
    return render_template(
        "feeders.html",
        feed_sites=feeder.read_data("general"),
        news_sites=feeder.read_data("news"),
        podcasts_sites=feeder.read_data("podcast"),
        newsletter_feeds=feeder.read_data("newsletter"),
    )


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/support")
def support():
    return render_template("support.html")


if __name__ == "__main__":
    app.run()

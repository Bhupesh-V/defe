from flask import Flask, render_template, jsonify, request
from feeders import reddit, feeder

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def feed():
    if request.method == "GET":
        data = feeder.all_feed()
        return render_template("feed.html", allfeed=data, feeder_sites=feeder.feeder_site_urls.keys())
    else:
        service = request.json
        print(service)
        if service["feed"] == "reddit":
            data = reddit.subreddit(service["sub"], service["sort"])
            return jsonify(data)
        else:
            data = feeder.feed(service["feed"])
            return jsonify(data)


@app.route("/podcasts", methods=["GET"])
def podcast():
    data = feeder.podcasts_feeds()
    return render_template("podcast.html", podcast_feed=data, feeder_sites=feeder.podcasts.keys())


@app.route("/newsletters", methods=["GET"])
def newsletter():
    data = feeder.newsletters_feeds()
    return render_template("newsletter.html", newsletter_feed=data, feeder_sites=feeder.newsletters.keys())


@app.route("/feeders", methods=["GET"])
def feeder_sites_info():
    print("jpjpfdjfjdf")
    return render_template("feeders.html", feed_sites=feeder.feeder_site_urls,
                           podcasts_sites=feeder.podcasts, newsletter_feeds=feeder.newsletters)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)

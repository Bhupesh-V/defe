function fetch_feed (argument) {
    var feed = document.getElementById("feed-input").value;
    console.log(feed);

    clear_previous_feed();

    data = get_feed(feed);
    var mainContainer = document.getElementById("feed");

    for (var i = 0; i < data.length; i++) {
        var story = document.createElement("div");
        var link = document.createElement("a");
        link.setAttribute("href", data[i].link);
        var title = document.createTextNode(data[i].title);
        link.appendChild(title);
        story.appendChild(link);

        mainContainer.appendChild(story);
    }
}

function clear_previous_feed() {
    // remove all childs of "feed"
    const feed_div = document.getElementById("feed");
    feed_div.innerHTML = '';
}

function get_feed(feeder) {
    const data = {
        feed: feeder
    };
    fetch('/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(data),
    }).then(response => {
        return response.json();
    }).then(data => {
        result = data;
    });
    /*let result = await res.json();*/

    return result;
}

function invoke_dev() {
    clear_previous_feed();

    data = get_feed("dev");
    var mainContainer = document.getElementById("feed");

    for (var i = 0; i < data.length; i++) {
        var article = document.createElement("div");
        article.setAttribute("id", "feed-card");
        var link = document.createElement("a");
        link.setAttribute("href", data[i].url);
        var title = document.createTextNode(data[i].title);
        link.appendChild(title);
        article.appendChild(link);

        mainContainer.appendChild(article);
    }
}

function invoke_hn() {
    clear_previous_feed();

    data = get_feed("hackernews");
    var mainContainer = document.getElementById("feed");

    for (var i = 0; i < data.length; i++) {
        var story = document.createElement("div");
        var link = document.createElement("a");
        link.setAttribute("href", data[i].url);
        var title = document.createTextNode(data[i].title);
        link.appendChild(title);
        story.appendChild(link);

        mainContainer.appendChild(story);
    }
}

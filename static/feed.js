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
        })
        .then((response) => response.json())
        .then((data) => {
            console.log('Success');
            feeder_response_data = data;
        })
        .catch((error) => {
            console.error('Error:', error);
        });

    return feeder_response_data;
}

function invoke_dev() {
    clear_previous_feed();

    data = get_feed("dev");
    var mainContainer = document.getElementById("feed");

    for (var i = 0; i < data.length; i++) {
        var article = document.createElement("div");
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

function invoke_tc() {
    clear_previous_feed();

    data = get_feed("techcrunch");
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

function invoke_ph() {
    clear_previous_feed();

    data = get_feed("producthunt");
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

function invoke_fcc() {
    clear_previous_feed();

    data = get_feed("freecodecamp");
    var mainContainer = document.getElementById("feed");

    for (var i = 0; i < data.length; i++) {
        var article = document.createElement("div");
        var link = document.createElement("a");
        link.setAttribute("href", data[i].link);
        var title = document.createTextNode(data[i].title);
        link.appendChild(title);
        article.appendChild(link);

        mainContainer.appendChild(article);
    }
}

function invoke_hackernoon() {
    clear_previous_feed();

    data = get_feed("hackernoon");
    var mainContainer = document.getElementById("feed");

    for (var i = 0; i < data.length; i++) {
        var article = document.createElement("div");
        var link = document.createElement("a");
        link.setAttribute("href", data[i].link);
        var title = document.createTextNode(data[i].title);
        link.appendChild(title);
        article.appendChild(link);

        mainContainer.appendChild(article);
    }
}

function reddit(sub) {
    clear_previous_feed();

    const data = {
        feed: 'reddit',
        sub: sub
    };
    fetch('/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(data),
        })
        .then((response) => response.json())
        .then((data) => {
            console.log('Success');
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
        })
        .catch((error) => {
            console.error('Error:', error);
        });
}
function storycount(argument) {
    feed_cards = document.getElementsByClassName("feed-card");
    var ff = document.getElementById("filter-feed");
    var scount = document.createElement("div");
    scount.setAttribute("id", "story-count");
    scount.innerHTML = feed_cards.length + " stories fetched";
    // attach after div="filter-feed"
    ff.parentNode.insertBefore(scount, ff.nextSibling);
}

function rewrite_summary(argument) {
    fs = document.getElementsByClassName("feed-summary");
    for (var i = 0; i < fs.length; i++) {
        fs[i].innerHTML = fs[i].textContent;
    }
}

function rewrite_description(argument) {
    fs = document.getElementsByClassName("feed-description");
    for (var i = 0; i < fs.length; i++) {
        fs[i].innerHTML = fs[i].textContent;
    }
}

function append_feed(data) {
    var mainContainer = document.getElementById("feed");

    for (var i = 0; i < data.length; i++) {

        feed_card = document.createElement("div");
        feed_card.setAttribute("class", "feed-card");
        h4 = document.createElement("h4");
        h4.textContent = data[i].title;
        /*        blockquote = document.createElement("blockquote");
                blockquote.textContent = data[i].published_parsed.tm_day;*/

        var link = document.createElement("a");

        link.setAttribute("href", data[i].link);
        var title = document.createTextNode(data[i].title);

        link.appendChild(title);

        feed_card.appendChild(link);
        feed_card.appendChild(h4);
        //feed_card.appendChild(blockquote);

        mainContainer.appendChild(feed_card);
    }
}

function fetch_feed(argument) {
    var feed = document.getElementById("feed-input").value;
    clear_previous_feed();

    get_feed(feed);
}

function clear_previous_feed() {
    // remove all childs of "feed"
    const feed_div = document.getElementById("feed");
    feed_div.innerHTML = '';
    const story_count = document.getElementById("story-count");
    if (story_count != null){
        story_count.innerHTML = '';
    }
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
        setTimeout(append_feed, 500, data);
    });
}

function share(title, link) {
    if (navigator.share) {
        navigator.share({
                title: title,
                url: link,
            })
            .then(() => console.log('Successful Share'))
            .catch((error) => console.log('Error sharing', error));
    }
}

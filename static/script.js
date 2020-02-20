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
    deleteLoadSVG();
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
    addLoadSVG();
    clear_previous_feed();

    get_feed(feed);
}

function clear_previous_feed() {
    // remove all childs of "feed"
    const feed_div = document.getElementById("feed");
    feed_div.innerHTML = '';
    const story_count = document.getElementById("story-count");
    story_count.innerHTML = '';
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

function show_subreddits(argument) {
    container1 = document.getElementById("filter-feed");
    var input = document.createElement("input");
    input.setAttribute("name", "subreddit");
    input.setAttribute("list", "subreddit");

    label = document.createElement("label");
    label.setAttribute("for", "subreddit");
    label.innerHTML = "Select Subreddit";

    data_list = document.createElement("datalist");
    data_list.setAttribute("id", "subreddit");

    input.appendChild(data_list);
    var sub_div = document.getElementById("subreddit-div");
    sub_div.appendChild(label);
    sub_div.appendChild(input);
    /*          <input name="subreddit" list="subreddit" />
                <datalist id="subreddit"></datalist> */
    container1.appendChild(sub_div);
    var subreddit_options = ["programming", "Android", "webdev", "technology", "python", "javascript", "learnprogramming", "software", "startups", "tech", "web_design", "linux", "computing", "coding", "AskTechnology", "cpp"];
    var options = '';

    for (var i = 0; i < subreddit_options.length; i++)
        options += '<option value="' + subreddit_options[i] + '" />';

    document.getElementById('subreddit').innerHTML = options;
}
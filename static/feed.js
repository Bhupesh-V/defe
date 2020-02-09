function removethis() {
    // remove all childs of "feed"
    const feed_div = document.getElementById("feed");
    feed_div.innerHTML = '';
}

function invoke_dev() {
    removethis();

    const data = {
        feed: 'dev'
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
                var article = document.createElement("div");
                var link = document.createElement("a");
                link.setAttribute("href", data[i].url);
                var title = document.createTextNode(data[i].title);
                link.appendChild(title);
                article.appendChild(link);

                mainContainer.appendChild(article);
            }
        })
        .catch((error) => {
            console.error('Error:', error);
        });
}

function invoke_hn() {
    removethis();

    const data = {
        feed: 'hackernews'
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
                link.setAttribute("href", data[i].url);
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

function invoke_tc() {
    removethis();

    const data = {
        feed: 'techcrunch'
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

function reddit(sub) {
    removethis();

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
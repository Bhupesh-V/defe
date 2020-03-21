let deferredPrompt;
const btnAdd = document.querySelector('#btnAdd');

window.addEventListener('beforeinstallprompt', (e) => {
    console.log('beforeinstallprompt event fired');
    e.preventDefault();
    deferredPrompt = e;
    btnAdd.style.visibility = 'visible';
});

btnAdd.addEventListener('click', (e) => {
    btnAdd.style.visibility = 'hidden';
    deferredPrompt.prompt();
    deferredPrompt.userChoice.then((choiceResult) => {
        if (choiceResult.outcome === 'accepted') {
            console.log('User accepted the A2HS prompt');
        } else {
            console.log('User dismissed the A2HS prompt');
        }
        deferredPrompt = null;
    });
});

function storycount(argument) {
    feed_cards = document.getElementsByClassName("feed-card");
    var ff = document.getElementById("filter-feed");
    var scount = document.createElement("div");
    scount.setAttribute("id", "story-count");
    scount.innerHTML = feed_cards.length + " stories fetched ✨";
    // attach after div="filter-feed"
    if (ff != null) {
        ff.parentNode.insertBefore(scount, ff.nextSibling);
    }
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


function clear_previous_feed() {
    // remove all childs of "feed"
    const feed_div = document.getElementById("feed");
    feed_div.innerHTML = '';
    const story_count = document.getElementById("story-count");
    if (story_count != null) {
        story_count.innerHTML = '';
    }
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

function get_version_info() {
    const fetchPromise = fetch('https://api.github.com/repos/Bhupesh-V/tutorialdb/releases');
    fetchPromise.then(response => {
        return response.json();
    }).then(releases => {
        version_ref = document.getElementById("version-info");
        if (version_ref != null) {
            version_ref.innerHTML = releases[0].name;
        }
        version_ref_nav = document.getElementById("version-info-nav");
        if (version_ref_nav != null) {
            version_ref_nav.innerHTML = "Version " + releases[0].name;
        }
    });
}

function copyToClip(str) {
    function listener(e) {
        e.clipboardData.setData("text/html", str);
        e.clipboardData.setData("text/plain", str);
        e.preventDefault();
    }
    document.addEventListener("copy", listener);
    document.execCommand("copy");
    document.removeEventListener("copy", listener);
};

function select_feed(e) {
    var curr_location = window.location.pathname;
    document.getElementById("fetchfeed").href = curr_location + "?filter=" + escape(e.target.value);
}

function display_loading() {
    var loading_element = document.querySelector(".progress");
    loading_element.style.display = "block";
}

function media_notify(podcast, author, podcast_url) {
/*    console.log(podcast);
    var podcast_list = [];
    var pod = document.querySelector("audio");
    for (var podcast_ele = 0; podcast_ele < pod.link; podcast_ele++) {
        podcast_list.push(podcast_ele[0].src);
    }*/
    // When audio starts playing...
    if ('mediaSession' in navigator) {
        navigator.mediaSession.metadata = new MediaMetadata({
            title: podcast,
            artist: author
        });

/*        navigator.mediaSession.setActionHandler('play', function() {});
        navigator.mediaSession.setActionHandler('pause', function() {});
        navigator.mediaSession.setActionHandler('previoustrack', function(podcast_list) {
            current_podcast = podcast_list.indexOf(podcast_url);
            index = (index - 1 + playlist.length) % playlist.length;
            playAudio();
        });
        navigator.mediaSession.setActionHandler('nexttrack', function() {})*/
    }
}
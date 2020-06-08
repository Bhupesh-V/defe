let deferredPrompt;
const btnAdd = document.querySelector("#btnAdd");

window.addEventListener("beforeinstallprompt", (e) => {
    console.log("beforeinstallprompt event fired");
    e.preventDefault();
    deferredPrompt = e;
    btnAdd.style.visibility = "visible";
});

btnAdd.addEventListener("click", (e) => {
    btnAdd.style.visibility = "hidden";
    deferredPrompt.prompt();
    deferredPrompt.userChoice.then((choiceResult) => {
        if (choiceResult.outcome === "accepted") {
            console.log("User accepted the A2HS prompt");
        } else {
            console.log("User dismissed the A2HS prompt");
        }
        deferredPrompt = null;
    });
});

function storyCount(argument) {
    var feedCards = document.getElementsByClassName("feed-card");
    var filterFeedElement = document.getElementById("filter-feed");
    var storyCountElement = document.createElement("div");
    storyCountElement.setAttribute("id", "story-count");
    storyCountElement.innerHTML = feedCards.length + " stories fetched ✨";
    // attach after div="filter-feed"
    if (filterFeedElement !== null) {
        filterFeedElement.parentNode.insertBefore(storyCountElement, filterFeedElement.nextSibling);
    }
}

function rewriteSummary(argument) {
    var feedSummary = document.getElementsByClassName("feed-summary");
    for (var i = 0; i < feedSummary.length; i++) {
        feedSummary[i].innerHTML = feedSummary[i].textContent;
    }
}

function rewriteDescription(argument) {
    var feedDescription = document.getElementsByClassName("feed-description");
    for (var i = 0; i < feedDescription.length; i++) {
        feedDescription[i].innerHTML = feedDescription[i].textContent;
    }
}


function clear_previous_feed() {
    // remove all childs of "feed"
    const feed = document.getElementById("feed");
    feed.innerHTML = "";
    const storyCount = document.getElementById("story-count");
    if (storyCount !== null) {
        storyCount.innerHTML = "";
    }
}


function share(feedTitle, feedLink) {
    if (navigator.share) {
        navigator.share({
                title: feedTitle,
                url: feedLink,
            })
            .then(() => console.log("Successful Share"))
            .catch((error) => console.log("Error sharing", error));
    }
}

function get_version_info() {
    const fetchPromise = fetch("https://api.github.com/repos/Bhupesh-V/defe/releases");
    fetchPromise.then(response => {
        return response.json();
    }).then(releases => {
        var versionElement = document.getElementById("version-info");
        if (versionElement !== null) {
            versionElement.innerHTML = releases[0].name;
        }
        var versionNavElement = document.getElementById("version-info-nav");
        if (versionNavElement !== null) {
            versionNavElement.innerHTML = "Version " + releases[0].name;
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
}

function select_feed(e) {
    var currentPath = window.location.pathname;
    document.getElementById("fetchfeed").href = currentPath + "?filter=" + escape(e.target.value);
}

function displayLoading() {
    var loading_element = document.querySelector(".progress");
    loading_element.style.display = "block";
}

function media_notify(podcast, author, image, podcast_src) {
    /*    console.log(podcast);
        var podcast_list = [];
        var pod = document.querySelector("audio");
        for (var podcast_ele = 0; podcast_ele < pod.link; podcast_ele++) {
            podcast_list.push(podcast_ele[0].src);
        }*/
    // When audio starts playing...
    if ("mediaSession" in navigator) {
        navigator.mediaSession.metadata = new MediaMetadata({
            title: podcast,
            artist: author,
            album: podcast_src,
            artwork: [{
                src: image,
                sizes: '3000x3000',
                type: 'image/jpg'
            }]
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

function implement_dark_mode() {
    document.querySelector('body').classList.add('dark');
}

function implement_light_mode() {
    document.querySelector('body').classList.remove('dark');
}

function local_storage_supported() {
    var test = 'test';
    try {
        localStorage.setItem(test, test);
        localStorage.removeItem(test);
        return true;
    } catch(e) {
        return false;
    }
}

function toggle_darkmode() {
    if (!local_storage_supported()) {
        return;
    }
    const currentMode = localStorage.getItem('mode');
    if (currentMode === 'dark') {
        localStorage.setItem('mode', 'light');
        implement_light_mode();
    } else {
        localStorage.setItem('mode', 'dark');
        implement_dark_mode();
    }
}

function apply_theme() {
    if (!local_storage_supported()) {
        return;
    }
    const theme_name = localStorage.getItem("mode");
    if (theme_name === 'dark') {
        implement_dark_mode();
    } else {
        implement_light_mode();
    }
}

function add_service_worker() {
    if ("serviceWorker" in navigator) {
        navigator.serviceWorker.register("/sw.js").then(function(registration) {
          console.log("ServiceWorker registration successful with scope: ", registration.scope);
        }).catch(function(err) {
          console.log("ServiceWorker registration failed: ", err);
        });
    }
}
self.addEventListener("fetch", fetchEvent => {
  fetchEvent.respondWith(
    caches.match(fetchEvent.request).then(res => {
      return res || fetch(fetchEvent.request)
    })
  )
})

const staticdevfeed = "devfeed-site-v1"
const assets = [
  "/",
  "/static/script.js",
  "/static/js/materialize.js",
  "/static/js/materialize.min.js",
  "/static/css/materialize.css",
  "/static/css/materialize.min.css",
  "/static/css/custom.css",
  "/static/images/email.png",
  "/static/images/telegram.png",
  "/static/images/twitter.png",
]

self.addEventListener("install", installEvent => {
  console.log('[ServiceWorker] Install');
  installEvent.waitUntil(
    caches.open(staticdevfeed).then(cache => {
      cache.addAll(assets)
    })
  )
})

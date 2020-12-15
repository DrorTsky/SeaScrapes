

importScripts(
  "https://storage.googleapis.com/workbox-cdn/releases/5.1.2/workbox-sw.js"
);

if (workbox) {
  console.log(`Yay! Workbox is loaded 🎉`);
} else {
  console.log(`Boo! Workbox didn't load 😬`);
}
url_not_2_cache = ["silk", "admin", "API", "accounts"];

workbox.routing.registerRoute(
  ({ url }) => url.href.includes("API/user.json"),
  new workbox.strategies.NetworkFirst()
);

workbox.routing.registerRoute(
  ({ url }) => !url_not_2_cache.some((key) => url.href.includes(key)),
  new workbox.strategies.StaleWhileRevalidate({
    cacheName: "SW-cache",
  })
);
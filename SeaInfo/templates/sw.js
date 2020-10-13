// ************** 
// CACHE
// **************

// const cacheName = 'Scrapes';
// const resourcesToPrecache = [
//     'base.html',
//     'SeaInfo/forecast.html',
//     'SeaInfo/sea_details.html',
//     'SeaInfo/wave_forecast.html',
//     'static/js/app.js',
//     'static/css/styles.css',
// ];

// // ************** 
// // INSTALL EVENT
// // **************

// self.addEventListener('install', event => {
//     console.log("installed");
//     event.waitUntil(caches.open(cacheName)
//     .then(cache => {
//         return cache.addAll(resourcesToPrecache);
//     })
//     .then(self.skipWaiting())
//     );
// });

// // ************** 
// // ACTIVATE EVENR
// // **************

// self.addEventListener('activate', event => {
//     event.waitUntil(self.clients.claim());
// });

// // ************** 
// // FETCH EVENT
// // **************

// self.addEventListener('fetch', function(event) {
//     event.respondWith(
//       caches.open(cacheName).then(function(cache) {
//         return fetch(event.request).then(function(response) {
//           cache.put(event.request, response.clone());
//           return response || fetch(event.request);;
//         });
//       })
//     );
//   });


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
/*
 Copyright 2016 Google Inc. All Rights Reserved.
 Licensed under the Apache License, Version 2.0 (the "License");
 you may not use this file except in compliance with the License.
 You may obtain a copy of the License at
 http://www.apache.org/licenses/LICENSE-2.0
 Unless required by applicable law or agreed to in writing, software
 distributed under the License is distributed on an "AS IS" BASIS,
 WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 See the License for the specific language governing permissions and
 limitations under the License.
 */

// Names of the two caches used in this version of the service worker.
// Change to v2, etc. when you update any of the local resources, which will
// in turn trigger the install event again.
const PRECACHE = 'precache-v0.0.22';
const RUNTIME = 'runtime-v0.0.22';
importScripts('https://storage.googleapis.com/workbox-cdn/releases/5.1.2/workbox-sw.js');

// importScripts('https://storage.googleapis.com/workbox-cdn/releases/4.3.1/workbox-sw.js');

if (workbox) {
  console.log(`Workbox loaded.`);
} else {
  console.log(`ERROR: Workbox failed to load.`);
}

workbox.precaching.precacheAndRoute([]);


// workbox.routing.registerRoute(
//   /\.js$/,
//   // Use cache but update in the background.
//   new workbox.strategies.StaleWhileRevalidate({
//     // Use a custom cache name.
//     cacheName: 'js-cache',
//   })
// );

// workbox.routing.registerRoute(
//   /\.(?:js|css)$/,
//   new workbox.strategies.StaleWhileRevalidate({
//     cacheName: 'static-resources',
//   })
// );


addEventListener('message', (event) => {
  console.log("message received I  guess.")
  if (event.data && event.data.type === 'SKIP_WAITING') {
    skipWaiting();
  }
});
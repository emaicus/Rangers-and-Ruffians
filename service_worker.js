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
const PRECACHE = 'precache-v0.0.18';
const RUNTIME = 'runtime-v0.0.18';

// A list of local resources we always want to be cached.
const PRECACHE_URLS = [
  // Copy pasted from script
  "new_site/images/race/male/gnome.jpg",
  "new_site/images/class/sorcerer.jpg",
  "new_site/images/class/druid.jpg",
  "new_site/icons/flame.svg",
  "new_site/images/class/female/highborn.jpg",
  "new_site/images/class/female/monk.jpg",
  "new_site/icons/favicon/android-chrome-512x512.png",
  "new_site/images/class/barbarian.jpg",
  "new_site/images/race/female/kragraven.jpg",
  "new_site/images/race/female/hardfoot_halfling.jpg",
  "new_site/images/race/male/dwarf.jpg",
  "new_site/icons/favicon/android-chrome-192x192.png",
  "new_site/images/race/female/waterborn.jpg",
  "new_site/images/class/wizard.jpg",
  "new_site/known_dependencies.json",
  "new_site/images/class/male/fighter.jpg",
  "new_site/images/class/ranger.jpg",
  "new_site/images/backdrops/landscape_character_creation.jpg",
  "new_site/images/race/male/hissling.jpg",
  "new_site/images/backdrops/portrait_character_creation.jpg",
  "new_site/images/race/female/sprout.jpg",
  "new_site/images/race/male/lizkin.jpg",
  "new_site/images/class/female/archer.jpg",
  "new_site/printed_materials/standard_character_sheet.pdf",
  "new_site/icons/swap-bag.svg",
  "new_site/images/race/female/high_elf.jpg",
  "new_site/images/backdrops/landscape_beasts.jpg",
  "new_site/icons/power-lightning.svg",
  "new_site/icons/magic-swirl.svg",
  "new_site/images/class/knight.jpg",
  "new_site/pages/level_up_sheet.html",
  "new_site/icons/favicon/browserconfig.xml",
  "new_site/templates/selector_template.html",
  "new_site/icons/favicon/favicon-16x16.png",
  "new_site/images/race/male/kragraven.jpg",
  "new_site/images/class/bard.jpg",
  "new_site/css/rangers.css",
  "new_site/images/race/female/deep_elf.jpg",
  "new_site/images/race/male/catterwol.jpg",
  "new_site/images/race/male/human.jpg",
  "new_site/images/race/male/waterborn.jpg",
  "new_site/js/nunjucks.js",
  "new_site/images/race/male/orc.jpg",
  "new_site/templates/character_sheet_template.html",
  "new_site/icons/circle.svg",
  "new_site/icons/favicon/favicon-32x32.png",
  "new_site/images/race/female/catterwol.jpg",
  "new_site/templates/role_selection_template.html",
  "new_site/images/race/female/goblin.jpg",
  "new_site/icons/quiver.svg",
  "new_site/icons/prayer.svg",
  "new_site/pages/GENERATED/Printed_Materials.html",
  "new_site/images/backdrops/landscape_ancients.jpg",
  "new_site/images/race/female/wood_elf.jpg",
  "new_site/images/class/highborn.jpg",
  "new_site/images/class/necromancer.jpg",
  "new_site/icons/hearts.svg",
  "new_site/pages/GENERATED/Book_of_Known_Beasts.html",
  "new_site/pages/GENERATED/ALT.json",
  "new_site/images/race/male/high_elf.jpg",
  "new_site/images/race/female/daemonspawn.jpg",
  "new_site/images/class/male/knight.jpg",
  "new_site/icons/favicon/mstile-150x150.png",
  "new_site/images/class/hedge_knight.jpg",
  "new_site/pages/GENERATED/Book_of_Lore.html",
  "new_site/images/class/monk.jpg",
  "new_site/images/class/female/gunslinger.jpg",
  "new_site/css/character_selection.css",
  "new_site/images/class/archer.jpg",
  "new_site/images/backdrops/portrait_banner.jpg",
  "new_site/images/race/female/human.jpg",
  "new_site/images/race/male/goblin.jpg",
  "new_site/icons/bordered-shield.svg",
  "new_site/images/backdrops/portrait_changelog.jpg",
  "new_site/images/class/rogue.jpg",
  "new_site/pages/GENERATED/Changelog.html",
  "new_site/images/class/fighter.jpg",
  "new_site/images/race/female/lizkin.jpg",
  "new_site/pages/GENERATED/Tome_of_the_Ancients.html",
  "new_site/images/race/male/daemonspawn.jpg",
  "new_site/images/race/female/orc.jpg",
  "new_site/images/backdrops/landscape_banner.jpg",
  "new_site/images/class/paladin.jpg",
  "new_site/images/class/male/cleric.jpg",
  "new_site/pages/character_sheet.html",
  "new_site/images/class/cleric.jpg",
  "new_site/printed_materials/visual_character_sheet.pdf",
  "new_site/templates/level_up_sheet_template.html",
  "new_site/images/race/male/sprout.jpg",
  "new_site/icons/circle-halved.svg",
  "new_site/pages/GENERATED/Rulebook.html",
  "new_site/images/class/beastmaster.jpg",
  "new_site/icons/favicon/apple-touch-icon.png",
  "new_site/icons/shield.svg",
  "new_site/icons/ink-swirl.svg",
  "new_site/images/class/gunslinger.jpg",
  "new_site/images/backdrops/landscape_lore.jpg",
  "new_site/images/class/female/beastmaster.jpg",
  "new_site/icons/fire-spell-cast.svg",
  "new_site/icons/favicon/favicon.ico",
  "new_site/images/race/male/automaton.jpg",
  "new_site/images/race/male/wood_elf.jpg",
  "new_site/images/class/battle_mage.jpg",
  "new_site/icons/swords-power.svg",
  "new_site/pages/GENERATED/Compendium_of_Character_Creation.html",
  "new_site/icons/favicon/safari-pinned-tab.svg",
  "new_site/images/race/male/deep_elf.jpg",
  "new_site/js/rangers.js",
  "new_site/images/class/female/sorcerer.jpg",
  "new_site/images/backdrops/portrait_lore.jpg",
  "new_site/pages/character_creation_helper_page.html",
  "new_site/images/backdrops/landscape_rulebook.jpg",
  "new_site/templates/character_creation_helper_template.html",
  "new_site/images/backdrops/portrait_ancients.jpg",
  "new_site/icons/tombstone.svg",
  "new_site/images/race/female/gnome.jpg",
  "new_site/images/race/male/halfling.jpg",
  "new_site/images/race/female/dwarf.jpg",
  "new_site/css/character_creation_helper.css",
  "new_site/templates/character_selection_template.html",
  "new_site/images/class/male/alt_knight.jpg",
  "new_site/pages/GENERATED/Poohbah_Printables.html",
  "new_site/images/backdrops/portrait_beasts.jpg",
  "new_site/icons/raise-zombie.svg",
  "new_site/icons/sword-brandish.svg",
  "new_site/images/race/female/automaton.jpg",
  "new_site/pages/GENERATED/Examples.html",
  "new_site/images/class/magic_arrow.jpg",
  "new_site/images/backdrops/portrait_rulebook.jpg",
  "new_site/images/class/male/rogue.jpg",
  "new_site/css/iterated_char_sheet.css",
  "new_site/icons/bolt-shield.svg",
  "new_site/images/race/female/fleetfoot_halfling.jpg",
  "new_site/images/race/female/hissling.jpg",
  "new_site/icons/heart-beats.svg",
  "/assets/css/style.css",
  "/node_modules/bootstrap-select/dist/js/bootstrap-select.min.js",
  "/node_modules/bootstrap/dist/js/bootstrap.min.js",
  "/node_modules/jquery/dist/jquery.min.js",
  "/node_modules/popper.js/dist/umd/popper.min.js",
  "/site.webmanifest",
  // pages
  'index.html',
  './', // Alias for index.html
];

// The install handler takes care of precaching the resources we always need.
self.addEventListener('install', event => {
  event.waitUntil(
    caches.open(PRECACHE)
      .then(cache => cache.addAll(PRECACHE_URLS))
      .then(self.skipWaiting())
  );
});

// The activate handler takes care of cleaning up old caches.
self.addEventListener('activate', event => {
  const currentCaches = [PRECACHE, RUNTIME];
  event.waitUntil(
    caches.keys().then(cacheNames => {
      return cacheNames.filter(cacheName => !currentCaches.includes(cacheName));
    }).then(cachesToDelete => {
      return Promise.all(cachesToDelete.map(cacheToDelete => {
        return caches.delete(cacheToDelete);
      }));
    }).then(() => self.clients.claim())
  );
});

// The fetch handler serves responses for same-origin resources from a cache.
// If no response is found, it populates the runtime cache with the response
// from the network before returning it to the page.
self.addEventListener('fetch', event => {
  // Skip cross-origin requests, like those for Google Analytics.
  if (event.request.url.startsWith(self.location.origin)) {
    event.respondWith(
      caches.match(event.request).then(cachedResponse => {
        if (cachedResponse) {
          return cachedResponse;
        }

        return caches.open(RUNTIME).then(cache => {
          return fetch(event.request)
            .catch(function(error) { console.log("ERROR!") })
            .then(response => {
            // Put a copy of the response in the runtime cache.
            return cache.put(event.request, response.clone()).then(() => {
              return response;
            });
          })
        });
      })
    );
  }
});
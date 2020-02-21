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

importScripts('https://storage.googleapis.com/workbox-cdn/releases/4.3.1/workbox-sw.js');

if (workbox) {
  console.log(`Workbox loaded.`);
} else {
  console.log(`ERROR: Workbox failed to load.`);
}

workbox.precaching.precacheAndRoute([
  {
    "url": "new_site/css/character_creation_helper.css",
    "revision": "d41d8cd98f00b204e9800998ecf8427e"
  },
  {
    "url": "new_site/css/character_selection.css",
    "revision": "5351f61fed9d7ece2b4767d04eea02b6"
  },
  {
    "url": "new_site/css/iterated_char_sheet.css",
    "revision": "388d4393bc3d603cbcc91cfabd956a38"
  },
  {
    "url": "new_site/css/rangers.css",
    "revision": "dce4b1e899df221f966c792f2306f2fc"
  },
  {
    "url": "new_site/css/two_sided_character_sheet.css",
    "revision": "5c257a9ed6d120944c26b43f79db3477"
  },
  {
    "url": "new_site/icons/bolt-shield.svg",
    "revision": "15597019d5e5ecb94339f1c3a14dad3b"
  },
  {
    "url": "new_site/icons/bordered-shield.svg",
    "revision": "2817f846d2581d39be55b8532e233ca1"
  },
  {
    "url": "new_site/icons/circle-halved.svg",
    "revision": "bf8b93da9a86eaec639f942f6377e4d8"
  },
  {
    "url": "new_site/icons/circle.svg",
    "revision": "a1eb0f67100d684bb055cf1605ebc86a"
  },
  {
    "url": "new_site/icons/fast-backward-button.svg",
    "revision": "8b66a30bce8737653e0a2722f8d4271c"
  },
  {
    "url": "new_site/icons/favicon/android-chrome-192x192.png",
    "revision": "ab2a1ccdea67316da8c94952f8556a52"
  },
  {
    "url": "new_site/icons/favicon/android-chrome-512x512.png",
    "revision": "83cf00ca81517e5a0178f3322895462b"
  },
  {
    "url": "new_site/icons/favicon/apple-touch-icon.png",
    "revision": "98a23a75e655ec08f2b91fa9b0b0dd96"
  },
  {
    "url": "new_site/icons/favicon/favicon-16x16.png",
    "revision": "93e6f1244ed4772f8392f390a1eca560"
  },
  {
    "url": "new_site/icons/favicon/favicon-32x32.png",
    "revision": "2534f65605216584b632c9003835b9c3"
  },
  {
    "url": "new_site/icons/favicon/favicon.ico",
    "revision": "3a98ca9abe14bc47f5ef6a53d66e30a9"
  },
  {
    "url": "new_site/icons/favicon/mstile-150x150.png",
    "revision": "0f472f85aa4becee99d607ce59371054"
  },
  {
    "url": "new_site/icons/favicon/safari-pinned-tab.svg",
    "revision": "f99372dd39eefaacda39fa89afc985fc"
  },
  {
    "url": "new_site/icons/fire-spell-cast.svg",
    "revision": "e6c09f4fceb5d0f9b9da29547102801e"
  },
  {
    "url": "new_site/icons/flame.svg",
    "revision": "e7879a3663ef74eb3d6f54de66f1d54d"
  },
  {
    "url": "new_site/icons/heart-beats.svg",
    "revision": "78b50894a514de0ff5d61a5c454b4d5d"
  },
  {
    "url": "new_site/icons/hearts.svg",
    "revision": "034a48b95c54e76616dc0e042b79cace"
  },
  {
    "url": "new_site/icons/ink-swirl.svg",
    "revision": "03f49b4335e04b72962a39500550bcd0"
  },
  {
    "url": "new_site/icons/magic-swirl.svg",
    "revision": "4b5f5651f170ee64e54d4b097e18f2d7"
  },
  {
    "url": "new_site/icons/power-lightning.svg",
    "revision": "96d1686c81be23108c2b1406f257bfbc"
  },
  {
    "url": "new_site/icons/prayer.svg",
    "revision": "68f8bc222e88c2fa69518c8fdb44d230"
  },
  {
    "url": "new_site/icons/quiver.svg",
    "revision": "901d20011d0dc10cc23b3f0558993a33"
  },
  {
    "url": "new_site/icons/raise-zombie.svg",
    "revision": "7a1e1dc035aaa4789c7e7acef779ad7c"
  },
  {
    "url": "new_site/icons/shield.svg",
    "revision": "8396f1cb288bb874fabd6fb1dc5bee2b"
  },
  {
    "url": "new_site/icons/swap-bag.svg",
    "revision": "afec826ccb7fa028059ef137e6ef1102"
  },
  {
    "url": "new_site/icons/sword-brandish.svg",
    "revision": "218202da8fc960eb2c13a2ee20b7d5b5"
  },
  {
    "url": "new_site/icons/swords-power.svg",
    "revision": "50efddea824e634ab7a44d8f432de928"
  },
  {
    "url": "new_site/icons/tombstone.svg",
    "revision": "5080916dfa69b9c2adac3a167f1052a7"
  },
  {
    "url": "new_site/images/backdrops/landscape_ancients.jpg",
    "revision": "e22e7269fb9314452b72d23ea43cbc60"
  },
  {
    "url": "new_site/images/backdrops/landscape_banner.jpg",
    "revision": "5580f710d66b5e4cd4dfe99c46691c86"
  },
  {
    "url": "new_site/images/backdrops/landscape_beasts.jpg",
    "revision": "7a33c0a62c5fab937b4b7677523e7eb4"
  },
  {
    "url": "new_site/images/backdrops/landscape_character_creation.jpg",
    "revision": "c5e0795787e1db3cbb753f98c98b4510"
  },
  {
    "url": "new_site/images/backdrops/landscape_lore.jpg",
    "revision": "6a27c2037518e35e4c4ee58f6de9aa97"
  },
  {
    "url": "new_site/images/backdrops/landscape_rulebook.jpg",
    "revision": "b2ee495bc25a7026f43ea7db8272c8c7"
  },
  {
    "url": "new_site/images/backdrops/portrait_ancients.jpg",
    "revision": "7ec9decf862921cc1ea60bea762bd9d9"
  },
  {
    "url": "new_site/images/backdrops/portrait_banner.jpg",
    "revision": "5980bf88e7efc5d841ee9671ab15161f"
  },
  {
    "url": "new_site/images/backdrops/portrait_beasts.jpg",
    "revision": "71a0161a70b465cd1156f92360a7d501"
  },
  {
    "url": "new_site/images/backdrops/portrait_changelog.jpg",
    "revision": "9653915b6ca59c6d39aa4ce3a2ea9a8d"
  },
  {
    "url": "new_site/images/backdrops/portrait_character_creation.jpg",
    "revision": "6a683801cbac81f4ea43375927fabbde"
  },
  {
    "url": "new_site/images/backdrops/portrait_lore.jpg",
    "revision": "27cc0755e47d500a2bee7c17e7cd1194"
  },
  {
    "url": "new_site/images/backdrops/portrait_rulebook.jpg",
    "revision": "dc3f2ed21d0f1715ad88f57cf09daaeb"
  },
  {
    "url": "new_site/images/class/barbarian.jpg",
    "revision": "b2172b0688299e11d4f78e2d8a6d3b05"
  },
  {
    "url": "new_site/images/class/bard.jpg",
    "revision": "9cae1e59e04670a9d525051951d7af68"
  },
  {
    "url": "new_site/images/class/cleric.jpg",
    "revision": "fd91d6aedf758c204f31f30cd6325f03"
  },
  {
    "url": "new_site/images/class/druid.jpg",
    "revision": "d27f0aef1dc566bd36d27422e662ba5e"
  },
  {
    "url": "new_site/images/class/female/archer.jpg",
    "revision": "e307193a995d45f8dfd0823817d60929"
  },
  {
    "url": "new_site/images/class/female/beastmaster.jpg",
    "revision": "782c91369af5f3f3a5e1b4bc601d859c"
  },
  {
    "url": "new_site/images/class/fighter.jpg",
    "revision": "d8b3923fbf791754e06513f8477c298a"
  },
  {
    "url": "new_site/images/class/gunslinger.jpg",
    "revision": "71aacf4abd579be8cef7cd3424386bf1"
  },
  {
    "url": "new_site/images/class/highborn.jpg",
    "revision": "4df3aec08c7de62d136b9266aae6bd29"
  },
  {
    "url": "new_site/images/class/male/knight.jpg",
    "revision": "f0b835bd2e4e24965be812f191921670"
  },
  {
    "url": "new_site/images/class/male/rogue.jpg",
    "revision": "85542a55467e48e83214cd8bdb5b8288"
  },
  {
    "url": "new_site/images/class/monk.jpg",
    "revision": "524d941063e99603ccaf0027f48cc54e"
  },
  {
    "url": "new_site/images/class/necromancer.jpg",
    "revision": "8d92816cb04e9e53ac956eb271c6e64b"
  },
  {
    "url": "new_site/images/class/paladin.jpg",
    "revision": "7aef7fee2515cc43067b2419554106d0"
  },
  {
    "url": "new_site/images/class/ranger.jpg",
    "revision": "6bbec3c4a9132c3ccf93602cec423bee"
  },
  {
    "url": "new_site/images/class/sorcerer.jpg",
    "revision": "b5c88a1fc90d3b906d1e426c6bdad30e"
  },
  {
    "url": "new_site/images/class/wizard.jpg",
    "revision": "6a4120f4fcea6e0b0dd4bc70d4f6e658"
  },
  {
    "url": "new_site/images/race/female/catterwol.jpg",
    "revision": "775cc3f7e10770fdb0540d27ac5dcccd"
  },
  {
    "url": "new_site/images/race/female/deep_elf.jpg",
    "revision": "467f98e069bcfe94acdd9f2e1192cf3a"
  },
  {
    "url": "new_site/images/race/female/fleetfoot_halfling.jpg",
    "revision": "d2cd1e738dcaa07cf70d576758cc3146"
  },
  {
    "url": "new_site/images/race/female/gnome.jpg",
    "revision": "e05c11926a86536c9ffd829f63a7f106"
  },
  {
    "url": "new_site/images/race/female/hardfoot_halfling.jpg",
    "revision": "dc073ffa3aad64e46eaccb2b907d6a2a"
  },
  {
    "url": "new_site/images/race/female/high_elf.jpg",
    "revision": "c34619c914fb05a63381af21a48997d7"
  },
  {
    "url": "new_site/images/race/female/orc.jpg",
    "revision": "88e1dee0ab61c729ab76b869e9910bbc"
  },
  {
    "url": "new_site/images/race/female/sprout.jpg",
    "revision": "b1c2bb1a2d69922299a9c39c1e221010"
  },
  {
    "url": "new_site/images/race/female/waterborn.jpg",
    "revision": "065d24d896b4328dea94021229cf4f2e"
  },
  {
    "url": "new_site/images/race/female/wood_elf.jpg",
    "revision": "c29997f8a3d9fa1ccc30ab640923429d"
  },
  {
    "url": "new_site/images/race/male/automaton.jpg",
    "revision": "9de7bcb704dd7804e99e18cfa83d6fb4"
  },
  {
    "url": "new_site/images/race/male/daemonspawn.jpg",
    "revision": "99bad0f4a7fb28b6ffd8a652f8fc91aa"
  },
  {
    "url": "new_site/images/race/male/dwarf.jpg",
    "revision": "7498b94114e2e6875e848c0a0e24a694"
  },
  {
    "url": "new_site/images/race/male/goblin.jpg",
    "revision": "bebfa44ab43d49034e908ff9b0720bf3"
  },
  {
    "url": "new_site/images/race/male/hissling.jpg",
    "revision": "7484df0c4a008e66de38e7955f95dcab"
  },
  {
    "url": "new_site/images/race/male/human.jpg",
    "revision": "939c1eb3a24baccf8ac9f35db938feb8"
  },
  {
    "url": "new_site/images/race/male/kragraven.jpg",
    "revision": "20389ee0b9bd86032c725fce3545ac6f"
  },
  {
    "url": "new_site/images/race/male/lizkin.jpg",
    "revision": "2646b164f0d55091f04b9ec1901816e7"
  },
  {
    "url": "new_site/js/nunjucks.js",
    "revision": "6c7d8c15676636621e7b48dbf1589b6b"
  },
  {
    "url": "new_site/js/rangers.js",
    "revision": "7fe7b6634946aec76bc0f0391ce743b3"
  },
  {
    "url": "new_site/known_dependencies.json",
    "revision": "93129f5a9d5b628abfb7abf46690d95c"
  },
  {
    "url": "new_site/pages/character_creation_helper_page.html",
    "revision": "56c89e9ac009ea5d161f7e83e4ba95b7"
  },
  {
    "url": "new_site/pages/character_sheet.html",
    "revision": "5b6c6be751108e44f7c10408494e8073"
  },
  {
    "url": "new_site/pages/GENERATED/ALT.json",
    "revision": "4383fe24988e4211784b2e02a7baad7a"
  },
  {
    "url": "new_site/pages/GENERATED/Book_of_Known_Beasts.html",
    "revision": "76d4bf6c3fff85f7da33346687c7be6b"
  },
  {
    "url": "new_site/pages/GENERATED/Book_of_Lore.html",
    "revision": "c9f896604dd3d2afc3a8a2e0f4ba46ab"
  },
  {
    "url": "new_site/pages/GENERATED/Changelog.html",
    "revision": "6ac61837476c44192d4267820d0ca8c3"
  },
  {
    "url": "new_site/pages/GENERATED/Compendium_of_Character_Creation.html",
    "revision": "4829cd15b0ede8b5abe964599adb0740"
  },
  {
    "url": "new_site/pages/GENERATED/Examples.html",
    "revision": "8e5a85686f3437032d60ef5679a98696"
  },
  {
    "url": "new_site/pages/GENERATED/Examples.md",
    "revision": "8aaf19c18647c8ea210ab92b58479ac7"
  },
  {
    "url": "new_site/pages/GENERATED/Poohbah_Printables.html",
    "revision": "6131c993a24982665816efcd18aefd09"
  },
  {
    "url": "new_site/pages/GENERATED/Printed_Materials.html",
    "revision": "2bb1f700ab8b36455efe8f2a4e27a864"
  },
  {
    "url": "new_site/pages/GENERATED/Rulebook.html",
    "revision": "c5e3f15a341b51c8492f58f3745a1e7f"
  },
  {
    "url": "new_site/pages/GENERATED/Tome_of_the_Ancients.html",
    "revision": "e3b08bbac7168c2e09d09b3f3b62c202"
  },
  {
    "url": "new_site/pages/level_up_sheet.html",
    "revision": "97182cc377215087d486ff865e1d7483"
  },
  {
    "url": "new_site/pages/weapons.html",
    "revision": "29402cdbd6aa7ccf38634d3bf7f73f4f"
  },
  {
    "url": "new_site/pages/weapons.md",
    "revision": "d41d8cd98f00b204e9800998ecf8427e"
  },
  {
    "url": "new_site/printed_materials/standard_character_sheet.pdf",
    "revision": "d35a5df20af914ebddcf1d8a75d25dd6"
  },
  {
    "url": "new_site/printed_materials/visual_character_sheet.pdf",
    "revision": "6d820079132e3df6db99056a271948f4"
  },
  {
    "url": "new_site/templates/character_creation_helper_template.html",
    "revision": "e09aa89cd95cc17afad569e14262734d"
  },
  {
    "url": "new_site/templates/character_selection_template.html",
    "revision": "3a976401cadbf56fe507f1e27f1dcf14"
  },
  {
    "url": "new_site/templates/character_sheet_template.html",
    "revision": "c2719f44a5a3f903c71bf40dbc6effd4"
  },
  {
    "url": "new_site/templates/level_up_sheet_template.html",
    "revision": "b157940d167d37cc0fb12a45cf0aa89a"
  },
  {
    "url": "new_site/templates/macros.html",
    "revision": "d577b9bc2d10d8b2ce728a8aa37a450e"
  },
  {
    "url": "new_site/templates/role_selection_template.html",
    "revision": "58e4d48325d9df2abfb8c4e64c10eb0b"
  },
  {
    "url": "new_site/templates/selector_template.html",
    "revision": "0d100a00d55cc3cc0b25d1e787b6ba79"
  },
  {
    "url": "new_site/templates/two_sided_character_sheet.html",
    "revision": "6b222bc6d88e40ee05e4b70fd9915e77"
  },
  {
    "url": "node_modules/bootstrap-select/dist/js/bootstrap-select.min.js",
    "revision": "69c3d7926d5af92d72665aeb1136fc40"
  },
  {
    "url": "node_modules/bootstrap/dist/js/bootstrap.min.js",
    "revision": "61f338f870fcd0ff46362ef109d28533"
  },
  {
    "url": "node_modules/jquery/dist/jquery.min.js",
    "revision": "220afd743d9e9643852e31a135a9f3ae"
  },
  {
    "url": "node_modules/popper.js/dist/umd/popper.min.js",
    "revision": "84415b7368fd6fc764cbe86039ce0626"
  },
  {
    "url": "site.webmanifest",
    "revision": "fbb38e2f8d4407c7ee2c47a6ee4ebcf5"
  },
  {
    "url": "index.html",
    "revision": "f4c01abb06076c3366ce8929fd56d93f"
  },
  {
    "url": "assets/css/style.css",
    "revision": "c7e1f14408ce1b70b55553bb79eaed18"
  }
]);


// workbox.routing.registerRoute(
//   /\.js$/,
//   // Use cache but update in the background.
//   new workbox.strategies.StaleWhileRevalidate({
//     // Use a custom cache name.
//     cacheName: 'js-cache',
//   })
// );

workbox.routing.registerRoute(
  /\.(?:js|css)$/,
  new workbox.strategies.StaleWhileRevalidate({
    cacheName: 'static-resources',
  })
);
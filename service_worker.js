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
    "revision": "b7c6e4018e834399215c0b73a0d1fa42"
  },
  {
    "url": "new_site/css/iterated_char_sheet.css",
    "revision": "e40e4976b3b4868617820d6516f75938"
  },
  {
    "url": "new_site/css/rangers.css",
    "revision": "e12fae75d619d03263a4804a3a183469"
  },
  {
    "url": "new_site/css/two_sided_character_sheet.css",
    "revision": "7d8516af9857ee1ed9b320ff842eb2c9"
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
    "revision": "f1d922149bf80c718ea648be0a1900c5"
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
    "url": "new_site/icons/moebius-trefoil.svg",
    "revision": "7b94303778ad48c63358d87c49d8fee4"
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
    "url": "new_site/icons/shiny-purse.svg",
    "revision": "9a3f782eb1bf77236ac121fd1e251770"
  },
  {
    "url": "new_site/icons/swap-bag.svg",
    "revision": "fad31dd66c26b06eab6af038e704aef8"
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
    "url": "new_site/icons/token.svg",
    "revision": "40e9a049484cfe284bfb9ccb60090bb2"
  },
  {
    "url": "new_site/icons/tombstone.svg",
    "revision": "5080916dfa69b9c2adac3a167f1052a7"
  },
  {
    "url": "new_site/icons/two-coins.svg",
    "revision": "5a44d7766e4ec80be3024ab0f75aaf83"
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
    "revision": "a06cdf42fa706a43aa7d1aa835187589"
  },
  {
    "url": "new_site/known_dependencies.json",
    "revision": "cbec16f2ca1287a782f330a10b1c19d0"
  },
  {
    "url": "new_site/pages/character_creation_helper_page.html",
    "revision": "0d64aad29751530edf9a97b7358c34b4"
  },
  {
    "url": "new_site/pages/character_sheet.html",
    "revision": "4648c6a091b54eaccb6ff640ce08ffa6"
  },
  {
    "url": "new_site/pages/GENERATED/ALT.json",
    "revision": "316da169b3aa7b91e21f0a7bbb90ffc0"
  },
  {
    "url": "new_site/pages/GENERATED/Book_of_Known_Beasts.html",
    "revision": "20ed3481b7c276fcd75b8495f50a9dc3"
  },
  {
    "url": "new_site/pages/GENERATED/Book_of_Lore.html",
    "revision": "12472371923ed752683fdd08b60ab636"
  },
  {
    "url": "new_site/pages/GENERATED/Changelog.html",
    "revision": "a804ae2b1fa978fb89dc71b43e2661a0"
  },
  {
    "url": "new_site/pages/GENERATED/Compendium_of_Character_Creation.html",
    "revision": "89efce34365610dd5f050c36f2ad9e1f"
  },
  {
    "url": "new_site/pages/GENERATED/Examples.html",
    "revision": "080851ce4f186b94f18d43daadf9df59"
  },
  {
    "url": "new_site/pages/GENERATED/Examples.md",
    "revision": "f31fc1f7483675fcb13d69b2f64f7c4c"
  },
  {
    "url": "new_site/pages/GENERATED/Poohbah_Printables.html",
    "revision": "c0a6de81838de246b2e93cd56789b9f4"
  },
  {
    "url": "new_site/pages/GENERATED/Printed_Materials.html",
    "revision": "c3f8821e0669dade588fe235c129fa51"
  },
  {
    "url": "new_site/pages/GENERATED/Rulebook.html",
    "revision": "831b49ee75500c5646afe3b61c821753"
  },
  {
    "url": "new_site/pages/GENERATED/Tome_of_the_Ancients.html",
    "revision": "87033f4814309644c188ded96f12fc57"
  },
  {
    "url": "new_site/pages/level_up_sheet.html",
    "revision": "586c165f87209df255d9fb04ea02f87e"
  },
  {
    "url": "new_site/pages/weapons.html",
    "revision": "c9152b29e03bd67cd9b5da7005cd2c38"
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
    "revision": "5c6749fba3df18ae45478670ee684f74"
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
    "revision": "ea76cee52a24fd2fee2d4fb3a1c3ef41"
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
    "revision": "5ac34931108e41cd8b49dd357fc01fb7"
  },
  {
    "url": "new_site/templates/updated_character_sheet.html",
    "revision": "7d505bad6de682940a165fe9431072d8"
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
    "revision": "0877921a3b68cafd2aba5d1d325f4118"
  },
  {
    "url": "assets/css/style.css",
    "revision": "5ea27f0fecfa9ef1a9b0c6d83cb26148"
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
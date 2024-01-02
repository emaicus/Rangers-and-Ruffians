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

workbox.precaching.precacheAndRoute([
  {
    "url": "site/css/character_creation_helper.css",
    "revision": "d41d8cd98f00b204e9800998ecf8427e"
  },
  {
    "url": "site/css/character_selection.css",
    "revision": "b7c6e4018e834399215c0b73a0d1fa42"
  },
  {
    "url": "site/css/iterated_char_sheet.css",
    "revision": "e40e4976b3b4868617820d6516f75938"
  },
  {
    "url": "site/css/rangers.css",
    "revision": "e12fae75d619d03263a4804a3a183469"
  },
  {
    "url": "site/css/two_sided_character_sheet.css",
    "revision": "5651ff04089e9134238011ad4d0a58bf"
  },
  {
    "url": "site/css/weapons.css",
    "revision": "d6ef295c6a0f418fa837160634e50ec3"
  },
  {
    "url": "site/icons/bolt-shield.svg",
    "revision": "15597019d5e5ecb94339f1c3a14dad3b"
  },
  {
    "url": "site/icons/bordered-shield.svg",
    "revision": "2817f846d2581d39be55b8532e233ca1"
  },
  {
    "url": "site/icons/circle-halved.svg",
    "revision": "f1d922149bf80c718ea648be0a1900c5"
  },
  {
    "url": "site/icons/circle.svg",
    "revision": "a1eb0f67100d684bb055cf1605ebc86a"
  },
  {
    "url": "site/icons/fast-backward-button.svg",
    "revision": "8b66a30bce8737653e0a2722f8d4271c"
  },
  {
    "url": "site/icons/favicon/android-chrome-192x192.png",
    "revision": "ab2a1ccdea67316da8c94952f8556a52"
  },
  {
    "url": "site/icons/favicon/android-chrome-512x512.png",
    "revision": "83cf00ca81517e5a0178f3322895462b"
  },
  {
    "url": "site/icons/favicon/apple-touch-icon.png",
    "revision": "98a23a75e655ec08f2b91fa9b0b0dd96"
  },
  {
    "url": "site/icons/favicon/favicon-16x16.png",
    "revision": "93e6f1244ed4772f8392f390a1eca560"
  },
  {
    "url": "site/icons/favicon/favicon-32x32.png",
    "revision": "2534f65605216584b632c9003835b9c3"
  },
  {
    "url": "site/icons/favicon/favicon.ico",
    "revision": "3a98ca9abe14bc47f5ef6a53d66e30a9"
  },
  {
    "url": "site/icons/favicon/mstile-150x150.png",
    "revision": "0f472f85aa4becee99d607ce59371054"
  },
  {
    "url": "site/icons/favicon/safari-pinned-tab.svg",
    "revision": "f99372dd39eefaacda39fa89afc985fc"
  },
  {
    "url": "site/icons/fire-spell-cast.svg",
    "revision": "e6c09f4fceb5d0f9b9da29547102801e"
  },
  {
    "url": "site/icons/firearm.svg",
    "revision": "f8ffd83b16edda1681bd26b3893df59d"
  },
  {
    "url": "site/icons/flame.svg",
    "revision": "e7879a3663ef74eb3d6f54de66f1d54d"
  },
  {
    "url": "site/icons/heart-beats.svg",
    "revision": "78b50894a514de0ff5d61a5c454b4d5d"
  },
  {
    "url": "site/icons/heart-plus.svg",
    "revision": "cd3d5ee936fd58667b97c3d08a0a72bb"
  },
  {
    "url": "site/icons/hearts.svg",
    "revision": "034a48b95c54e76616dc0e042b79cace"
  },
  {
    "url": "site/icons/horseshoe.svg",
    "revision": "77ec4c52b8c7e8bbba0c79c5fd722148"
  },
  {
    "url": "site/icons/ink-swirl.svg",
    "revision": "03f49b4335e04b72962a39500550bcd0"
  },
  {
    "url": "site/icons/magic-swirl.svg",
    "revision": "4b5f5651f170ee64e54d4b097e18f2d7"
  },
  {
    "url": "site/icons/moebius-trefoil.svg",
    "revision": "7b94303778ad48c63358d87c49d8fee4"
  },
  {
    "url": "site/icons/one-handed.svg",
    "revision": "1c80e863faaa775785de4b580e7526e7"
  },
  {
    "url": "site/icons/power-lightning.svg",
    "revision": "96d1686c81be23108c2b1406f257bfbc"
  },
  {
    "url": "site/icons/prayer.svg",
    "revision": "68f8bc222e88c2fa69518c8fdb44d230"
  },
  {
    "url": "site/icons/quiver.svg",
    "revision": "901d20011d0dc10cc23b3f0558993a33"
  },
  {
    "url": "site/icons/raise-zombie.svg",
    "revision": "7a1e1dc035aaa4789c7e7acef779ad7c"
  },
  {
    "url": "site/icons/ranged.svg",
    "revision": "0ae7c35e62ba21bdd47309256b0a49f4"
  },
  {
    "url": "site/icons/shield.svg",
    "revision": "8396f1cb288bb874fabd6fb1dc5bee2b"
  },
  {
    "url": "site/icons/shiny-purse.svg",
    "revision": "9a3f782eb1bf77236ac121fd1e251770"
  },
  {
    "url": "site/icons/swap-bag.svg",
    "revision": "fad31dd66c26b06eab6af038e704aef8"
  },
  {
    "url": "site/icons/sword-brandish.svg",
    "revision": "218202da8fc960eb2c13a2ee20b7d5b5"
  },
  {
    "url": "site/icons/swords-power.svg",
    "revision": "50efddea824e634ab7a44d8f432de928"
  },
  {
    "url": "site/icons/token.svg",
    "revision": "40e9a049484cfe284bfb9ccb60090bb2"
  },
  {
    "url": "site/icons/tombstone.svg",
    "revision": "5080916dfa69b9c2adac3a167f1052a7"
  },
  {
    "url": "site/icons/two-coins.svg",
    "revision": "5a44d7766e4ec80be3024ab0f75aaf83"
  },
  {
    "url": "site/icons/two-handed.svg",
    "revision": "c67d2aa1c461aa581fd98593bce4592d"
  },
  {
    "url": "site/images/backdrops/landscape_ancients.jpg",
    "revision": "e22e7269fb9314452b72d23ea43cbc60"
  },
  {
    "url": "site/images/backdrops/landscape_banner.jpg",
    "revision": "5580f710d66b5e4cd4dfe99c46691c86"
  },
  {
    "url": "site/images/backdrops/landscape_beasts.jpg",
    "revision": "7a33c0a62c5fab937b4b7677523e7eb4"
  },
  {
    "url": "site/images/backdrops/landscape_character_creation.jpg",
    "revision": "c5e0795787e1db3cbb753f98c98b4510"
  },
  {
    "url": "site/images/backdrops/landscape_lore.jpg",
    "revision": "6a27c2037518e35e4c4ee58f6de9aa97"
  },
  {
    "url": "site/images/backdrops/landscape_rulebook.jpg",
    "revision": "b2ee495bc25a7026f43ea7db8272c8c7"
  },
  {
    "url": "site/images/backdrops/portrait_ancients.jpg",
    "revision": "7ec9decf862921cc1ea60bea762bd9d9"
  },
  {
    "url": "site/images/backdrops/portrait_banner.jpg",
    "revision": "5980bf88e7efc5d841ee9671ab15161f"
  },
  {
    "url": "site/images/backdrops/portrait_beasts.jpg",
    "revision": "71a0161a70b465cd1156f92360a7d501"
  },
  {
    "url": "site/images/backdrops/portrait_changelog.jpg",
    "revision": "9653915b6ca59c6d39aa4ce3a2ea9a8d"
  },
  {
    "url": "site/images/backdrops/portrait_character_creation.jpg",
    "revision": "6a683801cbac81f4ea43375927fabbde"
  },
  {
    "url": "site/images/backdrops/portrait_lore.jpg",
    "revision": "27cc0755e47d500a2bee7c17e7cd1194"
  },
  {
    "url": "site/images/backdrops/portrait_rulebook.jpg",
    "revision": "dc3f2ed21d0f1715ad88f57cf09daaeb"
  },
  {
    "url": "site/images/class/barbarian.jpg",
    "revision": "b2172b0688299e11d4f78e2d8a6d3b05"
  },
  {
    "url": "site/images/class/bard.jpg",
    "revision": "9cae1e59e04670a9d525051951d7af68"
  },
  {
    "url": "site/images/class/cleric.jpg",
    "revision": "fd91d6aedf758c204f31f30cd6325f03"
  },
  {
    "url": "site/images/class/druid.jpg",
    "revision": "d27f0aef1dc566bd36d27422e662ba5e"
  },
  {
    "url": "site/images/class/fighter.jpg",
    "revision": "56fde3a6762260ca423e529428aa51dd"
  },
  {
    "url": "site/images/class/knight.jpg",
    "revision": "f0b835bd2e4e24965be812f191921670"
  },
  {
    "url": "site/images/class/monk.jpg",
    "revision": "070f82df4cdc760f508f7c108b0dfddd"
  },
  {
    "url": "site/images/class/rogue.jpg",
    "revision": "85542a55467e48e83214cd8bdb5b8288"
  },
  {
    "url": "site/images/class/warlock.jpg",
    "revision": "b5c88a1fc90d3b906d1e426c6bdad30e"
  },
  {
    "url": "site/images/class/wizard.jpg",
    "revision": "6a4120f4fcea6e0b0dd4bc70d4f6e658"
  },
  {
    "url": "site/images/race/catterwol.jpg",
    "revision": "67bb21376b089844d3ee310ac42b4103"
  },
  {
    "url": "site/images/race/daemonspawn.jpg",
    "revision": "99bad0f4a7fb28b6ffd8a652f8fc91aa"
  },
  {
    "url": "site/images/race/deep_elf.jpg",
    "revision": "467f98e069bcfe94acdd9f2e1192cf3a"
  },
  {
    "url": "site/images/race/dwarf.jpg",
    "revision": "7498b94114e2e6875e848c0a0e24a694"
  },
  {
    "url": "site/images/race/gnome.jpg",
    "revision": "b84432d8709aefeab1691b77bdbe8d84"
  },
  {
    "url": "site/images/race/goblin.jpg",
    "revision": "bebfa44ab43d49034e908ff9b0720bf3"
  },
  {
    "url": "site/images/race/halfling.jpg",
    "revision": "dc073ffa3aad64e46eaccb2b907d6a2a"
  },
  {
    "url": "site/images/race/high_elf.jpg",
    "revision": "c34619c914fb05a63381af21a48997d7"
  },
  {
    "url": "site/images/race/human.jpg",
    "revision": "939c1eb3a24baccf8ac9f35db938feb8"
  },
  {
    "url": "site/images/race/lizkin.jpg",
    "revision": "2646b164f0d55091f04b9ec1901816e7"
  },
  {
    "url": "site/images/race/orc.jpg",
    "revision": "88e1dee0ab61c729ab76b869e9910bbc"
  },
  {
    "url": "site/images/race/sprout.jpg",
    "revision": "b1c2bb1a2d69922299a9c39c1e221010"
  },
  {
    "url": "site/images/race/waterborn.jpg",
    "revision": "065d24d896b4328dea94021229cf4f2e"
  },
  {
    "url": "site/images/race/wood_elf.jpg",
    "revision": "c29997f8a3d9fa1ccc30ab640923429d"
  },
  {
    "url": "site/images/skill_trees/barbarian.jpg",
    "revision": "1bb229e86dca74b8e8cbc341275841c7"
  },
  {
    "url": "site/images/skill_trees/fighter.jpg",
    "revision": "67719d813c0652f23d2c41ceb3d594af"
  },
  {
    "url": "site/images/skill_trees/knight.jpg",
    "revision": "2f11f76c8ea17c6fa9503f3323af0e91"
  },
  {
    "url": "site/images/skill_trees/monk.jpg",
    "revision": "770809db18e256f85edb44c16b1f9d8c"
  },
  {
    "url": "site/images/skill_trees/rogue.jpg",
    "revision": "6b1d36abbbd838297a3c623fec46bf72"
  },
  {
    "url": "site/images/under_construction/under_construction.jpg",
    "revision": "2e486932d009d0b6efa79b197b184734"
  },
  {
    "url": "site/js/nunjucks.js",
    "revision": "6c7d8c15676636621e7b48dbf1589b6b"
  },
  {
    "url": "site/js/rangers.js",
    "revision": "e225b6d6b2218ebd7a3d5ce70113e05b"
  },
  {
    "url": "site/pages/character_creation_helper_page.html",
    "revision": "ce2ffeb734624b0807b355977f08f04f"
  },
  {
    "url": "site/pages/character_sheet.html",
    "revision": "01f43c3b9f5fb5970f5c4eadb58899f1"
  },
  {
    "url": "site/pages/character_store.html",
    "revision": "c3ed2e2bb875e914e2c41c6eb7003cf0"
  },
  {
    "url": "site/pages/GENERATED/ALT.json",
    "revision": "012fe9b3b5d9cc021a670a40f8907cae"
  },
  {
    "url": "site/pages/GENERATED/Book_of_Known_Beasts.html",
    "revision": "dd9afeac212ce4a77228cd9e4032466e"
  },
  {
    "url": "site/pages/GENERATED/Book_of_Lore.html",
    "revision": "bd6284586848e8b9ac937086a94374c1"
  },
  {
    "url": "site/pages/GENERATED/Changelog.html",
    "revision": "d57aeae21969fbaf599cd4ff265c77db"
  },
  {
    "url": "site/pages/GENERATED/Compendium_of_Character_Creation.html",
    "revision": "cdfa4ec02c8b5092edebb4d73bface15"
  },
  {
    "url": "site/pages/GENERATED/Examples.html",
    "revision": "2dabafbcff7e5dee69fd4b8edbedef6c"
  },
  {
    "url": "site/pages/GENERATED/Examples.md",
    "revision": "18119a93572a91f6107e4c458aa8d141"
  },
  {
    "url": "site/pages/GENERATED/Items.html",
    "revision": "5b591604d3978c31620c781411457f22"
  },
  {
    "url": "site/pages/GENERATED/Poohbah_Printables.html",
    "revision": "457703a8cc4055f5f38bd2117674c959"
  },
  {
    "url": "site/pages/GENERATED/Printed_Materials.html",
    "revision": "a6b08c6e7e1ffe89132f8b949e84be7d"
  },
  {
    "url": "site/pages/GENERATED/Rulebook.html",
    "revision": "5df6d8f19153d2cd29f2336fbd948ece"
  },
  {
    "url": "site/pages/GENERATED/Tome_of_the_Ancients.html",
    "revision": "c6da19a5598405cb8f928eca5a1dd0a5"
  },
  {
    "url": "site/pages/level_up_sheet.html",
    "revision": "5dd8616a3a416011a6bf389b0e7d86d5"
  },
  {
    "url": "site/pages/weapons.html",
    "revision": "bf27f14a2e793b83103879ea9c7d3b17"
  },
  {
    "url": "site/printed_materials/standard_character_sheet.pdf",
    "revision": "d35a5df20af914ebddcf1d8a75d25dd6"
  },
  {
    "url": "site/printed_materials/visual_character_sheet.pdf",
    "revision": "6d820079132e3df6db99056a271948f4"
  },
  {
    "url": "site/templates/character_creation_helper_template.html",
    "revision": "8ed4e8ec10e151b216f87abddd3324ad"
  },
  {
    "url": "site/templates/character_selection_template.html",
    "revision": "5c6749fba3df18ae45478670ee684f74"
  },
  {
    "url": "site/templates/character_sheet_template.html",
    "revision": "97c570a6596711631ef620130216382a"
  },
  {
    "url": "site/templates/level_up_sheet_template.html",
    "revision": "b157940d167d37cc0fb12a45cf0aa89a"
  },
  {
    "url": "site/templates/macros.html",
    "revision": "756030b9b3370fac41efafb1a0663f14"
  },
  {
    "url": "site/templates/role_selection_template.html",
    "revision": "58e4d48325d9df2abfb8c4e64c10eb0b"
  },
  {
    "url": "site/templates/selector_template.html",
    "revision": "0d100a00d55cc3cc0b25d1e787b6ba79"
  },
  {
    "url": "site/templates/two_sided_character_sheet.html",
    "revision": "5ac34931108e41cd8b49dd357fc01fb7"
  },
  {
    "url": "site/templates/updated_character_sheet.html",
    "revision": "7d505bad6de682940a165fe9431072d8"
  },
  {
    "url": "site/templates/weapons_page.html",
    "revision": "b067ce9cd227482cc59734cbd7aefc08"
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
    "revision": "e75ccbfcd6a5bc16b87fe1df0450b583"
  },
  {
    "url": "index.html",
    "revision": "4c9fb34f8b4d62f9a1ef4c7e98bcd6e2"
  },
  {
    "url": "assets/css/style.css",
    "revision": "695d5b66cc9278ab58c2c1f391627c21"
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
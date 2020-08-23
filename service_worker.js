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
    "url": "site/css/character_creation_helper.css",
    "revision": "d41d8cd98f00b204e9800998ecf8427e"
  },
  {
    "url": "site/css/character_selection.css",
    "revision": "5351f61fed9d7ece2b4767d04eea02b6"
  },
  {
    "url": "site/css/iterated_char_sheet.css",
    "revision": "388d4393bc3d603cbcc91cfabd956a38"
  },
  {
    "url": "site/css/rangers.css",
    "revision": "dce4b1e899df221f966c792f2306f2fc"
  },
  {
    "url": "site/css/two_sided_character_sheet.css",
    "revision": "2c128cc2b7d1a7ccf2cf9f2f66a2af7e"
  },
  {
    "url": "site/css/weapons.css",
    "revision": "8aee2ef265a9b764c5951d6b91aababc"
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
    "revision": "bf8b93da9a86eaec639f942f6377e4d8"
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
    "revision": "8d901973cd01ea944a0ac8c06fc80f98"
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
    "url": "site/icons/hearts.svg",
    "revision": "034a48b95c54e76616dc0e042b79cace"
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
    "url": "site/images/class/female/archer.jpg",
    "revision": "e307193a995d45f8dfd0823817d60929"
  },
  {
    "url": "site/images/class/female/beastmaster.jpg",
    "revision": "782c91369af5f3f3a5e1b4bc601d859c"
  },
  {
    "url": "site/images/class/fighter.jpg",
    "revision": "d8b3923fbf791754e06513f8477c298a"
  },
  {
    "url": "site/images/class/gunslinger.jpg",
    "revision": "71aacf4abd579be8cef7cd3424386bf1"
  },
  {
    "url": "site/images/class/highborn.jpg",
    "revision": "4df3aec08c7de62d136b9266aae6bd29"
  },
  {
    "url": "site/images/class/male/knight.jpg",
    "revision": "f0b835bd2e4e24965be812f191921670"
  },
  {
    "url": "site/images/class/male/rogue.jpg",
    "revision": "85542a55467e48e83214cd8bdb5b8288"
  },
  {
    "url": "site/images/class/monk.jpg",
    "revision": "524d941063e99603ccaf0027f48cc54e"
  },
  {
    "url": "site/images/class/necromancer.jpg",
    "revision": "8d92816cb04e9e53ac956eb271c6e64b"
  },
  {
    "url": "site/images/class/paladin.jpg",
    "revision": "7aef7fee2515cc43067b2419554106d0"
  },
  {
    "url": "site/images/class/ranger.jpg",
    "revision": "6bbec3c4a9132c3ccf93602cec423bee"
  },
  {
    "url": "site/images/class/sorcerer.jpg",
    "revision": "b5c88a1fc90d3b906d1e426c6bdad30e"
  },
  {
    "url": "site/images/class/wizard.jpg",
    "revision": "6a4120f4fcea6e0b0dd4bc70d4f6e658"
  },
  {
    "url": "site/images/race/female/catterwol.jpg",
    "revision": "775cc3f7e10770fdb0540d27ac5dcccd"
  },
  {
    "url": "site/images/race/female/deep_elf.jpg",
    "revision": "467f98e069bcfe94acdd9f2e1192cf3a"
  },
  {
    "url": "site/images/race/female/fleetfoot_halfling.jpg",
    "revision": "d2cd1e738dcaa07cf70d576758cc3146"
  },
  {
    "url": "site/images/race/female/gnome.jpg",
    "revision": "e05c11926a86536c9ffd829f63a7f106"
  },
  {
    "url": "site/images/race/female/hardfoot_halfling.jpg",
    "revision": "dc073ffa3aad64e46eaccb2b907d6a2a"
  },
  {
    "url": "site/images/race/female/high_elf.jpg",
    "revision": "c34619c914fb05a63381af21a48997d7"
  },
  {
    "url": "site/images/race/female/orc.jpg",
    "revision": "88e1dee0ab61c729ab76b869e9910bbc"
  },
  {
    "url": "site/images/race/female/sprout.jpg",
    "revision": "b1c2bb1a2d69922299a9c39c1e221010"
  },
  {
    "url": "site/images/race/female/waterborn.jpg",
    "revision": "065d24d896b4328dea94021229cf4f2e"
  },
  {
    "url": "site/images/race/female/wood_elf.jpg",
    "revision": "c29997f8a3d9fa1ccc30ab640923429d"
  },
  {
    "url": "site/images/race/male/automaton.jpg",
    "revision": "9de7bcb704dd7804e99e18cfa83d6fb4"
  },
  {
    "url": "site/images/race/male/daemonspawn.jpg",
    "revision": "99bad0f4a7fb28b6ffd8a652f8fc91aa"
  },
  {
    "url": "site/images/race/male/dwarf.jpg",
    "revision": "7498b94114e2e6875e848c0a0e24a694"
  },
  {
    "url": "site/images/race/male/goblin.jpg",
    "revision": "bebfa44ab43d49034e908ff9b0720bf3"
  },
  {
    "url": "site/images/race/male/hissling.jpg",
    "revision": "7484df0c4a008e66de38e7955f95dcab"
  },
  {
    "url": "site/images/race/male/human.jpg",
    "revision": "939c1eb3a24baccf8ac9f35db938feb8"
  },
  {
    "url": "site/images/race/male/kragraven.jpg",
    "revision": "20389ee0b9bd86032c725fce3545ac6f"
  },
  {
    "url": "site/images/race/male/lizkin.jpg",
    "revision": "2646b164f0d55091f04b9ec1901816e7"
  },
  {
    "url": "site/js/nunjucks.js",
    "revision": "c178e89701fc685e9617e99ea7dd632b"
  },
  {
    "url": "site/js/rangers.js",
    "revision": "7fe7b6634946aec76bc0f0391ce743b3"
  },
  {
    "url": "site/pages/character_creation_helper_page.html",
    "revision": "08c6c9d6a89994312a00fa4b884dda0d"
  },
  {
    "url": "site/pages/character_sheet.html",
    "revision": "d66bf00a9f61a9092c03d571d0f2e734"
  },
  {
    "url": "site/pages/GENERATED/ALT.json",
    "revision": "cd11e76ab09b08e1fadc809cdf5f5e14"
  },
  {
    "url": "site/pages/GENERATED/Book_of_Known_Beasts.html",
    "revision": "31d159c01f369e9e5b721cc7efd87f05"
  },
  {
    "url": "site/pages/GENERATED/Book_of_Lore.html",
    "revision": "f9c310ddd79892dd383c6401ab21da06"
  },
  {
    "url": "site/pages/GENERATED/Changelog.html",
    "revision": "c5736131be519ad44d3217256ed1d277"
  },
  {
    "url": "site/pages/GENERATED/Compendium_of_Character_Creation.html",
    "revision": "2cc643685c8c509d2f83561797eea4ec"
  },
  {
    "url": "site/pages/GENERATED/Examples.html",
    "revision": "51f38842fa6e98af6fa63dce52b178c0"
  },
  {
    "url": "site/pages/GENERATED/Examples.md",
    "revision": "75df1a67d77f1386f57dfc07affa29e1"
  },
  {
    "url": "site/pages/GENERATED/Poohbah_Printables.html",
    "revision": "6f52c1598e6e81095163b7e44503a1c5"
  },
  {
    "url": "site/pages/GENERATED/Printed_Materials.html",
    "revision": "00f2838d3ba62b8307a8694839d5c077"
  },
  {
    "url": "site/pages/GENERATED/Rulebook.html",
    "revision": "f7a51af89fec38ec24e663cf9225b983"
  },
  {
    "url": "site/pages/GENERATED/Tome_of_the_Ancients.html",
    "revision": "a0765b54736a0c61dea6b09f644a551f"
  },
  {
    "url": "site/pages/level_up_sheet.html",
    "revision": "df868b14dabe2001eeedef62616606e3"
  },
  {
    "url": "site/pages/weapons.html",
    "revision": "97cb4330dd71f8429b61d31d6ba7509f"
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
    "url": "site/static/images/backdrops/background.jpg",
    "revision": "2c692cad948778c80a202e013214cc03"
  },
  {
    "url": "site/static/images/backdrops/background.png",
    "revision": "e75427d85b09ba5aa3698dc04116b9f2"
  },
  {
    "url": "site/static/images/backdrops/landscape_ancients.jpg",
    "revision": "b03d858a673e95bdeffcfaaa644ef535"
  },
  {
    "url": "site/static/images/backdrops/landscape_banner.jpg",
    "revision": "9ea4fdfb8a0148f3d4ba9fede2fafbb2"
  },
  {
    "url": "site/static/images/backdrops/landscape_beasts.jpg",
    "revision": "2ef2d02a4d26e467a893488bef78def6"
  },
  {
    "url": "site/static/images/backdrops/landscape_character_creation.jpg",
    "revision": "8519970502eb77b28240d10131369131"
  },
  {
    "url": "site/static/images/backdrops/landscape_lore.jpg",
    "revision": "f7fddbee8cd119b89e1091621a1b167c"
  },
  {
    "url": "site/static/images/backdrops/landscape_rulebook.jpg",
    "revision": "a59adaea03e9204a6cf20ecf7427a007"
  },
  {
    "url": "site/static/images/backdrops/OLD_landscape_rulebook.jpg",
    "revision": "46f04def8c31da3d468376488b0e3f3a"
  },
  {
    "url": "site/static/images/backdrops/portrait_ancients.jpg",
    "revision": "92ed4af280fb084238f092a17c55e171"
  },
  {
    "url": "site/static/images/backdrops/portrait_banner.jpg",
    "revision": "783b11ce1c5b1b38e054eee9e2e9b4f0"
  },
  {
    "url": "site/static/images/backdrops/portrait_beasts.jpg",
    "revision": "f04bfda14c5f16b914962ebf5eeb3c8c"
  },
  {
    "url": "site/static/images/backdrops/portrait_changelog.jpg",
    "revision": "9291c3f86c096594cde0714346e80238"
  },
  {
    "url": "site/static/images/backdrops/portrait_character_creation.jpg",
    "revision": "3dc6350c493e9ce6191101815afd6c0d"
  },
  {
    "url": "site/static/images/backdrops/portrait_lore.jpg",
    "revision": "09fd88d72a88def338f00f20870ab157"
  },
  {
    "url": "site/static/images/class/archer.jpg",
    "revision": "9a8a7c9e37358a6a9c154713f0efbf45"
  },
  {
    "url": "site/static/images/class/barbarian.jpg",
    "revision": "be862e87d881523d7c3d90667b6235b8"
  },
  {
    "url": "site/static/images/class/bard.jpg",
    "revision": "656b3e1d72c14568aa33877589db498f"
  },
  {
    "url": "site/static/images/class/battle_mage.jpg",
    "revision": "d02b88d4a81fcf070be017532486aa1d"
  },
  {
    "url": "site/static/images/class/beastmaster.jpg",
    "revision": "350a4c30e3815ebffbabc34aaf44e3da"
  },
  {
    "url": "site/static/images/class/cleric.jpg",
    "revision": "6bdc047f3ffa9afaf02c35f74011a273"
  },
  {
    "url": "site/static/images/class/druid.jpg",
    "revision": "d40b5b25309ba6894d41e10b6ee56be8"
  },
  {
    "url": "site/static/images/class/female/archer.jpg",
    "revision": "e307193a995d45f8dfd0823817d60929"
  },
  {
    "url": "site/static/images/class/female/beastmaster.jpg",
    "revision": "782c91369af5f3f3a5e1b4bc601d859c"
  },
  {
    "url": "site/static/images/class/female/gunslinger.jpg",
    "revision": "04aff6cf8e1380b516e461ddd6f0b2e5"
  },
  {
    "url": "site/static/images/class/female/highborn.jpg",
    "revision": "a7bae166755a4a8b56512df2fed3386f"
  },
  {
    "url": "site/static/images/class/female/monk.jpg",
    "revision": "070f82df4cdc760f508f7c108b0dfddd"
  },
  {
    "url": "site/static/images/class/female/sorcerer.jpg",
    "revision": "2e2a18b38e792308ad7b76531cbe4a77"
  },
  {
    "url": "site/static/images/class/fighter.jpg",
    "revision": "b63902d10c0b5e1a9b2c071c7450f77d"
  },
  {
    "url": "site/static/images/class/gunslinger.jpg",
    "revision": "2d3905b1056534c3bcde5b7c5ea01ede"
  },
  {
    "url": "site/static/images/class/hedge_knight.jpg",
    "revision": "36cf1bf27d1c171480e8c8688962f7dc"
  },
  {
    "url": "site/static/images/class/highborn.jpg",
    "revision": "c96332d93d0fe79409856ff18a80ced1"
  },
  {
    "url": "site/static/images/class/knight.jpg",
    "revision": "e2dfaecb08d16ecd78d3f0bee9c37a90"
  },
  {
    "url": "site/static/images/class/magic_arrow.jpg",
    "revision": "2f7227808543f4ccf9674e2c9b386c7d"
  },
  {
    "url": "site/static/images/class/male/cleric.jpg",
    "revision": "8c7bae96abc9ff9cdcef8dfbbb1fdb2b"
  },
  {
    "url": "site/static/images/class/male/fighter.jpg",
    "revision": "f1d00f332215c1c96b77acb843765ea4"
  },
  {
    "url": "site/static/images/class/male/knight.jpg",
    "revision": "8a502c9afd0d6f83ef8435e298805600"
  },
  {
    "url": "site/static/images/class/monk.jpg",
    "revision": "6fc43153057383069d0f237eff48bdc5"
  },
  {
    "url": "site/static/images/class/necromancer.jpg",
    "revision": "81492506a1542531e468d5088608b42d"
  },
  {
    "url": "site/static/images/class/old/barbarian.jpg",
    "revision": "fabca670d5bc7fb72edbbcbdff7a6149"
  },
  {
    "url": "site/static/images/class/old/beastmaster.jpg",
    "revision": "3cdab6d56120065e5209ae5c170340b3"
  },
  {
    "url": "site/static/images/class/old/d7if7sj-96d92cd4-efbf-4492-8a1c-d624e8a3788c.jpg",
    "revision": "e6ab5ab2f4c38482f88f310cc501b573"
  },
  {
    "url": "site/static/images/class/old/knight.jpg",
    "revision": "98f98f5b980788074a2b65a4fcf73219"
  },
  {
    "url": "site/static/images/class/paladin.jpg",
    "revision": "3b709b65f3a2728ed076ec75a1316acd"
  },
  {
    "url": "site/static/images/class/ranger.jpg",
    "revision": "4a8b309903ebabed31595f246525c674"
  },
  {
    "url": "site/static/images/class/rogue.jpg",
    "revision": "b7cae218a65b58876668cbac0f811a44"
  },
  {
    "url": "site/static/images/class/sorcerer.jpg",
    "revision": "49f5b9e4c38ecf94cfe6d988ba7f592e"
  },
  {
    "url": "site/static/images/class/wizard.jpg",
    "revision": "14f8b0f8c57164cf3359b5a59f6b59cf"
  },
  {
    "url": "site/static/images/gender/female.jpg",
    "revision": "1cc83002a90ea72d8d2a81181b4d041d"
  },
  {
    "url": "site/static/images/gender/male.jpg",
    "revision": "267892e1a79d24d0f27d4d031d1bc0b2"
  },
  {
    "url": "site/static/images/icons/bolt-shield.svg",
    "revision": "15597019d5e5ecb94339f1c3a14dad3b"
  },
  {
    "url": "site/static/images/icons/bordered-shield.svg",
    "revision": "2817f846d2581d39be55b8532e233ca1"
  },
  {
    "url": "site/static/images/icons/circle-halved.svg",
    "revision": "bf8b93da9a86eaec639f942f6377e4d8"
  },
  {
    "url": "site/static/images/icons/circle.svg",
    "revision": "a1eb0f67100d684bb055cf1605ebc86a"
  },
  {
    "url": "site/static/images/icons/favicon/android-chrome-192x192.png",
    "revision": "ab2a1ccdea67316da8c94952f8556a52"
  },
  {
    "url": "site/static/images/icons/favicon/android-chrome-512x512.png",
    "revision": "83cf00ca81517e5a0178f3322895462b"
  },
  {
    "url": "site/static/images/icons/favicon/apple-touch-icon.png",
    "revision": "98a23a75e655ec08f2b91fa9b0b0dd96"
  },
  {
    "url": "site/static/images/icons/favicon/favicon-16x16.png",
    "revision": "93e6f1244ed4772f8392f390a1eca560"
  },
  {
    "url": "site/static/images/icons/favicon/favicon-32x32.png",
    "revision": "2534f65605216584b632c9003835b9c3"
  },
  {
    "url": "site/static/images/icons/favicon/favicon.ico",
    "revision": "3a98ca9abe14bc47f5ef6a53d66e30a9"
  },
  {
    "url": "site/static/images/icons/favicon/mstile-150x150.png",
    "revision": "0f472f85aa4becee99d607ce59371054"
  },
  {
    "url": "site/static/images/icons/favicon/safari-pinned-tab.svg",
    "revision": "f99372dd39eefaacda39fa89afc985fc"
  },
  {
    "url": "site/static/images/icons/fire-spell-cast.svg",
    "revision": "e6c09f4fceb5d0f9b9da29547102801e"
  },
  {
    "url": "site/static/images/icons/flame.svg",
    "revision": "e7879a3663ef74eb3d6f54de66f1d54d"
  },
  {
    "url": "site/static/images/icons/heart-beats.svg",
    "revision": "78b50894a514de0ff5d61a5c454b4d5d"
  },
  {
    "url": "site/static/images/icons/hearts.svg",
    "revision": "034a48b95c54e76616dc0e042b79cace"
  },
  {
    "url": "site/static/images/icons/ink-swirl.svg",
    "revision": "03f49b4335e04b72962a39500550bcd0"
  },
  {
    "url": "site/static/images/icons/magic-swirl.svg",
    "revision": "4b5f5651f170ee64e54d4b097e18f2d7"
  },
  {
    "url": "site/static/images/icons/power-lightning.svg",
    "revision": "96d1686c81be23108c2b1406f257bfbc"
  },
  {
    "url": "site/static/images/icons/prayer.svg",
    "revision": "68f8bc222e88c2fa69518c8fdb44d230"
  },
  {
    "url": "site/static/images/icons/quiver.svg",
    "revision": "901d20011d0dc10cc23b3f0558993a33"
  },
  {
    "url": "site/static/images/icons/raise-zombie.svg",
    "revision": "7a1e1dc035aaa4789c7e7acef779ad7c"
  },
  {
    "url": "site/static/images/icons/shield.svg",
    "revision": "8396f1cb288bb874fabd6fb1dc5bee2b"
  },
  {
    "url": "site/static/images/icons/swap-bag.svg",
    "revision": "afec826ccb7fa028059ef137e6ef1102"
  },
  {
    "url": "site/static/images/icons/sword-brandish.svg",
    "revision": "218202da8fc960eb2c13a2ee20b7d5b5"
  },
  {
    "url": "site/static/images/icons/swords-power.svg",
    "revision": "50efddea824e634ab7a44d8f432de928"
  },
  {
    "url": "site/static/images/icons/tombstone.svg",
    "revision": "5080916dfa69b9c2adac3a167f1052a7"
  },
  {
    "url": "site/static/images/monsters/slime_assumzaek.jpg",
    "revision": "1787eea0ad338efe0e6fea9d372cb576"
  },
  {
    "url": "site/static/images/pantheon/beleth_by_000fesbra000_dd4u96o-fullview.jpg",
    "revision": "c705101449296cee62a9268451c1e0c3"
  },
  {
    "url": "site/static/images/pantheon/dbv83x5-e64aab12-1473-48e1-99d9-33a57cbac7f2.jpg",
    "revision": "c981813b16f3e4bb0a306bb1d5d4f9fb"
  },
  {
    "url": "site/static/images/pantheon/dd75667-75db882d-42cc-4a00-9b68-115fe9f028bc.jpg",
    "revision": "b43ad66aec4d5c888fb042e6f29810a7"
  },
  {
    "url": "site/static/images/pantheon/morgoth_and_the_silmarils_by_000fesbra000_dbf2kfp-fullview.jpg",
    "revision": "aca7e93d3ccc99f83beaa03c4e3dcb6d"
  },
  {
    "url": "site/static/images/pantheon/owl_by_ex_trident_daiynql-fullview.jpg",
    "revision": "a9a6dbfda7e8543ad89d4518ddee7e50"
  },
  {
    "url": "site/static/images/pantheon/sea_serpent_by_co_boldt_d2qbcdy-fullview.jpg",
    "revision": "c9b665985afe321f7b5197cbbcbc2d47"
  },
  {
    "url": "site/static/images/pantheon/under_the_willow_tree__by_secret_s_d8yzsg9-fullview.jpg",
    "revision": "6a2b0762265b7d1cb1f6a7258149ed48"
  },
  {
    "url": "site/static/images/parchement.png",
    "revision": "2d99c17ac4ce8f38eae682d967ebade9"
  },
  {
    "url": "site/static/images/race/female/automaton.jpg",
    "revision": "9de7bcb704dd7804e99e18cfa83d6fb4"
  },
  {
    "url": "site/static/images/race/female/catterwol.jpg",
    "revision": "775cc3f7e10770fdb0540d27ac5dcccd"
  },
  {
    "url": "site/static/images/race/female/comingsoon.jpg",
    "revision": "fabca670d5bc7fb72edbbcbdff7a6149"
  },
  {
    "url": "site/static/images/race/female/daemonspawn.jpg",
    "revision": "6c76f6dd11cf37dbd96b9fe8cfc3f02a"
  },
  {
    "url": "site/static/images/race/female/deep_elf.jpg",
    "revision": "467f98e069bcfe94acdd9f2e1192cf3a"
  },
  {
    "url": "site/static/images/race/female/dwarf.jpg",
    "revision": "93a43cc1967a7e3d8a0c017f74e07089"
  },
  {
    "url": "site/static/images/race/female/fleetfoot.jpg",
    "revision": "60742cc835b36e0a6e21516991c10cf5"
  },
  {
    "url": "site/static/images/race/female/gnome.jpg",
    "revision": "e05c11926a86536c9ffd829f63a7f106"
  },
  {
    "url": "site/static/images/race/female/goblin.jpg",
    "revision": "71bba3ea30434b1566eb498ec7b2ff7e"
  },
  {
    "url": "site/static/images/race/female/halfling.jpg",
    "revision": "dc073ffa3aad64e46eaccb2b907d6a2a"
  },
  {
    "url": "site/static/images/race/female/high_elf.jpg",
    "revision": "e640076451af1fd0268405e45e88fd99"
  },
  {
    "url": "site/static/images/race/female/hissling.jpg",
    "revision": "7484df0c4a008e66de38e7955f95dcab"
  },
  {
    "url": "site/static/images/race/female/human.jpg",
    "revision": "7458baecb86e0eaf5c1118d6d2a6300a"
  },
  {
    "url": "site/static/images/race/female/kragraven.jpg",
    "revision": "20389ee0b9bd86032c725fce3545ac6f"
  },
  {
    "url": "site/static/images/race/female/lizkin.jpg",
    "revision": "d61adf5ce906f891c70eece649e11833"
  },
  {
    "url": "site/static/images/race/female/orc.jpg",
    "revision": "88e1dee0ab61c729ab76b869e9910bbc"
  },
  {
    "url": "site/static/images/race/female/sprout.jpg",
    "revision": "b1c2bb1a2d69922299a9c39c1e221010"
  },
  {
    "url": "site/static/images/race/female/waterborn.jpg",
    "revision": "065d24d896b4328dea94021229cf4f2e"
  },
  {
    "url": "site/static/images/race/female/wood_elf.jpg",
    "revision": "c29997f8a3d9fa1ccc30ab640923429d"
  },
  {
    "url": "site/static/images/race/male/automaton.jpg",
    "revision": "9de7bcb704dd7804e99e18cfa83d6fb4"
  },
  {
    "url": "site/static/images/race/male/catterwol.jpg",
    "revision": "54b4122103d69841b773cc761f9fe016"
  },
  {
    "url": "site/static/images/race/male/comingsoon.jpg",
    "revision": "fabca670d5bc7fb72edbbcbdff7a6149"
  },
  {
    "url": "site/static/images/race/male/daemonspawn.jpg",
    "revision": "99bad0f4a7fb28b6ffd8a652f8fc91aa"
  },
  {
    "url": "site/static/images/race/male/deep_elf.jpg",
    "revision": "97f27e20eeef644b4972dedd6c608283"
  },
  {
    "url": "site/static/images/race/male/dwarf.jpg",
    "revision": "7498b94114e2e6875e848c0a0e24a694"
  },
  {
    "url": "site/static/images/race/male/gnome.jpg",
    "revision": "b84432d8709aefeab1691b77bdbe8d84"
  },
  {
    "url": "site/static/images/race/male/goblin.jpg",
    "revision": "bebfa44ab43d49034e908ff9b0720bf3"
  },
  {
    "url": "site/static/images/race/male/halfling.jpg",
    "revision": "8e8c6364ade8e305ff0848b30bf93ba8"
  },
  {
    "url": "site/static/images/race/male/high_elf.jpg",
    "revision": "d933810b86ce8c9710c02fa9203247a9"
  },
  {
    "url": "site/static/images/race/male/hissling.jpg",
    "revision": "7484df0c4a008e66de38e7955f95dcab"
  },
  {
    "url": "site/static/images/race/male/human.jpg",
    "revision": "939c1eb3a24baccf8ac9f35db938feb8"
  },
  {
    "url": "site/static/images/race/male/kragraven.jpg",
    "revision": "20389ee0b9bd86032c725fce3545ac6f"
  },
  {
    "url": "site/static/images/race/male/lizkin.jpg",
    "revision": "2646b164f0d55091f04b9ec1901816e7"
  },
  {
    "url": "site/static/images/race/male/OLD_waterborn.jpg",
    "revision": "1d2326ae7abef333e63fa52d69e7c7e7"
  },
  {
    "url": "site/static/images/race/male/orc.jpg",
    "revision": "3cdab6d56120065e5209ae5c170340b3"
  },
  {
    "url": "site/static/images/race/male/sprout.jpg",
    "revision": "3d08d7b301aea0107d4a7dace6e4f0a1"
  },
  {
    "url": "site/static/images/race/male/waterborn.jpg",
    "revision": "d14fa84ae9513e69b44b743bdc0e3238"
  },
  {
    "url": "site/static/images/race/male/wood_elf.jpg",
    "revision": "b4676c5f49aee59e353adfc1aee47f47"
  },
  {
    "url": "site/static/images/subtle_white_mini_waves_transparent.png",
    "revision": "46fa7bc6701397be5c2dc6c54204f8a9"
  },
  {
    "url": "site/static/images/subtle_white_mini_waves.png",
    "revision": "12104a00b998ab058b6dbec0580411c6"
  },
  {
    "url": "site/static/images/tier/heroic.jpg",
    "revision": "8a502c9afd0d6f83ef8435e298805600"
  },
  {
    "url": "site/static/images/tier/legendary.jpg",
    "revision": "454b58a41c2f58f18040733e4fbc32dd"
  },
  {
    "url": "site/static/images/tier/new.jpg",
    "revision": "a9dcde70c1a63cdb4deb5428a1e8068c"
  },
  {
    "url": "site/static/images/tried.png",
    "revision": "14ac00699cc215a6ada0a9d7049dd171"
  },
  {
    "url": "site/templates/character_creation_helper_template.html",
    "revision": "b3ca7bd0af54d17489753ce8f38bbc76"
  },
  {
    "url": "site/templates/character_selection_template.html",
    "revision": "3a976401cadbf56fe507f1e27f1dcf14"
  },
  {
    "url": "site/templates/character_sheet_template.html",
    "revision": "5c12a42ac61d4cd59efbf1617e658311"
  },
  {
    "url": "site/templates/level_up_sheet_template.html",
    "revision": "e5f1df6b6985458318ea6a84a18db3d4"
  },
  {
    "url": "site/templates/macros.html",
    "revision": "20b2655c0f33a390bf72a1a5dcf06eaa"
  },
  {
    "url": "site/templates/role_selection_template.html",
    "revision": "dd67cf0817ca2711216907cddc37b938"
  },
  {
    "url": "site/templates/selector_template.html",
    "revision": "966c0c5dde4bcd5a551636cbaaf60f66"
  },
  {
    "url": "site/templates/two_sided_character_sheet.html",
    "revision": "ba9898bfb4d76c7bc1b6e725a0504b8e"
  },
  {
    "url": "site/templates/updated_character_sheet.html",
    "revision": "a32376ee2b7821548b76c58dd517411f"
  },
  {
    "url": "site/templates/weapons_page.html",
    "revision": "1630b7330520194e4999120297e13ae4"
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
    "revision": "5a1215765255fc4952aa7df2ef125f0a"
  },
  {
    "url": "index.html",
    "revision": "20698344722a4b1e1ea4d3107b7b234f"
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
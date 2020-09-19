---
landscape_banner_path: /site/images/backdrops/landscape_banner.jpg
landscape_banner_link: https://www.deviantart.com/themefinland/art/The-winding-path-commission-800945478
landscape_banner_name: The winding path
landscape_banner_artist: ThemeFinland
landscape_banner_artist_link: https://www.deviantart.com/themefinland
landscape_banner_license: CC BY-NC-SA 3.0
landscape_banner_license_link: https://creativecommons.org/licenses/by-nc-sa/3.0/

portrait_banner_path: /site/images/backdrops/portrait_banner.jpg
portrait_banner_link: https://www.deviantart.com/ncorva/art/Call-to-adventure-664775437
portrait_banner_name: Call to Adventure
portrait_banner_artist: ncorva
portrait_banner_artist_link: https://www.deviantart.com/ncorva
portrait_banner_license: CC BY-NC-ND 3.0
portrait_banner_license_link: https://creativecommons.org/licenses/by-nc-nd/3.0/

show_download: true
indexpage: true
---
<script type="module">
import {Workbox, messageSW} from 'https://storage.googleapis.com/workbox-cdn/releases/5.1.2/workbox-window.prod.mjs';

function createUIPrompt(opts) {
  if (confirm('Hey, it looks like you have an old version of the RnR site cached. Would you like to update it?')) {
     opts.onAccept()
  }
}

if ('serviceWorker' in navigator) {
  const wb = new Workbox('/service_worker.js');
  console.log("true");
  let registration;

  const showSkipWaitingPrompt = (event) => {
    // `event.wasWaitingBeforeRegister` will be false if this is
    // the first time the updated service worker is waiting.
    // When `event.wasWaitingBeforeRegister` is true, a previously
    // updated service worker is still waiting.
    // You may want to customize the UI prompt accordingly.

    // Assumes your app has some sort of prompt UI element
    // that a user can either accept or reject.
    const prompt = createUIPrompt({
      onAccept: async () => {
        // Assuming the user accepted the update, set up a listener
        // that will reload the page as soon as the previously waiting
        // service worker has taken control.
        wb.addEventListener('controlling', (event) => {
          window.location.reload();
        });

        if (registration && registration.waiting) {
          // Send a message to the waiting service worker,
          // instructing it to activate.
          // Note: for this to work, you have to add a message
          // listener in your service worker. See below.
          messageSW(registration.waiting, {type: 'SKIP_WAITING'});
        }
      },

      onReject: () => {
        prompt.dismiss();
      }
    });
  };

  // Add an event listener to detect when the registered
  // service worker has installed but is waiting to activate.
  wb.addEventListener('waiting', showSkipWaitingPrompt);
  wb.addEventListener('externalwaiting', showSkipWaitingPrompt);

  wb.register().then((r) => registration = r);
}
</script>

# Rangers and Ruffians
_Version 2.4.0_


## What is Rangers and Ruffians?
Rangers and Ruffians
is a fantasy tabletop roleplaying game (RPG) created for and by a group of
nerdy friends. It can be dramatic, epic, and meaningful.
It can also be silly and funny. We think that it is usually pretty fun.

### How do you play?
1. [Read The Rulebook](/site/pages/GENERATED/Rulebook.md)


### Build your Character
1. [Choose your Race and Class](/site/pages/GENERATED/Compendium_of_Character_Creation.md)
2. [Choose your Spells](site/pages/GENERATED/Tome_of_the_Ancients.md)
3. [Choose your Deity](site/pages/GENERATED/Book_of_Lore.md)
4. [Create your Character Sheet](site/pages/character_sheet.html)


### Run the Game
1. [Read The Rulebook](/site/pages/GENERATED/Rulebook.md)
2. [Study the Monsters](site/pages/GENERATED/Book_of_Known_Beasts.md)
3. [Download Printed Materials](site/pages/GENERATED/Printed_Materials.md)


## Keep up to Date
1. [View the Changelog](site/pages/GENERATED/Changelog.md)


## Work in Progress
1. [Test the Character Creation Helper](site/pages/character_creation_helper_page.html)

<!-- ### Why Should You Play Rangers and Ruffians?
* __Good for Beginners__
  * Rangers and Ruffians is a great introduction to the world of tabletop gaming. With a simple to understand
    set of rules and easily scalable difficulty, R&R was designed with new players in mind. To this end, R&R
    boasts simple but scalable core mechanics, while removing the complicated bloat that makes other tabletop
    games daunting for beginners.
* __Cheap to Start__
  * All core rules necessary to play Rangers and Ruffians are housed on this site. This keeps the cost of
    entry low, so that you can start playing almost immediately.
* __Constant Updates__
  * Rangers and Ruffians is a passion project, which is constantly receiving new content including new
    classes, races, rules, and tuning.
 -->

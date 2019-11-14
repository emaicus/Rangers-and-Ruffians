 * [Rangers and Ruffians Rulebook _Version 2.1.0_](#rangers-and-ruffians-rulebook-_version-2.1.0_)  
   * [Versioning and the Changelog](#versioning-and-the-changelog)  
   * [Introduction](#introduction)  
     * [What is Rangers and Ruffians?](#what-is-rangers-and-ruffians?)  
     * [What do you need to play?](#what-do-you-need-to-play?)  
     * [How does the game work?](#how-does-the-game-work?)  
   * [Being the Grand Poohbah](#being-the-grand-poohbah)  
   * [Participating as a Player](#participating-as-a-player)  
   * [Dice and Rolling](#dice-and-rolling)  
     * [Advantage and Disadvantage](#advantage-and-disadvantage)  
     * [Inspiration Dice](#inspiration-dice)  
     * [Saving Throws](#saving-throws)  
   * [Stats and Abilities](#stats-and-abilities)  
     * [Core Stats](#core-stats)  
     * [Stat Values](#stat-values)  
     * [Diminishing Returns: The Most Confusing Rule in Rangers and Ruffians](#diminishing-returns-the-most-confusing-rule-in-rangers-and-ruffians)  
     * [Bonus Stat: Health Die](#bonus-stat-health-die)  
     * [Abilities](#abilities)  
     * [Action Points](#action-points)  
     * [Spell Power](#spell-power)  
   * [Combat](#combat)  
     * [Initiative](#initiative)  
     * [Your Turn](#your-turn)  
     * [The Enemy Turn](#the-enemy-turn)  
     * [Attacking](#attacking)  
     * [Critical Hits](#critical-hits)  
     * [Weapons](#weapons)  
     * [Combat Abilities](#combat-abilities)  
     * [Hitting Zero Health](#hitting-zero-health)  
   * [Health, Rest, and Healing](#health,-rest,-and-healing)  
     * [Rest](#rest)  
   * [Magic](#magic)  
     * [Spell Tiers](#spell-tiers)  
     * [Learning new Spells](#learning-new-spells)  
   * [Leveling Up](#leveling-up)  
     * [When do I Level Up?](#when-do-i-level-up?)  
     * [What Happens when I Level Up?](#what-happens-when-i-level-up?)  
   * [Building a Character](#building-a-character)  
     * [Personality and Background](#personality-and-background)  
     * [Health Dice Pieces](#health-dice-pieces)  
   * [How do I Compute my Character's Stats?](#how-do-i-compute-my-character's-stats?)  
     * [Method 1 (Easiest) Use Pre-generated Stats:](#method-1-(easiest)-use-pre-generated-stats)  
     * [Method 2 (Easy) Standard Array:](#method-2-(easy)-standard-array)  
     * [Method 3 (High Risk, High Reward) Roll:](#method-3-(high-risk,-high-reward)-roll)  
   * [Races](#races)  
     * [Automaton](#automaton)  
     * [Catterwol](#catterwol)  
     * [Daemonspawn](#daemonspawn)  
     * [Deep Elf](#deep-elf)  
     * [Dwarf](#dwarf)  
     * [Fleetfoot Halfling](#fleetfoot-halfling)  
     * [Gnome](#gnome)  
     * [Goblin](#goblin)  
     * [Hardfoot Halfling](#hardfoot-halfling)  
     * [High Elf](#high-elf)  
     * [Hissling](#hissling)  
     * [Human](#human)  
     * [Kragraven](#kragraven)  
     * [Lizkin](#lizkin)  
     * [Orc](#orc)  
     * [Sprout](#sprout)  
     * [Waterborn](#waterborn)  
     * [Wood Elf](#wood-elf)  
   * [Classes](#classes)  
     * [Archer](#archer)  
     * [Barbarian](#barbarian)  
     * [Bard](#bard)  
     * [Beastmaster](#beastmaster)  
     * [Cleric](#cleric)  
     * [Druid](#druid)  
     * [Fighter](#fighter)  
     * [Gunslinger](#gunslinger)  
     * [Highborn](#highborn)  
     * [Knight](#knight)  
     * [Monk](#monk)  
     * [Necromancer](#necromancer)  
     * [Paladin](#paladin)  
     * [Ranger](#ranger)  
     * [Rogue](#rogue)  
     * [Sorcerer](#sorcerer)  
     * [Wizard](#wizard)  
   * [Skills](#skills)  
   * [Spellbooks](#spellbooks)  
     * [The Bard's Songbook](#the-bard's-songbook)  
     * [The Book Of Chi](#the-book-of-chi)  
     * [The Book Of Healing](#the-book-of-healing)  
     * [The Druid's Guidebook](#the-druid's-guidebook)  
     * [The Macabre Manual](#the-macabre-manual)  
     * [The Novice Spellbook](#the-novice-spellbook)  
     * [The Sorcerer's Scrolls](#the-sorcerer's-scrolls)  
     * [The Tome Of The Ancients](#the-tome-of-the-ancients)  
     * [The Wizard's Addendum](#the-wizard's-addendum)  

  
# Rangers and Ruffians Rulebook _Version 2.1.0_

  
## Versioning and the Changelog
The Version Number used by Rangers and Ruffians is broken into
3 parts, each of which is separated by a period. The greatest (leftmost)
digit represents a massive refactor to the core systems of the game
which requires an entirely new ruleset to be adopted. This version was first
incremented when the character leveling system was added to Rangers and Ruffians.
  
  
The second digit represents the introduction of a new subsystem to the
rules of the game which is not significant enough so as to impact the
broader ruleset. This number was first incremented in Rangers and Ruffians
2.1.0, when ```Skills``` were added to the game which could be learned
when leveling up as an alternative to a Stat increase.
  
  
The final, and least significant digit represents a balance change
which does not change any existing systems within the game. These
are usually binned together into one large incremental update.
For example, if a set of spells were deemed to be underpowered and
there power was slightly increased, the the third version digit
would be incremented.
  
  
The majority of revisions made to Rangers and Ruffians after the
transition to version 2.0.0 are recorded in the ```changelog.md``` file
found in the ```docs``` folder of the Rangers and Ruffians repository.
For details about what changed between two versions of the game,
please consult that documentation.
  
  

  
## Introduction
  
  

  
### What is Rangers and Ruffians?
Rangers and Ruffians (also called just "Rangers" or "RnR")  
is a tabletop roleplaying game (RPG) created for and by a group of
nerdy friends. It can be dramatic, epic, and meaningful.
It can also be silly and funny. We think that it is usually pretty fun.  
  
  
Once upon a time, Rangers and Ruffians was built from the
ground up to be as easy to jump into as possible, especially
for brand new players. The initial rule-set included in
what is now called Rangers And Ruffians 1.0.0 was so
bare-bones that it didn't include numbers for the player to
reference. As the game grew, and the core rules were expanded
upon, some numbers became necessary. New ideas, like character
leveling and specialized skills crept in. These ideas have
greatly enriched the RnR experience, but have also slowly
added to the complexity of the game. With the introduction
of RnR 2.1.0, we look to formalize the rules of the game,
and to re-evaluate them through the lens of our initial vision:
that tabletop RPGs are for _everyone,_ and not just for people
who like to crunch numbers and watch fantasy movies and
shows on the weekend. We have found that other (far more popular)
tabletop RPGs are difficult for an outsider to join without
the help of a friend who is "in the know," and even then that
their rulesets can be obtuse and difficult to parse.
We hope that our iteration on the awesome genre that is the
tabletop RPG is deep and rich enough to serve as an engine
for epic, fun adventures, while still being simple enough
so that you and your friends can play for the first time
this weekend.
  
  

  
### What do you need to play?
  
  
In order to play Rangers and Ruffians, you need the following:
  
  
1. At least one set of polyhedral dice (the nerdy ones).
2. One player who has read these rules, and who will [run the story of your game](#being-the-grand-poohbah).
3. A printed or digital version of this manual and the Poohbah's Handbook,
   which contain all of the rules necessary to embark upon your adventure!
  
  

  
### How does the game work?
The core idea of a tabletop roleplaying game is relatively simple; a group of
players come together and weave a shared tale of adventure. To give these
adventures structure, most tabletop RPGs have two classes of participant,
one or more "players" and a single "storyteller". Each "player" takes control
of one ingame avatar, while the imagination of the storyteller drives everything
else in the world. Many games call the storyteller a "Game Master" (GM) or "Dungeon Master"
(DM). We chose to give this role a title which we feel is more befitting of the importance
of its station, the __Grand Poohbah.__ In Rangers and Ruffians (and many other tabletop
roleplaying games) __dice__ are used to determine the outcome of player actions within
the game world. It is the Poohbah’s job, then, to call for and interpret dice rolls.
  
  
A realistic ingame interaction might look something like this:
  
  
>Poohbah: The door before you stands locked. The corridors of the castle are quiet, save for the steady dripping of water from the ceilings.  
Player 1: I’ll attempt to pick the lock.  
Poohbah: Alright, roll for it.
Player 1: 8, and my dexterity is 2, so that’s an 11.  
Poohbah: You spend a moment trying to pick the lock, but it doesn’t seem to want to budge.  
Player 2: URTAG THE STRONG KICKS THE DOOR DOWN!  
Player 1: Urtag! You’re going to wake the whole castle!  
Poohbah (grinning): Roll for it.  
Player 2: I got an 18!  
Poohbah (grinning): There is a crash as the door bursts into splinters, but that sound is drowned out by Urtag’s savage cries.  
Player 2 (nodding): Damn right it is.  
  
  
In the above interaction, there are a few things to note. Twice, the Poohbah called for rolls.
If Player 1 had rolled higher, the lock would have been picked. The difficulty of this lock was
set by the Poohbah before the roll was called for. This failure gave Player 2, or "Urtag the
Strong," the chance to jump in and do something. There is no inherent turn order in this scenario,
so it is up to the Poohbah to choose who goes first.
  
  
On the topic of Player 2, it is important to make certain that your party likes the idea of
having a "kill first, ask questions later" character in their party. Hijinks are incredibly fun,
and are the font from which most of the life of a tabletop RPG flows, but remember not to be a jerk.
  
  
  
  

  
## Being the Grand Poohbah
Regardless of the tabletop RPG being played, the Game Master (or Grand Poohbah)
is the unsung hero. It is up to the Poohbah to present the game's world,
arbitrate player interactions, and to interpret the game's rules. Despite
(and because of) this, being the Grand Poohbah can be an enormously satisfying
experience. To be a Grand Poohbah and run Rangers and Ruffians, you will need
three things in addition to those presented above in the ```What do you need to play?```
section:
  
  
1. To read the rules presented in this document, so that you can make informed decisions
   and help your players learn the game.
2. To read the ```Poohbah's Handbook```, a companion to this document which provides
   additional insight into the rules, help with encounter building, and much, much more!
3. To remember the most important rule of being a Game Master or Poohbah in _any_ tabletop RPG:
  
  
>If the players are having fun, you are doing a good job.
  
  

  
## Participating as a Player
Participating as a player in Rangers and Ruffians is a bit easier than being the
Poohbah. However, that doesn't mean that you shouldn't take it seriously. The
Poohbah may present the world, but only _you_ can engage with it! Before we get
into the intricacies of the rules of Rangers and Ruffians, please remember the
following rules, which are integral to _all_ tabletop RPGs:
  
  
1. It is the Poohbah's job to present the world. It is my job to engage with it.
2. Tabletop RPGs are cooperative. This means that all players should have a chance to shine.
3. Treat your fellow players and the Poohbah the way that you want to be treated.
  
  
  
  

  
## Dice and Rolling
As mentioned above in the section [How does the Game Work?](#how-does-the-game-work)
Rangers and Ruffians uses dice to determine whether or not an action succeeds.
The process of making a __check__ is simple:
  
  
1. The Poohbah presents a situation his or her players.
2. One of the players declares that they would like to do something.
3. If the Poohbah thinks that they could reasonably succeed or fail,
   they call for a check, and assign that check a target difficulty.
  
  
It is left entirely to the Poohbah's discretion for which actions a check
should or should not be called for. For example, if a player is playing
a Rogue (a dexterous, sneaky character) and they say that they want to
climb a small wall, the Poohbah may not ask for a check, as it is reasonable
to say that the player could easily perform that action without failure.
If a player playing a heavily armored Hardfoot Halfling (a short, stocky race)
asked to climb the same wall, the Poohbah may call for a check. Similarly,
if the wall was slick with rain, even the Rogue may have to make a check
due to the increased difficulty of the task at hand.
  
  
There are a total of seven dice that are used in RnR, all of which can
be purchased online as a set or at your local hobby shop. These dice are
the ```d4```, ```d6```, ```d8```, ```d10```, ```d12```, ```d20```, and
the ```percentile``` die (a ```d10``` with two digits on each side).
We name dice with ```d``` and then the number of sides on the die.
Therefore, a ```d4``` has 4 sides, a ```d6``` is the 6 sided die with
which you are most familiar, a ```d8``` has 8 sides, and so on and so forth.
  
  
The most important dice in our toolbox is the ```d20```, which is rolled whenever
a __check__ is made.
  
  
When multiple dice of a type must be rolled, a number is put before the ```d```.
Therefore ```2d6``` means that 2 six sided die must be rolled, and their value
summed. ```4d8``` means that 4 eight sided die must be rolled and their
total summed.
  
  
Sometimes, a __modifier__ is applied to a roll. This is added as a ```+```
or ```-``` at the end of a roll. For example ```1d6 + 2``` calls for
1 six sided die to be rolled, and then 2 added to the result.
  
  
In some cases, it is necessary to roll a ```d100```. Since we
don't actually have a 100 sided die, we instead roll a ```percentile```
and a ```d10```. When we do this, the ```percentile``` represents the tens
place, and the ```d10``` the ones place. The minimum roll, then, is
a ```0``` (where we roll a zero on both the ```d10``` and the ```percentile```)
and the maximum roll is a ```99``` (where we roll a ```90``` on the ```percentile```
and a ```9``` on the ```d10```).
If we rolled a ```60``` on the ```percentile```, and a ```4``` on the ```d10```,
we would say that we rolled a ```64```.
  
  

  
### Advantage and Disadvantage
When a character is especially good or bad at something in Rangers and Ruffians,
they may have __Advantage__ or __Disadvantage__ at that thing. For example, the
sneaky Rogue mentioned earlier earlier is good at hiding, so it has advantage.
This means that, when the rogue tries to hide, they get to roll a ```d20``` twice,
and keep the higher roll. So if the rogue rolled a ```10``` followed by a ```15```,
they would keep the ```15```. __Disadvantage__ is similar, but the player keeps the
_worse_ of the two rolls. So in the case above, if the rogue had disadvantage,
they would keep the ```10```. When you build your character, you advantages and
disadvantages will be explicitly listed out for you. However, your Poohbah
may sometimes call for a role with advantage or disadvantage even though
the rules of the game do not explicitly give you advantage or disadvantage
in that scenario. There is no concept of "double advantage" or "double disadvantage"
in Rangers and Ruffians. If you are performing a task and are gaining advantage
from multiple abilities, you still only role twice. If you have advantage and
disadvantage at the same time, they cancel out.
  
  
  
  

  
### Inspiration Dice
Sometimes, an ability or spell cast on a player will give them an __Inspiration Dice__.
An Inspiration Dice is a dice which can be added to a check of the players
choosing. Once an inspiration dice is spent, it disappears, and cannot be used
again. So if a player had a ```d4``` inspiration dice and was asked to make
a stealth check, they could choose to roll ```1d4``` and add the result
to their check. You must declare your intent to use an inspiration dice _before_
your Poohbah says if you succeed or fail at a check.
  
  

  
### Saving Throws
Saving throws are special checks that are made when something bad is happening
to an entity (a player, npc, or enemey) in RnR. The most important of these is the
__Spell Saving Throw.__ A spell saving throw occurs when someone tries to cast
a spell on someone else. For example, if a character is a wizard, and tries
to turn a villager into a frog, the villager must make a spell saving
throw. See the [Spell Power](#spell-power) section for details about
this saving throw.
  
  

  
## Stats and Abilities
Characters in RnR are made up of __Stats__ and __Abilities__. __Stats__ attempt
to capture the physical, mental, and social prowess of a character. A relevant stat
is almost always added to the result of a check. The seven stats in Rangers and
Ruffians are as follows:
  
  

  
### Core Stats

  
#### Strength
__Strength__ (STR) is defined as raw power of the body. Strength influences the way that
you play the game in three ways:
1. __Strength is added to strength checks.__ You enter a dungeon, and see
  a friend trapped in a cell. You desperately want to get them out, so you decide
  to bend the bars. In this scenario, you add your strength to a ```d20``` roll.
2. __Strength affects strength weapon damage.__ In combat, your strength is added to
  the amount of damage you do with strength based weapons such as warhammers, great-axes,
  and clubs.
3. __Strength affects the type of armor you can wear.__ The stronger you are, the heavier
  the armor that you can wear.
  
  

  
#### Dexterity
__Dexterity__ (DEX) is defined as mobility, nimbleness, and ability with the body.
Dexterity affects the way that you play the game in two ways:
1. __Dexterity is added to dexterity checks.__ You are chasing a fleeing thief across
  the rooftops of a city. You come up to a gap, and have to jump! In this scenario,
  you would add your dexterity to a ```d20``` roll.
2. __Dexterity affects your dexterity weapon damage.__ In a combat scenario, dexterity
  is added to the amount of damage you do with dexterity based weapons, such as spears,
  daggers, and falchions.
  
  

  
#### Intelligence
__Intelligence__ (INT) is defined as raw aptitude with the mind. Intelligence affects the
way that you play the game in two key ways.
1. __Intelligence is added to intelligence checks.__
2. __Intelligence affects your number of action points.__ In Rangers and Ruffians, action points
  are treated as a resource which is used to perform special abilities or to cast spells. This means
  that the more action points you have, the more abilities you can use or spells you can cast. Action
  points are further detailed in the [Action Points](#action-points) section.
  
  

  
#### Inner Fire
__Inner Fire__ (INF) is defined as mental fortitude, resolve, and strength of will. Inner Fire affects the way
that you play the game in three ways.
1. __Inner Fire is added to magical attacks.__ If your character is a mage who attacks with magic,
   Inner Fire is added to any damage that you deal.
2. __Inner Fire affects how susceptible your character is to spells.__ Inner Fire is added to most
  [__Spell Saving Throws__](#spell-saving-throws) in the game. This means that having a higher Inner Fire means
  that you are less likely to be affected by enemy spells.
3. __Inner Fire determines how likely your spells are to affect an enemy.__ If one of your spells imposes
  a  [__Spell Saving Throws__](#spell-saving-throws) on an enemy, the target that the enemy is trying to beat
  is directly influenced by your inner fire. This is further detailed in the
  [__Spell Power__](#spell-power) section.
  
  

  
#### Charisma
__Charisma__ (CHA) is defined as force of personality, or how charming your character can be. Charisma can
affect the way you play the game in two ways:
1. __Charisma is added to charisma checks.__ You speak with the local innkeeper and have a feeling that
  he's keeping something from you. You don't think that he's a dangerous person, but rather that someone
  or *something* is stopping him. In this scenario, you would want high charisma, so that you can convince
  him to help you despite the risk.
2. __(Conditional) If you are playing a Sorcerer, Charisma determines whether or not your spells succeed or
  fail.__ Further detailed in the [Sorcerer](#sorcerer) section.
  
  

  
#### Perception
__Perception__ (PER) determines how likely it is your character will notice things going on in the world around them.
It affects the way you play the game in two ways:
1. __Perception is added to perception checks.__ You are riding through the forest at night. Little do you know,
   a trio of goblins lie in ambush. In this scenario, you would want high perception.
2. __Perception is added to combat initiative.__ When in combat, __Initiative__ is rolled to determine turn order.
  Perception is added to such checks, so that characters who are better at reading a situation tend to go first.
  Initiative is further detailed in the [Initiative](#initiative) section.
  
  

  
#### Luck
When all else fails, there's always __luck__ (LUK)! Luck is a special stat, and is the only stat that cannot go negative.
Each day, a player gets __Luck Tokens__ equal to their luck. When a roll doesn't go your way, you may spend
one luck token to re-roll it. See the section on [Resting](#resting) for information about
how to get luck tokens back.
  
  

  
### Stat Values
Stats in Rangers and Ruffians range between ```-5``` and ```+5```. However, usually they are
between ```-3``` and ```3```. When a character is at very low levels, their stats tend to be relatively low.
As they grow and get stronger, their stats increase. For more details about increasing stats, see the
[Leveling Up](#leveling-up) section.
  
  

  
### Diminishing Returns: The Most Confusing Rule in Rangers and Ruffians
Thus far, we have treated stats as increasing linearly (e.g. if you dexterity is 3, you add 3 to a roll).
In fact, for the balancing of leveling up in Rangers and Ruffians
to work, this is not always true. Instead, the rule is as follows.
1. If your value for a stat is between -3 and 3, that is the value that you add to a roll.
2. If your value for a stat is less than -3 or greater than 3, we treat things a little bit differently.
  1. The first 3 in either direction are worth 1 full point.
  2. After that, further values are worth .5 points.
  3. Half points are rounded towards zero.
  4. So, if a character's Dexterity is 5, they would add 4 to a check.
  
  
Let's unpack this idea with a table:
  
  
| Stat Value     | What is added to a check |
| -------------- |---------------|
| -7             | -5 |
| -6             | -4 |
| -5             | -4 |
| -4             | -3 |
| -3             | -3 |
| -2             | -2 |
| -1             | -1 |
|  0             |  0 |
|  1             |  1 |
|  2             |  2 |
|  3             |  3 |
|  4             |  3 |
|  5             |  4 |
|  6             |  4 |
|  7             |  5 |
  
  
Note how for the core of the table (-3 to 3) the stats behave linearly.
  
  
| Stat Value     | What is added to a check |
| -------------- |---------------|
| -3             | -3 |
| -2             | -2 |
| -1             | -1 |
|  0             |  0 |
|  1             |  1 |
|  2             |  2 |
|  3             |  3 |
  
  
After that, we begin adding half points. However, half points don't make any sense, so we round down:
  
  
| Stat Value     |  Half Point |Rounds To |
| -------------- |---------------| --------------- |
|  0             |  0   | 0 |
|  1             |  1   | 1 |
|  2             |  2   | 2 |
|  3             |  3   | 3 |
|  4             |  3.5 | 3 |
|  5             |  4   | 4 |
|  6             |  4.5 | 4 |
|  7             |  5   | 5 |
  
  

  
#### Why are Diminishing Returns Important?
__Diminishing Returns__ are very important to [Leveling Up](#leveling-up) in Rangers and Ruffians
in two ways:
  
  
1. __They provide a buffer against values getting to high.__ Because players can increase whatever
   stat they want when leveling up, a buffer is needed to avoid stat values getting out of hand.
2. __They encourage stat diversification upon level up.__ Diminishing returns incentivize players
   to spend stat points on stats that they wouldn't ordinarily take, promoting well rounded characters.
  
  
  
  

  
### Bonus Stat: Health Die
Every character in Rangers and Ruffians has a __Health Die__ (HD). When a character levels up (detailed in the
section [Leveling Up](#leveling-up)), they roll their health dice, and ```1d4``` and add the numbers rolled
to their maximum health.
  
  

  
### Abilities
Abilities are special things that a character is capable of. Abilities include special
[advantages and disadvantages](#advantage-and-disadvantage), as well as special attacks
that can be made in combat. Some abilities cost one or more [Action Points](#action-points)
to perform.
  
  

  
### Action Points
__Action Points__ (AP) can be spent to perform special abilities and to cast spells in Rangers and Ruffians.
A characters total number of Action Points is equal to ```5 + their Intelligence```. So if a characters
intelligence is ```-3```, they have ```2``` Action Points. If their intelligence is ```2```, they have ```7```
Action Points. Spent Action Points are restored after resting. See the [Resting](#resting)
section for more details.
  
  

  
### Spell Power
A character's __Spell Power__ (SP) determines how likely it is that an enemy will succumb to the affects
of their abilities or spells. A character's Spell Power is defined to be ```12 + their Inner Fire```.
So if a character has ```3``` Inner Fire, their Spell Power is ```15.``` This means that, if our wizard
tried to turn someone into a frog, that entity would have to succeed a saving throw with a target
of ```15``` (our wizard's spell power).
  
  
  
  

  
## Combat
Your party of adventurers is slowly making its way through the corridors of a dungeon when suddenly
a trio of skeletons bursts through a nearby door. You're under attack!
  
  

  
### Initiative
You know that combat has officially begun when your Poohbah asks you to roll Initiative.
__Initiative__ is a special sort of check, performed at the beginning of combat which
determines the order in which players and enemies are to take action on each round.
A __round__ is defined as one complete run through initiative order.
Initiative is modified by perception, and does not change one it is rolled. Your Poohbah
may choose to either keep enemy initiatives a secret, or to display them for all to see.
We actually recommend having a player keep track of initiative for all players and enemies.
That way, there is one less thing for the Poohbah to have to handle.
  
  
As an example, let's say that we have 2 players and 1 enemy goblin. Each player and
the goblin roll initiative. Let's say the first player rolls a ```10``` and has
a perception of ```0```. There initiative value for this combat is ```10```. The second
player rolls a ```14``` and has ```2``` perception, so their initiative is ```16```.
Finally, the goblin rolls a ```15``` but has a perception of ```-3```, so its initiative
is ```12```. So, in this combat, player 2 would go first (as ```16``` is highest),
then the goblin with ```12```, then player 1 with ```10``` initiative.
  
  
  
  

  
### Your Turn

  
#### Actions
On your turn you are able to take one __Action.__ An action is defined as doing something
that takes your full attention for a few seconds. This can include casting a spell, making
an attack, lifting a heavy object, or feeding a potion to an ally.
  
  

  
#### Offhand Actions
On your turn you may also take an offhand action. An offhand action is defined as doing something
that can be done quickly without removing your full attention from combat. This includes leaping
across a ledge, drinking a potion yourself, or opening an unlocked door. It does _not_ include
making an attack.
  
  

  
#### Reaction
Some abilities in Rangers and Ruffians are listed as __Reactions.__ As it's name implies,
a reaction is done in response to something. This can include either an allied or enemy action,
or some other event or change in battle conditions. When a triggering event occurs, you are
able to take a reaction. You may take up to one reaction per turn.
  
  

  
#### Movement
On each turn, you are able to make 15 feet of movement. This movement can be decomposed however
you wish. For example, you might drink a potion as an offhand action, walk 5 feet forward, lift
a cauldron as an action, and then walk ten 10 feet to the right.
  
  

  
#### Exposed Attacks
If you move past an enemy or break melee (move away from) an enemy you leave yourself exposed,
allowing the enemy to get a free attack against you. Similarly, if an enemy moves away from
or runs past you, you may make an attack against them. An entity can make only one such free attack
per turn.
  
  

  
#### Free Actions
It costs neither an action nor an offhand action to perform very simple actions such as shouting
out to your allies, pointing at something, or sheathing or unsheathing a blade. It is up to your
Poohbah's discretion what counts as a Free Action.
  
  

  
#### The Dash Action
You are able to spend your action moving an additional 15 feet.
  
  

  
### The Enemy Turn
Enemies and Monsters in Rangers and Ruffians can do all of the same things that you can,
including taking Actions, using Offhand Actions, Moving, taking Free Actions, and Dashing.
However, in some cases, __Villains,__ the high level monsters and their generals,
can perform extra, more advanced actions. If these
extra actions strike fear in your heart, good! You should not fight a villain lightly!
  
  

  
#### Villain Actions
High level enemies in Rangers and Ruffians are able to take ```Villain Actions```.
These actions allow them to do something (usually take an action) out of turn.
Each turn, a villain gets a number of villain actions specified by the Poohbah (usually
on the order of between 1 and 3). Villain Actions are usually reserved for high ranking
"boss monsters" in a campaign. You would not expect to see a town guard taking villain actions.
  
  

  
#### Sanctuary Actions
If you fight a high level villain on their own terms, things are likely to go in their favor.
If you attack a villain in their Sanctuary, one (but maybe more) special event may happen
at the start of each turn. For example, if you fight a dragon in its den, the thunderous
crashes of your combat may cause stalactites to fall from the ceiling!
  
  

  
#### Conditional Actions
At the start of each of its turns, a Villain may take a special conditional action.
Conditional actions are not generally attacks, but rather events that may turn the tide of
a battle. For example, an ```Orc General``` may order all of it's allies to move at once. A
heavily damaged ```Frost Worm``` may writhe, causing its frozen blood to shower over the battlefield,
damaging everyone and making the floor slick with ice!
  
  
Some example conditions that may trigger a conditional action include:
1. A Villain reaches a Hit Point Threshold, for example, one quarter health.
2. A certain turn is reached. For example, on the first turn, the ```Orc General``` may order all
  of its allies to move. On the second, it may order all of them to attack a single target, etc.
3. An event occurs. For example, a Character slays a ```Dire Wolf's``` pup.
  
  

  
### Attacking
Attacks nearly always hit in Rangers and Ruffians. Therefore, to make a sword attack against an
adjacent enemy, there are two steps.
  
  
1. Roll the attack. If you are in possession of a ```1d6 +1``` sword, this means rolling ```1d6```. Let's say we rolled a 3.
2. Add any relevant modifiers. Our sword was ```+1```, so we will add ```1```. Let's say we have ```2``` strength,
   so we will also add that. So our total is ```3 (our roll) + 1 (our weapon's modifier) + 2 (our strength) = 6```.
3. Deduct the enemy's armor (if they have any). Let's say our enemy had 1 armor. That means that we actually did ```6 - 1 = 5``` damage.
  
  

  
### Critical Hits
A critical hit occurs when a player rolls the highest possible value for an eligible weapon.
When this occurs, the player may roll the dice a second time and add that to the damage total.
So let's say that we have a ```1d8``` spear, ```2``` dexterity, and are attacking an enemy
with ```0``` armor. It might play out like this:
1. We roll an ```8``` on our ```d8``` spear, a critical hit!
2. We roll again. Another ```8```! But there is no such thing as a "double critical", so
  that's the end of our rolling.
3. We total our rolls and add our modifiers ```8 (first roll) + 8 (a lucky critical hit roll) + 0 (our weapons modifier) + 2 (our dexterity)```.
4. Deduct our enemy's armor ```18 - 0 = 18```. We did a massive ```18``` damage!
  
  

  
### Weapons
Weapons have 3 parts in RnR:
1. Their primary die.
2. Their modifier.
3. Their effect.
  
  
A weapons primary die might be ```1d4```, It's modifier might be ```+1```, and it's affect
might be that it returns to a players hand after it is thrown.
  
  
Another weapon's primary die might be ```1d6.``` It's modifier might be 0, and it's affect
might be that it does an extra ```1d6``` damage to the undead.
  
  
A third weapon's primary die might be ```1d12.``` It's modifier might be 0, and it's affect
might be that, if an enemy is stabbed with it, they must make a saving throw against the
wielder's [Spell Power](#spell-power) or be struck blind.
  
  
  
  

  
### Combat Abilities
As mentioned in the [Abilities](#abilities) section, there are many abilities in Rangers
and Ruffians that make the various [Races](#races) and [Classes](#classes) unique.
Many of these abilities are specific to combat. For example, a character might be able
to spend one of their [Action Points](#action-points) to add an additional dice of damage
to an attack. This means that, if they have a ```1d6 + 1``` weapon, they can spend
an action point to add an extra ```1d6``` damage to their attack.
  
  

  
### Hitting Zero Health
If an enemy hits zero health, it is understood to have died. If a player hits zero health,
everything is not over quite yet. When a player hits zero health, the following happens:
  
  
1. Any remaining damage forces the player into negative health. This means that,
   if a player has ```3``` health remaining, and is attacked for ```5``` damage,
   they now have ```-2```  health. At this point, the player is said to be
   __On Death's Door.__
2. When the player's turn arrives, they must make a __Death Coin Flip.__ The player must
   flip a coin, and on failure, their character dies.
3. To save the character before death occurs, the other players must heal them to above zero
   health.
4. If a player is healed enough to bring them back to positive health, they begin playing
   again, and need not make further death coin flips.
  
  

  
#### Reversible Death
Sometimes, death _really_ isn't the end. This depends heavily on the world that your Poohbah
has created, and whether or not certain resources are available. If your party is carrying a
rare item, the ___green lizard in a jar,___ it is possible to resurrect a character who has
died within the past twenty four hours. Similarly, if another player is a high level
__Cleric__ or __Paladin,__ or if the party knows a high level Cleric or Paladin, it is
possible that they may be able to cast the __Resurrect__ spell. Or, in dire cases, a
__Necromancer__ may come to a dead character's aid. Although, some fates may be worse than
dying...
  
  

  
#### Irreversible Death
Sometimes, however, death is here to stay. It is important to remember that the death of a
character doesn't have to be the end of your fun! Losing a character can be hard and
emotional, but there is more fun to be had with a brand new character! Maybe a relative of
your old character is bent on avenging them! Or maybe that halfling barbarian you've been
joking about! Or maybe you could roll up a random character! The point is, while it can be
sad to lose a character, it is definitely not the end, and certainly not something to be
angry about. Instead, treat it as an opportunity to interface with the world in a whole new
way!
  
  
  
  

  
## Health, Rest, and Healing
Character's begin with an amount of health equal to the maximum roll of their
health die + ```1d4.``` Health lost in combat can be regained by resting, using items,
or receiving healing magic.
  
  

  
### Rest
There are three types of rest in Rangers and Ruffians: __Quick Rest__, __Sleep__, and
__Sleep in a bed.__
  
  
| Rest Type      | Required Time | Health Restored | Action Points Restored | Luck Tokens Restored | Frequency       |
| -------------- |---------------| --------------- | ---------------------- | ---------------------| --------------- |
| Quick Rest     | 1 hour        | 20%             | 2                      |  0                   | 3 times per day |
| Sleep          | 8 hours       | 50%             | 5                      | All                  | Once per day    |
| Sleep in a bed | 8 hours       | 75%             | All                    | All                  | Once per day    |
  
  
  
  

  
## Magic
As mentioned in the [Action Points](#action-points) section, a mage may spend action points
to cast spells. This section details the different tiers of spells, as well as how learning
new spells works.
  
  

  
### Spell Tiers
There are 6 spell tiers in Rangers and Ruffians, ranging from ```Tier 0``` to ```Tier 5```.
In general, lower tier spells cost fewer action points to use than higher tier spells.
Access to new spell tiers is treated as an ability, which is gained at certain levels upon
[Leveling Up](#leveling-up).
  
  

  
### Learning new Spells
Mages can learn new spells in two ways. First, a mage passively learns new spells upon
[Leveling Up](#leveling-up). Second, your Poohbah may present you with a spell book as
during your game. A spell book may contain a specific spell hand selected by the Poohbah.
If the spell is of a higher tier than you could normally learn, you may learn it, but
you do not learn spells of that tier upon leveling up. If the spell book does not contain
a specific spell, you may use it to learn any one spell of up to the max spell tier that you
are able to learn.
  
  

  
## Leveling Up
As your character gains experience, they grow stronger. This process is called __Leveling Up.__
There are 16 levels in Rangers and Ruffians, ranging from ```Level 0``` to ```Level 15.``` These
Levels neatly fit into 3, 5 level arcs.
  
  
| Level Range    | Arc           |
| -------------- |---------------|
| 0 - 5          | Burgeoning adventurer. You are small, and the world is a large, scary place. You must struggle to become the hero of a local area. |
| 6 - 10         | Hero. You begin to make real change in the land that you are in.             |
| 11 - 15        | Hero of Legend. You begin fighting ancient evils. The fate of the world may be in your hands. |
  
  

  
### When do I Level Up?
Rangers and Ruffians recommends a system of __Milestone Leveling.__ This means that it is left up to the
Poohbah's discretion when a party should level up. However, as a general guideline, you should expect to level
up every 1-2 sessions for a short adventure, every 3-4 sessions for a moderate length adventure, and
less frequently for a long adventure. Generally, leveling up happens after a major story event occurs.
Such events could include:
1. Victory in a major combat encounter.
2. Success in a stealthy infiltration.
3. Snatching an artifact from a villain's lair.
4. Saving an kidnapped noble.
  
  

  
### What Happens when I Level Up?
  
  

  
#### Increasing Your Maximum Health
Every time that you level up, you get to roll your health die + ```1d4``` and add add the
result to your maximum health. For example, if your maximum health is ```26``` and your
health die is ```1d8``` the following might occur:
1. You roll a ```3``` on your health die.
2. You roll a ```2``` on your 1d4.
3. Your new maximum health is ```26 (your old max health) + 3 (your health die roll) + 2 (your d4 roll) = 31```.
  
  

  
#### Odd Levels: New Abilities
When you level up, you get better at being your class. That is to say, you are a better _Rouge_ or _Knight_
or _Gunslinger_ or _Bard_ than you were before. When you reach an odd level, you receive new abilities, allowing
you to perform all new actions or granting you new advantages.
  
  

  
#### Even Levels: New Stats
When you reach an even level, you get ```2``` __Stat Points__ to spend. You can spend these to increase your stats.
Review the [Effective Stats](#effective-stats) section for details on how this works.
Alternatively instead of increasing your stats, you are able to instead take a new [Skill](#skills). See the
[Skills](#skills) section for more details.
  
  
  
  

  
#### New Spells
If you are a magic user, you are able to learn 1 new spell of _every_ spell tier that you know each time you level up.
This means that if you know tier 0, 1, and 2 spells, you get to learn 3 spells: 1 spell each of tier 0, 1, and 2.
  
  
  
  

  
## Building a Character
Now that you understand (or at least glanced at) the rules of Rangers and Ruffians, you can now get started building
your character. In terms of gameplay, a character is made up of two major components: a __Race__ and a __Class.__
A Race represents the racial background that your character comes from. Your choice of race grants you base
abilities and stats, and can greatly affect the way that you interact with the world. If you choose to play a
tiny _Sprout_, you might ride atop the shoulders of the another player's _Orc_ character.
  
  
__Class,__ meanwhile, affects your role within your adventuring party. A _Rouge_ might spend their time
scouting, skulking, and sneaking. A _Highborn_ might use their high Charisma to barter for goods or
get information out of an important non-player character. A _Barbarian_ will spend their time in combat
shielding and soaking up damage for their more-squishy counterparts.
When you level up in Rangers and Ruffians, it is your class that grants you new abilities.
  
  

  
### Personality and Background
It is important to remember that a character can be much, _much_ more than just a sack of stats an abilities.
As a player, it is up to you to breathe life into your character, and make them into a living, breathing
part of the world that your Poohbah is weaving. To this end, consider the following:
1. Where did my character come from? Do they have family? Friends?
2. What does my character want? Where are they going? What motivates them?
3. Why would my character be interested in going on an adventure?
4. What are a few of my characters virtues? What about vices?
5. How did my character end up being the class that they are?
6. How does my character interact with others? How do they speak? What are they're mannerisms?
  
  
As you come up with a backstory for your character remember the following:
Try to keep things vague but evocative, so that your Poohbah can easily weave them into their world.
Consider the following quick backstory: 
> "Elizabeth is from the town of Lindhearth. Some years ago she 
was visited by an aged wizard, who warned her of a great trial approaching in her future. Ever since that
day, she has been preparing for an evil that may never come." 
  
  
While quite basic, let's examine what the above backstory does well.
1. While it introduces a town, ```Lindhearth```, the town is not rigidly defined, and is simple for a Poohbah to add to their campaign setting.
  As a bonus, wouldn't it be cool if the Poohbah included Lindhearth in their campaign! Maybe some of your friends or family could make an appearance,
  or maybe even the mysterious wizard!
2. While you have been warned of a "great trial," the nature of that trial is left entirely up to the Poohbah. That means that it can easily 
  be tied into the adventure. This is awesome, as it can easily fit into any story that the Poohbah might want to tell. Just like that, you
  are personally invested in the adventure!
3. It provides a basis for you to start further fleshing out Elizabeth's character. How has she been preparing? Has she been learning magic?
  Practicing her skill with the sword? Praying to her deity? How has this training affected her personality? Is her adventuring career part
  of these preparations?
  
  
Let's make a second backstory.
> "Richard spent his entire childhood in the Lost Library. Only, it wasn't called the 'Lost' Library, but the Holy Library.
   He had made friends with the old Clerics and Paladins that kept their noses in books all day, and had even gotten them to
   teach him some of their divine magics. His favorite of them was an old greybeard named Scanderbeg. All of this changed
   when a Gold Dragon descended on the Library, tearing through the roof and killing many of those within. With the help of
   Scanderbeg, Richard had fled, helpless, with no home and nowhere to go, displaced and a refugee."
  
  
Again, this backstory introduces a location, the Lost Library, which can easily be integrated into a Poohbah's campaign. This
backstory also introduces a villain, an evil ```Gold Dragon.``` Perhaps this fits perfectly into the Poohbah's plans, but maybe it doesn't.
Perhaps the Poohbah is planning on running an ```undead``` heavy campaign, in which a ```Lich``` is the main villain. Together, the player and
the Poohbah can tailor Richards backstory, so that instead, it reads:
  
  
> "All of this changed the army of the dead arrived, swarming throughout the City of Linth and leaving a path of carnage in their wake. 
   With the help of the holy magics he had learned from Scanderbeg, Richard fled, but not before laying eyes on ___him.___ The face of death itself. Hozius the
   Defiler. As Richard watched, Hozius raised his hands, and all of those who had been dead rose up to join his army."
  
  
Now the backstory fits the Poohbah's campaign, and it's maybe even cooler than it was before! This is the benefit of talking things through with
your Poohbah before the game begins, and why it is a great idea to come up with vague and evocative character concepts to run past them.
  
  

  
### Health Dice Pieces
Races and Classes each have ```Health Dice Pieces```. When building a character,
you add these pieces together to get your total health dice. For example,
if you race has ```2``` health dice pieces, and your class has ```4```,
your health dice would be ```6```.

  
## How do I Compute my Character's Stats?
There are three ways that you can compute your characters starting stats in Rangers and Ruffians.
All three of them are very easy to do, but if this is your first time playing, method zero is
recommended.
  
  

  
### Method 1 (Easiest) Use Pre-generated Stats:
Every Race and Class in Rangers and Ruffians comes with recommended stats.
Therefore, the simplest method of creating a character is to just use those!
  
  
Let us have an imaginary race with the following stats:
  
  
| STR | DEX | INT | INF | CHA | PER | LUK | HD  |  
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|  
|  0  | -1  | -1  |  1  |  1  |  0  |  1  |  4  |
  
  
And an imaginary Class with the following stats:
  
  
| STR | DEX | INT | INF | CHA | PER | LUK |  HD |  
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|  
|  1  |  2  | -1  | -2  | -3  |  0  |  1  |  4  |
  
  
Then in this method, we would just sum them up!
  
  
| STR | DEX | INT | INF | CHA | PER | LUK |  HD |  
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|  
|  1  |  1  | -2  | -1  | -2  |  0  |  2  |  8  |
  
  
  
  

  
### Method 2 (Easy) Standard Array:
The second method allows us for a little bit more customization
by letting us _switch around our class stats_.
In rangers and Ruffians, every class has a standard array of stat values,
that is to say, each class has one stat with each of the following values,
not including its ```Health Dice``` and ```Luck```: ```2```, ```1```, ```0```, 
```-1```, ```-2```, and ```-3```.
  
  
Let's recall the stats from our imaginary class above:
  
  
| STR | DEX | INT | INF | CHA | PER | LUK |  HD |  
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|  
|  1  |  2  | -1  | -2  | -3  |  0  |  1  |  4  |
  
  
Under this method, we can switch them around a bit.
Let's say that we didn't like that we have ```-3``` charisma, and are fine with having low perception.
Under this method, we can switch those values!
  
  
| STR | DEX | INT | INF | CHA | PER | LUK |  HD |  
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|  
|  1  |  2  | -1  | -2  | 0   |  -3  |  1 | 4   |
  
  
Let's also switch our Strength and Dexterity.
  
  
| STR | DEX | INT | INF | CHA | PER | LUK |  HD |  
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|  
|  2  |  1  | -1  | -2  | 0   |  -3  |  1 | 4   |
  
  
Now that we're happy with our class stats, we can add in our race stats, which were:
  
  
| STR | DEX | INT | INF | CHA | PER | LUK | HD  |  
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|  
|  0  | -1  | -1  |  1  |  1  |  0  |  1  |  4  |
  
  
So our final stats are:
  
  
| STR | DEX | INT | INF | CHA | PER | LUK | HD  |  
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|  
|  2  | 0   | -2  |  -1 |  1  |  -3 |  2  |  8  |
  
  

  
### Method 3 (High Risk, High Reward) Roll:
The final way that we can generate our stats is by rolling them randomly!
This method of stat creation can result in very strong or very weak characters, which leads
to a very fun sense of risk and reward. Remember that, if you roll poorly it's not the end of the world.
It can be hilarious to have a mage who is very bad at charisma, or a surprisingly intelligent Barbarian.
  
  
__Remember:__ Stats should always be rolled at the table with people watching. That way, there can be no doubt
when you roll 4 consecutive 18s!
  
  
To role your own stats, perform the following steps:
1. For each of your stats except for ```Health Dice``` and ```Luck,``` roll ```4d6``` and drop the lowest ```d6```. 
2. Take that number, and apply it to the chart below to get your stat.
3. After you are finished add your race stat modifiers to the result to get your final stats.
4. __Variant Option:__ Rather than rolling for each stat, just roll six times, and then apply the results to whatever stat you want. 
   If you are using this method of rolling, make sure to get Poohbah approval first. 
  
  
| Your Roll  | Value  | What is added to a Roll  | 
|------------|-------|-----------------|
|      3     |   -5  |        -4       |
|      4     |   -4  |        -3       |
|      5     |   -3  |        -3       |
|      6     |   -2  |        -2       |
|      7     |   -2  |        -2       |
|      8     |   -1  |        -1       |
|      9     |   -1  |        -1       |
|     10     |    0  |         0       |
|     11     |    0  |         0       |
|     12     |    1  |         1       |
|     13     |    1  |         1       |
|     14     |    2  |         2       |
|     15     |    2  |         2       |
|     16     |    3  |         3       |
|     17     |    4  |         3       |
|     18     |    5  |         4       |
  
  
Let's go through an example.
1. For each of your stats you roll 4d6 and drop the lowest dice. For the first roll, you roll a ```5```, a ```5```, a ```1``` and a ```3```, so you drop the 1. 
2. Your total for the first stat is ```5 + 5 + 3 = 13```, which the table tells us is a ```+1``` You record that for strength.
3. After rolling a few more times, you end up with a ```7```, a ```17```, a ```9```, a ```9```, and a ```16```. 
4. You look up those numbers on the table above, and find that you have the following class stat block:
  
  
  
  
| STR | DEX | INT | INF | CHA | PER | LUK | HD  |  
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|  
|  1  | -2  |  4  |  -1 |  -1 |  3  |  1  |  4  |
  
  
Then, we can add our race stats:
  
  
| STR | DEX | INT | INF | CHA | PER | LUK | HD  |  
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|  
|  0  | -1  | -1  |  1  |  1  |  0  |  1  |  4  |
  
  
To get a final stat block of:
  
  
| STR | DEX | INT | INF | CHA | PER | LUK | HD  |  
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|  
|  1  | -3  |  3  |  0  |  0  |  3  |  2  |  8  |
  
  
Let's compare that to our stat block from method one:
  
  
  
  
| STR | DEX | INT | INF | CHA | PER | LUK |  HD |  
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|  
|  1  |  1  | -2  | -1  | -2  |  0  |  2  |  8  |
  
  
It looks like we have  better ```Dexterity``` and ```Perception.```
However, our ```Intelligence``` and ```Charisma``` are worse.
Depending on what our class was built for, this could be good or bad.
The fun is in the rolling!

  
## Races
Your racial background in Rangers and Ruffians can greatly impact the way that you interact with the world.
Will you play a short but hearty _Hardfoot Halfling?_ The incredibly  tiny _Sprout?_ A metalic _Automaton?_ Perhaps you
brutish _Orc_ or a lithe, erudite _High Elf._ Or, you could stick to the basics and play a _Human._ Races provide
you with minor stat increases and a handful of starting abilities. Any race should easily be able to be paired with any
class, though some pairings will start out slightly stronger than others. That's fine, though! It will all balance out in the end!
  
### Automaton
<div></div>
<div></div>

<img src='https://github.com/emaicus/Rangers-and-Ruffians/blob/rangers_v2.1/site/static/images/race/female/automaton.jpg?raw=true' style='width:350px' />

>Well, for a time, I was working on a project to produce artificial life forms, automata, if you will. The project had limited success, and was on the brink of being defunded. In a desperate attempt to keep things going, we turned to magic as a solution. So it was, that he soul gem was discovered. To this day, I wonder what it is exactly that we created. Was it life, or was it some crude approximation? I know not. Nor, I think, does the automaton.
>
>—Simon, Gnome Tinker

  
  
The biproduct of tinkers and mages, the automaton is considered by many to be an artificial being. For this reason, many are persecuted, and treated as mere objects. And perhaps they are. To question your place is to be an automaton, and the quest for meaning is a path that all such beings must walk.
  
  
|STR|DEX|INT|INF|CHR|PER|LUK|HD|  
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|  
|2|-1|0|0|-1|0|0|6|  
  
  
__Automaton Abilities:__ 
* __Rules:__   
  * __Power Core:__ The source of your power is housed within you. If you are destroyed in combat, you can be rebuilt so long as the power core survives.  
  * __Repair:__ You cannot heal using potions or rest. Rather, you must perform repairs. Self repair counts as rest. Repair with help counts as sleep. Repair with a tinker or blacksmith's help counts as sleep in a bed. Blacksmith's must have access to a forge, and tinkers to their tools. Tinker and blacksmith repairs take a minimum of 6 hours.  
  * __Upgrades:__ A tinker can craft upgrades for you.  
* __General Abilities:__   
  * __Overdrive:__ Spend 5 health per turn (or 1 health per minute) to increase your strength and dexterity by 3.  
  * __True Sleeplessness:__ You cannot grow tired, nor can you sleep.  
  * __Armored Exterior:__ You naturally have an armor of 1.  
* __Combat Abilities:__   
  * __Self Repair:__ During combat, you can self repair in place of a full turn.  
  * __Gyroscopic Center of Mass:__ It is difficult to knock you over. Add 5 to any check that involves knocking you prone.  
  * __Piston Punch:__ You may perform a 1d6 strength based punch on an enemy of your choice. On a critical hit, the enemy is knocked prone.  
  
  
  
___

  
### Catterwol
<div></div>
<div></div>

<img src='https://github.com/emaicus/Rangers-and-Ruffians/blob/rangers_v2.1/site/static/images/race/female/catterwol.jpg?raw=true' style='width:350px' />

>Ah, yes, well... It was then that we stumbled upon an encampment of cat-folk. They seemed a nice enough sort, so we bought some of their wares, beads and knives and potions, that sort of thing. After that, we supped with them. Well, before we knew it, we were all unconcious; they drugged the food, no doubt. They made off with everything; my staff, my hat, and even my sandles!
>
>—Archibold, the Wizard

__Silent and Dexterous__  
Stalking on padded feet, the Catterwol Rouge makes her way carefully across the rooves of the city of Linth. Her target is simple, information and nothing more. Unfortunately, the information that she needs is buried inside of a chest locked in the room of Lord Edmire himself. Far below, her party waits with baited breath, as she hops from roof to roof, and then slips into Edmire's quarters. *Roll a Stealth Check!*  
  
__Perceptive__  
Needlelike teeth show in a sharp smile as the Catterwol Bard steps forward. "Hold on, surely we can work something out?" Isak, the kingpin of the city's thieves' guild, scoffs. "Not this time." From the corner of his eye, the Bard just notices two shadowy figures slip into view. His smile grows, and with a flash, he whips around and slings a throwing knife at one of the figures. *Roll for initiative!*  
  
__Tribal__  
Cattterwol tend to live in loose, nomadic tribes. As a general rule, they are deeply distrustful of outsiders, and are known to act in their own self-interest more often than not.  
  
__Building a Cattwol Character__  
When building your Catterwol, consider how they came to belong to your party. Remember that, while Catterwol are tribal, they are deeply protective of those close to them. Is the party their family now? What members of the party is your character close to?  
  
  
  
Catterwol are among the most lithe and dexterous of the races, and are adept at passign unseen and unheard. With padded feet and strong claws for climing, more than one Catterwol has turned to the life of a sneak-theif. Catterwol hail from dense, thicketed jungles and dry, dusty deserts. They make average mages, but prefer slim, dexterity based weapons.
  
  
|STR|DEX|INT|INF|CHR|PER|LUK|HD|  
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|  
|-1|1|0|-1|0|1|1|4|  
  
  
__Catterwol Abilities:__ 
* __General Abilities:__   
  * __Dark Vision:__ You can see even in perfect darkness.  
  * __Land on your feet:__ You can fall 40 feet before taking fall damage.  
* __Advantages:__   
  * __Predator:__ When tracking, you have advantage on perception checks.  
  * __Loose Skin:__ You have advantage when breaking grapples.  
* __Combat Abilities:__   
  * __They're Retractable:__ You have retractable, razor sharp claws capable of doing 1d6 damage.  
  * __Fast Paws:__ _(Cost 1)_ Gain an additional offhand action.  
  
  
  
___

  
### Daemonspawn
<div></div>
<div></div>

<img src='https://github.com/emaicus/Rangers-and-Ruffians/blob/rangers_v2.1/site/static/images/race/female/daemonspawn.jpg?raw=true' style='width:350px' />

>Never trust a daemonspawn, that's what I've alwasy been told. They're as liable to use their dark and terrible magicks as to give you a passing smile. I've never met one though; I've been careful to avoid them.
>
>—Miss Maribel Merkland, Busybody and Baker of Exquisite Pies.

  
  
The daemonspawn were born of an unholy union between elves and the demons of old. When the demons were thrown down and destroyed, the daemonspawn remained. Now, the daemonspawn are left in a world that at best doesn't understand them, and at worst fears and persecutes them. As such, the wise daemonspawn is always vigilant and trusts no one.
  
  
|STR|DEX|INT|INF|CHR|PER|LUK|HD|  
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|  
|0|-1|1|1|0|-1|1|4|  
  
  
__Daemonspawn Abilities:__ 
* __General Abilities:__   
  * __Fix Your Eyes on Me:__ Conversation spell. If the person you are talking with fails an inner fire saving throw against your spell power, the world goes black for them except for you. Make charisma and intimidation checks with advantage for the remainder of the conversation.  
  * __True Sight:__ You are able to see invisible entities.  
  * __Sleepless:__ Your can rest without sleeping for one day, allowing you to keep watch long into the night.  
  * __Incombustible:__ You take half damage from heat and fire.  
* __Combat Abilities:__   
  * __Sacrificial Rite:__ At the cost of 10 hp, make a second action during combat.  
  
  
  
___

  
### Deep Elf
<div></div>
<div></div>

<img src='https://github.com/emaicus/Rangers-and-Ruffians/blob/rangers_v2.1/site/static/images/race/female/deep_elf.jpg?raw=true' style='width:350px' />

>Elves can be slippery folk. It seems to me that rarely say what they mean, and they seldom mean what they say. They're strong mages, though, and too clever for their own good. If you're dealing with elves, try to appeal to their pride, but be careful about it. They can see through simple flattery.
>
>—Ser Gillthunder, Human Knight, Leader of the Hetzer Company (Mercenaries)

  
  
Elves are the most magical of the races. Forest-dwellers with long lives, many elves spend their days practicing magic and honing their skills. Elves are naturally beautiful, and this beauty benefits them when they deal with the other races. Elves make strong mages and good dexterity based fighters.
  
  
|STR|DEX|INT|INF|CHR|PER|LUK|HD|  
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|  
|1|0|0|0|-2|1|1|4|  
  
  
__Deep Elf Abilities:__ 
* __General Abilities:__   
  * __Sleepless:__ Your can rest without sleeping for one day, allowing you to keep watch long into the night.  
  * __Dark Vision:__ You can see even in perfect darkness.  
* __Advantages:__   
  * __Winged Feet:__ You have advantage on acrobatics checks.  
* __Combat Abilities:__   
  * __Counter Attack:__ _(Cost 1)_ Once per round of combat, you may strike back when an enemy attacks you. Role a d20 and add your dexterity. If greater than 15, you land the blow.  
  
  
  
___

  
### Dwarf
<div></div>
<div></div>

<img src='https://github.com/emaicus/Rangers-and-Ruffians/blob/rangers_v2.1/site/static/images/race/female/dwarf.jpg?raw=true' style='width:350px' />

>Dwarves are difficult to hunt. They're thick, and sturdy; your shot has to be well placed if you want to bring one down.
>
>—Orkinshield, Orc Gunslinger

  
  
A stocky, brooding people, many dwarves are natural craftsman and artisans. Dwarves prefer low places, and many of their strongholds can be found deep within mountain ranges. Dwarves have a shrewd eye for business, and have been known to drink their adversaries under the table.
  
  
|STR|DEX|INT|INF|CHR|PER|LUK|HD|  
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|  
|1|-2|0|1|0|0|1|4|  
  
  
__Dwarf Abilities:__ 
* __General Abilities:__   
  * __Incombustible:__ You take half damage from heat and fire.  
* __Advantages:__   
  * __Stocky:__ You have advantage against any check that could cause you to go prone.  
  * __Very Dangerous Over Short Distances:__ If you begin your turn next to an enemy, take advantage on your attack roll.  
  * __Boozehound:__ You have a very high tolerance for alcohol. Do not take disadvantage when drunk.  
  * __Thick Headed:__ You have advantage on any checks involving an enemy breaking into your mind or dominating you.  
  * __Forgeborn:__ When dealing with minerals or works made of stone, gain advantage on any checks made to assess or manipulate them.  
  
  
  
___

  
### Fleetfoot Halfling
<div></div>
<div></div>

<img src='https://github.com/emaicus/Rangers-and-Ruffians/blob/rangers_v2.1/site/static/images/race/female/halfling.jpg?raw=true' style='width:350px' />

>Halflings are decent enough, and fun to be around. They have potential as since they can see without being seen, but I'm not sure if they're clever enough.
>
>—Vasha, Catterwol Thief

  
  
Small folk, the Halflings would rather be drinking tea and eating toast in their holes than adventuring. They are naturally tricksters, are hardy for their size, and are adept at sqeezing into tight spots. On average, the Halflings stand at three-and-a-half feet, and have warm, chestnut colored eyes and hair.
  
  
|STR|DEX|INT|INF|CHR|PER|LUK|HD|  
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|  
|-2|1|0|0|0|1|2|2|  
  
  
__Fleetfoot Halfling Abilities:__ 
* __General Abilities:__   
  * __Carry a Tune:__ Offhand. You know a song which, when sung, grants all members of your party +1 to a stat of your choice. Concentration.  
  * __Lightweight:__ Any cup of alcohol affects you like two.  
* __Starting Items:__   
  * __Sling:__ Your character begins their journey with a 1d6 sling.  
* __Advantages:__   
  * __Padfoot:__ You have advantage on stealth checks.  
  * __Nimble Fingers:__ You have advantage on dexterity and stealth checks made while stealing.  
* __Combat Abilities:__   
  * __Nimble:__ Targeted ranged attacks take disadvantage against you.  
  
  
  
___

  
### Gnome
<div></div>
<div></div>

<img src='https://github.com/emaicus/Rangers-and-Ruffians/blob/rangers_v2.1/site/static/images/race/female/gnome.jpg?raw=true' style='width:350px' />

>Gnomes are tiny. They make things, sometimes. I can crush them.
>
>—Throgar, Barbarian and Sheriff

__Tinker__  
Moonlight paints the room as the Gnomish Tinker bites her lip. Her project is coming along quite well, better than expected, actually. Not far away, the rest of her party snores as they sleep. She should be sleeping as well, tomorrow is the big day. But then, that's why she needs a spring loaded spear-thrower in the first place. For a moment, she considers lying down, but then pulls her goggles over her eyes. Hopefully, her party was sleeping heavily. With a grin, she lights her acetaline torch, and sparks begin to fly. *Roll an intelligence check!*  
  
__None__  
__Eccentric__  
Most consider gnomes to be eccentric at best, and obtuse at worse.  
  
  
  
Tinkerers by nature, Gnomes are known to craft miraculous inventions to help them deal with difficult situations. Gnomes typically stand about three feet in height, and can be recognized by their signature goggles. Gnomes are well rounded and are capable of succeeding at anything they put their minds to.
  
  
|STR|DEX|INT|INF|CHR|PER|LUK|HD|  
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|  
|0|0|1|1|-1|-1|2|2|  
  
  
__Gnome Abilities:__ 
* __Rules:__   
  * __Build:__ Once you have a recipe for an item, you can build it. You can attempt to build one item per rest, or two per sleep.  
* __General Abilities:__   
  * __Tinker:__ Every night, you can attempt to to create a device. Once you create one, you get its recipe. Must have ingredients. You begin with recipes for smokebombs, firebombs, and saddles. (Tinkering requires an intelligence check)  
  * __See and Remember:__ Once you see something, you will probably remember it.  
  * __Gather:__ You passively collect ingredients for your tinkering.  
* __Starting Items:__   
  * __Grapple Gun:__ You carry a retractable grappling gun. The gun carries 40 feet of rope.  
* __Advantages:__   
  * __Resist Magic:__ You may make any rolls against an enemy's spell power with advantage.  
  
  
  
___

  
### Goblin
<div></div>
<div></div>

<img src='https://github.com/emaicus/Rangers-and-Ruffians/blob/rangers_v2.1/site/static/images/race/female/goblin.jpg?raw=true' style='width:350px' />

>It is a rarity to find a kindly goblin, but when I have, I have found them to be most agreeable companions. Mind you, their penchant for raw flesh can be most off-putting... As can their little yellow eyes. Still, though, if ever you are in a pinch, a loyal goblin-ling can be a fierce, nay, a vicious ally.
>
>—Tamberdoodle, Bard Extraordinare

  
  
Small and wicked, most goblins are tricksters and thieves. Known for eating their kills and living in the dark, goblins prefer to fight with ranged or short weapons. Morally good goblins are rare, and have often been outcast from their clan and family. This can be very painful, as goblins are communal creatures by nature.
  
  
|STR|DEX|INT|INF|CHR|PER|LUK|HD|  
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|  
|0|1|0|-1|-1|1|2|2|  
  
  
__Goblin Abilities:__ 
* __General Abilities:__   
  * __Still Warm:__ You can eat raw meat without penalty.  
  * __Dark Vision:__ You can see even in perfect darkness.  
  * __Seek Gold:__ You are able to smell gold. You can perform gold detection checks.  
* __Advantages:__   
  * __Mantel:__ You have advantage on dexterity checks when climbing.  
* __Combat Abilities:__   
  * __Cheap Blow:__ On a critical hit, knock an enemy prone.  
  
  
  
___

  
### Hardfoot Halfling
<div></div>
<div></div>

<img src='https://github.com/emaicus/Rangers-and-Ruffians/blob/rangers_v2.1/site/static/images/race/female/halfling.jpg?raw=true' style='width:350px' />

>Halflings are decent enough, and fun to be around. They have potential as since they can see without being seen, but I'm not sure if they're clever enough.
>
>—Vasha, Catterwol Thief

  
  
Small folk, the Halflings would rather be drinking tea and eating toast in their holes than adventuring. They are naturally tricksters, are hardy for their size, and are adept at sqeezing into tight spots. On average, the Halflings stand at three-and-a-half feet, and have warm, chestnut colored eyes and hair.
  
  
|STR|DEX|INT|INF|CHR|PER|LUK|HD|  
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|  
|0|-1|-1|1|1|0|1|4|  
  
  
__Hardfoot Halfling Abilities:__ 
* __General Abilities:__   
  * __Warm Butter:__ Your are naturally talented chef. Any food that you cook heals 1d6 health.  
  * __Soft Bed:__ You recover 2d8 extra health from sleeping in a real bed.  
  * __Carry a Tune:__ Offhand. You know a song which, when sung, grants all members of your party +1 to a stat of your choice. Concentration.  
* __Starting Items:__   
  * __Sling:__ Your character begins their journey with a 1d6 sling.  
  * __Courageous Blow:__ _(Cost 1)_ Add your Inner Fire to an attack.  
* __Advantages:__   
  * __Thick Headed:__ You have advantage on any checks involving an enemy breaking into your mind or dominating you.  
  
  
  
___

  
### High Elf
<div></div>
<div></div>

<img src='https://github.com/emaicus/Rangers-and-Ruffians/blob/rangers_v2.1/site/static/images/race/female/high_elf.jpg?raw=true' style='width:350px' />

>High Elves can be slippery folk. It seems to me that rarely say what they mean, and they seldom mean what they say. They're strong mages, though, and too clever for their own good. If you're dealing with elves, try to appeal to their pride, but be careful about it. They can see through simple flattery.
>
>—Ser Gillthunder, Human Knight, Leader of the Hetzer Company (Mercenaries)

  
  
High elves are among the most magical of the races. Reclusive by nature, high elves often confine themselves to gleaming costal cities. When a high elf does venture out into the world at large, it is often in a diplomatic capacity. High elves are as charming as they are naturally beautiful, and commonly feel as though it is their duty to maintain balance in the world. High elves make good mages.
  
  
|STR|DEX|INT|INF|CHR|PER|LUK|HD|  
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|  
|-1|0|1|-1|1|0|2|2|  
  
  
__High Elf Abilities:__ 
* __General Abilities:__   
  * __Sleepless:__ Your can rest without sleeping for one day, allowing you to keep watch long into the night.  
  * __Low-Light Vision:__ You can see in low light.  
  * __Inherent Magic:__ You are able to cast tier zero spells naturally, and begin with 2 extra tier zero spells from any spellbook.  
  * __Detect Magic:__ You are able to perform magic detection checks.  
* __Advantages:__   
  * __Wink Wink, Nudge Nudge:__ Due to your beauty, you have advantage on charisma checks when dealing with races that find you attractive.  
  
  
  
___

  
### Hissling
<div></div>
<div></div>

<img src='https://github.com/emaicus/Rangers-and-Ruffians/blob/rangers_v2.1/site/static/images/race/female/hissling.jpg?raw=true' style='width:350px' />

>So here's one for you: A while back, we were called to a town by the name of Broshtik to help some yokels. Apparently, things had been going missing. Little things, mostly; utensils and fire pokers and the like. Normally, we wouldn't have taken such a small job, but work had been scarce and beggars can't be choosers. So, anyway, we get to Broshtik, and we spend a good three days poking around, but can't find anything. It gets to the point that we are ready to call it quits and get out of there. Then, one of Harley's rings goes missing overnight. We look around, and find a trail, barely anything, leading through one of the windows. So, out we go, and over to one of the sewer grates in town. We pried it open, and dropped down in. And what do you think we saw? An entire civilization of tiny little lizardlings, that's what. Generations of them, all living in houses built of mud and candlesticks. All at once, the little buggers start taking off like they'd see Melikar, skittering and running in every direction. Then, an elder approaches us. Or, at least, I think it was an elder; it only came to my knees, and wore a robe made out of a piece of towel. In broken speech, it asked us to leave them be in return for a great gift: two necklaces and a pair of children's shoes. Some times, I wonder if they're still down there.
>
>—Gillthunder, Human Knight

  
  
Next to Sprouts, Hisslings are the smallest of races. Lizardlike entities, Hisslings try their very best to be ferocious. While naturally clever, Hisslings do not cherish knowledge, but rather focus upon helping their clan flourish. The life of a Hissling is often a bleak one: while hisslings can live upwards of 40 years, they rarely do. Instead, most die early due to their fragile nature and disregard for their own safety. Because of the commonality of death in Hissling tribes, most Hisslings put the long-term wellbeing of the collective above that of themselves or even their closest friends and family. Hisslings reach full maturity after only two years, and can reproduce just a few years after. 
  
  
|STR|DEX|INT|INF|CHR|PER|LUK|HD|  
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|  
|-1|1|0|-1|0|1|2|2|  
  
  
__Hissling Abilities:__ 
* __Choices:__   
  * __I'm a Red One!:__ At the start of your journey, choose your color. This choice affects elemental resistances.  
* __General Abilities:__   
  * __Small Fry:__ Your size is considered tiny. You can fit into small spaces, be easily carried, and be easily thrown.  
  * __All Tuckered Out:__ You must sleep once every six hours, or suffer exhaustion.  
  * __Tossed Around:__ You take half damage from blunt attacks, but are tossed 5 feet backward for every size larger than you your enemy is.  
* __Combat Abilities:__   
  * __Chomp Chomp:__ You can make a 1d6 bite attack. Once you have bitten an enemy, your jaw sets, and you won't let go until even after you are dead. The enemy can attempt contested dexterity checks to try to free themselves of you.  
  * __Riding High:__ Allies take no disadvantage while you ride them. You gain advantage on attacks while riding a party member.  
  * __Dig Dig Dig:__ You are able to burrow through earth at a rate of 1 foot per minute.  
  
  
  
___

  
### Human
<div></div>
<div></div>

<img src='https://github.com/emaicus/Rangers-and-Ruffians/blob/rangers_v2.1/site/static/images/race/female/human.jpg?raw=true' style='width:350px' />

>Humans are good, but a little bit tough. That's why you have to eat them raw.
>
>—Orkensheild, Orc Archer

  
  
Humans are the most average of the races. The race of men can become good at most things, but it takes a concerted effort for them to become great at anything. That doesn't stop them from trying, though, and it is this natural willpower that makes them a force to be reckoned with.
  
  
|STR|DEX|INT|INF|CHR|PER|LUK|HD|  
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|  
|1|-1|0|1|0|-1|1|4|  
  
  
__Human Abilities:__ 
* __Choices:__   
  * __Skilled:__ Begin your journey with one extra skill.  
* __General Abilities:__   
  * __Adaptable:__ Once affected by an effect or spell, gain advantage on saves against for the remainder of the day.  
* __Combat Abilities:__   
  * __Last Stand:__ When your health is below 25%, you can take an extra action on your turn.  
  * __Strength of Men:__ _(Cost 1)_ You have basic healing abilities. You may heal a party member for 1d6 + inner fire health.  
  * __Rally:__ _(Cost 1)_ You may use an aura which gives all of your allies a 1d8 inspiration dice.  
  
  
  
___

  
### Kragraven
<div></div>
<div></div>

<img src='https://github.com/emaicus/Rangers-and-Ruffians/blob/rangers_v2.1/site/static/images/race/female/kragraven.jpg?raw=true' style='width:350px' />

>I don't trust them, those bird-men that live to the west. Don't trust them one bit.
>
>—Old Man Mcuffit, Racist Old Man

  
  
Kragraven stand at about the height of a human, though they are known to hunch over, slightly. Kragraven are reclusive, taking to lofty homes amidst ancient forests. Myths say that Kragraven were first created by the god Ragnhall, and that they are his servants.
  
  
|STR|DEX|INT|INF|CHR|PER|LUK|HD|  
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|  
|0|0|1|-1|-1|1|1|4|  
  
  
__Kragraven Abilities:__ 
* __Choices:__   
  * __Peck:__ _(Cost 1)_ As an offhand action, peck an enemy, dealing 1d6 damage. On a critical hit, blind them until they succeed a SP save.  
* __General Abilities:__   
  * __High Jump:__ Flap your vestigial wings to jump twice your height directly upward.  
  * __Coast:__ Use your wings to coast from great heights.  
  * __Carrion:__ You can eat raw and rotten meat without penalty.  
  * __Mimic:__ You can mimic any voice you've heard.  
  
  
  
___

  
### Lizkin
<div></div>
<div></div>

<img src='https://github.com/emaicus/Rangers-and-Ruffians/blob/rangers_v2.1/site/static/images/race/female/lizkin.jpg?raw=true' style='width:350px' />

>Skin changes like mist. Poisoned teeth lurking within. A Lizkin fighter.
>
>—Mister Li, Gnomeish Monk

  
  
  
  
  
  
|STR|DEX|INT|INF|CHR|PER|LUK|HD|  
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|  
|1|-1|0|0|-1|1|1|4|  
  
  
__Lizkin Abilities:__ 
* __General Abilities:__   
  * __Poison Resist:__ You are resistant to most poisons. You have advantage on any poison related checks, and take half damage at worst.  
  * __Shed Tail:__ Once per week, you can shed your tail to escape a grapple.  
  * __Taste Air:__ Gain advantage on tracking perception checks by tasting the air. Works in all environments.  
* __Advantages:__   
  * __Color Choice:__ _(Cost 1)_ You may choose what color your scales are. Scales may hold only three colors at a time unless Camouflage is being used. This may be used to gain advantage on a stealth check.  
  * __Smokevision:__ Your double eyelids allows you to see well when underwater or in smoke.  
* __Combat Abilities:__   
  * __Poison Bite:__ _(Cost 1)_ You may make a bite attack for 1d6 damage. If your enemy fails a D10 inner fire saving throw, they are poisoned and take an additional 1d6 damage at the start of each turn until they pass a D14 inner fire saving throw.  
  
  
  
___

  
### Orc
<div></div>
<div></div>

<img src='https://github.com/emaicus/Rangers-and-Ruffians/blob/rangers_v2.1/site/static/images/race/female/orc.jpg?raw=true' style='width:350px' />

>The full-orc is a dangerous specimen. Known to hunt and eat the other races, it is difficult to domesticate them. As the saying goes, you can take the orc out of the wilderness, but you can't stop him from trying to eat you.
>
>—unattributed folk wisdom

  
  
A brutish and warlike race, orcs stab first and ask questions later. Orcs are often used to living in harsh environments, and living off the land.
  
  
|STR|DEX|INT|INF|CHR|PER|LUK|HD|  
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|  
|1|0|0|1|-2|0|1|4|  
  
  
__Orc Abilities:__ 
* __General Abilities:__   
  * __Still Warm:__ You can eat raw meat without penalty.  
* __Advantages:__   
  * __Predator:__ When tracking, you have advantage on perception checks.  
* __Combat Abilities:__   
  * __Bellow:__ _(Cost 1)_ On your turn, spend one action point to unleash a mighty bellow. All who hear must make an Spell Power save of be frightened.  
  * __Thunderous Blow:__ _(Cost 2)_ Roll an extra dice for your attack.  
  * __Vengeful Death:__ When you are reduced to zero hit points, you may make one last retaliatory action. If you take the retaliatory action, you must make your death coin flips with disadvantage.  
  
  
  
___

  
### Sprout
<div></div>
<div></div>

<img src='https://github.com/emaicus/Rangers-and-Ruffians/blob/rangers_v2.1/site/static/images/race/female/sprout.jpg?raw=true' style='width:350px' />

>And as I walked through the forest, I heard a sound, like the laughter of children. Fearing some trick, I summoned forth my hammer of light. To my shock, the sound came from a race of tree folk, smaller even than the smallest halfling. They were quite dexterous, and spoke the language of my people. I spent some time among their woodland village before continuing on my way.
>
>—Harley, Elf Paladin

  
  
Sprouts are among the smallest of the races, standing at about 2 feet. As a result, they are very weak, but are fast, and good at sneaking. The wise sprout should avoid the front line of combat, and instead stay in relative hiding, jumping out to attack at opportune moments. Sprouts are not necessarily wise, however, and it is not strange to see a sprout knight attempting to make a name for themself.
  
  
|STR|DEX|INT|INF|CHR|PER|LUK|HD|  
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|  
|-2|1|0|0|0|1|2|2|  
  
  
__Sprout Abilities:__ 
* __General Abilities:__   
  * __Photosynthesis:__ Every turn or once per hour, regain 1d4 health.  
  * __Small Fry:__ Your size is considered tiny. You can fit into small spaces, be easily carried, and be easily thrown.  
  * __Soft Landing:__ Reduce any falling damage by 20 feet.  
  * __Commune with Nature:__ You are naturally able to speak with plants and animals.  
  * __Lightweight:__ Any cup of alcohol affects you like two.  
  * __Blade of Grass:__ Summon a 1d6 blade of woven plant fiber on command.  
  * __Harden:__ As an offhand action, harden or unharden yourself. While hardened, gain 2 defense and loose 2 dexterity.  
* __Advantages:__   
  * __Scurry:__ You have advantage on dexterity based athletics checks.  
* __Combat Abilities:__   
  * __Dodge:__ Any time you are attacked, roll a d20 and add your dexterity. If you get above a 15, the attack misses.  
  
  
  
___

  
### Waterborn
<div></div>
<div></div>

<img src='https://github.com/emaicus/Rangers-and-Ruffians/blob/rangers_v2.1/site/static/images/race/female/waterborn.jpg?raw=true' style='width:350px' />

>Most Waterborn I've seen have been dried up and dying. Their need for water is their undoing, out here in the desert. Once they've been wetted down a bit, they perk right up. It's then that you have to watch yourself; Waterborn are liable to charm you when you're not looking.
>
>—Leaf, Gnome Rogue from the Wild Desert

  
  
Alien among the other races, Waterborn hail from the depths of oceans, lakes, and rivers. Waterborn come in a pleathora of colors, and have ruddy, splotched skin which dries up if it isn't exposed to water regularly. Waterborn are powerful magic users, and are naturally adept at charming the other races.
  
  
|STR|DEX|INT|INF|CHR|PER|LUK|HD|  
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|  
|-1|0|1|-1|1|0|2|2|  
  
  
__Waterborn Abilities:__ 
* __General Abilities:__   
  * __Water Breathing:__ You only need to breathe once every three days. If you do not go underwater to breath, you will suffocate.  
  * __Flows Like Water:__ You can walk on water, and swim as fast as a horse can run.  
  * __Water Healing:__ When you sleep in water, it is as if you are in a bed.  
  * __Lightweight:__ Any cup of alcohol affects you like two.  
* __Combat Abilities:__   
  * __Become Mist:__ _(Cost 1)_ Spend one action point to become mist to have an attack pass right through you as a reaction.  
  * __Charm:__ _(Cost 1)_ As an action, you may cast a charm spell on an entity. If the entity fails an inner fire saving throw against your spell power, they cannot attack you until you attack them or they succeed.  
  
  
  
___

  
### Wood Elf
<div></div>
<div></div>

<img src='https://github.com/emaicus/Rangers-and-Ruffians/blob/rangers_v2.1/site/static/images/race/female/wood_elf.jpg?raw=true' style='width:350px' />

>Elves can be slippery folk. It seems to me that rarely say what they mean, and they seldom mean what they say. They're strong mages, though, and too clever for their own good. If you're dealing with elves, try to appeal to their pride, but be careful about it. They can see through simple flattery.
>
>—Ser Gillthunder, Human Knight, Leader of the Hetzer Company (Mercenaries)

  
  
Elves are the most magical of the races. Forest-dwellers with long lives, many elves spend their days practicing magic and honing their skills. Elves are naturally beautiful, and this beauty benefits them when they deal with the other races. Elves make strong mages and good dexterity based fighters.
  
  
|STR|DEX|INT|INF|CHR|PER|LUK|HD|  
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|  
|-1|1|0|-1|0|1|1|4|  
  
  
__Wood Elf Abilities:__ 
* __General Abilities:__   
  * __Sleepless:__ Your can rest without sleeping for one day, allowing you to keep watch long into the night.  
  * __Low-Light Vision:__ You can see in low light.  
* __Advantages:__   
  * __Winged Feet:__ You have advantage on acrobatics checks.  
  * __Tracker:__ You are an excellent tracker, and have advantage when looking for trails and sign of passage.  
* __Combat Abilities:__   
  * __Counter Attack:__ _(Cost 1)_ Once per round of combat, you may strike back when an enemy attacks you. Role a d20 and add your dexterity. If greater than 15, you land the blow.  
  
  
  
___

  
## Classes
Choosing your class in Rangers and Ruffians is perhaps the most important choice that you will make.
While your race determines what you look like, your class determines what your role will be in your
adventuring party. Will you play a high charisma _Bard_, or a heavily armored _Knight?_ Perhaps a
_Gunslinger_ or an _Archer?_ Is magic more your style? Then perhaps you will play as a priestly _Cleric_,
an intelligent _Wizard_ or a naturalistic _Druid._ Perhaps you want an animal companion ever at your side.
In that case, the wild _Beastmaster_ may be right up your alley. While there are many choices at your fingertips,
we have worked hard to make sure that all of them are very fun, so no matter what you pick, you're certain
to have a good time!
  
### Archer
<div></div>
<div></div>

<img src='https://github.com/emaicus/Rangers-and-Ruffians/blob/rangers_v2.1/site/static/images/class/female/archer.jpg?raw=true' style='width:350px' />

  
  
Some of the best marksmen in the world, archers are naturals with ranged weapons. They are often attached to their bow, and carry it with them everywhere. Archers come from all walks of life; some compete in tournaments, others are hunters and farmer's sons. Still others have served in the military. Archers should stay off of the front line, instead picking off foes from a distance.
  
  
|STR|DEX|INT|INF|CHR|PER|LUK|HD|  
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|  
|-3|2|-1|-2|0|1|1|4|  
  
  
__Archer Abilities:__ 
* __General Abilities:__   
  * __Fletcher:__ You know how to craft your own arrows, and always seem to have some on hand.  
* __Starting Items:__   
  * __Longbow:__ You begin your journey with a d6 longbow.  
  * __Boot Knife:__ You carry a hidden d6 knife in your boot.  
* __Combat Abilities:__   
  * __Focus:__ _(Cost 1)_ Focus before a shot to gain advantage on it. Removes distance penalties.  
  * __Huntsman:__ You have advantage when attacking beasts.  
  
  
__Level 0 Archer__

* __General Abilities:__   
  * __Fletcher:__ You know how to craft your own arrows, and always seem to have some on hand.  
  
  
* __Combat Abilities:__   
  * __Focus:__ _(Cost 1)_ Focus before a shot to gain advantage on it. Removes distance penalties.  
  * __Huntsman:__ You have advantage when attacking beasts.  
  
  
__Level 1 Archer__

* __Advantages:__   
  * __Mantel:__ You have advantage on dexterity checks when climbing.  
  
  
* __Combat Abilities:__   
  * __Arrow Stab:__ You can stab an enemy with an arrow for 1d6 damage.  
  * __Crippling Shot:__ You can aim at an opponents knees for 1d4 damage, making them go prone on a critical hit.  
  
  
__Level 2 Archer__

* __Choices:__   
  * __Stat Increase:__ You gain two stat points to add to a stat or stats of your choosing.  
  
  
__Level 3 Archer__

* __General Abilities:__   
  * __Fire and Ice Arrows:__ _(Cost 1)_ You have mastered the art of crafting fire and ice arrows, and can craft at most 2 per day. Fire arrows do an additional 1d6 fire damage and deal 1d6 burn damage to enemies that fail a saving throw against your spell power. Ice arrows deal an additional 1d8 ice damage, and cause an enemy to move backward 1d4 spaces in the initiative order of they fail a saving throw against your spell power.  
  
  
* __Combat Abilities:__   
  * __Dual Shot:__ _(Cost 1)_ Fire two arrows at the same target in a single attack.  
  
  
__Level 4 Archer__

* __Choices:__   
  * __Stat Increase:__ You gain two stat points to add to a stat or stats of your choosing.  
  
  
* __General Abilities:__   
  * __Rope Arrows:__ _(Cost 1)_ You have mastered the art of crafting rope arrows using minor magic. As soon as a rope arrow hits its target, a rope instantly appears connecting the target to your hand. This can be used to climb, or to grapple opponents. To grapple an opponent, you must make a contested strength check.  
  
  
__Level 5 Archer__

* __General Abilities:__   
  * __Net Arrows:__ _(Cost 1)_ You can now craft net arrows. When a net arrow hits its target, they must make an inner fire saving throw against your spell power. On failure, they are instantly wrapped in a net, and are considered restrained. Each turn, they may make a strength saving throw against your spell power to attempt to break out of the net.  
  * __Smoke Arrow:__ _(Cost 1)_ You can now craft smoke arrows. When a smoke arrow hits the ground, it creates a smokescreen with a 30 foot radius.  
  
  
__Level 6 Archer__

* __Choices:__   
  * __Stat Increase:__ You gain two stat points to add to a stat or stats of your choosing.  
  
  
* __General Abilities:__   
  * __Shadow and Light Arrows:__ _(Cost 1)_ You have mastered the art of crafting shadow and light arrows. Shadow arrows do an additional 1d6 dark damage and cause enemies who fail an inner fire saving throw against your spell power to go blind for 1d4 turns. Shadow arrows may also be used to fill a 10 foot radius with pitch darkness. Light arrows deal an additional 1d6 light damage, and deal another 1d12 damage to the undead.  
  
  
__Level 7 Archer__

* __Actions:__   
  * __Offhand Attack:__ You may use an offhand action to make an attack.  
  
  
* __General Abilities:__   
  * __Reflexes:__ Once per turn, attempt to catch a projectile. Roll a d20, and reduce the projectile's damage by that amount. If reduced to zero, you catch the projectile.  
  
  
* __Advantages:__   
  * __Steady:__ Do not take disadvantage when being jostled about.  
  
  
__Level 8 Archer__

* __Choices:__   
  * __Stat Increase:__ You gain two stat points to add to a stat or stats of your choosing.  
  
  
* __General Abilities:__   
  * __Explosive Arrows:__ _(Cost 2)_ After much experimentation, you have finally mastered the art of crafting explosive arrows. Explosive arrows do 2d10 damage to all enemies in a twenty foot radius.  
  
  
__Level 9 Archer__

* __General Abilities:__   
  * __Vampiric Arrow:__ _(Cost 2)_ You can now craft vampiric arrows. Vampiric arrows do an additional 2d6 damage to an entity. You regain half of the damage done by a vampiric arrow to your health.  
  
  
__Level 10 Archer__

* __Choices:__   
  * __Stat Increase:__ You gain two stat points to add to a stat or stats of your choosing.  
  
  
* __General Abilities:__   
  * __True Mastery:__ Every ranged weapon functions as at least a d12 weapon in your hands.  
  
  
__Level 11 Archer__

* __General Abilities:__   
  * __Blink Arrows:__ _(Cost 1)_ After learning more about magic, you have learned how to create blink arrows. Blink arrows instantly teleport you to the position that they hit.  
  
  
* __Advantages:__   
  * __Uncanny Perception:__ You have uncanny perception, which allows you to sense your way in total darkness, and gives you advantage on all perception checks.  
  
  
__Level 12 Archer__

* __Choices:__   
  * __Stat Increase:__ You gain two stat points to add to a stat or stats of your choosing.  
  
  
* __General Abilities:__   
  * __Shock Arrow:__ _(Cost 2)_ You can now craft shock arrows. When a shock arrow hits an enemy, it deals 2d8 shock damage to them and any other entities within 30 feet. If an affected entity is wearing metal armor or is made of or standing in water, they take an extra 2d8 damage. All affected entities must make an inner fire saving throw against your spell power. On failure, they are knocked prone.  
  
  
__Level 13 Archer__

* __General Abilities:__   
  * __Expert Fletcher:__ All arrows now cost 1 action point less.  
  * __Anti-Gravity Arrows:__ _(Cost 1)_ You can now craft Anti-Gravity arrows. When an Anti-Gravity arrow hits its target, they must make an inner fire saving throw against your spell power. On failure, gravity is reversed for them, and they fly towards the sky. Anti-gravity arrows last for one minute, 1d4 turns, or until the entity succeeds its inner fire saving throw.  
  
  
* __Combat Abilities:__   
  * __Volley:__ Once per rest, attack every enemy you can see in a single action.  
  
  
__Level 14 Archer__

* __Choices:__   
  * __Stat Increase:__ You gain two stat points to add to a stat or stats of your choosing.  
  
  
__Level 15 Archer__

* __General Abilities:__   
  * __Firestorm Arrow:__ _(Cost 3)_ You can now craft firestorm arrows. A firestorm arrow does nothing for one turn or one minute after it strikes something. Then, it explodes into a massive pillar of flame with a fifteen foot diameter. All entities caught in the pillar of flame take 4d10 damage instantly. The pillar of flame stays for 3 turns.  
  
  
  
___

  
### Barbarian
<div></div>
<div></div>

<img src='https://github.com/emaicus/Rangers-and-Ruffians/blob/rangers_v2.1/site/static/images/class/barbarian.jpg?raw=true' style='width:350px' />

  
  
Barbarians are hearty, and can dole out a lot of damage, making them great tanks for a party of adventurers. They are marked by their berserk ability, which allows them to fly into a battle frenzy, gaining extra attacks and health. Barbarians cannot use magic, and are much better up close than at a distance. They are known for their rugged ways, and usually prefer wide open spaces to cities.
  
  
|STR|DEX|INT|INF|CHR|PER|LUK|HD|  
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|  
|2|1|-3|-1|-2|0|0|6|  
  
  
__Barbarian Abilities:__ 
* __General Abilities:__   
  * __Colossal:__ You stand 2 feet taller than the average individual of your race, and are treated as one size larger.  
* __Advantages:__   
  * __Boozehound:__ You have a very high tolerance for alcohol. Do not take disadvantage when drunk.  
  * __Ruffians:__ Gain advantage on charisma checks when speaking with seedy individuals, townspeople, or bandits.  
  * __Intimidate:__ You have advantage on intimidation checks.  
* __Combat Abilities:__   
  * __Berserk:__ Once per rest, you can go into a rage, giving you +1 strength and dexterity, but decreasing your intelligence and perception by 3. A rage lasts for 1 hour. Coming out of a rage prematurely makes you fatigued, and gives you disadvantage on all rolls until you next sleep.  
  * __Taunt:__ _(Cost 1)_ You can taunt your opponents. Foes within 30 feet of you must make an inner fire saving throw or be forced to attack you instead of others. Repeat save each turn.  
  
  
__Level 0 Barbarian__

* __Advantages:__   
  * __Intimidate:__ You have advantage on intimidation checks.  
  
  
* __Combat Abilities:__   
  * __Berserk:__ Once per rest, you can go into a rage, giving you +1 strength and dexterity, but decreasing your intelligence and perception by 3. A rage lasts for 1 hour. Coming out of a rage prematurely makes you fatigued, and gives you disadvantage on all rolls until you next sleep.  
  * __Taunt:__ _(Cost 1)_ You can taunt your opponents. Foes within 30 feet of you must make an inner fire saving throw or be forced to attack you instead of others. Repeat save each turn.  
  
  
__Level 1 Barbarian__

* __General Abilities:__   
  * __Throw Anything:__ You can throw anything up to one size larger than yourself.  
  
  
* __Combat Abilities:__   
  * __Throw Caution to the Wind:__ On your turn, optionally add an extra damage dice to all of your attacks, but all enemy attacks get advantage on you for a turn.  
  
  
__Level 2 Barbarian__

* __Choices:__   
  * __Stat Increase:__ You gain two stat points to add to a stat or stats of your choosing.  
  
  
__Level 3 Barbarian__

* __Combat Abilities:__   
  * __Crushing Blow:__ On a critical hit, you give all enemies who see, including the attacked enemy, disadvantage on the first action of their next turn.  
  * __Line Them Up:__ If you slay an enemy, gain another attack action.  
  
  
__Level 4 Barbarian__

* __Choices:__   
  * __Stat Increase:__ You gain two stat points to add to a stat or stats of your choosing.  
  
  
__Level 5 Barbarian__

* __Combat Abilities:__   
  * __Blind Rage:__ You make all spell saving throws with advantage while going berserk.  
  * __Savage Critical:__ On a critical hit, do an additional dice of damage.  
  
  
__Level 6 Barbarian__

* __Choices:__   
  * __Stat Increase:__ You gain two stat points to add to a stat or stats of your choosing.  
  
  
__Level 7 Barbarian__

* __Combat Abilities:__   
  * __Always Angry:__ You may now go berserk once per battle.  
  * __Furious Blows:__ When going berserk, you can make two attacks in a single action.  
  
  
__Level 8 Barbarian__

* __Choices:__   
  * __Stat Increase:__ You gain two stat points to add to a stat or stats of your choosing.  
  
  
__Level 9 Barbarian__

* __Combat Abilities:__   
  * __Berserker:__ You take half damage from physical attacks while going berserk.  
  
  
__Level 10 Barbarian__

* __Choices:__   
  * __Stat Increase:__ You gain two stat points to add to a stat or stats of your choosing.  
  
  
__Level 11 Barbarian__

* __Combat Abilities:__   
  * __Warmaster:__ Going berserk now gives you an additional +1 strength and inner fire.  
  
  
__Level 12 Barbarian__

* __Choices:__   
  * __Stat Increase:__ You gain two stat points to add to a stat or stats of your choosing.  
  
  
__Level 13 Barbarian__

* __Combat Abilities:__   
  * __Controlled Rage:__ Ending berserk early no longer gives you any negative effects and no longer has a time limit.  
  * __Glory:__ When your health falls below 25%, double all damage you deal.  
  
  
__Level 14 Barbarian__

* __Choices:__   
  * __Stat Increase:__ You gain two stat points to add to a stat or stats of your choosing.  
  
  
__Level 15 Barbarian__

* __Combat Abilities:__   
  * __Spirit of Rage:__ Once per day, double one of your turns.  
  
  
  
___

  
### Bard
<div></div>
<div></div>

<img src='https://github.com/emaicus/Rangers-and-Ruffians/blob/rangers_v2.1/site/static/images/class/bard.jpg?raw=true' style='width:350px' />

  
  
Showmen by nature, Bards are known for their skills at performing and distracting others from the sorrows of life. Bards are usually at least a little bit gaudy and outgoing. They are quick in a fight, and often fight with dexterity based weapons such a shortswords or knives. Bards are powerful spellcasters, and are excellent at providing support to their party and at making enemies weaker. As you prepare your bard, consider how they chose this way of life. How did they learn magic? How do they perform? Do they play music? Dance? Tell stories? How did they learn to fight? Who did they learn to fight from? How old are they? How many places have they been? Where do they perform? Why do they perform there? How will being a bard change the way you interact with your party?
  
  
|STR|DEX|INT|INF|CHR|PER|LUK|HD|  
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|  
|-3|0|1|-1|2|-2|1|4|  
  
  
__Bard Abilities:__ 
* __Rules:__   
  * __Learning Spells:__ New spells or techniques are obtained by leveling up or by finding spellbooks or scrolls in the world. A spellbook may contain a specific spell, or a maximum spell tier. Spellbooks with a maximum spell tier contain one spell of your choice from the spellbooks that you can learn from with a tier up to the spellbook's maximum spell tier.  
  * __Learn Spells:__ Each time you level up, learn one new spell of each spell tier that you have access to. Spells must be learned from one of your spellbooks.  
* __Choices:__   
  * __Spell Choice:__ At the start of your journey, you know 2 extra tier zero spells.  
  * __My Father's Oboe:__ You are proficient and start with two instruments of your choice.  
* __General Abilities:__   
  * __Tier Zero Spells:__ You have achieved a basic knowledge of the arcane, and may now learn tier zero spells from any of your spellbooks.  
* __Starting Items:__   
  * __The Bard's Songbook:__ You can learn spells from the Bard's Songbook.  
* __Advantages:__   
  * __Boozehound:__ You have a very high tolerance for alcohol. Do not take disadvantage when drunk.  
  * __Regular Patron:__ You may add 1d6 to charisma checks made in a tavern.  
  * __Slight of Hand:__ You have advantage when performing slight of hand actions.  
  
  
__Level 0 Bard__

* __Rules:__   
  * __Learning Spells:__ New spells or techniques are obtained by leveling up or by finding spellbooks or scrolls in the world. A spellbook may contain a specific spell, or a maximum spell tier. Spellbooks with a maximum spell tier contain one spell of your choice from the spellbooks that you can learn from with a tier up to the spellbook's maximum spell tier.  
  * __Learn Spells:__ Each time you level up, learn one new spell of each spell tier that you have access to. Spells must be learned from one of your spellbooks.  
  
  
* __Choices:__   
  * __My Father's Oboe:__ You are proficient and start with two instruments of your choice.  
  
  
* __General Abilities:__   
  * __Tier Zero Spells:__ You have achieved a basic knowledge of the arcane, and may now learn tier zero spells from any of your spellbooks.  
  
  
* __Starting Items:__   
  * __The Bard's Songbook:__ You can learn spells from the Bard's Songbook.  
  
  
* __Advantages:__   
  * __Regular Patron:__ You may add 1d6 to charisma checks made in a tavern.  
  * __Slight of Hand:__ You have advantage when performing slight of hand actions.  
  
  
__Level 1 Bard__

* __General Abilities:__   
  * __Tier One Spells:__ Your powers are growing. You may now learn tier one spells from any of your spellbooks.  
  * __Minor Restful Melody:__ _(Cost 1)_ When your party is resting, you may perform a song for them which grants them an extra 1d8 healing.  
  
  
* __Combat Abilities:__   
  * __One up the Sleeve:__ _(Cost 1)_ You may make a throwing knife attack as an offhand action.  
  
  
__Level 2 Bard__

* __Choices:__   
  * __Stat Increase:__ You gain two stat points to add to a stat or stats of your choosing.  
  
  
__Level 3 Bard__

* __General Abilities:__   
  * __Spell Coin:__ You have one spell coin, which may store a spell of up to tier one. Any person who rubs the coin may cast the spell as an offhand action. Each day, you may re-summon the coin to yourself, and may put a spell into it free of cost.  
  
  
* __Advantages:__   
  * __Nimble Fingers:__ You have advantage on dexterity and stealth checks made while stealing.  
  
  
__Level 4 Bard__

* __Choices:__   
  * __Stat Increase:__ You gain two stat points to add to a stat or stats of your choosing.  
  
  
* __General Abilities:__   
  * __Tier Two Spells:__ You have graduated from novice to proficient! You may now learn tier two spells from any of your spellbooks.  
  
  
__Level 5 Bard__

* __General Abilities:__   
  * __Additional Spell Coin:__ You have an additional spell coin.  
  
  
__Level 6 Bard__

* __Choices:__   
  * __Stat Increase:__ You gain two stat points to add to a stat or stats of your choosing.  
  
  
__Level 7 Bard__

* __Actions:__   
  * __Offhand Attack:__ You may use an offhand action to make an attack.  
  
  
* __General Abilities:__   
  * __Tier Three Spells:__ Magical energy flows through you. You may now learn tier three spells from any of your spellbooks.  
  * __Greater Restful Melody:__ _(Cost 1)_ When your party is resting, you may perform a song for them which grants them an extra 2d8 healing.  
  
  
* __Combat Abilities:__   
  * __Imbue Weapon:__ _(Cost 1)_ As an offhand action, add 1d6 elemental damage to your weapon at the cost of 1 action point. Lasts 1 battle or 1 hour.  
  
  
__Level 8 Bard__

* __Choices:__   
  * __Stat Increase:__ You gain two stat points to add to a stat or stats of your choosing.  
  
  
__Level 9 Bard__

* __General Abilities:__   
  * __Greater Spell Coin:__ You have learned the art of storing second tier spells in your spell coins.  
  
  
* __Combat Abilities:__   
  * __Greater Imbue Weapon:__ _(Cost 1)_ As an offhand action, add 1d8 elemental damage to your weapon at the cost of 1 action points. Lasts 1d4 turns.  
  
  
__Level 10 Bard__

* __Choices:__   
  * __Stat Increase:__ You gain two stat points to add to a stat or stats of your choosing.  
  
  
* __General Abilities:__   
  * __Tier Four Spells:__ You are a master of your spellcraft. You can now learn tier four spells from any of your spellbooks.  
  
  
__Level 11 Bard__

* __General Abilities:__   
  * __Major Restful Melody:__ _(Cost 1)_ When your party is resting, you may perform a song for them which grants them an extra 3d8 healing.  
  
  
__Level 12 Bard__

* __Choices:__   
  * __Stat Increase:__ You gain two stat points to add to a stat or stats of your choosing.  
  
  
__Level 13 Bard__

* __General Abilities:__   
  * __Additional Spell Coin:__ You have an additional spell coin.  
  * __Tier Five Spells:__ You have achieved the highest form of sorcery, and are a mage to be reckoned with. You can now learn tier five spells from any of your spellbooks.  
  
  
__Level 14 Bard__

* __Choices:__   
  * __Stat Increase:__ You gain two stat points to add to a stat or stats of your choosing.  
  
  
__Level 15 Bard__

* __General Abilities:__   
  * __Major Spell Coin:__ You have learned the art of storing third tier spells in your spell coins.  
  
  
  
___

  
### Beastmaster
<div></div>
<div></div>

<img src='https://github.com/emaicus/Rangers-and-Ruffians/blob/rangers_v2.1/site/static/images/class/female/beastmaster.jpg?raw=true' style='width:350px' />

  
  
For the Beastmaster 'Animal Person' is an understatement. Beastmaster's begin their adventure with a loyal animal companion, which they can select from the Book of Known Beasts. This can include a wolf, a bear, and eagle, or even a dragon! Most Beastmasters have forgone civilization, choosing instead to roam the wilds, capturing and befriending animals. They are quick, dexterity based fighters, and are good at tackling and hobbling enemies and leading their party through the wilds.
  
  
|STR|DEX|INT|INF|CHR|PER|LUK|HD|  
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|  
|2|1|-1|-2|-3|0|1|4|  
  
  
__Beastmaster Abilities:__ 
* __Rules:__   
  * __Pup:__ Your companion animal is small size. See the book of known beasts for details.  
* __Choices:__   
  * __Animal Companion:__ At the beginning of your journey, you may choose a an animal companion. See the book of known beasts for stats.  
  * __Favorite Terrain:__ At the beginning of your journey, pick a favorite terrain. Whenever you are on it, you have advantage on any check related to the terrain, and may take advantage on an action every third turn during combat.  
* __General Abilities:__   
  * __Animal Magnetism:__ Most animals inherently understand you on some level. You can attempt to persuade the actions of animals.  
  
  
__Level 0 Beastmaster__

* __Rules:__   
  * __Pup:__ Your companion animal is small size. See the book of known beasts for details.  
  
  
* __Choices:__   
  * __Animal Companion:__ At the beginning of your journey, you may choose a an animal companion. See the book of known beasts for stats.  
  * __Favorite Terrain:__ At the beginning of your journey, pick a favorite terrain. Whenever you are on it, you have advantage on any check related to the terrain, and may take advantage on an action every third turn during combat.  
  
  
* __General Abilities:__   
  * __Animal Magnetism:__ Most animals inherently understand you on some level. You can attempt to persuade the actions of animals.  
  
  
__Level 1 Beastmaster__

* __General Abilities:__   
  * __Hobble:__ You are capable of quickly tying very strong knots without a check. If you have an entity grappled, you may hobble them with an action. Hobbled entities may attempt a strength saving throw against your spell power each turn to attempt to escape. Hobbled entities make all movements with disadvantage, and cannot attack with a handheld weapon.  
  
  
* __Advantages:__   
  * __Tackle:__ You can tackle an enemy up to one size larger than you to the ground. Attempt either a dexterity or strength contested throw against the enemy, on which you have advantage. If they fail, you grapple them.  
  
  
__Level 2 Beastmaster__

* __Choices:__   
  * __Stat Increase:__ You gain two stat points to add to a stat or stats of your choosing.  
  
  
__Level 3 Beastmaster__

* __Combat Abilities:__   
  * __Leaping Strike:__ _(Cost 1)_ Leap 5 feet forward to attack an enemy, dealing 1d6 additional damage. At level five, damage increases to 2d6. At level ten, it increases to 3d6.  
  * __Huntsman:__ You have advantage when attacking beasts.  
  
  
__Level 4 Beastmaster__

* __Choices:__   
  * __Stat Increase:__ You gain two stat points to add to a stat or stats of your choosing.  
  
  
__Level 5 Beastmaster__

* __General Abilities:__   
  * __Dog Pile:__ Any sleep taken while with your animal companion counts as sleep in a bed.  
  
  
* __Advantages:__   
  * __Tracker:__ You are an excellent tracker, and have advantage when looking for trails and sign of passage.  
  
  
* __Combat Abilities:__   
  * __Coordinated Attack:__ If you and your animal companion are both attacking the same entity, you both gain advantage on your attacks.  
  
  
__Level 6 Beastmaster__

* __Choices:__   
  * __Stat Increase:__ You gain two stat points to add to a stat or stats of your choosing.  
  
  
__Level 7 Beastmaster__

* __Actions:__   
  * __Offhand Attack:__ You may use an offhand action to make an attack.  
  
  
* __Combat Abilities:__   
  * __Closest Friend:__ Gain advantage in all things if your animal companion is on deaths door or has died in the current battle. Similarly, if you are at death's door or have died, your animal companion takes advantage in all things.  
  
  
__Level 8 Beastmaster__

* __Choices:__   
  * __Stat Increase:__ You gain two stat points to add to a stat or stats of your choosing.  
  
  
__Level 9 Beastmaster__

* __General Abilities:__   
  * __Wild Sight:__ You are able to see through the eyes of your animal companion.  
  
  
__Level 10 Beastmaster__

* __Choices:__   
  * __Stat Increase:__ You gain two stat points to add to a stat or stats of your choosing.  
  
  
__Level 11 Beastmaster__

* __General Abilities:__   
  * __Inseparable:__ _(Cost 1)_ Instantly teleport from your current position to a spot within five feet of your animal companion. The same can be done by your animal companion. Counts as an offhand action.  
  
  
__Level 12 Beastmaster__

* __Choices:__   
  * __Stat Increase:__ You gain two stat points to add to a stat or stats of your choosing.  
  
  
__Level 13 Beastmaster__

* __General Abilities:__   
  * __Dominate:__ _(Cost 1)_ You may attempt to dominate an enemy. If they fail an inner fire saving throw, they must obey you. They can attempt a saving throw every turn thereafter.  
  
  
__Level 14 Beastmaster__

* __Choices:__   
  * __Stat Increase:__ You gain two stat points to add to a stat or stats of your choosing.  
  
  
__Level 15 Beastmaster__

* __General Abilities:__   
  * __Beast Form:__ _(Cost 2)_ Transform yourself into a dire creature of your choosing. For one hour, you may transform back and forth as an action. While in your beast form, you have the physical stats of the chosen creature. If your health falls to zero, you are instantly transformed back into your normal form, with the health that you had prior to using beast shape.  
  
  
  
___

  
### Cleric
<div></div>
<div></div>

<img src='https://github.com/emaicus/Rangers-and-Ruffians/blob/rangers_v2.1/site/static/images/class/cleric.jpg?raw=true' style='width:350px' />

  
  
After pledging their allegiance to their deity, Clerics have made it their duty to follow their will. Clerics are weak, and do not fight with physical magic. However, they are powerful spellcasters who are adept at healing, and who can make a huge difference in combat. Clerics try to embody the ideals of their deity, paying them homage and working to enact their will in the world. As you design your cleric, ask yourself how they chose this path. When and how did their deity reach out to them? How did they make their pledge? Under what circumstances? How often do they pray to their deity? How do they react to people who don't believe? What do they believe in? What is their moral code, and how does that interact with that of their deity? How will being a cleric affect the way that you interact with your party?
  
  
|STR|DEX|INT|INF|CHR|PER|LUK|HD|  
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|  
|-3|-2|2|0|1|-1|2|2|  
  
  
__Cleric Abilities:__ 
* __Rules:__   
  * __Learning Spells:__ New spells or techniques are obtained by leveling up or by finding spellbooks or scrolls in the world. A spellbook may contain a specific spell, or a maximum spell tier. Spellbooks with a maximum spell tier contain one spell of your choice from the spellbooks that you can learn from with a tier up to the spellbook's maximum spell tier.  
  * __Learn Spells:__ Each time you level up, learn one new spell of each spell tier that you have access to. Spells must be learned from one of your spellbooks.  
* __Spellbooks:__   
  * __The Book of Healing:__ You are able to learn spells from the Book of Healing.  
* __Choices:__   
  * __Spell Choice:__ At the start of your journey, you know 2 extra tier zero spells.  
  * __Pledge:__ At the start of your journey, you may select a deity to pledge yourself to.  
* __General Abilities:__   
  * __Tier Zero Spells:__ You have achieved a basic knowledge of the arcane, and may now learn tier zero spells from any of your spellbooks.  
  
  
__Level 0 Cleric__

* __Rules:__   
  * __Learning Spells:__ New spells or techniques are obtained by leveling up or by finding spellbooks or scrolls in the world. A spellbook may contain a specific spell, or a maximum spell tier. Spellbooks with a maximum spell tier contain one spell of your choice from the spellbooks that you can learn from with a tier up to the spellbook's maximum spell tier.  
  * __Learn Spells:__ Each time you level up, learn one new spell of each spell tier that you have access to. Spells must be learned from one of your spellbooks.  
  
  
* __Spellbooks:__   
  * __The Book of Healing:__ You are able to learn spells from the Book of Healing.  
  
  
* __Choices:__   
  * __Pledge:__ At the start of your journey, you may select a deity to pledge yourself to.  
  
  
* __General Abilities:__   
  * __Tier Zero Spells:__ You have achieved a basic knowledge of the arcane, and may now learn tier zero spells from any of your spellbooks.  
  
  
__Level 1 Cleric__

* __General Abilities:__   
  * __Tier One Spells:__ Your powers are growing. You may now learn tier one spells from any of your spellbooks.  
  
  
* __Combat Abilities:__   
  * __Purge Decay:__ Gain 1d6 damage when fighting the undead.  
  
  
__Level 2 Cleric__

* __Choices:__   
  * __Stat Increase:__ You gain two stat points to add to a stat or stats of your choosing.  
  
  
__Level 3 Cleric__

* __Actions:__   
  * __Minor Offhand Spell:__ You may cast a tier zero spell as an offhand action.  
  
  
* __Combat Abilities:__   
  * __Last Ditch Prayer:__ _(Cost 1)_ Say a fervent prayer to your deity, and add 1d8 to your roll.  
  
  
__Level 4 Cleric__

* __Choices:__   
  * __Stat Increase:__ You gain two stat points to add to a stat or stats of your choosing.  
  
  
* __General Abilities:__   
  * __Tier Two Spells:__ You have graduated from novice to proficient! You may now learn tier two spells from any of your spellbooks.  
  
  
__Level 5 Cleric__

* __Combat Abilities:__   
  * __Feint:__ _(Cost 1)_ You may roll a d20 against an enemy attack. Reduce the attack by the amount rolled.  
  
  
__Level 6 Cleric__

* __Actions:__   
  * __Greater Offhand Spell:__ You may cast a tier one spell as an offhand action.  
  
  
* __Choices:__   
  * __Stat Increase:__ You gain two stat points to add to a stat or stats of your choosing.  
  
  
__Level 7 Cleric__

* __Actions:__   
  * __Offhand Attack:__ You may use an offhand action to make an attack.  
  
  
* __General Abilities:__   
  * __Tier Three Spells:__ Magical energy flows through you. You may now learn tier three spells from any of your spellbooks.  
  
  
__Level 8 Cleric__

* __Choices:__   
  * __Stat Increase:__ You gain two stat points to add to a stat or stats of your choosing.  
  
  
__Level 9 Cleric__

* __Combat Abilities:__   
  * __Link Lifeforce:__ As an action, link your lifeforce to that of another. Any damage they take is transferred directly to you. Remove the link as an offhand action.  
  
  
__Level 10 Cleric__

* __Choices:__   
  * __Stat Increase:__ You gain two stat points to add to a stat or stats of your choosing.  
  
  
* __General Abilities:__   
  * __Tier Four Spells:__ You are a master of your spellcraft. You can now learn tier four spells from any of your spellbooks.  
  
  
__Level 11 Cleric__

* __General Abilities:__   
  * __True Heal:__ Re-roll any ones or twos rolled while healing.  
  
  
__Level 12 Cleric__

* __Actions:__   
  * __Major Offhand Spell:__ You may cast a tier two spell as an offhand action.  
  
  
* __Choices:__   
  * __Stat Increase:__ You gain two stat points to add to a stat or stats of your choosing.  
  
  
__Level 13 Cleric__

* __General Abilities:__   
  * __Tier Five Spells:__ You have achieved the highest form of sorcery, and are a mage to be reckoned with. You can now learn tier five spells from any of your spellbooks.  
  
  
* __Advantages:__   
  * __Halo:__ A halo shines about your head. Take advantage when dealing with god-fearing people, and when intimidating anyone wicked.  
  
  
* __Combat Abilities:__   
  * __Burning Bright:__ At will, you can make your halo blaze with the same intensity as the light spell, dealing damage 1d6 damage to the undead.  
  
  
__Level 14 Cleric__

* __Choices:__   
  * __Stat Increase:__ You gain two stat points to add to a stat or stats of your choosing.  
  
  
__Level 15 Cleric__

* __General Abilities:__   
  * __Angelic Wings:__ Once per day, summon angelic wings to your back for one hour. These give you an effect identical to the fly spell.  
  
  
* __Combat Abilities:__   
  * __Aura of Advantage:__ _(Cost 2)_ Give all party members advantage on their next action.  
  
  
  
___

  
### Druid
<div></div>
<div></div>

<img src='https://github.com/emaicus/Rangers-and-Ruffians/blob/rangers_v2.1/site/static/images/class/druid.jpg?raw=true' style='width:350px' />

  
  
Gaurdians of nature, most druids prefer to live in tribes in the forests, mountains, prairie, tundra, or desert. Druid's command powerful nature based magic, which they use to smite those who threaten them, their friends, or their home. Druids utilize intelligence based action points to cast spells, and are a good match for players interested in playing a mage. As you build your druid, consider where they came from. Why are they so attached to nature? How does their attachment to the natural world change how they think? How do they react to large towns and cities? What do they wear, and how do they speak? How do they feel about other types of magic? Why are they on their adventure? How do they feel about eating meat? What are their values? What do they think the place of people is in the world? How will being a druid change the way you interact with your party?
  
  
|STR|DEX|INT|INF|CHR|PER|LUK|HD|  
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|  
|-2|-1|0|2|-3|1|1|4|  
  
  
__Druid Abilities:__ 
* __Rules:__   
  * __Learning Spells:__ New spells or techniques are obtained by leveling up or by finding spellbooks or scrolls in the world. A spellbook may contain a specific spell, or a maximum spell tier. Spellbooks with a maximum spell tier contain one spell of your choice from the spellbooks that you can learn from with a tier up to the spellbook's maximum spell tier.  
  * __Learn Spells:__ Each time you level up, learn one new spell of each spell tier that you have access to. Spells must be learned from one of your spellbooks.  
* __Spellbooks:__   
  * __Novice Spellbook:__ You are able to learn spells from the Novice Spellbook.  
  * __The Druid's Field Guide:__ You can learn spells from the Druid's Field Guide.  
* __Choices:__   
  * __Spell Choice:__ At the start of your journey, you know 2 extra tier zero spells.  
* __General Abilities:__   
  * __Tier Zero Spells:__ You have achieved a basic knowledge of the arcane, and may now learn tier zero spells from any of your spellbooks.  
  
  
__Level 0 Druid__

* __Rules:__   
  * __Learning Spells:__ New spells or techniques are obtained by leveling up or by finding spellbooks or scrolls in the world. A spellbook may contain a specific spell, or a maximum spell tier. Spellbooks with a maximum spell tier contain one spell of your choice from the spellbooks that you can learn from with a tier up to the spellbook's maximum spell tier.  
  * __Learn Spells:__ Each time you level up, learn one new spell of each spell tier that you have access to. Spells must be learned from one of your spellbooks.  
  
  
* __Spellbooks:__   
  * __Novice Spellbook:__ You are able to learn spells from the Novice Spellbook.  
  * __The Druid's Field Guide:__ You can learn spells from the Druid's Field Guide.  
  
  
* __General Abilities:__   
  * __Tier Zero Spells:__ You have achieved a basic knowledge of the arcane, and may now learn tier zero spells from any of your spellbooks.  
  
  
__Level 1 Druid__

* __General Abilities:__   
  * __Tier One Spells:__ Your powers are growing. You may now learn tier one spells from any of your spellbooks.  
  
  
__Level 2 Druid__

* __Choices:__   
  * __Stat Increase:__ You gain two stat points to add to a stat or stats of your choosing.  
  
  
__Level 3 Druid__

* __Actions:__   
  * __Minor Offhand Spell:__ You may cast a tier zero spell as an offhand action.  
  
  
__Level 4 Druid__

* __Choices:__   
  * __Stat Increase:__ You gain two stat points to add to a stat or stats of your choosing.  
  
  
* __General Abilities:__   
  * __Tier Two Spells:__ You have graduated from novice to proficient! You may now learn tier two spells from any of your spellbooks.  
  
  
__Level 5 Druid__

* __Advantages:__   
  * __Tracker:__ You are an excellent tracker, and have advantage when looking for trails and sign of passage.  
  
  
__Level 6 Druid__

* __Actions:__   
  * __Greater Offhand Spell:__ You may cast a tier one spell as an offhand action.  
  
  
* __Choices:__   
  * __Stat Increase:__ You gain two stat points to add to a stat or stats of your choosing.  
  
  
__Level 7 Druid__

* __Actions:__   
  * __Offhand Attack:__ You may use an offhand action to make an attack.  
  
  
* __General Abilities:__   
  * __Tier Three Spells:__ Magical energy flows through you. You may now learn tier three spells from any of your spellbooks.  
  
  
__Level 8 Druid__

* __Choices:__   
  * __Stat Increase:__ You gain two stat points to add to a stat or stats of your choosing.  
  
  
__Level 9 Druid__

* __General Abilities:__   
  * __Ascend:__ Once per day, you may enter the ascended state. While ascended you immediately gain 5 action points. he ascended state lasts for 3 turns or five minutes. When you fall out of the ascended state, you are fatigued. Immediately take 4d10 damage, and have disadvantage in all things until you are able to sleep. If you are killed in the ascended state, you cannot be resurrected.  
  
  
__Level 10 Druid__

* __Choices:__   
  * __Stat Increase:__ You gain two stat points to add to a stat or stats of your choosing.  
  
  
* __General Abilities:__   
  * __Tier Four Spells:__ You are a master of your spellcraft. You can now learn tier four spells from any of your spellbooks.  
  
  
__Level 11 Druid__

* __General Abilities:__   
  * __Ascended Flight:__ While in the Ascended state, you may take flight as an offhand action.  
  
  
__Level 12 Druid__

* __Actions:__   
  * __Major Offhand Spell:__ You may cast a tier two spell as an offhand action.  
  
  
* __Choices:__   
  * __Stat Increase:__ You gain two stat points to add to a stat or stats of your choosing.  
  
  
__Level 13 Druid__

* __General Abilities:__   
  * __Tier Five Spells:__ You have achieved the highest form of sorcery, and are a mage to be reckoned with. You can now learn tier five spells from any of your spellbooks.  
  
  
* __Combat Abilities:__   
  * __True Ascension:__ Ascension no longer has a time limit. While ascended, you make all perception checks and inner fire saving throws with advantage. You may enter and leave the ascended state as often as you want. When you leave the ascended state, make an inner fire saving throw. If it is less than 10, you are fatigued.  
  
  
__Level 14 Druid__

* __Choices:__   
  * __Stat Increase:__ You gain two stat points to add to a stat or stats of your choosing.  
  
  
* __General Abilities:__   
  * __Power of Ascension:__ While in the ascended state, gain 5 inner fire, strength, and dexterity.  
  
  
__Level 15 Druid__

* __Combat Abilities:__   
  * __Ascended Action:__ Once per turn while ascended, you may take an extra action and movement when it is not your turn.  
  
  
  
___

  
### Fighter
<div></div>
<div></div>

<img src='https://github.com/emaicus/Rangers-and-Ruffians/blob/rangers_v2.1/site/static/images/class/fighter.jpg?raw=true' style='width:350px' />

  
  
Fighters are powerful strength or dexterity based warriors. Unlike the knight, fighters are unarmored, and have a skillset more suited to keeping themselves alive and bringing down enemies than providing support.
  
  
|STR|DEX|INT|INF|CHR|PER|LUK|HD|  
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|  
|1|2|-2|-3|-1|0|1|4|  
  
  
__Fighter Abilities:__ 
* __Combat Abilities:__   
  * __Trained Attack:__ _(Cost 1)_ Re-roll an attack after you make it.  
  
  
__Level 0 Fighter__

* __Combat Abilities:__   
  * __Trained Attack:__ _(Cost 1)_ Re-roll an attack after you make it.  
  
  
__Level 1 Fighter__

* __General Abilities:__   
  * __Determination:__ _(Cost 1)_ Gain a d10 inspiration dice as an offhand action.  
  
  
__Level 2 Fighter__

* __Choices:__   
  * __Stat Increase:__ You gain two stat points to add to a stat or stats of your choosing.  
  
  
__Level 3 Fighter__

* __General Abilities:__   
  * __Minor Second Wind:__ _(Cost 1)_ Heal yourself for 1d6 damage as an offhand action.  
  
  
* __Combat Abilities:__   
  * __Resolve:__ When your health drops below 25%, all attacks do half damage against you.  
  
  
__Level 4 Fighter__

* __Choices:__   
  * __Stat Increase:__ You gain two stat points to add to a stat or stats of your choosing.  
  
  
__Level 5 Fighter__

* __Combat Abilities:__   
  * __Nimble:__ Targeted ranged attacks take disadvantage against you.  
  * __Reduced Critical:__ You perform a critical hit if you roll one less than your die's number of sides.  
  
  
__Level 6 Fighter__

* __Choices:__   
  * __Stat Increase:__ You gain two stat points to add to a stat or stats of your choosing.  
  
  
__Level 7 Fighter__

* __Actions:__   
  * __Offhand Attack:__ You may use an offhand action to make an attack.  
  
  
__Level 8 Fighter__

* __Choices:__   
  * __Stat Increase:__ You gain two stat points to add to a stat or stats of your choosing.  
  
  
__Level 9 Fighter__

* __General Abilities:__   
  * __Major Second Wind:__ _(Cost 1)_ Heal yourself for 2d10 damage as an offhand action.  
  
  
__Level 10 Fighter__

* __Choices:__   
  * __Stat Increase:__ You gain two stat points to add to a stat or stats of your choosing.  
  
  
__Level 11 Fighter__

* __Combat Abilities:__   
  * __Find Center:__ _(Cost 1)_ Free Action. Take advantage in all things for one turn.  
  
  
__Level 12 Fighter__

* __Choices:__   
  * __Stat Increase:__ You gain two stat points to add to a stat or stats of your choosing.  
  
  
__Level 13 Fighter__

* __Combat Abilities:__   
  * __Stay on Your Feet:__ If you fall to zero health, make a D14 inner fire saving throw. If you succeed, drop to 1 health instead.  
  
  
__Level 14 Fighter__

* __Choices:__   
  * __Stat Increase:__ You gain two stat points to add to a stat or stats of your choosing.  
  
  
__Level 15 Fighter__

* __Combat Abilities:__   
  * __Reduced Critical:__ You perform a critical hit if you roll one less than your die's number of sides.  
  * __Whirlwind of Blades:__ _(Cost 2)_ Make an additional 3 attacks on your turn.  
  
  
  
___

  
### Gunslinger
<div></div>
<div></div>

<img src='https://github.com/emaicus/Rangers-and-Ruffians/blob/rangers_v2.1/site/static/images/class/female/gunslinger.jpg?raw=true' style='width:350px' />

  
  
Through luck, valor, or perhaps trickery, the Gunslinger has managed to acquire one of the rarest weapons in the world. As such, they have a close bond with their gun, which is usually their primary means of income. At the beginning of their adventure, a gunsling may choose to start with either a rifle or a pistol, a decision that determines engagement range and their upgrade path.
  
  
|STR|DEX|INT|INF|CHR|PER|LUK|HD|  
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|  
|-2|1|-1|-3|0|2|1|4|  
  
  
__Gunslinger Abilities:__ 
* __Choices:__   
  * __This is my Weapon:__ Your gun is the only friend you need. Make sure to give it a name.  
  * __Gunslinger or Marksman:__ You may choose to subclass into a Gunslinger or a Marksman. Gunslinger's carry Pistols, and focus on shooting quickly and frequently. Marksmen carry a rifle, and aim to do high damage on single shots. On subsequent level-ups, you will gain unique abilities based on your choice.  
* __Advantages:__   
  * __Regular Patron:__ You may add 1d6 to charisma checks made in a tavern.  
* __Combat Abilities:__   
  * __Focus:__ _(Cost 1)_ Focus before a shot to gain advantage on it. Removes distance penalties.  
  
  
__Level 0 Gunslinger__

* __Choices:__   
  * __This is my Weapon:__ Your gun is the only friend you need. Make sure to give it a name.  
  * __Gunslinger or Marksman:__ You may choose to subclass into a Gunslinger or a Marksman. Gunslinger's carry Pistols, and focus on shooting quickly and frequently. Marksmen carry a rifle, and aim to do high damage on single shots. On subsequent level-ups, you will gain unique abilities based on your choice.  
  
  
* __Advantages:__   
  * __Regular Patron:__ You may add 1d6 to charisma checks made in a tavern.  
  
  
* __Combat Abilities:__   
  * __Focus:__ _(Cost 1)_ Focus before a shot to gain advantage on it. Removes distance penalties.  
  
  
__Gunslinger Abilities__  
* Combat Abilities:   
  * __Pistol:__ You begin your adventure with a 1d6 pistol.  
  
  
__Marksman Abilities__  
* Combat Abilities:   
  * __Rifle:__ You begin your adventure with a 1d8 rifle.  
  
  
__Level 1 Gunslinger__

__Gunslinger Abilities__  
* Combat Abilities:   
  * __Flash Grenade:__ _(Cost 1)_ Throw a flash grenade. These grenades have a 10ft radius on explosion. If an entity that sees the explosion a D10 dexterity saving throw, they are blinded for 2 turns, and all actions they take have disadvantage.  
  
  
__Marksman Abilities__  
* Combat Abilities:   
  * __Bayonet:__ You can affix a blade to your rifle, which functions as a 1d6 bayonet.  
  * __Bull Rush:__ _(Cost 1)_ Spend 1 action point to burst forward 15 feet, doing 1d6 damage to everyone you hit and causing them to fall prone if they fail a spell power saving throw.  
  
  
__Level 2 Gunslinger__

* __Choices:__   
  * __Stat Increase:__ You gain two stat points to add to a stat or stats of your choosing.  
  
  
__Level 3 Gunslinger__

* __Combat Abilities:__   
  * __High Grain:__ Add 1 to your firearm damage.  
  * __From the Hip:__ Once per combat round, fire a retaliation shot when you are attacked. Roll a contested dexterity saving throw against the enemy. On success, it hits, hurting the enemy and stopping their attack.  
  
  
__Level 4 Gunslinger__

* __Choices:__   
  * __Stat Increase:__ You gain two stat points to add to a stat or stats of your choosing.  
  
  
__Level 5 Gunslinger__

* __Combat Abilities:__   
  * __High Grain:__ Add 1 to your firearm damage.  
  
  
__Gunslinger Abilities__  
* Combat Abilities:   
  * __Quickdraw:__ Add 1d4 to your initiative.  
  
  
__Level 6 Gunslinger__

* __Choices:__   
  * __Stat Increase:__ You gain two stat points to add to a stat or stats of your choosing.  
  
  
__Level 7 Gunslinger__

* __Combat Abilities:__   
  * __Line Them Up:__ If you slay an enemy, gain another attack action.  
  
  
__Gunslinger Abilities__  
* Actions:   
  * __Twin Guns:__ You are able to wield two firearms. You may attack with both in a single action.  
  
  
__Marksman Abilities__  
* Actions:   
  * __Offhand Attack:__ You may use an offhand action to make an attack.  
  
  
__Level 8 Gunslinger__

* __Choices:__   
  * __Stat Increase:__ You gain two stat points to add to a stat or stats of your choosing.  
  
  
__Level 9 Gunslinger__

__Gunslinger Abilities__  
* Combat Abilities:   
  * __Feeling Lucky:__ _(Cost 1)_ Add a number of d4's equal to your luck to an attack.  
  * __Fastest Gun:__ Add 1d10 to your initiative.  
  
  
__Marksman Abilities__  
* Combat Abilities:   
  * __Savage Critical:__ On a critical hit, do an additional dice of damage.  
  * __Reduced Critical:__ You perform a critical hit if you roll one less than your die's number of sides.  
  
  
__Level 10 Gunslinger__

* __Choices:__   
  * __Stat Increase:__ You gain two stat points to add to a stat or stats of your choosing.  
  
  
__Level 11 Gunslinger__

__Gunslinger Abilities__  
* Combat Abilities:   
  * __Hollowpoint:__ Your shots do 1d6 additional damage to unarmored targets.  
  
  
__Marksman Abilities__  
* Combat Abilities:   
  * __Re-chamber:__ Add 1d6 to your rifle damage.  
  * __Armor Penetrating Rounds:__ Your shots now pass through up to 1 foot of stone and are unaffected by armor.  
  
  
__Level 12 Gunslinger__

* __Choices:__   
  * __Stat Increase:__ You gain two stat points to add to a stat or stats of your choosing.  
  
  
__Level 13 Gunslinger__

* __Combat Abilities:__   
  * __Harrying Shot:__ On a critical hit, the attacked entity must make their next move with disadvantage.  
  
  
__Gunslinger Abilities__  
* Combat Abilities:   
  * __Strike First:__ _(Cost 1)_ Reaction. When an enemy attacks you, attack them first.  
  
  
__Marksman Abilities__  
* Combat Abilities:   
  * __High Grain:__ Add 1 to your firearm damage.  
  
  
__Level 14 Gunslinger__

* __Choices:__   
  * __Stat Increase:__ You gain two stat points to add to a stat or stats of your choosing.  
  
  
__Level 15 Gunslinger__

* __Combat Abilities:__   
  * __Reduced Critical:__ You perform a critical hit if you roll one less than your die's number of sides.  
  
  
__Gunslinger Abilities__  
* Combat Abilities:   
  * __Volley:__ Once per rest, attack every enemy you can see in a single action.  
  
  
__Marksman Abilities__  
* Combat Abilities:   
  * __Re-chamber:__ Add 1d6 to your rifle damage.  
  * __Assassinate:__ If an enemy is unsuspecting, do double damage. An enemy is unsuspecting if they don't know you are present.  
  
  
  
___

  
### Highborn
<div></div>
<div></div>

<img src='https://github.com/emaicus/Rangers-and-Ruffians/blob/rangers_v2.1/site/static/images/class/female/highborn.jpg?raw=true' style='width:350px' />

  
  
Highborns were born into a noble house and have connections and money as a result. They are well trained fighters, and have the charisma necessary to rally people to their side. While the typical highborn is not as hardened as a knight or fighter, they are able to call upon their gumption for spurts of incredible heroism.
  
  
|STR|DEX|INT|INF|CHR|PER|LUK|HD|  
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|  
|-2|1|0|-3|2|-1|1|4|  
  
  
__Highborn Abilities:__ 
* __General Abilities:__   
  * __Lightweight:__ Any cup of alcohol affects you like two.  
  * __Happy Smiles:__ Your presence increases party cheer in good weather, giving them a d8 inspiration dice once per day. It also decreases it in bad weather, giving them -1 charisma.  
* __Starting Items:__   
  * __My Father's Coffers:__ Begin your journey with 1000 extra gold pieces.  
  * __The Family Sword:__ Begin your journey with a 1d8 sword with a ruby on its hilt and an engraving of your family's sigil.  
* __Advantages:__   
  * __Beauty Incarnate:__ Gain advantage and +2 charisma when speaking to individuals who find your sex attractive.  
  * __My People:__ Gain advantage when speaking with guards and +2 charisma when speaking with citizens in your family's territory.  
* __Combat Abilities:__   
  * __Swoon:__ During battle, you can faint as a reaction or offhand action to avoid further damage. You may wake up after one turn.  
  
  
__Level 0 Highborn__

* __General Abilities:__   
  * __Happy Smiles:__ Your presence increases party cheer in good weather, giving them a d8 inspiration dice once per day. It also decreases it in bad weather, giving them -1 charisma.  
  
  
* __Advantages:__   
  * __My People:__ Gain advantage when speaking with guards and +2 charisma when speaking with citizens in your family's territory.  
  
  
* __Combat Abilities:__   
  * __Swoon:__ During battle, you can faint as a reaction or offhand action to avoid further damage. You may wake up after one turn.  
  
  
__Level 1 Highborn__

* __Advantages:__   
  * __Mantel:__ You have advantage on dexterity checks when climbing.  
  
  
__Level 2 Highborn__

* __Choices:__   
  * __Stat Increase:__ You gain two stat points to add to a stat or stats of your choosing.  
  
  
__Level 3 Highborn__

* __Actions:__   
  * __Gumption:__ You have gumption points equal to your action points. Spend one to add 1d10 to a check.  
  
  
* __Combat Abilities:__   
  * __Disarming:__ _(Cost 0)_ Force an enemy that attacks you to make an inner fire saving throw against your charisma. If they fail, their attack must be made with disadvantage.  
  
  
__Level 4 Highborn__

* __Choices:__   
  * __Stat Increase:__ You gain two stat points to add to a stat or stats of your choosing.  
  
  
__Level 5 Highborn__

* __General Abilities:__   
  * __Fallen:__ While you are on death's door, all of your allies gain a bonus action.  
  
  
* __Combat Abilities:__   
  * __Feeling Lucky:__ _(Cost 1)_ Add a number of d4's equal to your luck to an attack.  
  
  
__Level 6 Highborn__

* __Choices:__   
  * __Stat Increase:__ You gain two stat points to add to a stat or stats of your choosing.  
  
  
__Level 7 Highborn__

* __Actions:__   
  * __Spurred to Movement:__ You may now spend a point of gumption to perform an action on your turn.  
  
  
__Level 8 Highborn__

* __Choices:__   
  * __Stat Increase:__ You gain two stat points to add to a stat or stats of your choosing.  
  
  
__Level 9 Highborn__

* __Actions:__   
  * __Offhand Attack:__ You may use an offhand action to make an attack.  
  
  
__Level 10 Highborn__

* __Choices:__   
  * __Stat Increase:__ You gain two stat points to add to a stat or stats of your choosing.  
  
  
__Level 11 Highborn__

* __Advantages:__   
  * __Lionhearted:__ Gain advantage on SP saves.  
  
  
__Level 12 Highborn__

* __Choices:__   
  * __Stat Increase:__ You gain two stat points to add to a stat or stats of your choosing.  
  
  
__Level 13 Highborn__

* __General Abilities:__   
  * __Aura of Peace:__ Passive. All allies near you take heart, and gain 10 health while in your presence.  
  
  
* __Combat Abilities:__   
  * __Rally Cry:__ _(Cost 1)_ Let out a rally cry as an offhand action which allows all allies to do an additional dice of damage on their next attack.  
  
  
__Level 14 Highborn__

* __Choices:__   
  * __Stat Increase:__ You gain two stat points to add to a stat or stats of your choosing.  
  
  
__Level 15 Highborn__

* __Combat Abilities:__   
  * __Strike First:__ _(Cost 1)_ Reaction. When an enemy attacks you, attack them first.  
  
  
  
___

  
### Knight
<div></div>
<div></div>

<img src='https://github.com/emaicus/Rangers-and-Ruffians/blob/rangers_v2.1/site/static/images/class/knight.jpg?raw=true' style='width:350px' />

  
  
Knights are heavy, armored fighters who should place themselves between their party and harm's way. The ideal knight is a bastion of good, a defender of the innocent and the embodiment of chivalry. Knights hold sway over kingsmen, and are able to protect their allies.
  
  
|STR|DEX|INT|INF|CHR|PER|LUK|HD|  
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|  
|2|-3|-1|1|0|-2|0|6|  
  
  
__Knight Abilities:__ 
* __Starting Items:__   
  * __Armored:__ You begin your journey with a suit of +2 armor light plate.  
* __Advantages:__   
  * __Kingsmen:__ Gain advantage on charisma checks when speaking with kingsmen.  
* __Combat Abilities:__   
  * __Shield Bash:__ Use an action to shield bash an enemy, dealing 1d6 damage and staggering them if they fail a contested strength check. A staggered enemy looses one of its actions. At level 4, damage increases to 1d8. At level 8, damage increases to 1d10. At level 12, damage increases to 1d12.  
  
  
__Level 0 Knight__

* __Advantages:__   
  * __Kingsmen:__ Gain advantage on charisma checks when speaking with kingsmen.  
  
  
* __Combat Abilities:__   
  * __Shield Bash:__ Use an action to shield bash an enemy, dealing 1d6 damage and staggering them if they fail a contested strength check. A staggered enemy looses one of its actions. At level 4, damage increases to 1d8. At level 8, damage increases to 1d10. At level 12, damage increases to 1d12.  
  
  
__Level 1 Knight__

* __Combat Abilities:__   
  * __Shield of Men:__ Reaction. Once per round of combat, you can throw yourself in front of a teammate, taking their damage for them. Any damage you receive as a result is halved. Works up to 30 feet.  
  
  
__Level 2 Knight__

* __Choices:__   
  * __Stat Increase:__ You gain two stat points to add to a stat or stats of your choosing.  
  
  
__Level 3 Knight__

* __General Abilities:__   
  * __Shield Up:__ Take half damage from non-magic piercing or blunt force ranged attacks if holding a shield.  
  
  
* __Combat Abilities:__   
  * __Taunt:__ _(Cost 1)_ You can taunt your opponents. Foes within 30 feet of you must make an inner fire saving throw or be forced to attack you instead of others. Repeat save each turn.  
  
  
__Level 4 Knight__

* __Choices:__   
  * __Stat Increase:__ You gain two stat points to add to a stat or stats of your choosing.  
  
  
__Level 5 Knight__

* __Combat Abilities:__   
  * __Trained Precision:__ _(Cost 1)_ Gain an additional damage dice on your attack.  
  
  
__Level 6 Knight__

* __Choices:__   
  * __Stat Increase:__ You gain two stat points to add to a stat or stats of your choosing.  
  
  
__Level 7 Knight__

* __Actions:__   
  * __Offhand Attack:__ You may use an offhand action to make an attack.  
  
  
* __General Abilities:__   
  * __Ready Stance:__ As an offhand action, take up a stance that grants you 1d6 armor until your next turn.  
  
  
__Level 8 Knight__

* __Choices:__   
  * __Stat Increase:__ You gain two stat points to add to a stat or stats of your choosing.  
  
  
__Level 9 Knight__

* __Combat Abilities:__   
  * __Steel Yourself:__ _(Cost 1)_ Choose to take half damage from an attack.  
  * __Cleave:__ Strike up to two adjacent foes when you make a melee attack.  
  
  
__Level 10 Knight__

* __Choices:__   
  * __Stat Increase:__ You gain two stat points to add to a stat or stats of your choosing.  
  
  
__Level 11 Knight__

* __Combat Abilities:__   
  * __Stalwart Defender:__ Grant all allies within 30 feet of you +1 armor.  
  
  
__Level 12 Knight__

* __Choices:__   
  * __Stat Increase:__ You gain two stat points to add to a stat or stats of your choosing.  
  
  
__Level 13 Knight__

* __Combat Abilities:__   
  * __Last Line of Defense:__ If any of your allies are on death's door or have died during this encounter, add an extra damage dice to all of your attacks.  
  
  
__Level 14 Knight__

* __Choices:__   
  * __Stat Increase:__ You gain two stat points to add to a stat or stats of your choosing.  
  
  
__Level 15 Knight__

* __Combat Abilities:__   
  * __Sword of Honor:__ _(Cost 3)_ Imbue your blade with radiant light. The light lasts for 5 turns, and causes your blade to deal an additional 2d6 damage. While your blade is imbued with light, you take advantage on all spell saving throws, and cannot be frightened.  
  
  
  
___

  
### Monk
<div></div>
<div></div>

<img src='https://github.com/emaicus/Rangers-and-Ruffians/blob/rangers_v2.1/site/static/images/class/female/monk.jpg?raw=true' style='width:350px' />

  
  
Monks are masters of hand to hand combat, who use their extensive control of their bodies to overcome their foes. Monks are able to learn abilities from scrolls, which they may find scattered throughout the world. Monks have dedicated themself to the art of understanding the natural and spiritual world, and are often levelheaded and intelligent. As you create your monk, consider what their goals are. How did they become a monk, and what are they hoping to gain by doing so? How do they react in stressful situations? How do they interact with other people? Are they quiet and reserved? Confident and sure of themself? How will being a monk affect the way you interact with your party?
  
  
|STR|DEX|INT|INF|CHR|PER|LUK|HD|  
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|  
|-1|1|-2|0|-3|2|1|4|  
  
  
__Monk Abilities:__ 
* __Rules:__   
  * __Learn Fighting Techniques:__ Each time you level up, learn one fighting technique from each fighting technique tier you have access to.  
* __Spellbooks:__   
  * __The Book of Chi:__ You may select 2 combat techniques and 2 general techniques from the Book of Chi at the start of your journey.  
* __Choices:__   
  * __Starting Fighting Techniques:__ Begin your journey with two standard fighting techniques.  
* __General Abilities:__   
  * __Fighting Techniques:__ You may learn a new fighting technique from the book of chi.  
  
  
__Level 0 Monk__

* __Rules:__   
  * __Learn Fighting Techniques:__ Each time you level up, learn one fighting technique from each fighting technique tier you have access to.  
  
  
* __Spellbooks:__   
  * __The Book of Chi:__ You may select 2 combat techniques and 2 general techniques from the Book of Chi at the start of your journey.  
  
  
* __General Abilities:__   
  * __Fighting Techniques:__ You may learn a new fighting technique from the book of chi.  
  
  
__Level 2 Monk__

* __Choices:__   
  * __Stat Increase:__ You gain two stat points to add to a stat or stats of your choosing.  
  
  
__Level 4 Monk__

* __Choices:__   
  * __Stat Increase:__ You gain two stat points to add to a stat or stats of your choosing.  
  
  
__Level 6 Monk__

* __Choices:__   
  * __Stat Increase:__ You gain two stat points to add to a stat or stats of your choosing.  
  
  
__Level 8 Monk__

* __Choices:__   
  * __Stat Increase:__ You gain two stat points to add to a stat or stats of your choosing.  
  
  
__Level 10 Monk__

* __Choices:__   
  * __Stat Increase:__ You gain two stat points to add to a stat or stats of your choosing.  
  
  
* __General Abilities:__   
  * __Master Fighting Techniques:__ You may learn a new master fighting technique from the book of chi.  
  
  
__Level 12 Monk__

* __Choices:__   
  * __Stat Increase:__ You gain two stat points to add to a stat or stats of your choosing.  
  
  
__Level 14 Monk__

* __Choices:__   
  * __Stat Increase:__ You gain two stat points to add to a stat or stats of your choosing.  
  
  
* __General Abilities:__   
  * __Legendary Fighting Techniques:__ You may learn a new legendary fighting technique from the book of chi.  
  
  
  
___

  
### Necromancer
<div></div>
<div></div>

<img src='https://github.com/emaicus/Rangers-and-Ruffians/blob/rangers_v2.1/site/static/images/class/necromancer.jpg?raw=true' style='width:350px' />

  
  
Death is not my enemy, nor is it my ally, it is my servant. So say Necromancers, mages who study the intricacies of death, and what follows after. Often fuled by macabre fasination or a god complex, Necromancy is deeply feared and considered taboo by almost everyone. Clerics and Paladins, in particular, may despise or hunt necromacers. At the beginning of their journey, necromancers may choose to be vegan, promising only to eat the souls of evil individuals. As you create your necromancer, consider their values. How did they end up studying such horrible magics? Was it out of necessity? Curiosity? What are they hoping to accomplish? How do they rationalize what they do? Do they have any ticks or quirks? How will being a necromancer affect how you interact with your party?
  
  
|STR|DEX|INT|INF|CHR|PER|LUK|HD|  
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|  
|0|-1|1|2|-3|-2|2|2|  
  
  
__Necromancer Abilities:__ 
* __Rules:__   
  * __Learn Spells:__ Each time you level up, learn one new spell of each spell tier that you have access to. Spells must be learned from one of your spellbooks.  
  * __Soul Harvest:__ You may harvest 1 soul from a sentient entity that has died within twenty four hours.  
  * __Learning Spells:__ New spells or techniques are obtained by leveling up or by finding spellbooks or scrolls in the world. A spellbook may contain a specific spell, or a maximum spell tier. Spellbooks with a maximum spell tier contain one spell of your choice from the spellbooks that you can learn from with a tier up to the spellbook's maximum spell tier.  
  * __Soul Based Magic:__ To fuel your magic, you use the concentrated essence of life, which you are able to harvest from the dead. These "souls" are stored in your soul jar until they are expended on a spell or by an ability. At that time, they escape to the hereafter.  
* __Spellbooks:__   
  * __The Macabre Manual:__ You are able to learn spells from the Macabre Manual.  
* __Choices:__   
  * __Spell Choice:__ At the start of your journey, you know 2 extra tier zero spells.  
  * __Vegan:__ At the start of your journey you may choose to become a 'vegan.' Deduct 1 point from your vitality and strength, and add 2 to your charisma. As a vegan, you swear not to harvest souls from the innocent, but increase the time limit on Mortal Coil to once per month.  
* __General Abilities:__   
  * __Mortal Coil:__ Once every week, you must consume a soul. If you do not, your body begins to rot away, causing fear and horror in those who see you.  
  * __Tier Zero Spells:__ You have achieved a basic knowledge of the arcane, and may now learn tier zero spells from any of your spellbooks.  
* __Starting Items:__   
  * __Soul Jar:__ You have a soul jar, which produces 1d6 souls each day at midnight, the jar can produce 2 souls at maximum. Your soul jar is capable of holding 20 souls at maximum.  
  
  
__Level 0 Necromancer__

* __Rules:__   
  * __Learn Spells:__ Each time you level up, learn one new spell of each spell tier that you have access to. Spells must be learned from one of your spellbooks.  
  * __Soul Harvest:__ You may harvest 1 soul from a sentient entity that has died within twenty four hours.  
  * __Learning Spells:__ New spells or techniques are obtained by leveling up or by finding spellbooks or scrolls in the world. A spellbook may contain a specific spell, or a maximum spell tier. Spellbooks with a maximum spell tier contain one spell of your choice from the spellbooks that you can learn from with a tier up to the spellbook's maximum spell tier.  
  * __Soul Based Magic:__ To fuel your magic, you use the concentrated essence of life, which you are able to harvest from the dead. These "souls" are stored in your soul jar until they are expended on a spell or by an ability. At that time, they escape to the hereafter.  
  
  
* __Spellbooks:__   
  * __The Macabre Manual:__ You are able to learn spells from the Macabre Manual.  
  
  
* __Choices:__   
  * __Vegan:__ At the start of your journey you may choose to become a 'vegan.' Deduct 1 point from your vitality and strength, and add 2 to your charisma. As a vegan, you swear not to harvest souls from the innocent, but increase the time limit on Mortal Coil to once per month.  
  
  
* __General Abilities:__   
  * __Mortal Coil:__ Once every week, you must consume a soul. If you do not, your body begins to rot away, causing fear and horror in those who see you.  
  * __Tier Zero Spells:__ You have achieved a basic knowledge of the arcane, and may now learn tier zero spells from any of your spellbooks.  
  
  
* __Starting Items:__   
  * __Soul Jar:__ You have a soul jar, which produces 1d6 souls each day at midnight, the jar can produce 2 souls at maximum. Your soul jar is capable of holding 20 souls at maximum.  
  
  
__Level 1 Necromancer__

* __General Abilities:__   
  * __Tier One Spells:__ Your powers are growing. You may now learn tier one spells from any of your spellbooks.  
  * __Edge of Eternity:__ You can consume a soul to increase a stat by 1 or to give yourself a temporary increase of 1d10 health. If you consume more than 3 in a day, decrease the time limit on Mortal Coil to once per day for three days.  
  
  
__Level 2 Necromancer__

* __Choices:__   
  * __Stat Increase:__ You gain two stat points to add to a stat or stats of your choosing.  
  
  
__Level 3 Necromancer__

* __Actions:__   
  * __Minor Offhand Spell:__ You may cast a tier zero spell as an offhand action.  
  
  
__Level 4 Necromancer__

* __Choices:__   
  * __Stat Increase:__ You gain two stat points to add to a stat or stats of your choosing.  
  
  
* __General Abilities:__   
  * __Tier Two Spells:__ You have graduated from novice to proficient! You may now learn tier two spells from any of your spellbooks.  
  
  
__Level 5 Necromancer__

* __General Abilities:__   
  * __Eyes of the Others:__ Consume a soul to give yourself darkvision and detect life for a day.  
  
  
__Level 6 Necromancer__

* __Rules:__   
  * __Larger Soul Jar:__ Your soul jar can produce at maximum 1 more soul per day.  
  
  
* __Actions:__   
  * __Greater Offhand Spell:__ You may cast a tier one spell as an offhand action.  
  
  
* __Choices:__   
  * __Stat Increase:__ You gain two stat points to add to a stat or stats of your choosing.  
  
  
__Level 7 Necromancer__

* __Actions:__   
  * __Offhand Attack:__ You may use an offhand action to make an attack.  
  
  
* __General Abilities:__   
  * __Tier Three Spells:__ Magical energy flows through you. You may now learn tier three spells from any of your spellbooks.  
  * __Reap:__ When you harvest a soul, roll a d20. If you roll 15 or above, harvest 2.  
  
  
__Level 8 Necromancer__

* __Choices:__   
  * __Stat Increase:__ You gain two stat points to add to a stat or stats of your choosing.  
  
  
__Level 9 Necromancer__

* __Rules:__   
  * __Larger Soul Jar:__ Your soul jar can produce at maximum 1 more soul per day.  
  
  
__Level 10 Necromancer__

* __Choices:__   
  * __Stat Increase:__ You gain two stat points to add to a stat or stats of your choosing.  
  
  
* __General Abilities:__   
  * __Tier Four Spells:__ You are a master of your spellcraft. You can now learn tier four spells from any of your spellbooks.  
  
  
__Level 11 Necromancer__

* __Rules:__   
  * __Larger Soul Jar:__ Your soul jar can produce at maximum 1 more soul per day.  
  
  
* __General Abilities:__   
  * __Phylactery:__ You may remove your soul and put it in a box. If the box is destroyed, are destroyed with it. If your body dies and you have a thrall, your consciousness may be transferred to the thrall. If you have no thralls remaining, your body is regenerated at your phylactery after one day.  
  
  
__Level 12 Necromancer__

* __Actions:__   
  * __Major Offhand Spell:__ You may cast a tier two spell as an offhand action.  
  
  
* __Choices:__   
  * __Stat Increase:__ You gain two stat points to add to a stat or stats of your choosing.  
  
  
__Level 13 Necromancer__

* __General Abilities:__   
  * __Freed from this Mortal Coil:__ You may bond your consciousness to one of your thralls, taking full control of them. If the thrall is destroyed, your soul returns to your primary body, another thrall, or to your phylactery.  
  
  
__Level 14 Necromancer__

* __Rules:__   
  * __Larger Soul Jar:__ Your soul jar can produce at maximum 1 more soul per day.  
  
  
* __Choices:__   
  * __Stat Increase:__ You gain two stat points to add to a stat or stats of your choosing.  
  
  
* __General Abilities:__   
  * __Tier Five Spells:__ You have achieved the highest form of sorcery, and are a mage to be reckoned with. You can now learn tier five spells from any of your spellbooks.  
  
  
__Level 15 Necromancer__

* __General Abilities:__   
  * __Army of the Damned:__ As an action, resurrect every entity within 100 feet as zombies at the cost of 5 souls.  
  
  
  
___

  
### Paladin
<div></div>
<div></div>

<img src='https://github.com/emaicus/Rangers-and-Ruffians/blob/rangers_v2.1/site/static/images/class/paladin.jpg?raw=true' style='width:350px' />

  
  
Palidins are Soldiers of the Light, and are adept both at hand to hand combat and basic healing magic. Paladins are devoted to their deity, and aim to bring their influence into the world. Paladins are especially good at taking out evil entities, and are known for their Faithful Weapon ability, which lets them summon their weapon to their hand after throwing it.
  
  
|STR|DEX|INT|INF|CHR|PER|LUK|HD|  
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|  
|2|-3|-1|1|0|-2|1|4|  
  
  
__Paladin Abilities:__ 
* __Rules:__   
  * __Learning Spells:__ New spells or techniques are obtained by leveling up or by finding spellbooks or scrolls in the world. A spellbook may contain a specific spell, or a maximum spell tier. Spellbooks with a maximum spell tier contain one spell of your choice from the spellbooks that you can learn from with a tier up to the spellbook's maximum spell tier.  
  * __Learn Spells:__ Each time you level up, learn one new spell of each spell tier that you have access to. Spells must be learned from one of your spellbooks.  
* __Spellbooks:__   
  * __The Book of Healing:__ You are able to learn spells from the Book of Healing.  
* __Choices:__   
  * __Minor Spell Choice:__ At the start of your journey, you know 1 extra tier zero spells.  
  * __Pledge:__ At the start of your journey, you may select a deity to pledge yourself to.  
* __General Abilities:__   
  * __Tier Zero Spells:__ You have achieved a basic knowledge of the arcane, and may now learn tier zero spells from any of your spellbooks.  
* __Starting Items:__   
  * __Chainmail:__ You begin your journey with a suit of chainmail plate. Take -1 damage on attacks while wearing it.  
  
  
__Level 0 Paladin__

* __Rules:__   
  * __Learning Spells:__ New spells or techniques are obtained by leveling up or by finding spellbooks or scrolls in the world. A spellbook may contain a specific spell, or a maximum spell tier. Spellbooks with a maximum spell tier contain one spell of your choice from the spellbooks that you can learn from with a tier up to the spellbook's maximum spell tier.  
  * __Learn Spells:__ Each time you level up, learn one new spell of each spell tier that you have access to. Spells must be learned from one of your spellbooks.  
  
  
* __Spellbooks:__   
  * __The Book of Healing:__ You are able to learn spells from the Book of Healing.  
  
  
* __Choices:__   
  * __Pledge:__ At the start of your journey, you may select a deity to pledge yourself to.  
  
  
* __General Abilities:__   
  * __Tier Zero Spells:__ You have achieved a basic knowledge of the arcane, and may now learn tier zero spells from any of your spellbooks.  
  
  
__Level 1 Paladin__

* __Combat Abilities:__   
  * __Hammer of Light:__ Any weapon that you wield does an additional dice of damage to undead.  
  * __Bash:__ Stun an enemy on a critical hit, causing them to miss an action and an offhand action on their next turn.  
  
  
__Level 2 Paladin__

* __Choices:__   
  * __Stat Increase:__ You gain two stat points to add to a stat or stats of your choosing.  
  
  
* __General Abilities:__   
  * __Tier One Spells:__ Your powers are growing. You may now learn tier one spells from any of your spellbooks.  
  
  
__Level 3 Paladin__

* __Combat Abilities:__   
  * __Faithful Weapon:__ After throwing your weapon, you can return it to yourself. You do not take disadvantage when throwing hammers or maces.  
  
  
__Level 4 Paladin__

* __Actions:__   
  * __Minor Offhand Spell:__ You may cast a tier zero spell as an offhand action.  
  
  
* __Choices:__   
  * __Stat Increase:__ You gain two stat points to add to a stat or stats of your choosing.  
  
  
__Level 5 Paladin__

* __Combat Abilities:__   
  * __Link Lifeforce:__ As an action, link your lifeforce to that of another. Any damage they take is transferred directly to you. Remove the link as an offhand action.  
  
  
__Level 6 Paladin__

* __Choices:__   
  * __Stat Increase:__ You gain two stat points to add to a stat or stats of your choosing.  
  
  
* __General Abilities:__   
  * __Tier Two Spells:__ You have graduated from novice to proficient! You may now learn tier two spells from any of your spellbooks.  
  
  
__Level 7 Paladin__

* __Actions:__   
  * __Greater Offhand Spell:__ You may cast a tier one spell as an offhand action.  
  * __Offhand Attack:__ You may use an offhand action to make an attack.  
  
  
* __Combat Abilities:__   
  * __Shield of Men:__ Reaction. Once per round of combat, you can throw yourself in front of a teammate, taking their damage for them. Any damage you receive as a result is halved. Works up to 30 feet.  
  
  
__Level 8 Paladin__

* __Choices:__   
  * __Stat Increase:__ You gain two stat points to add to a stat or stats of your choosing.  
  
  
__Level 9 Paladin__

* __General Abilities:__   
  * __Beacon of Hope:__ Passive. All allies within 100 feet of you gain +1 to all saving throws.  
  * __Tier Three Spells:__ Magical energy flows through you. You may now learn tier three spells from any of your spellbooks.  
  
  
__Level 10 Paladin__

* __Choices:__   
  * __Stat Increase:__ You gain two stat points to add to a stat or stats of your choosing.  
  
  
__Level 11 Paladin__

* __Combat Abilities:__   
  * __Last Line of Defense:__ If any of your allies are on death's door or have died during this encounter, add an extra damage dice to all of your attacks.  
  
  
__Level 12 Paladin__

* __Choices:__   
  * __Stat Increase:__ You gain two stat points to add to a stat or stats of your choosing.  
  
  
* __General Abilities:__   
  * __Tier Four Spells:__ You are a master of your spellcraft. You can now learn tier four spells from any of your spellbooks.  
  
  
__Level 13 Paladin__

* __Combat Abilities:__   
  * __Winged Jump:__ _(Cost 1)_ Leap up to 40 feet using ethereal, angelic wings. Counts as an action.  
  
  
__Level 14 Paladin__

* __Choices:__   
  * __Stat Increase:__ You gain two stat points to add to a stat or stats of your choosing.  
  
  
__Level 15 Paladin__

* __General Abilities:__   
  * __Tier Five Spells:__ You have achieved the highest form of sorcery, and are a mage to be reckoned with. You can now learn tier five spells from any of your spellbooks.  
  
  
* __Combat Abilities:__   
  * __Fires of Heaven:__ _(Cost 1)_ When you perform a plunging attack, create an explosion dealing 2d10 damage to all entities within a 20 foot radius.  
  
  
  
___

  
### Ranger
<div></div>
<div></div>

<img src='https://github.com/emaicus/Rangers-and-Ruffians/blob/rangers_v2.1/site/static/images/class/ranger.jpg?raw=true' style='width:350px' />

  
  
Rangers are the vigilante law keepers and monster hunters of the wilds. Rangers are powerful dexterity based fighters, and are known for their abiltiy to dual weild weapons. Rangers are masters of the wilds, and are able to easily traverse their favorite terrain, as well as to prepare simple medicines in times of need. Rangers are often known by common folk to be quiet and mysterious, however, they are well loved, as it is understood that they are the thin line that stands between many villages and an onslaught of monsters. As you create your ranger, consider how they ended up a ranger? How did they become so adept at navigating the wilderness? Do they feel the need to protect villagers? What kinds of monsters have they fought? Who trained them, if anyone? How will being a ranger affect the way that you interact with your party?
  
  
|STR|DEX|INT|INF|CHR|PER|LUK|HD|  
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|  
|-2|1|-3|-1|0|2|1|4|  
  
  
__Ranger Abilities:__ 
* __Choices:__   
  * __Learned:__ You are fluent in an extra language of your choosing.  
* __General Abilities:__   
  * __Under the Stars:__ You have been forced to learn to sleep anywhere. All sleep acts as though you are in a bed.  
  * __Minor Medicine:__ If you are in your favorite terrain, you can create 1 1d20 health potion per day. Potions keep for 24 hours.  
* __Starting Items:__   
  * __Shifting Cloak:__ You possess a unique cloak, which takes on the color of your surroundings, giving you a 1d10 bonus to stealth checks made while standing still.  
* __Advantages:__   
  * __Camouflage:__ If you stay absolutely still, you can take on the color of your surroundings. This gives you advantage on stealth checks while camouflaged.  
  
  
__Level 0 Ranger__

* __Choices:__   
  * __Learned:__ You are fluent in an extra language of your choosing.  
  
  
* __General Abilities:__   
  * __Minor Medicine:__ If you are in your favorite terrain, you can create 1 1d20 health potion per day. Potions keep for 24 hours.  
  
  
* __Advantages:__   
  * __Camouflage:__ If you stay absolutely still, you can take on the color of your surroundings. This gives you advantage on stealth checks while camouflaged.  
  
  
__Level 1 Ranger__

* __Choices:__   
  * __Favorite Terrain:__ At the beginning of your journey, pick a favorite terrain. Whenever you are on it, you have advantage on any check related to the terrain, and may take advantage on an action every third turn during combat.  
  
  
* __Combat Abilities:__   
  * __Entangling Attack:__ _(Cost 1)_ You may attempt to entangle an enemy during one of your attacks using minor magic. The enemy must make an inner fire saving throw against your spell power. On a failure, the entity is ensnared, and cannot move. It may re-attempt the saving throw to escape every turn thereafter. An ensnared enemy may not move, and all attacks made against it have advantage.  
  
  
__Level 2 Ranger__

* __Choices:__   
  * __Stat Increase:__ You gain two stat points to add to a stat or stats of your choosing.  
  
  
__Level 3 Ranger__

* __General Abilities:__   
  * __Ward of Tracking:__ _(Cost 1)_ Costs one action point. Lay your hand on an opponent. For the next forty-eight hours, you know their position within 100 feet.  
  
  
* __Advantages:__   
  * __Tracker:__ You are an excellent tracker, and have advantage when looking for trails and sign of passage.  
  
  
__Level 4 Ranger__

* __Choices:__   
  * __Stat Increase:__ You gain two stat points to add to a stat or stats of your choosing.  
  
  
__Level 5 Ranger__

* __Actions:__   
  * __Twin Blades:__ You are able to wield two weapons. You may attack with both in a single action.  
  
  
* __Combat Abilities:__   
  * __Finesse Strike:__ _(Cost 1)_ Add an additional dice of damage to an attack of your choosing. If the affected entity fails an inner fire saving throw against your spell power, it suffers an additional dice of bleeding damage at the start of its next turn.  
  
  
__Level 6 Ranger__

* __Choices:__   
  * __Stat Increase:__ You gain two stat points to add to a stat or stats of your choosing.  
  
  
__Level 7 Ranger__

* __General Abilities:__   
  * __Greater Medicine:__ You can create 2 1d10 health potions per day. Potions keep for 24 hours. If you are in on your favorite terrain, potions restore an additional 1d10 health.  
  
  
* __Combat Abilities:__   
  * __Twin Blade Parry:__ Once per round of combat, you may strike back when an enemy attacks you.  
  
  
__Level 8 Ranger__

* __Choices:__   
  * __Stat Increase:__ You gain two stat points to add to a stat or stats of your choosing.  
  
  
__Level 9 Ranger__

* __Combat Abilities:__   
  * __Monster Slayer:__ Whenever you attack a beast classified as a monster, do an additional dice of damage on the attack.  
  * __Disengage:__ Enemies take disadvantage when striking you while you are moving.  
  
  
__Level 10 Ranger__

* __Choices:__   
  * __Stat Increase:__ You gain two stat points to add to a stat or stats of your choosing.  
  
  
__Level 11 Ranger__

* __General Abilities:__   
  * __Spell of Darkvision:__ _(Cost 1)_ You may use minor magic to give yourself darkvision for one hour.  
  
  
* __Combat Abilities:__   
  * __Disarming Blow:__ On a critical hit, force an enemy to drop something they are holding.  
  
  
__Level 12 Ranger__

* __Choices:__   
  * __Stat Increase:__ You gain two stat points to add to a stat or stats of your choosing.  
  
  
__Level 13 Ranger__

* __Actions:__   
  * __Offhand Attack:__ You may use an offhand action to make an attack.  
  
  
* __General Abilities:__   
  * __Expert Tracker:__ Add 1d6 to any checks made to track an individual.  
  
  
__Level 14 Ranger__

* __Choices:__   
  * __Stat Increase:__ You gain two stat points to add to a stat or stats of your choosing.  
  
  
__Level 15 Ranger__

* __Combat Abilities:__   
  * __Fire and Ice:__ _(Cost 2)_ Imbue one of your blades with fire and the other with ice. Each do an additional 1d6 damage for the duration of a battle.  
  
  
  
___

  
### Rogue
<div></div>
<div></div>

<img src='https://github.com/emaicus/Rangers-and-Ruffians/blob/rangers_v2.1/site/static/images/class/rogue.jpg?raw=true' style='width:350px' />

  
  
Sneaktheives and criminals, rogues have often fallen in with bad company. Rogues are incredibly nimble and stealthy, and are able to clime, sneak, and lockpick their way into most anything. Rogues are very weak, however, and will have better luck running away than fighting if caught. When they have to fight, Rogues often pick daggers or shortswords, and strike from on high or from in the shadows, letting their more armored friends soak up the damage.
  
  
|STR|DEX|INT|INF|CHR|PER|LUK|HD|  
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|  
|-3|2|-1|-2|0|1|2|2|  
  
  
__Rogue Abilities:__ 
* __Starting Items:__   
  * __A Thief's Gear:__ You begin with 100 feet of rope, a lock-picking kit, a smoke-bomb, and a hidden 1d6 dagger.  
* __Advantages:__   
  * __Ruffians:__ Gain advantage on charisma checks when speaking with seedy individuals, townspeople, or bandits.  
  * __Lightfoot:__ Gain advantage on stealth checks.  
  * __Nimble Fingers:__ You have advantage on dexterity and stealth checks made while stealing.  
  
  
__Level 0 Rogue__

* __Advantages:__   
  * __Lightfoot:__ Gain advantage on stealth checks.  
  * __Nimble Fingers:__ You have advantage on dexterity and stealth checks made while stealing.  
  
  
__Level 1 Rogue__

* __General Abilities:__   
  * __Strike From the Shadows:__ Do an additional dice of damage on an attacks made from hiding.  
  
  
* __Advantages:__   
  * __Mantel:__ You have advantage on dexterity checks when climbing.  
  
  
__Level 2 Rogue__

* __Choices:__   
  * __Stat Increase:__ You gain two stat points to add to a stat or stats of your choosing.  
  
  
__Level 3 Rogue__

* __Advantages:__   
  * __Master of Disguise:__ You can easily fashion disguises to hide yourself with. Gain advantage when crafting disguises.  
  
  
* __Combat Abilities:__   
  * __High Ground:__ Gain advantage on any plunging attacks.  
  
  
__Level 4 Rogue__

* __Choices:__   
  * __Stat Increase:__ You gain two stat points to add to a stat or stats of your choosing.  
  
  
__Level 5 Rogue__

* __Choices:__   
  * __Thief or Assassin:__ You may choose to subclass into a Thief or an Assassin. Thieves focus on sneaking and theft. Assassins maximize their damage output to kill enemies before they have a chance to react. On subsequent level-ups, you will gain unique abilities based on your choice.  
  
  
__Assassin Abilities__  
* General Abilities:   
  * __Imposter:__ Gain 1d6 on any checks made to imitate someone.  
  
  
__Thief Abilities__  
* General Abilities:   
  * __Soft Landing:__ Reduce any falling damage by 20 feet.  
  * __Soundless:__ Gain an additional 1d6 on stealth checks.  
  
  
__Level 6 Rogue__

* __Choices:__   
  * __Stat Increase:__ You gain two stat points to add to a stat or stats of your choosing.  
  
  
__Level 7 Rogue__

__Assassin Abilities__  
* Actions:   
  * __Offhand Attack:__ You may use an offhand action to make an attack.  
  
  
* General Abilities:   
  * __Poison:__ Once per day, create a draught of deadly poison. If ingested, the poison does 3d20 damage. If placed on a blade, the blade does an additional 1d10 damage. Poison keeps for 24 hours. Creating poison takes 6 continuous hours.  
  
  
__Thief Abilities__  
* Actions:   
  * __Offhand Attack:__ You may use an offhand action to make an attack.  
  
  
* Combat Abilities:   
  * __Pickpocket:__ If you land a critical hit, steal an item the enemy is holding.  
  
  
__Level 8 Rogue__

* __Choices:__   
  * __Stat Increase:__ You gain two stat points to add to a stat or stats of your choosing.  
  
  
__Level 9 Rogue__

__Assassin Abilities__  
* General Abilities:   
  * __Minor Blink:__ _(Cost 1)_ Teleport to a position you can see within 100 feet.  
  * __Dark Vision:__ You can see even in perfect darkness.  
  
  
__Thief Abilities__  
* General Abilities:   
  * __Flee:__ You may use an offhand action to flee without provoking attacks.  
  * __Trap Expert:__ Gain advantage when looking for, disarming, or creating traps.  
  
  
__Level 10 Rogue__

* __Choices:__   
  * __Stat Increase:__ You gain two stat points to add to a stat or stats of your choosing.  
  
  
__Level 11 Rogue__

__Assassin Abilities__  
* Combat Abilities:   
  * __Reduced Critical:__ You perform a critical hit if you roll one less than your die's number of sides.  
  
  
__Thief Abilities__  
* General Abilities:   
  * __Lucky Actions:__ You may use your luck tokens to make an additional action on your turn as well as to re-roll any dice. These tokens refill on a long rest.  
  
  
__Level 12 Rogue__

* __Choices:__   
  * __Stat Increase:__ You gain two stat points to add to a stat or stats of your choosing.  
  
  
__Level 13 Rogue__

__Assassin Abilities__  
* Combat Abilities:   
  * __Line Them Up:__ If you slay an enemy, gain another attack action.  
  * __Savage Critical:__ On a critical hit, do an additional dice of damage.  
  
  
__Thief Abilities__  
* General Abilities:   
  * __Party Save:__ _(Cost 1)_ Add 1d10 to one party member's stealth check.  
  * __Superior Mantel:__ Add 1d6 to all climbing checks.  
  
  
__Level 14 Rogue__

* __Choices:__   
  * __Stat Increase:__ You gain two stat points to add to a stat or stats of your choosing.  
  
  
__Level 15 Rogue__

__Assassin Abilities__  
* Actions:   
  * __Double Strike:__ You may attack twice in a single action.  
  
  
* General Abilities:   
  * __All-consuming Shadow:__ _(Cost 1)_ Fill a 100 foot radius with pitch darkness as an offhand action.  
  
  
__Thief Abilities__  
* General Abilities:   
  * __Spider Climb:__ You are able to climb on walls as though you are a spider.  
  
  
  
___

  
### Sorcerer
<div></div>
<div></div>

<img src='https://github.com/emaicus/Rangers-and-Ruffians/blob/rangers_v2.1/site/static/images/class/female/sorcerer.jpg?raw=true' style='width:350px' />

  
  
Sorcerer's draw their magic not from cryptic tomes nor nuanced understanding, but rather through raw force of personality. To perform magic, a sorcerer wrestles with a spirit, natural or otherwise, and convinces them to do their bidding. To this end, Sorcerers do not use action points to cast spells, but rather must pass a charisma check to perform magic. As you create your sorcerer, consider how they learned magic. Who did they learn it from? How did they first wrestle a spirit to aid them? When they cast a spell, do they always use the same spirit, or different spirits? Is the spirit natural, or the soul of someone who is gone? How will being a sorcerer change the way that you interact with the world and your party?
  
  
|STR|DEX|INT|INF|CHR|PER|LUK|HD|  
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|  
|-1|-2|0|1|2|-3|1|4|  
  
  
__Sorcerer Abilities:__ 
* __Rules:__   
  * __Learning Spells:__ New spells or techniques are obtained by leveling up or by finding spellbooks or scrolls in the world. A spellbook may contain a specific spell, or a maximum spell tier. Spellbooks with a maximum spell tier contain one spell of your choice from the spellbooks that you can learn from with a tier up to the spellbook's maximum spell tier.  
  * __Learn Spells:__ Each time you level up, learn one new spell of each spell tier that you have access to. Spells must be learned from one of your spellbooks.  
  * __Charisma Based Spellcaster:__ To succeed at casting spells, you must convince your familiar to perform it for you. To do this, roll a d20 and add your charisma. The result must beat the difficulty of the spell.  
* __Spellbooks:__   
  * __Novice Spellbook:__ You are able to learn spells from the Novice Spellbook.  
  * __The Sorcerer's Scrolls:__ You are able to learn spells from the Sorcerer's Scrolls.  
* __Choices:__   
  * __Spell Choice:__ At the start of your journey, you know 2 extra tier zero spells.  
* __General Abilities:__   
  * __Tier Zero Spells:__ You have achieved a basic knowledge of the arcane, and may now learn tier zero spells from any of your spellbooks.  
  * __Influence:__ You may use action points to increase any charisma roll by 2.  
  
  
__Level 0 Sorcerer__

* __Rules:__   
  * __Learning Spells:__ New spells or techniques are obtained by leveling up or by finding spellbooks or scrolls in the world. A spellbook may contain a specific spell, or a maximum spell tier. Spellbooks with a maximum spell tier contain one spell of your choice from the spellbooks that you can learn from with a tier up to the spellbook's maximum spell tier.  
  * __Learn Spells:__ Each time you level up, learn one new spell of each spell tier that you have access to. Spells must be learned from one of your spellbooks.  
  * __Charisma Based Spellcaster:__ To succeed at casting spells, you must convince your familiar to perform it for you. To do this, roll a d20 and add your charisma. The result must beat the difficulty of the spell.  
  
  
* __Spellbooks:__   
  * __Novice Spellbook:__ You are able to learn spells from the Novice Spellbook.  
  * __The Sorcerer's Scrolls:__ You are able to learn spells from the Sorcerer's Scrolls.  
  
  
* __General Abilities:__   
  * __Tier Zero Spells:__ You have achieved a basic knowledge of the arcane, and may now learn tier zero spells from any of your spellbooks.  
  * __Influence:__ You may use action points to increase any charisma roll by 2.  
  
  
__Level 1 Sorcerer__

* __General Abilities:__   
  * __Tier One Spells:__ Your powers are growing. You may now learn tier one spells from any of your spellbooks.  
  
  
__Level 2 Sorcerer__

* __Choices:__   
  * __Stat Increase:__ You gain two stat points to add to a stat or stats of your choosing.  
  
  
__Level 3 Sorcerer__

* __Rules:__   
  * __Spell Modification:__ You may make one or more of the following modifications to your spells. Increase difficulty by 2 to double the radius, halve the radius, or change the volume of a spell. Increase difficulty by 4  to add an additional effect dice to the spell (e.g. making a spell that does 1d10 damage do 2d10) or to tie off a spell, making it last 1d20 minutes after casting even if it is a concentration spell.  
  
  
* __Actions:__   
  * __Minor Offhand Spell:__ You may cast a tier zero spell as an offhand action.  
  
  
__Level 4 Sorcerer__

* __Choices:__   
  * __Stat Increase:__ You gain two stat points to add to a stat or stats of your choosing.  
  
  
* __General Abilities:__   
  * __Tier Two Spells:__ You have graduated from novice to proficient! You may now learn tier two spells from any of your spellbooks.  
  
  
__Level 5 Sorcerer__

* __Actions:__   
  * __Prepare Spell:__ At the start of each day, choose a spell to have 2 less difficulty.  
  
  
__Level 6 Sorcerer__

* __Actions:__   
  * __Greater Offhand Spell:__ You may cast a tier one spell as an offhand action.  
  
  
* __Choices:__   
  * __Stat Increase:__ You gain two stat points to add to a stat or stats of your choosing.  
  
  
__Level 7 Sorcerer__

* __Actions:__   
  * __Offhand Attack:__ You may use an offhand action to make an attack.  
  
  
* __General Abilities:__   
  * __Tier Three Spells:__ Magical energy flows through you. You may now learn tier three spells from any of your spellbooks.  
  
  
__Level 8 Sorcerer__

* __Choices:__   
  * __Stat Increase:__ You gain two stat points to add to a stat or stats of your choosing.  
  
  
__Level 9 Sorcerer__

* __Combat Abilities:__   
  * __Spirits Within:__ Wrestle with a spirit, forcing it to fill you with its strength. Every turn that you are imbued with a spirit, make a D10 inner fire saving throw. If you fail, take 2d6 psychic damage. If you critically fail, the spirit escapes you. While you are imbued with a spirit, you have advantage on all charisma checks. You are also able to take an extra actions each turn, and may add +1 to strength, dexterity, perception, and inner fire.  
  
  
__Level 10 Sorcerer__

* __Choices:__   
  * __Stat Increase:__ You gain two stat points to add to a stat or stats of your choosing.  
  
  
* __General Abilities:__   
  * __Tier Four Spells:__ You are a master of your spellcraft. You can now learn tier four spells from any of your spellbooks.  
  
  
__Level 11 Sorcerer__

* __General Abilities:__   
  * __Spiritual Movement:__ While you contain a spirit, you may instantly teleport between patches of darkness as an offhand action or once per ten minutes out of combat.  
  
  
__Level 12 Sorcerer__

* __Actions:__   
  * __Major Offhand Spell:__ You may cast a tier two spell as an offhand action.  
  
  
* __Choices:__   
  * __Stat Increase:__ You gain two stat points to add to a stat or stats of your choosing.  
  
  
__Level 13 Sorcerer__

* __General Abilities:__   
  * __Tier Five Spells:__ You have achieved the highest form of sorcery, and are a mage to be reckoned with. You can now learn tier five spells from any of your spellbooks.  
  
  
__Level 14 Sorcerer__

* __Choices:__   
  * __Stat Increase:__ You gain two stat points to add to a stat or stats of your choosing.  
  
  
__Level 15 Sorcerer__

* __Combat Abilities:__   
  * __Light and Shadow:__ While you possess a spirit, add 1d10 damage to any attack that you make. Further, gain the darkvision ability, and advantage on any inner fire saving throws, including the one used to keep control of the spirit.  
  
  
  
___

  
### Wizard
<div></div>
<div></div>

<img src='https://github.com/emaicus/Rangers-and-Ruffians/blob/rangers_v2.1/site/static/images/class/wizard.jpg?raw=true' style='width:350px' />

  
  
Often eccentric, wizards are known to be wayfarers and meddlers. Most keep to themselves, approaching others only to entwine them in schemes only they know about. Wizards arrive precisely when they mean to. To use magic, Wizards use action points to cast spells. Wizards gain access to new spell tiers before any other class. As you create your wizard, consider what their past is. How old are they? What kind of family did they come from? How long have they been a wizard? Are they mysterious? Are they competent? How do they interact with others? Who taught them magic? How will being a wizard affect how you interact with your other party members?
  
  
|STR|DEX|INT|INF|CHR|PER|LUK|HD|  
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|  
|-1|-3|2|1|0|-2|2|2|  
  
  
__Wizard Abilities:__ 
* __Rules:__   
  * __Learn Spells:__ Each time you level up, learn one new spell of each spell tier that you have access to. Spells must be learned from one of your spellbooks.  
  * __Learning Spells:__ New spells or techniques are obtained by leveling up or by finding spellbooks or scrolls in the world. A spellbook may contain a specific spell, or a maximum spell tier. Spellbooks with a maximum spell tier contain one spell of your choice from the spellbooks that you can learn from with a tier up to the spellbook's maximum spell tier.  
* __Spellbooks:__   
  * __Novice Spellbook:__ You are able to learn spells from the Novice Spellbook.  
  * __The Wizard's Addendum:__ You are able to learn spells from the Wizard's Addendum.  
* __Choices:__   
  * __Spell Choice:__ At the start of your journey, you know 2 extra tier zero spells.  
* __General Abilities:__   
  * __Tier Zero Spells:__ You have achieved a basic knowledge of the arcane, and may now learn tier zero spells from any of your spellbooks.  
* __Starting Items:__   
  * __The Sword and the Satchel:__ You begin your adventure with a bottomless satchel.  
  * __Walking Stick:__ You begin your adventure with a wizard's staff which gives you 1d4 additional damage to all spells.  
* __Advantages:__   
  * __Historian:__ You have a deep knowledge of the land in which your adventure takes place. You gave advantage on any history or geography checks.  
  
  
__Level 0 Wizard__

* __Rules:__   
  * __Learn Spells:__ Each time you level up, learn one new spell of each spell tier that you have access to. Spells must be learned from one of your spellbooks.  
  * __Learning Spells:__ New spells or techniques are obtained by leveling up or by finding spellbooks or scrolls in the world. A spellbook may contain a specific spell, or a maximum spell tier. Spellbooks with a maximum spell tier contain one spell of your choice from the spellbooks that you can learn from with a tier up to the spellbook's maximum spell tier.  
  
  
* __Spellbooks:__   
  * __Novice Spellbook:__ You are able to learn spells from the Novice Spellbook.  
  * __The Wizard's Addendum:__ You are able to learn spells from the Wizard's Addendum.  
  
  
* __Choices:__   
  * __Spell Choice:__ At the start of your journey, you know 2 extra tier zero spells.  
  
  
* __General Abilities:__   
  * __Tier Zero Spells:__ You have achieved a basic knowledge of the arcane, and may now learn tier zero spells from any of your spellbooks.  
  
  
__Level 1 Wizard__

* __General Abilities:__   
  * __Tier One Spells:__ Your powers are growing. You may now learn tier one spells from any of your spellbooks.  
  
  
* __Advantages:__   
  * __Looming Presence:__ Gain advantage when attempting to intimidate anything of lower intelligence than yourself.  
  
  
__Level 2 Wizard__

* __Choices:__   
  * __Stat Increase:__ You gain two stat points to add to a stat or stats of your choosing.  
  
  
__Level 3 Wizard__

* __Actions:__   
  * __Minor Offhand Spell:__ You may cast a tier zero spell as an offhand action.  
  
  
__Level 4 Wizard__

* __Choices:__   
  * __Stat Increase:__ You gain two stat points to add to a stat or stats of your choosing.  
  
  
* __General Abilities:__   
  * __Tier Two Spells:__ You have graduated from novice to proficient! You may now learn tier two spells from any of your spellbooks.  
  
  
__Level 5 Wizard__

* __Actions:__   
  * __Greater Offhand Spell:__ You may cast a tier one spell as an offhand action.  
  
  
__Level 6 Wizard__

* __Choices:__   
  * __Stat Increase:__ You gain two stat points to add to a stat or stats of your choosing.  
  
  
__Level 7 Wizard__

* __Actions:__   
  * __Offhand Attack:__ You may use an offhand action to make an attack.  
  
  
* __General Abilities:__   
  * __Tier Three Spells:__ Magical energy flows through you. You may now learn tier three spells from any of your spellbooks.  
  
  
* __Combat Abilities:__   
  * __Commit to Memory:__ At the beginning of a day, you may commit one spell to memory of tier 2 or greater. For the remainder of the day, that spell costs 1 fewer action points.  
  
  
__Level 8 Wizard__

* __Choices:__   
  * __Stat Increase:__ You gain two stat points to add to a stat or stats of your choosing.  
  
  
__Level 9 Wizard__

* __Actions:__   
  * __Major Offhand Spell:__ You may cast a tier two spell as an offhand action.  
  
  
__Level 10 Wizard__

* __Choices:__   
  * __Stat Increase:__ You gain two stat points to add to a stat or stats of your choosing.  
  
  
* __General Abilities:__   
  * __Tier Four Spells:__ You are a master of your spellcraft. You can now learn tier four spells from any of your spellbooks.  
  
  
__Level 12 Wizard__

* __Choices:__   
  * __Stat Increase:__ You gain two stat points to add to a stat or stats of your choosing.  
  
  
* __General Abilities:__   
  * __Spell Invention:__ You are advanced enough in magic that you may begin inventing your own spells. To invent a spell, you must have either encountered something like it, or have a jumping off point in your spellbook. It can take long periods of time to craft a spell, and its success and cost will be determined by multiple rolls and saving throws, depending on complexity.  
  
  
__Level 13 Wizard__

* __General Abilities:__   
  * __Tier Five Spells:__ You have achieved the highest form of sorcery, and are a mage to be reckoned with. You can now learn tier five spells from any of your spellbooks.  
  
  
__Level 14 Wizard__

* __Choices:__   
  * __Stat Increase:__ You gain two stat points to add to a stat or stats of your choosing.  
  
  
__Level 15 Wizard__

* __Spellbooks:__   
  * __Tome of the Ancients:__ You are now able to learn spells from the tome of the ancients.  
  
  
  
___

  
## Skills
When you reach an even level, you are presented with a choice. You can either gain
2 stat points to spend, or you can unlock a new skill. These skills are enumerated
in this section. Skills are similar to abilities,
but their affects are generally somewhat more interesting. Using skills, you can break
the mold of your ordinary character by allowing them to do out of the ordinary things.
Many skills have requirements. These are either __stat based__ or __skill based__. 
If a skill has a stat based requirement, you must have a certain value for a stat
before you can learn the skill. If a skill has a skill requirement, you must learn
the required skill or skills first.
* __Cook:__ During a rest, you may cook food which heals 1d6 health.  
* __Master Chef:__ During a rest, you may cook food which heals 2d6 health.  
  * Skill Requirements: _Cook_  
* __Hearty:__ When you level up, you may roll your health dice with advantage.  
* __Hand to Hand Weapon Proficiency:__ You may wield physical weapons without disadvantage.  
* __Ranged Weapon Proficiency:__ You may wield non-firearm ranged weapons without disadvantage  
  * Stat Requirements: _Dexterity: 1_  
* __Firearm Proficiency:__ You may wield firearms without disadvantages  
  * Stat Requirements: _Intelligence: 2, Dexterity: 1_  
* __Basic Magic:__ You may use tier zero magic. Each time you level up, gain a tier zero spell.  
  * Stat Requirements: _Intelligence: 3_  
* __Advanced Magic:__ You may use tier one magic. Each time you level up, gain a tier one spell.  
  * Skill Requirements: _Basic Magic_  
  * Stat Requirements: _Intelligence: 5_  
* __Fast Draw:__ You may add 1d6 to your initiative roll.  
  * Stat Requirements: _Perception: 3_  
* __Tinker:__ You may attempt to make items and contraptions during rests.  
  * Stat Requirements: _Intelligence: 3, Dexterity: 1_  
* __Nimble Navigator:__ Don't take penalty from difficult terrain. Stand up for free after being knocked prone.  
  * Stat Requirements: _Dexterity: 3_  
* __En Garde:__ Reaction. When attacked, decrease the attack damage by your dexterity  
  * Stat Requirements: _Dexterity: 1_  
* __Shrug it Off:__ Reaction. Decrease the attack damage by your strength  
  * Stat Requirements: _Strength: 1_  
* __Leader:__ Give all allies a 1d6 inspiration dice at the start of each battle.  
  * Stat Requirements: _Inner Fire: 3, Charisma: 3_  
* __Mage Hunter:__ Gain advantage on breaking enemy concentration and on SP saves.  
  * Stat Requirements: _Inner Fire: 3_  
* __Minor Movement Distance Increase:__ Move an additional 5 feet per turn.  
  * Stat Requirements: _Dexterity: 2_  
* __Greater Movement Distance Increase:__ Move an additional 5 feet per turn.  
  * Skill Requirements: _Minor Movement Distance Increase_  
  * Stat Requirements: _Dexterity: 4_  
* __Major Movement Distance Increase:__ Move an additional 5 feet per turn.  
  * Skill Requirements: _Greater Movement Distance Increase_  
  * Stat Requirements: _Dexterity: 6_  
* __Lip-Reader:__ You can read the lips of anyone you can see.  
  * Stat Requirements: _Perception: 3_  
* __Insomniac:__ You can gain the benefits of normal sleep for one night without sleeping.  
  * Stat Requirements: _Inner Fire: 2_  
* __Battle Mage:__ Gain advantage on concentration checks. Re-roll 1's made on attack spells.  
* __Ventriloquist:__ You can throw your voice without a skill check.  
* __Fight from the Shadows:__ You are able to attempt to hide as an offhand action.  
  * Stat Requirements: _Dexterity: 3_  
* __Phallanx:__ When you are adjacent to an ally, enemy attacks are at disadvantage.  
* __Medic:__ You can stabilize a teammate as an action, and heal a teammate for 1d6 health for 1 SP.  
* __Greater Medic:__ You are able to heal a teammate for 2d6 health for 1SP.  
  * Skill Requirements: _Medic_  
  * Stat Requirements: _Inner Fire: 2, Dexterity: 1_  
* __Functioning Alcoholic:__ When intoxicated, gain advantage on charisma, strength, inner fire, and luck checks.  
  * Stat Requirements: _Inner Fire: 3_  
* __Sage:__ Re-roll any ones or twos rolled while casting magic.  
  * Stat Requirements: _Intelligence: 5, Inner Fire: 3_  
* __Close Quarters Combat:__ Do not take disadvantage with ranged weapons in close quarters.  
* __Empowered Spells:__ Roll double the damage dice for your tier zero spells.  
  * Stat Requirements: _Intelligence: 3, Inner Fire: 3_  
* __Two Handed Weapon Master:__ Carry two handed weapons with one hand.  
  * Stat Requirements: _Strength: 3, Dexterity: 1_  
* __Master of Concentration:__ Concentrate on two spells at the same time  
  * Stat Requirements: _Inner Fire: 5, Intelligence: 3_  
* __Duelist:__ When fighting an enemy take advantage on attacks if there are no other combatants within 30 feet.  
* __Demolitionist:__ Do double damage with non-spell based explosives.  
* __Controlled Retreat:__ Take half damage when retreating.  
* __Pivot:__ Swap positions with an adjacent teammate.  
* __Contortionist:__ You are able to easily contort your body.  
  * Stat Requirements: _Dexterity: 3_  
* __Tumble:__ Take 20 feet less fall damage.  
* __Fire Bug:__ Roll advantage when attacking with fire.  

  
## Spellbooks
Mage classes are able to harness the arcane or divine arts to cast powerful spells.
Each magic user is granted access to one or more __spellbooks__ from which they are 
able to learn new spells. These spellbooks are enumerated in this section.
For information about when new spells are learned, see the [New Spells](#new-spells)
section. For information on the ```Action Points``` used to cast spells, see the
[Action Points](#action-points) section. 

  
### The Bard's Songbook
  
__Tier 0:__  
* __Carry on the wind:__ _(Cost: 0)_ Point at someone and they hear you regardless of distance.  
* __Conceal Weapon:__ _(Cost: 0)_ Magically conceal up to three weapons on your person.  
* __Control Shadows:__ _(Cost: 0)_ Influence the movement of shadows within thirty yards of yourself.  
* __Cruel Limerick:__ _(Cost: 0)_ Tell a cruel rhyme, imbued with magic. If an entity fails an inner fire saving throw against your spell power, they take disadvantage on their next action.  
* __Folk Tune:__ _(Cost: 0)_ Play an old country classic to gain favor with commoners present, giving you advantage on charisma checks when speaking with them. The song must last at least three minutes.  
* __Forge Writing:__ _(Cost: 0)_ Magically forge the handwriting of anyone you have spoken with.  
* __Hypnotize:__ _(Cost: 0)_ Requires the use of a swinging trinket. Force someone to make an inner fire saving throw against your spell power. On failure, you may influence their actions for up to sixty seconds. The entity may attempt an additional saving throw if asked to do anything that causes themselves or those they love physical harm.  
* __Ode to Country:__ _(Cost: 0)_ Play a country's anthem, Gain favor with soldiers, guards, or kingsmen present, giving you advantage on charisma checks when speaking with them. The song must last at least three minutes.  
* __Steal Voice:__ _(Cost: 0)_ Force an entity to make an inner fire saving throw against your spell power. On failure, they loose their voice. They may attempt another saving throw at disadvantage every turn or once every minute thereafter.  
* __Sweet Nothings:__ _(Cost: 0)_ Force an individual attracted to your sex to make an inner fire saving throw against your spell power. On failure, they find you to be irresistibly attractive, and you gain advantage when persuading them.  
* __Throw Voice:__ _(Cost: 0)_ Magically throw your voice up to fifty feet.  
* __Trick up Your Sleeve:__ _(Cost: 0)_ Summon up to forty feet of tied together cloths from your sleeve.  
* __Harsh Note:__ _(Cost: 0)_ Create a harsh noise which either damages one enemy for 1d6 damage, or everyone who can hear for 1d4.  
  
__Tier 1:__  
* __Belch Fire:__ _(Cost: 1)_ Belch fire onto something for 1d6 damage. If a creature is targeted, they must make an inner fire saving throw against your spell power. On failure, they are burned, and take 1d6 damage at the start of each of their turns until they are healed or two more turns pass.  
* __Blocking Hand:__ _(Cost: 1)_ Reaction. Roll a contested dexterity check against an attacking enemy. If you succeed, reduce the damage they deal to you by your spell power.  
* __Cacophony:__ _(Cost: 1)_ Choose up to five objects that you can see. Those objects make a horrible ruckus until you stop concentrating on them.  
* __Counter Magic:__ _(Cost: 1)_ Reaction. May be cast at a higher tier for an additional cost equal to the tier increase. If the tier of the counter spell is equal to or greater than the opponent's spell, the opponent's spell is instantly dispelled. Otherwise, the casting entity must succeed in an inner fire saving throw against your spell power. If the difference between your counterspell's tier and the enemy's spell's tier is greater than 1, they make the check with advantage.  
* __Courage:__ _(Cost: 1)_ Make your party members immune to fear and give them advantage on inner fire saving throws. Lasts for three turns, or for 1 hour when out of combat.  
* __Create Sound:__ _(Cost: 1)_ Create any sound that you have heard before.  
* __Curse:__ _(Cost: 1)_ Spit a curse at an enemy. The magical vitriol in your voice does 1d8 damage and gives the enemy disadvantage on their next move if they fail an inner fire saving throw against your spell power.  
* __Curse of Crying:__ _(Cost: 1)_ Force an entity to make an inner fire saving throw against your spell power. On failure, they receive a curse which causes them to weep constantly. The curse does not leave until dispelled.  
* __Dazzling Lights:__ _(Cost: 1)_ Summon seven dazzling lights to dance about you. You may magically order them to go anywhere within twenty feet of yourself. The lights follow you for up to one hour. Concentration.  
* __Disarmor:__ _(Cost: 1)_ Force an enemy to make an inner fire saving throw against your spell power. If they fail, remove all armor from an entity for 1d4 turns or 1d20 minutes.  
* __Disguise:__ _(Cost: 1)_ Magically change yourself so that you look like a generic person from the region you are in.  
* __Fatigue:__ _(Cost: 1)_ Force someone to make an inner fire saving throw against your spell power. If you succeed, they become exhausted, and take disadvantage on all relevant checks.  
* __Gnomish Dream:__ _(Cost: 1)_ Gain line of sight on a sleeping entity. Impart upon them any dream that you wish, so long as the characters are all gnomes.  
* __Keen Blade:__ _(Cost: 1)_ Your blade gains an additional 1d6 damage on each attack over the course of one battle or one hour.  
* __Kiss and Tell:__ _(Cost: 1)_ Kiss someone to always know where they are. Know within 10 miles if the kiss is on the hand, within 5 miles if the kiss is on the cheek or forehead, within 100 feet if on the mouth. Lasts for 1 week.  
* __Liar's Tongue:__ _(Cost: 1)_ Force someone to make an inner fire saving throw against your spell power. If they fail, they believe the next thing that you tell them. They may re-evaluate their beliefs when provided with proof of their fallacy.  
* __Liquid Luck:__ _(Cost: 1)_ Cast on an intoxicated entity to give them 1d10 additional luck.  
* __Mark Enemy:__ _(Cost: 1)_ Give teammates advantage when they attack a specific enemy. Lasts 1 turn.  
* __Minor Trickery:__ _(Cost: 1)_ The target must make an inner fire saving throw against your spell power. On failure, convince the entity that it sees something that it does not.  
* __Not So Fast:__ _(Cost: 1)_ Reaction. Force an enemy to remake a roll, or to make a roll with disadvantage.  
* __Project Image:__ _(Cost: 1)_ Project an image of yourself. This image can move, but cannot speak, and lasts at most 1d4 minutes.  
* __Song of Haste:__ _(Cost: 1)_ Allow a teammate an extra action on their next turn and to move at double speed. Lasts for 1 minute when out of battle.  
* __Song of Inspiration:__ _(Cost: 1)_ Play a tune which grants an ally a 1d8 inspiration dice.  
* __Song of Slow:__ _(Cost: 1)_ Force an entity to make an inner fire saving throw against your spell power. If they fail, they are pushed back 1d4 spots in the initiative order.  
* __Song of Slow Healing:__ _(Cost: 1)_ Play a song that heals an entity for 1d4 health each turn for 2 turns.  
  
__Tier 2:__  
* __All the Little Creatures:__ _(Cost: 2)_ Summon a mob of 1d20 squirrels to fight for you. Each squirrel has 1 hp and is capable of doing 1 damage per turn. Squirrels move together in combat, and are attacked as a swarm.  
* __Battle Hymn:__ _(Cost: 2)_ Play a battle hymn which gives all nearby allies 1 additional point on a stat of their choice and a 1d6 inspiration dice. Lasts 1 hour.  
* __Forget:__ _(Cost: 2)_ Force an entity to make an inner fire saving throw against your spell power. On failure, the entity forgets 1d10 minutes of your choosing.  
* __Free Flowing Chalice:__ _(Cost: 2)_ Enchant a cup or vessel and it will flow with wine for up to 6 hours or 100 gallons.  
* __Greater Conceal Weapons:__ _(Cost: 2)_ Magically conceal up to three weapons on each of up to seven individuals.  
* __Invisible Servant:__ _(Cost: 2)_ Summon an invisible servant to aid you in a task. The servant cannot attack and has 20 hit points. Concentration.  
* __Kilgore's Thunderous Shout:__ _(Cost: 2)_ Unleash a mighty bellow against an enemy which does 2d8 damage. The enemy must make a strength check against your spell power or they are thrown backward 15 feet and take an additional 1d8 blunt damage. If they are of size small, they must make the check with disadvantage.  
* __Lullaby:__ _(Cost: 2)_ Sing a song which puts all enemies that can hear it to sleep if they fail an inner fire check against your spell power. Each turn thereafter, they can attempt the same saving throw. If harmed, they wake up.  
* __Magic Steed:__ _(Cost: 2)_ Summon a steed made of pure magical energy. The stallion has 20 health, and may be de-summoned on command.  
* __Marionette:__ _(Cost: 2)_ Force an enemy to make an inner fire saving throw against your spell power. On failure, you may control them as though they are a puppet and you hold their strings. The entity may attempt an inner fire saving throw each turn thereafter to break your control.  
* __Minor Gate:__ _(Cost: 2)_ Create a gate exactly big enough to fit yourself and one other individual of your size. The gate can transport you up to 300 feet.  
* __Raucous Laughter:__ _(Cost: 2)_ Tell a joke so funny that anyone who hears it falls prone if they fail an inner fire check against your spell power.  
* __Sleepwalking Suggestion:__ _(Cost: 2)_ Gain line of sight on a sleeping entity. Whisper up to a 14 word order. The entity must make a disadvantaged inner fire saving throw against your spell power. On failure, the entity will attempt to carry out your order while sleepwalking.  
* __Smokescreen:__ _(Cost: 2)_ Create a smokescreen with a 15 foot radius.  
* __Song of Strength:__ _(Cost: 2)_ Play a tune which gives all nearby allies an additional 1d4 strength. Concentration.  
* __Suggestion:__ _(Cost: 2)_ Force an enemy to make an inner fire saving throw against your spell power. If they fail, they must follow your orders for 1 turn or 5 minutes.  
* __Sweet Dreams:__ _(Cost: 2)_ Shape an entity's dreams. You must be within 100 feet of the entity. Roll a deception check against the entity (they take disadvantage) to see how convincing the false dream is.  
* __Tyrone's Ravenous Hunger:__ _(Cost: 2)_ Cause an entity to become ravenously hungry. If they fail an inner fire saving throw against your spell power, they will attempt to eat the nearest entity to them.  
* __Wall of Sound:__ _(Cost: 2)_ Create a wall up to 40 feet long and 100 feet wide of pure sonic energy. Any entity that attempts to pass through it must make an inner fire saving throw against your spell power or be thrown back and take 2d10 damage.  
  
__Tier 3:__  
* __Animal Form:__ _(Cost: 3)_ Transform yourself into an animal up to large in size. See the book of known beasts for more details.  
* __Conjure Carriage:__ _(Cost: 3)_ Summon a carriage capable of seating four individuals, with a seat for two drivers. The carriage comes with two magical steeds, which may not be detached, and with an optional ethereal driver.  
* __Curse of the Lowlife:__ _(Cost: 3)_ Force an enemy to make an inner fire saving throw against your spell power. On failure, they are cursed so that everyone they have ever met begins to forgets all positive memories associated with them. Within a week, everyone will remember only the negative aspects of the individual. The curse takes effect as soon as the individual leaves someone's presence, and lasts until dispelled.  
* __Ecstasy:__ _(Cost: 3)_ Force an enemy to make an inner fire saving throw against your spell power. On failure, they fall into a fit of overwhelming pleasure, and miss their turn. They may repeat the saving throw on their own turn every turn after the first.  
* __Harbinger of Doom:__ _(Cost: 3)_ Utter a word that hurts all that can hear it for 4d8 damage. Anyone who hears must make an inner fire saving throw against your spell power and moves as far away as possible on failure.  
* __Horace's Wholesome Homestead:__ _(Cost: 3, Charisma Cost: 10)_ Summon a pocket dimension containing a small homestead, capable of housing 6 people comfortably in two shared bedrooms. The homestead is fully stocked with modest food and drink. Only individuals that you want to have access to the homestead may enter it. The homestead lasts 24 hours. Nothing placed in the homestead will stay, and nothing from within may be taken out.  
* __Immovable:__ _(Cost: 3)_ Make an object immovable for 1 minute.  
* __Jerry's Race Dysmorphia:__ _(Cost: 3)_ Transform yourself into another race for 1 hour. You gain the race's stats and abilities, and loose those of your own race.  
* __Little Guardian:__ _(Cost: 3)_ Create a small familiar to aid you. The familiar has 20 health, and can attack for 3d6 damage.  
* __Mass Trickery:__ _(Cost: 3)_ Force everyone within a 100 foot radius to make an inner fire saving throw against your spell power. You can convince those who fail that they see something that is not there.  
* __Matchmaker:__ _(Cost: 3)_ Point at two individuals and speak their names. If they fail an inner fire check against your spell power, they fall madly in love.  
* __Power Shriek:__ _(Cost: 3)_ 4d6 damage to all that hear it. If those who hear it fail an inner fire save against your spell power, they are rendered deaf, and perform all actions with disadvantage for a turn.  
* __Prison of Ice:__ _(Cost: 3)_ Force an enemy to make a dexterity saving throw against your spell power. On failure, they are surrounded by ten foot tall walls of ice, lined with sharpened icicles.  
* __Song of Aging:__ _(Cost: 3)_ Force an enemy to make an inner fire saving throw against your spell power. On failure, the enemy begins aging at a rate of 10 years per turn. You may continue this spell as an offhand action each turn. The aging lasts until it is dispelled.  
* __Song of Healing:__ _(Cost: 3)_ Heal an ally for 5d6 health.  
* __Song of Rage:__ _(Cost: 3)_ Play a song which sends one of your teammates into a rage. See the barbarian's 'Berserk' ability for details on the affects.  
* __Unstoppable:__ _(Cost: 3)_ Make an object unstoppable for 1 minute.  
  
__Tier 4:__  
* __Ash Storm:__ _(Cost: 4)_ Summon a massive storm of ash 100 yards in diameter. All entities within are considered to be in low visibility. Any entity within the ash storm must make an inner fire saving throw against your spell power each turn to avoid choking on ash.  
* __Get Me Out of Here:__ _(Cost: 3)_ Teleport to a random place in the world that is at least 5 miles from your current position.  
* __Lightning Strike:__ _(Cost: 4)_ Call down a blast of lightning on an enemy. Does 5d8 damage.  
* __Mass Suggestion:__ _(Cost: 4)_ Force all enemies in earshot to make an inner fire saving throw against your spell power. If they fail, they must follow your orders for 3 turns or 5 minutes.  
* __Song of Dancing:__ _(Cost: 4)_ Play a song which is so catchy, all those who hear are forced to dance if they fail an inner fire saving throw against your spell power. While dancing, an entity may make no other action on its turn. An affected entity may repeat the save each turn.  
* __Strike Dumb:__ _(Cost: 4)_ An entity must perform an inner fire check against your spell power. If they fail, their intelligence is treated as -5. They lose the ability to speak, read, and otherwise communicate outside of grunts. This lasts until dispelled.  
* __Summon Ronin:__ _(Cost: 3)_ Summon knight of your level to fight for you. Lasts for one hour.  
* __Zone of Truth:__ _(Cost: 4)_ Create a zone with a 15 foot radius in which all must speak truthfully.  
  
__Tier 5:__  
* __Dominate Person:__ _(Cost: 5)_ An entity must perform an inner fire check against your spell power. If they fail, they are dominated until dispelled, and must do as you command.  
* __Edmire's Grand Manor:__ _(Cost: 2)_ Summon a pocket dimension containing a huge mansion, capable of housing up to 80 people comfortably, in up to 20 bedrooms. The mansion is fully stocked with extravagant food and drink. The mansion is manned by 100 servants, which are at the beck and call of the mansions creator. Upon learning this spell, the bard may design the mansion to have rooms that suit the needs of their party (e.g. a holy sanctum, dungeons, training grounds, a kitchen, etc.). Only individuals that you want to have access to the mansion may enter it. The mansion lasts 24 hours. Nothing that originated within the mansion may be taken out. However, items brought in may stay.  
* __Guards:__ _(Cost: 5)_ Summon 1d4 ethereal guardians to aid you. The guardians remain for 12 hours. They each have 50 health, and do 3d8 + 8 damage per attack.  
* __Manifest Will:__ _(Cost: 4)_ Say two words. The thing that you ask for appears.  
* __Mass Song of Healing:__ _(Cost: 5)_ Heal all allies in earshot for 4d10 health.  
* __Rewrite History:__ _(Cost: 5)_ Cast on everyone in earshot you wish. If they fail an inner fire saving throw against your inner fire, re-write up to one hour of their memory.  
* __Torugar, the Many Tongued Demon:__ _(Cost: 5)_ Summon a pit, housing an ancient, many tongued god of the underworld. Every turn for 5 turns, 1d6 tongues will writhe forth from the pit, and attempt to grab individuals within 1000 feet. If an individual is grabbed (fails a dexterity check against your spell power) it sustains 4d8 damage. If the blow kills the creature, it is ripped down into the pit, and is irrecoverable.  
* __Winged Magic Steed:__ _(Cost: 2)_ Summon a steed made of pure magical energy. The stallion has 20 health, and may be de-summoned on command.  

  
### The Book Of Chi
  
__Basic Techniques:__  
* __Brawler:__ Your hands are d6 weapons.  
* __Catch Projectile:__ Once per turn, attempt to catch a projectile. Roll a d20, and reduce the projectile's damage by that amount. If reduced to zero, you catch the projectile.  
* __Combo:__ You may make an unarmed attack as an offhand action.  
* __Disarm:__ _(Cost: 1)_ Attack with a single punch. If the opponent fails a strength saving throw against your spell power, they drop their weapon.  
* __Disengage:__ Enemies take disadvantage when striking you while you are moving, and may not make attacks of opportunity against you.  
* __Dodge:__ _(Cost: 1)_ Roll a contested dexterity check to attempt to dodge an opponent's attack.  
* __Find Balance:__ Use a bonus action to cleanse yourself of poison or other status effects.  
* __Grapple:__ You have advantage when grappling.  
* __Icy Kick:__ _(Cost: 1)_ Add an additional 1d6 cold damage to a kicking attack.  
* __Leap to your feet:__ Get to your feet without penalty.  
* __Sharpen blade:__ _(Cost: 1)_ Hone your physical weapon to give it an additional 1d4 blunt or slashing damage for the duration of a battle.  
* __Strike from on High:__ You do an additional 1d6 blunt damage on any plunging attack.  
* __Stunning Blow:__ _(Cost: 1)_ Attack with a single punch. If the target fails an inner fire save, they are stunned, and miss their next turn.  
* __Sweep the Leg:__ Attack with a single kick. If the target fails a dexterity save, they are knocked prone.  
* __Aerial Acrobatics:__ You can turn flips and spin in the air. If your feet touch something solid, you can spring from it.  
* __Balance:__ You have impeccable balance. You have advantage on any saving throws where you could be knocked prone.  
* __Calligraphy:__ Gain advantage on any fine motor skill dexterity checks.  
* __Escape:__ You have advantage on any checks involving breaking physical restraints.  
* __Inner Eye:__ You have advantage when detecting evil, good, or spiritual energy.  
* __Listen:__ You have advantage on perception checks.  
* __Mantle:__ You are able to mantle across objects. You have advantage on dexterity checks when climbing or leaping.  
* __Meditate:__ Gain an additional 1d6 health from any rest.  
* __Meld into Shadow:__ Take advantage on stealth checks when hiding in shadows.  
* __Minor Heal:__ _(Cost: 1)_ Heal yourself or another for 1d6 + inner fire damage.  
* __Run on water:__ Get a running start to run up to 50 feet on water.  
* __Silent:__ You have advantage on stealth checks.  
* __Tumble:__ You take half fall damage.  
  
__Master Techniques:__  
* __Aura of Calm:__ Allies near you gain +1 on all inner fire saving throws and checks against an enemy's spell power.  
* __Darkness:__ _(Cost: 2)_ Create a veil of darkness with a 50 foot radius which lasts for 1d4 + 1 turns. All entities within the shadow must make perception checks before attacking, and then must attack with disadvantage. You are not affected by the darkness.  
* __Fists of Steel:__ Your bare hands are d10 weapons.  
* __Flaming Fist:__ _(Cost: 1)_ Add an additional 1d12 fire damage to a punching attack.  
* __Hearty:__ Increase the size of your health dice by 1.  
* __Major Heal:__ _(Cost: 2)_ Heal yourself or an ally for 2d12 + inner fire health.  
* __Master of Body and Soul:__ Once per day, when you reach 0 health, drop to 2d20 health instead.  
* __Opening Blow:__ If you strike an opponent before it is able to move in combat, take advantage on all subsequent attacks against that foe so long as you continue attacking it with each of your actions. Add an additional 1d12 blunt damage to the initial strike.  
* __Perfect Zen:__ _(Cost: 1)_ As an offhand action, become untouchable by physical attacks for one turn or one minute.  
* __Press the Advantage:__ On a critical hit, gain another attack.  
* __Redirect Attack:__ Reaction. Once per turn, select an enemy attack aimed at you. Make a contested dexterity check. If you succeed, redirect the attack anywhere you wish.  
* __Second Action:__ Take two actions on your turn.  
* __Shadow Step:__ _(Cost: 1)_ Step from any point in darkness to any other point in darkness within 50 feet.  
* __Share Ability:__ Every day, share in a teammates ability for the day.  
* __Surrounded:__ Strike up to 5 foes in one action if you are surrounded.  
* __Thunderous Punch:__ _(Cost: 1)_ Your attack may make a thunder wave, which affects all enemies in front of you with the punch's damage. This ability can be stacked on top of any other punching attack.  
  
__Legendary Techniques:__  
* __Consecutive Normal Punches:__ _(Cost: 2)_ Take two attacks with each of your actions and offhand actions.  
* __Pressure Points:__ Whenever you attack an enemy, force them to make a spell power save. On failure, they fall instantly limp, and are stunned until they succeed.  
* __Consuming Blow:__ _(Cost: 2)_ When you attack an enemy, force them to make a spell power save. On failure, shadows fly forth from you at the point of contact, tearing at the flesh of your opponent. The opponent takes 4d10 damage as a result.  
* __Ultimate Punch:__ _(Cost: 2)_ As an action, channel the energy of your ancestors into a perfectly tuned punch. With a thunderclap, unleash a blow capable of destroying buildings with its shock-wave. Immediately take 4d10 + 20 damage, but deal 5d20 + 20 damage to all entities in a 100 foot cone in front of you.  
* __Perfect Understanding:__ Spend one full turn analyzing an enemy. On every attack made against it thereafter, you have advantage.  
* __Everywhere and Nowhere:__ _(Cost: 1)_ Instead of taking movement during combat, instantly teleport from one location to another within thirty feet of you. If you do not attack on your turn, you may choose to be ethereal until your next turn, and therefore to be immune to physical damage.  

  
### The Book Of Healing
  
__Tier 0:__  
* __Beguile:__ _(Cost: 0)_ Your holy presence shakes an enemy's constitution. Force them to make a spell power save. On failure, the entity does 1d4 fewer damage on all attacks it makes on its next turn.  
* __Bless Water:__ _(Cost: 1)_ You may bless water by praying over it, converting it to holy water. This can be done at a rate of one gallon per hour.  
* __Beam of Light:__ _(Cost: 0)_ Fire a bolt of radiant energy at an enemy, dealing 1d4 damage, or 1d6 damage if the enemy is undead.  
* __Detect Evil:__ _(Cost: 0)_ Make a perception check to detect if an evil entity is within 50 feet of you.  
* __Detect Magic:__ _(Cost: 0)_ Make a perception check to detect magic within 30 feet of you.  
* __Fake Death:__ _(Cost: 0)_ Touch a willing entity to send them into a catatonic state that is impossible to distinguish from death.  
* __Give of Yourself:__ _(Cost: 0)_ Give a teammate up to 20 points of your own health per turn.  
* __Guidance:__ _(Cost: 0)_ Give an ally a 1d4 inspiration dice as an offhand action.  
* __Extra Weight:__ _(Cost: 0)_ Double the weight of an object. The object must be no larger than a horse.  
* __Holy Orders:__ _(Cost: 0)_ As an offhand action, mark an enemy as a target for your group. Anyone who damages the target regains 1d4 health. Anyone who kills the target regains 1d6 health. You can mark at most one enemy at a time.  
* __Lighten Object:__ _(Cost: 0)_ Decrease the weight of an object by half. The object must be no larger than a horse.  
* __Mending:__ _(Cost: 0)_ You can magically mend small dents, dings, scratches, and tears in items.  
* __Purify:__ _(Cost: 0)_ Purify a food, drink, or potion to remove ill effects. Purify can be used to remove drunkenness from entities, or to render poison innocuous.  
* __Sacred Flame:__ _(Cost: 0)_ As an offhand action, summon a sacred flame to your hand. Ash created by the flame is considered sacred. The flame does 1d6 damage if it touches someone, and an additional 1d6 damage to corrupted entities or the undead.  
* __Spare:__ _(Cost: 0)_ Offhand. Touch an ally that is on death's door to stabilize them. Stabilized entities immediately return to 0 health. The are still unconcious, but no longer need to make death coin flips.  
* __The Face of Good:__ _(Cost: 0)_ Once per rest, the light of your deity shines from you. For five minutes, you gain advantage on charisma checks, and advantage on intimidation checks when attempting to intimidate evil enemies.  
* __Minor Heal:__ _(Cost: 1)_ Restore 2d4 health to one ally or yourself.  
  
__Tier 1:__  
* __Augment Allied Attack:__ _(Cost: 1)_ Reaction. When one of your allies attacks, you may add 1d6+your inner fire to their damage.  
* __Bulk Up:__ _(Cost: 1)_ Force an entity to make an inner fire saving throw against your spell power. On failure, the entity gains their weight in body fat.  
* __Delayed Heal:__ _(Cost: 1)_ Cast a healing spell on a teammate which does not take effect until you trigger it as a reaction or bonus action. At that time, they are healed for 1d6 health.  
* __Forget Ability:__ _(Cost: 1)_ Concentration. Force an entity to make an inner fire saving throw against your spell power. On failure, you may force the entity to forget one of it's combat or physical abilities. The entity may repeat the check with disadvantage every turn thereafter.  
* __Giant's Strength:__ _(Cost: 1)_ Grant a teammate one additional effective strength. Lasts a number of hours equal to your inner fire.  
* __Greater Guidance:__ _(Cost: 1)_ Give an ally a 1d8 inspiration dice.  
* __Haste:__ _(Cost: 1)_ Cast a spell which invigorates an ally, allowing them to take an extra action on their turn.  
* __Heighten Emotions:__ _(Cost: 0)_ Force an entity to make an inner fire saving throw against your spell power. On failure, the affected entity's emotions are amplified to the extreme. This may cause them to act recklessly or to take actions with disadvantage.  
* __Hold Weapon:__ _(Cost: 1)_ Concentration. Bind an enemy's weapon to their body. The enemy may attempt a strength check against your spell power to remove it.  
* __Hound's Resolve:__ _(Cost: 1)_ Grant a teammate one additional effective inner fire. Lasts a number of hours equal to your spell power.  
* __Light:__ _(Cost: 1)_ Summon a light with a 10ft radius. Evil and undead entities within the light take 1d6 damage every turn that they are in it. Concentration.  
* __Line in the Sand:__ _(Cost: 1)_ Draw a line in the sand. If an enemy crosses, you and a chosen ally have advantage when attacking them.  
* __Minor Dispel Magic:__ _(Cost: 1)_ Undo the effects wrought by up to a 2nd tier spell.  
* __Minor Holy weapon:__ _(Cost: 1)_ Imbue your weapon with the spirit of righteousness. Your weapon gets +2 damage for a day, and advantage against evil and undead entities.  
* __Monkey's Dexterity:__ _(Cost: 1)_ Grant a teammate one additional effective dexterity. Lasts a number of hours equal to your inner fire.  
* __Omen:__ _(Cost: 0)_ Once per day, ask your deity for an omen in regards to a decision you will make.  
* __Pacify:__ _(Cost: 1)_ If an enemy fails a saving throw against your spell power, it becomes passive and calm. A pacified enemy cannot attack. The entity may make a saving throw every turn thereafter. This effect ends if they entity is attacked.  
* __Share Sense:__ _(Cost: 0)_ Concentration. Touch a teammate. For the duration of the spell, you are able to share their senses.  
* __Shield of Light:__ _(Cost: 1)_ Reaction. Make a contested dexterity check against an attacking opponent. On success, block the enemy attack. You may increase the cost of this spell by 1 to give yourself advantage on the check.  
* __Slow:__ _(Cost: 1)_ Force an entity to make an inner fire saving throw against your spell power. If they fail, they are pushed back 1d4 spots in the initiative order.  
* __Slow Heal:__ _(Cost: 1)_ Cast a healing spell upon an ally that restores 1d6 health to them per turn. Lasts 2 turns.  
* __Strong Lungs:__ _(Cost: 1)_ Grant a teammate or yourself strong lungs, rendering them immune to airborne toxins and smoke.  
* __Truth:__ _(Cost: 1)_ If an entity fails a saving throw against your spell power, force it to speak only the truth for one hour.  
* __Ward:__ _(Cost: 1)_ Touch a teammate and place a ward on them. This ward adds 2 armor and magic armor to the touched party member the next 3 times they are successfully attacked.  
* __Warmth/Cool:__ _(Cost: 1)_ Warm or cool an area with a 10ft radius.  
* __Water Breathing:__ _(Cost: 1)_ Grant a teammate or yourself the ability to breathe underwater. Lasts 1+inner fire hours.  
  
__Tier 2:__  
* __Babel:__ _(Cost: 1)_ If an enemy of your choice fails a saving throw against your spell power, it becomes agitated and angry, but is incapable of meaningful communication for 1 hour.  
* __Blind:__ _(Cost: 2)_ Force an enemy to make an inner fire saving throw against your spell power. On failure, the entity is struck blind, and must make all checks with disadvantage unless it has darkvision or equivalent. The spell lasts until it is dispelled.  
* __Chains of Light:__ _(Cost: 2)_ Force an entity to make an inner fire saving throw against your spell power. On failure, the entity is restrained by chains of burning light which wrap about its limbs and suspend it. The entity may not move on it's turn, but may attempt strength saving throws against your spell power with any of its actions. If the entity is corrupt or undead, it takes 1d10 damage each turn while restrained.  
* __Detect Life:__ _(Cost: 1)_ Make a check to see if you can detect life nearby. You may also check to see whether you can detect a particular entity or entity type nearby.  
* __Greater Heal:__ _(Cost: 2)_ Restore 2d8 health to one teammate or yourself.  
* __Greater Ward:__ _(Cost: 2)_ Touch a teammate and place a ward on them. This ward adds 4 armor and magic armor to the touched party member the next 3 times they are successfully attacked.  
* __Purge Decay:__ _(Cost: 2)_ Create an aura of positive energy with a 10 foot radius around yourself. Undead or evil entities that enter the area take 2d10 damage per turn.  
* __Radiant Light:__ _(Cost: 2)_ Create a beacon of holy light. Enemies who gaze into it must make a saving throw against your spell power. Upon failure, they are blinded for 3 turns, and are knocked prone. Undead and evil enemies have disadvantage. The beacon stays at your side for 1 battle or 1 hour unless dispelled.  
* __Remove Curse:__ _(Cost: 2)_ Remove a curse or dispel a negative enchantment on an individual. Requires an inner fire check, and may be repeated daily.  
* __Speak Tongues:__ _(Cost: 2)_ Your deity touches your tongue to allow you to communicate its word to others. You are able to speak any language for 1 hour.  
* __Wall of Light:__ _(Cost: 2)_ Create a wall up to 40 feet high and 100 feet long of solid light.  
* __Ward of Light:__ _(Cost: 2)_ Etch a glyph into the ground which makes a 20ft radius around it undetectable to evil eyes.  
* __Greater Mending:__ _(Cost: 2)_ Instantly repair up to a moderately sized or broken object such as a wagon wheel or broken sword.  
* __Greater Purify:__ _(Cost: 2)_ Purify all food, drink, or potions in a 100 foot area to remove ill effects. Greater purify can be used to remove drunkenness from entities, to render poison innocuous, or to make spoiled food fresh again.  
  
__Tier 3:__  
* __Greater Delayed Heal:__ _(Cost: 2)_ Cast a healing spell on a teammate which does not take effect until you trigger it as a reaction or bonus action. At that time, they are healed for 2d8 health.  
* __Death Ward:__ _(Cost: 1)_ Cast a powerful ward on an ally. If they are downed in combat, they immediately return to 1d20 hp.  
* __Greater Dispel Magic:__ _(Cost: 3)_ Undo the effects wrought by up to a 4th tier spell.  
* __Major Guidance:__ _(Cost: 1)_ Give an ally a 1d12 inspiration dice.  
* __Major Heal:__ _(Cost: 3)_ Restore 6d10 health to one teammate or yourself  
* __Major Ward:__ _(Cost: 3)_ Touch a teammate and place a ward on them. This ward adds 10 armor and magic armor to the touched party member the next 3 times they are successfully attacked.  
* __Mass Heal:__ _(Cost: 3)_ Restore 3d6 health to all allies in a 30ft radius.  
* __Mass Strong Lungs:__ _(Cost: 3)_ Grant a teammate or yourself strong lungs, rendering them immune to airborne toxins and smoke.  
  
__Tier 4:__  
* __Major Mending:__ _(Cost: 3)_ Spend 1 minute to repair everything you choose within a 1000 foot radius. This can include large objects such as castle walls, fallen pillars, and destroyed property.  
* __Hold Your Weapons:__ _(Cost: 3)_ Concentration. Bind an up to 10 enemies' weapons to their body. Each enemy may attempt a strength check against your spell power to remove it.  
* __Major Holy weapon:__ _(Cost: 3)_ Imbue a weapon with the spirit of righteousness. Your weapon gets +6 damage for a day, and advantage against evil and undead entities.  
* __Major Mass Heal:__ _(Cost: 3)_ Restore 5d10 health to all allies in a 30ft radius.  
* __Sealed Promise:__ _(Cost: 1)_ The cost for this spell is one action point. Requires a piece of white rope and one ounce of holy water blessed by your deity. Have two individuals wash their hands using the holy water, then tie their clasped hands together. Any promise they make in this state must be kept, or the one who does not follow through will die. If the promise becomes impossible, you may render the promise invalid. If you do this in an evil manner, your deity will punish you.  
  
__Tier 5:__  
* __Battle Angel:__ _(Cost: 3)_ Summon a holy great weapon of your choice to your hand, and a shield to your other. The weapon does 1d20 damage plus 3d10 radiant damage, and the shield allows you to perform the shield bash ability as a bonus action. While you are in the battle angel state, you may perform spells at -1 cost, have +3 strength, and have 50 hit points. When the 50 hit points drop to zero, you fall out of the battle angel state, and gain your previous hit points.  
* __Cleanse with Fire:__ _(Cost: 5)_ Tongues of white flame spiral around you, enveloping any enemies within a twenty foot radius. Evil or undead enemies take 5d20 damage, other enemies take 5d10.  
* __Divine Intervention:__ _(Cost: 0)_ Roll 1d20. On a critical success, call upon your deity and ask of them a favor. Can be attempted once per day. Success can happen at most once per week.  
* __Hallowed Ground:__ _(Cost: 5)_ Requires holy water, blessed by your deity, charcoal created by a holy flame, and at least 3 diamonds worth 1000 gold each. Arrange the diamonds in a ring, spaced no more than 20 feet apart. Connect them with a trail of holy water, and etch the sigil of your deity into the rings center. After one hour of prayer, it becomes impossible for any entity to be injured within the ring. Lasts for one week. The diamonds are destroyed at the spell's end.  
* __Holy Avatar:__ _(Cost: 3)_ Summon a radiant projection of yourself within 15 feet of an ally, regardless of where they are in the world. The projection has your stats, and you may share its senses. The projection may attack, cast spells, and perform any of your abilities, but can not be healed. You may not act in any way while controlling the projection, and loose track of your surroundings.  
* __Resurrection:__ _(Cost: 5)_ Requires holy water, holy oil (optional), and a sacred flame. Takes six hours to cast. If an individual has suffered an incurable injury or has died, wash them in holy water and and oil. Burn wood using your sacred flame, and draw the mark of your deity on their brow. After six hours of prayer, make an inner fire saving throw. If holy oil was used, you have advantage. If the roll is 15 or higher, the entity is resurrected.  

  
### The Druid's Guidebook
  
__Tier 0:__  
* __Catseye:__ _(Cost: 0)_ Change your eyes to those of a cat, giving yourself low light vision for one hour.  
* __Claws:__ _(Cost: 0)_ Grow claws from your fingers capable of dealing 1d6 damage.  
* __Cold Resistance:__ _(Cost: 0)_ Resist cold. You take 1d4 fewer damage from cold or frost based attacks. Passive. You may have at most one passive resistance active at a time. You may apply a passive resistance as an offhand action.  
* __Control Plant Growth:__ _(Cost: 0)_ Quickly grow a plant up to the size of a hedge in about 5 minutes or 1 turn in combat.  
* __Crown of Fireflies:__ _(Cost: 0)_ Summon a crown of fireflies to dance around your head, casting candlelight around you. You may command the fireflies up to a distance of 100 feet.  
* __Echolocate:__ _(Cost: 0)_ Let out an inaudible sonic pulse, which allows you to gain a picture of a room as a perception check, even if it is completely dark.  
* __Fire Resistance:__ _(Cost: 0)_ Resist fire damage. You take 1d4 fewer damage from fire based attacks. Passive. You may have at most one passive resistance active at a time. You may apply a passive resistance as an offhand action.  
* __Forest Sense:__ _(Cost: 0)_ Perform perception checks using the natural world around you. Take advantage on perception checks made using living natural entities to aid you.  
* __Lightning Resistance:__ _(Cost: 0)_ Resist electricity. You take 1d4 fewer damage from lightning based attacks. Passive. You may have at most one passive resistance active at a time. You may apply a passive resistance as an offhand action.  
* __Mend:__ _(Cost: 0)_ Instantly mend a broken item or object. You must have most of the pieces and the object must not be too complicated. Make an intelligence check if repairing a complex object.  
* __Spider Web:__ _(Cost: 0)_ Create incredibly sticky spiderweb, capable of holding a person. You are able to create it at the rate of five cubic feet per five minute span, or one five foot cube per action.  
* __Walk on Water:__ _(Cost: 0)_ Walk atop the water. Concentration.  
* __Constricting Vine:__ _(Cost: 1)_ A vine bursts from the ground at an enemies feet dealing 1d4 damage. On a failed dex save against your inner fire, the enemy is held in place until it hacks the vines away or succeeds at the save.  
* __Hurl Stone:__ _(Cost: 1)_ Magically hurl a stone at an enemy for 1d6 damage.  
  
__Tier 1:__  
* __Bark Armor:__ _(Cost: 1)_ Add 1d4 armor to an individual. The armor breaks after they take 3 hits. Bark armor breaks instantly if attacked by fire.  
* __Become Flame:__ _(Cost: 1)_ Become wreathed in fire for 1d20 seconds or two turns. During that time you are immune to fire or heat based damage, and anything that you touch is set aflame. Flaming entities take 1d4 damage per turn until they are extinguished as a bonus action. Your belongings disappear and are undamaged.  
* __Cloud of Fog:__ _(Cost: 1)_ Create a heavy fog on a position that you can see. The fog may have a radius of up to 50 feet. Entities in the fog make relevant checks with disadvantage.  
* __Commanding Presence:__ _(Cost: 1)_ Steel yourself and cast a magical aura which grants nearby allies an additional 1d4 inner fire. Concentration.  
* __Commune with Nature:__ _(Cost: 1)_ Speak in the language of plants or animals for 3d20 minutes.  
* __Fool the Senses:__ _(Cost: 1)_ Force an enemy to make an inner fire saving throw against your spell power. On failure, convince them that they see, hear, or smell something that they do not.  
* __Moonlight:__ _(Cost: 1)_ Summon moonlight and attach it to an object or person. The light lasts one hour past when you break concentration on it, and is bright enough to allow you to see 50 feet.  
* __Poison Jet:__ _(Cost: 1)_ Hit an enemy with a blast of liquid poison, dealing 1d6 damage. Further, force them to make an inner fire saving throw against your spell power. On failure, they are poisoned, and take an additional 1d4 damage each turn for 3 turns.  
* __Purify:__ _(Cost: 1)_ Remove poison from an item or person.  
* __Tailwind:__ _(Cost: 1)_ Summon a tailwind or current behind you.  
* __Thorned Caltrops:__ _(Cost: 1)_ Cast thorn based spikes onto the ground. Anyone moving across them will move at half speed and take 1d4 damage per step. The caltrops cover 10 square feet.  
* __Transmute Weapon:__ _(Cost: 1)_ Magically alter a weapon so that its damage scales with inner fire rather than dexterity or strength. Lasts for one day.  
* __Swarm of Eagles:__ _(Cost: 1)_ Summon a swarm of eagles which attacks an enemy for 1d6 damage each turn for two turns.  
* __Elemental Beam:__ _(Cost: 1)_ Hurl forth a jet of an element of your choice, dealing 1d8 damage. On a critical hit, the enemy is affected by the element.  
  
__Tier 2:__  
* __Charm Animal:__ _(Cost: 2)_ Charm an animal or beast to make it your friend. The animal must roll an inner fire saving throw against your spell power. On failure, the animal regards you as friendly, and a member of its pack.  
* __Control Water, Wind, or Fire:__ _(Cost: 2)_ Choose an element from Earth, Wind, or Fire. Gain some control over this element. Attacks made with the element do 1d10 damage. You can move at most 100 pounds of water at a time, blow wind hard enough to give an entity disadvantage, or control a sphere with up to a 10 foot radius of fire. Concentration.  
* __Elemental Weapon:__ _(Cost: 2)_ Imbue a weapon with 1 battle's worth of elemental damage. Every blow with the weapon does an additional 1d6 elemental damage of the element of your choosing.  
* __Freezing Rain:__ _(Cost: 2)_ Make terrain difficult by causing a freezing rain to fall over it. Entities moving across the terrain must make a dexterity check against your spell power. On failure, they fall prone.  
* __Geyser:__ _(Cost: 2)_ Create a geyser with a 3 foot radius which fires water 40 feet directly upward into the air. The geyser may be created at a range of up to 100 feet from the caster.  
* __Hurl Boulder:__ _(Cost: 2)_ Hurl a boulder at an enemy. They may make an inner fire saving throw against your spell power. On failure, they take 2d8 damage, on success, they take 1d8.  
* __Remove Curse:__ _(Cost: 2)_ Remove a curse or dispel a negative enchantment on an individual. Requires an inner fire check, and may be repeated daily.  
* __Scorpions:__ _(Cost: 2)_ Create a 5 cubic foot block of scorpions. Scorpion stings do 1d4 poison damage. The block of scorpions has 10 + inner fire hit points and makes a number of attacks equal to its hit points each turn.  
* __Shape Earth:__ _(Cost: 2)_ Move up to 15 cubic feet of earth.  
* __Snowblind:__ _(Cost: 2)_ Summon a localized snowstorm with a 1 mile radius. The snows are incredibly heavy, and are considered low light.  
* __Spores:__ _(Cost: 2)_ Release poison spores into a 30 foot radius. Anyone who inhales them must take 1d6 damage and make an inner fire saving throw against your spell power. On failure, they are poisoned, and take an additional 1d6 damage each turn for 3 turns.  
* __Thieve's Curse:__ _(Cost: 1)_ Force an entity to make an inner fire saving throw against your spell power. On failure, they are cursed so that they have an irresistible urge to steal something once per hour. They then forget their acts of thievery, and stow the stolen goods in their quarters or a private place. The curse remains until it is dispelled.  
* __Wall of ice:__ _(Cost: 2)_ Create a wall up to 40 feet high and 100 feet long of solid ice.  
  
__Tier 3:__  
* __Animal Form:__ _(Cost: 3)_ Transform yourself into an adult sized animal. See the book of known beasts for more details.  
* __Forest Guardians:__ _(Cost: 3)_ Summon an adult animal to aid you in battle.  
* __Greater Control Plant Growth:__ _(Cost: 3)_ Quickly grow a plant up to the size of a tree in about 30 seconds. The spell lasts for as long as you concentrate on it, allowing you to grow up to 120 trees per hour. After the first hour, begin making inner fire saving throws to see if you are too exhausted to continue.  
* __Heart Fruit:__ _(Cost: 2)_ Grow a heart fruit, capable of healing an entity 2d8 damage. Heart fruit keep for up to one day.  
* __Hurricane Force Winds:__ _(Cost: 3)_ Summon hurricane force winds with up to a 30 foot vertical diameter. Any entity that passes through the winds must make a strength check against your spell power to make any headway, and then must move at half speed. Creatures of size large or greater may make the check with advantage.  
* __Resist an element:__ _(Cost: 3)_ Select an element. An entity of your choice takes half damage from that element. Lasts 1 hour.  
* __Wall of Brambles:__ _(Cost: 3)_ Create up to a 100 foot long wall of bramble bushes. Moving through them requires 3 dexterity checks against your spell power, each of which results in 1d10 damage on failure. If a check is failed, the entity is stuck in the brambles until its next turn.  
  
__Tier 4:__  
* __Criminals:__ _(Cost: 4)_ Cast a mass curse on up to 100 people that you can see. All individuals who fail an inner fire saving throw against your spell power are gripped with the irresistible urge to steal anything that isn't boarded down. Lasts 1d12 hours.  
* __Plant Golems:__ _(Cost: 4)_ Summon 2 plant golems to your aid. The golems have 40 health, attack twice, and do 1d8 damage per attack. Each golem has 5 action points, and is capable of casting twisting vine, bark armor, and thorned caltrops.  
* __Resist the elements:__ _(Cost: 4)_ An entity of your choice takes half damage from all elemental attacks. Lasts 12 hours.  
* __Thunder Cloud:__ _(Cost: 4)_ Create a thunder cloud which lasts for 3 turns. Each turn, the thundercloud may summon a two lightning strikes which deal 2d10 damage to an entity of your choice.  
* __Tornado:__ _(Cost: 4)_ Trap an entity of your choice in a swirling whirlwind. The entity may make a dexterity check against your spell power each turn to attempt to escape. If the entity escapes, it slams to the ground, causing fall damage.  
* __Wildfire:__ _(Cost: 4)_ Create a swirling inferno of fire. Fills a 20x20 foot space. The flames do 4d8 damage to all inside of them. Concentration.  
* __Wings:__ _(Cost: 3)_ Summon an eagles wings to your back, giving you the ability to fly for 1d6 hours.  
  
__Tier 5:__  
* __Awaken Animal:__ _(Cost: 5)_ Give an animal sentience. If you wish, is bound to you for one month, and must follow you. Regardless of type, the animal immediately gains the ability to speak the common tongue.  
* __Bountiful Harvest:__ _(Cost: 5)_ Grow a feast. Up to 8 entities may partake of the feast. Each of these entities fully heal, and gain 1d8 + 4 additional hit points for the next 24 hours.  
* __Control Weather:__ _(Cost: 5)_ Cast a ritual spell which changes the weather in a region. Further, control that weather to accomplish specific tasks. Concentration. Weather does not change back when concentration is broken.  
* __Fix Season:__ _(Cost: 7)_ Find the highest point in a region. Atop this point, create a pillar of rock, at least ten feet tall and with a three foot radius. Spend some time carving symbols significant to you into the stones. Affix crystals valuing 250 gold to the top of the spire, and channel your energy into it. After 1 hour, the crystals begin to glow, and an area of up to 50 miles will be stuck in the season of your choice.  
* __Starfall:__ _(Cost: 4)_ Spend one full round of combat focusing on bringing down a massive meteor. If you are attacked, make a concentration check. On failure, you loose control of the spell at no action point penalty. On success, call down a meteor which strikes all enemies in a 10 foot radius for 10d10 damage.  
* __Tsunami:__ _(Cost: 4)_ Summon a massive tidal wave to crash down on the battlefield originating from the focus point for your magic. The tidal wave does 4d10 damage to all enemies in a cone in front of you. All affected entities must make a strength saving throw against your spell power, or be swept away by the tsunami. Large or greater entities may make the check with advantage. Entities that are swept away move until they hit something solid or have moved 50 feet. When they stop, they take 2d8 damage. After the tsunami has swept across the battlefield, the battlefield has 2 feet of water on it, and all movement must be taken at half speed.  
* __Volcano:__ _(Cost: 5)_ Call forth a volcano with a caldera with a 10 foot radius at a point within 50 feet of yourself. Lava bubbles forth, spewing onto the battlefield. All standing where the volcano appears must make a dexterity saving throw against your spell power. On a failure, they are partially submerged in lava, and take 4d8 fire damage. On a critical failure, they are fully submerged, and take 10d10 damage. Each turn, the volcano spews lava. All creatures on the battlefield must make a dexterity check against your spell power. On failure they take 4d8 fire damage. The volcano lasts until it is dispelled.  
* __Winter's Fury:__ _(Cost: 5)_ Call a massive blizzard. All entities within the blizzard take 4d6 damage per turn, have disadvantage in all things, and are considered to be low light. Concentration.  

  
### The Macabre Manual
  
__Tier 0:__  
* __Detect Death:__ _(Cost: 0)_ You may make perception checks to detect nearby corpses.  
* __Drain Spirit:__ _(Cost: 0)_ Steal 1 point of an enemies inner fire and add it to your own. The increased inner fire lasts for one hour. If an entity reaches -10 inner fire, it instantly dies.  
* __Ghastly Visage:__ _(Cost: 0)_ Make yourself look like a horrible monster. Gain advantage on intimidation checks.  
* __Isolate:__ _(Cost: 0)_ Force an entity to make an inner fire saving throw against your spell power. On failure, sever any magical or psychic connections that they maintain with other entities. Such connections can not be re-established so long as you maintain concentration.  
* __Minor Death Coil:__ _(Cost: 0)_ Fire a ball of pure death from your hand. Deals 1d6 damage. Heals undead.  
* __Night Terror:__ _(Cost: 0)_ Force a sleeping entity to make a disadvantaged inner fire saving throw against your spell power. On failure, impose your will on them by manifesting yourself in their dreams.  
* __Rot:__ _(Cost: 0)_ Cause an item to rot or deal 1d4 damage. Must touch the item.  
* __Sentient Shadow:__ _(Cost: 0)_ Bring to life a sentient shadow. The shadow lasts for one minute, and will follow your orders. The shadow is capable of influencing objects by manipulating their shadows. The shadow is capable of attacking for 1d4 damage, and has a strength of -3. It can be killed by being exposed to bright light.  
* __Shadow:__ _(Cost: 0)_ Move like shadow through the darkness. Gain advantage on stealth checks when in shadow.  
* __Vampiric Touch:__ _(Cost: 0)_ Touch an enemy and deal 1d4 damage. Increase your health by the damage dealt.  
* __Vivify:__ _(Cost: 0)_ Make something rotten or dead appear living.  
  
__Tier 1:__  
* __Bloodlust:__ _(Cost: 1)_ Cast a spell of an ally which sends them into a frenzy. Their intelligence and perception is decreased by 3 for the duration, but they are granted an additional attack action on their turn.  
* __Cripple:__ _(Cost: 1)_ Force an enemy to make an inner fire saving throw against your spell power and deal 1d6 damage. On a failure, the enemy misses an action on their next turn.  
* __Disease:__ _(Cost: 1)_ Force an entity to make an inner fire saving throw against your spell power. If the entity fails, it is cursed with a disease which deals 1d6 damage per day. Any damage dealt by the disease cannot be healed until the disease is cured. The disease does not go go away until cured or dispelled. Any entity that comes into physical contact with a diseased entity must make an inner fire saving throw against your spell power, and become diseased on failure.  
* __Ectoplasmic Discharge:__ _(Cost: 1)_ Release a torrent of screaming ghosts which damages all enemies in a 15 foot cone in front of you. Does 1d8 damage.  
* __Haunt:__ _(Cost: 1)_ Summon forth a spirit to haunt an individual. The spirit lasts for one week, at which time it returns to you briefly to report its actions before disappearing.  
* __Major Death Coil:__ _(Cost: 1)_ Fire a ball of pure death from your hand. Deals 1d8 damage. Heals undead.  
* __Minor Through the Eyes of the Little Ones:__ _(Cost: 1)_ Take control of a nearby small animal such as a rat or crow. You lose control after 1 hour or after the animal moves 1 mile away. For the duration, your consciousness can inhabit the creature's.  
* __Minor darkness:__ _(Cost: 1)_ Fill a 15 square foot area with pitch darkness. Entities within the darkness must roll a perception check against your spell power to act effectively on their turn. If they pass, they act with disadvantage.  
* __Pain:__ _(Cost: 1)_ Cause an enemy to feel incredible pain, dealing 1d6 damage. Force the entity to make an inner fire saving throw against your spell power. On failure, they are partially incapacitated, and must make their next action with disadvantage.  
* __Painless:__ _(Cost: 1)_ Remove an entities ability to feel pain. Pain does not cause disadvantage for the entity for the duration of the spell. Lasts 1 hour.  
* __Sentry Skull:__ _(Cost: 1)_ Take the skull of a fallen entity and infuse it with the power of a soul to link yourself to it. From this point on, you may see through the eyes of the skull.  
* __Shadow-step:__ _(Cost: 1)_ Teleport from one shadow to another over a maximum distance of 50 feet.  
* __Siphon:__ _(Cost: 1)_ Eat the life-force of a wounded enemy, dealing 1d8 damage, and healing yourself for that amount. An enemy may only be siphoned once, and You cannot harvest a soul from an entity that you have siphoned.  
* __Skeleton:__ _(Cost: 1)_ Raise a skeletal minion from a fallen entity. The skeleton has 4 health, does 1d4 damage, and lasts at most 48 hours.  
* __Surrogate:__ _(Cost: 1)_ Reaction. Force the nearest entity to make an inner fire saving throw against your spell power. On failure, they dive in front of you to save you from an attack.  
* __Vampiric Blade:__ _(Cost: 1)_ Enchant any blade so that it does an additional 1d4 damage. You heal an amount equivalent to this damage. This spell lasts for 3 turns or one hour.  
  
__Tier 2:__  
* __Constricting Shadow:__ _(Cost: 2)_ Summon forth a dozen shadowy hands which deal 1d8 damage and attempt to grapple an entity. Force the entity to make a dexterity check against your spell power. On failure, the entity is grappled. Each turn that the entity is grappled, it takes an additional 1d8 damage. Each turn, the entity may make a strength check against your spell power to attempt to break the grapple.  
* __Major Vivify:__ _(Cost: 2)_ Make everything rotten or dead in 100 foot radius appear living.  
* __Murder of Crows:__ _(Cost: 2)_ Summon a murder of crows to attack an enemy. Does 1d10 damage per turn, lasts 3 turns.  
* __Spikes of Blood:__ _(Cost: 2)_ Form any blood on the ground into spiked daggers which are hurled at the enemy. More blood causes more damage for a maximum of 6d6 damage.  
* __Steal Senses:__ _(Cost: 2)_ Cover an entity's eyes, ears, and/or mouth with your hand to remove them. Lasts until dispelled.  
* __Wall of Bone:__ _(Cost: 2)_ Create a wall up to 40 feet high and 100 feet long of solid bone.  
* __Zombie:__ _(Cost: 2)_ Raise a zombie minion from a fallen entity. The zombie has 8 health, does 1d6 damage, and lasts at most seven days.  
  
__Tier 3:__  
* __Trauma:__ _(Cost: 3)_ Cause an enemy to see into the unseen realm of darkness. If they fail an inner fire saving throw against your spell power, they collapse, unable to move on their next turn. On a critical fail, their mind is broken until they are healed.  
* __Death Beam:__ _(Cost: 3)_ Fire a beam of concentrated death at an enemy, dealing 4d10 damage.  
* __Ghoul:__ _(Cost: 3)_ Raise a ghoul from a fallen entity. The ghoul has 20 health and may attack twice for 1d10 damage per attack. Ghouls last for up to one month. Also allows resurrection of larger enemies with Poohbah generated stats.  
* __Hungry Shadows:__ _(Cost: 3)_ Concentration. Summon a pack of 3 shadowy hounds which attempt to devour an entity. Each hound has 10 hit points, and can bite for 1d6 damage.  
* __Major Darkness:__ _(Cost: 3)_ Fill a 100 square foot area with pitch darkness. Entities within the darkness must roll a perception check against your spell power to act effectively on their turn. If they pass, they act with disadvantage.  
* __Major Through the eyes of the little ones:__ _(Cost: 3)_ Take control of a large animal, a weak minded person, or child. You lose control after 1 hour or after the creature moves 1 mile away. For the duration, your consciousness can inhabit the creature.  
* __Possess:__ _(Cost: 3)_ Force a vulnerable entity to make an inner fire saving throw against your spell power. On failure, you can temporarily possess the entity, taking control of its actions. Once every hour, or when you do or are about to do something that significantly distresses the entity, it can repeat it's saving throw at disadvantage.  
* __Tenmu's Terrible Tentacles:__ _(Cost: 3)_ Concentration. Sprout shadowy tentacles from your back. The tentacles are able to lift you up to seven feet from the ground, and allow you to climb like a spider. Each turn you may make a tentacle attack for 1d10 + inner fire damage as an offhand attack.  
  
__Tier 4:__  
* __Death Knight:__ _(Cost: 4)_ Resurrect a greater ghoul to aid you. The death knight has 40 health, and may attack twice for 1d10 damage. Death Knights last for one month, and may throw themselves in front of you as a reaction. If a death knight reaches zero health, it may make a saving throw. If it rolls 5 or higher, it does not die, but returns to 1 health.  
* __Anti-life field:__ _(Cost: 4)_ Create a field of death around yourself with a 10 foot radius. Anything living that enters the field takes 4d10 damage per turn. The field wilts and kills everything. Lasts for one hour or until de-summoned.  
* __Fall:__ _(Cost: 4)_ Force all enemies within a 100 foot radius to make an inner fire saving throw against your spell power. If they fail, they take 4d10 damage and miss their next turn. On success they take half as much damage.  
* __Putrid Air:__ _(Cost: 4)_ Fill a large room with noxious gas. Force all enemies within a 50 foot radius to make an inner fire saving throw against your spell power. On failure, the enemy takes 3d10 and must take all actions on their next turn at disadvantage. On success, the enemy takes half damage and is not at disadvantage. Repeat the check every turn for three turns.  
* __Sap Age:__ _(Cost: 4)_ Steal the life-force from someone. Every 10 seconds or 1 turn in combat, you steal 1 year of their life. This life force can be given to someone else.  
  
__Tier 5:__  
* __Abomination:__ _(Cost: 5)_ Knit together a monstrous abomination to fight for you. Requires 5 corpses. The monster has 60 health, and may attack three times for 1d10 blunt damage plus 1d10 dark damage. The abomination can cast spikes of blood or cripple once every 3 turns. Abominations last for one month. If a abomination reaches zero health, it may make a saving throw. If it rolls 5 or higher, it does not die, but returns to 1 health. If the abomination dies, it releases a putrid cloud. Any entity in the putrid cloud must make an inner fire saving throw against your spell power. The entity takes 3d10 damage on failure, or half as much on success.  
* __Death Inducement:__ _(Cost: 5)_ Mark the time that a person will die. Requires a piece of paper made from the skin of a sentient being, one ounce of the blood of the one who is to die, and blood diamonds valuing 20,000 gold. At the prescribed time, the entity must make an inner fire saving throw against your spell power. If they fail, they take take 10d20 damage, which cannot be healed for 24 hours. On success, they take half damage.  
* __Horrors:__ _(Cost: 5)_ Summon a mass of fog with a one mile radius. Any entity within the fog sees apparitions of their worst fears. Each turn, they must make a saving throw against your spell power at disadvantage. On success, they can act. On failure, they are considered afraid, and must move as far away from the mist as possible. The mists are considered to be low light.  
* __Partial Resurrection:__ _(Cost: 5)_ Recall the soul of a being which has died within the past 100 years. Requires the carcass of a freshly dead man, and the heart of a high level beast. The entity is trapped in the body of the dead man, but comes back to life. Requires an inner fire check.  
* __Resurrect:__ _(Cost: 5)_ Resurrect an entity who has died within the past 24 hours. The entity will suffer from nightmares of the other side, and bear the scars of their injuries. Requires an inner fire check.  
* __Unending Darkness:__ _(Cost: 7)_ Go to a blacksmith and ask them to craft for you a lockbox of obsidian, which contains room for an object weighing roughly a pound. While it is being crafted, gather the heart of a high level beast, blood diamonds valued at 10,000 gold, and a soul gem containing the soul of something freshly killed. Combine the gems, diamonds, and heart to craft a beating heart of darkness. Lock the heart in the obsidian box, and bury it somewhere safe. After 24 hours, all land within 40 miles of the heart's position will be trapped in eternal night.  

  
### The Novice Spellbook
  
__Tier 0:__  
* __Acrid Mist:__ _(Cost: 0, Charisma Cost: 8)_ Summon noxious green gas around an enemy's head, doing 2 turns of 1d4 damage. If the enemy fails a saving throw against your spell power, they have disadvantage on their next action.  
* __Candlelight:__ _(Cost: 0, Charisma Cost: 8)_ Concentration. Summon a dim candlelight that floats near to you, and obeys your subconscious commands. The candlelight can move up to forty feet away from you before it is dispelled.  
* __Cold Hands:__ _(Cost: 0, Charisma Cost: 8)_ Render your hands so cold that they freeze water on contact. While in this state, your hands do 1d4 damage if laid on an enemy.  
* __Drain:__ _(Cost: 0, Charisma Cost: 8)_ Take 1 action points from an enemy and do 1d4 damage.  
* __Ephemeral Text:__ _(Cost: 0, Charisma Cost: 8)_ Write a message that disappears ten seconds after being read.  
* __Flare:__ _(Cost: 0, Charisma Cost: 8)_ Fire a colored flare from the source of your magic. The flare reaches up to 100 feet, and casts light equivalent to daylight. The flare does 1d4 damage to anything that it strikes, and is capable of setting fire to flammable materials.  
* __Force Push:__ _(Cost: 0, Charisma Cost: 8)_ Knock an enemy backwards, doing 1d6 damage. If you roll a critical hit, they are knocked prone.  
* __Liver of Steel:__ _(Cost: 0, Charisma Cost: 8)_ Render someone immune to the effects of additional alcohol. If the entity is unwilling, force them to make an inner fire saving throw against your spell power.  
* __Minor Levitation:__ _(Cost: 0, Charisma Cost: 8)_ Levitate an object up to 20 pounds. Concentration.  
* __Minor Move Air:__ _(Cost: 0, Charisma Cost: 8)_ Create a small gust of air, capable of pushing objects up to 20 pounds away from you and slowing the advance of approaching enemies.  
* __Muffle Footsteps:__ _(Cost: 0, Charisma Cost: 8)_ Give a teammate or yourself advantage on stealth checks. The teammate must be in line of sight. Concentration.  
* __Noodles:__ _(Cost: 0, Charisma Cost: 8)_ Fire a jet of noodles from the source of your magic. The noodles are steaming hot, and do 1d6 damage to whoever they hit. You can generate ten pounds of noodles per hour.  
* __Rapid-Fire Snowballs of Fury:__ _(Cost: 0, Charisma Cost: 8)_ Roll 1d6. Fire that many snowballs at up to as many targets. Each snowball does 1 damage.  
* __Rend Fabric:__ _(Cost: 0, Charisma Cost: 8)_ Shred a piece of fabric within one hundred feet of yourself into a million tiny pieces.  
* __Scourge:__ _(Cost: 0, Charisma Cost: 8)_ Instantly clean an object by pointing at it. The object must be within ten feet of you.  
* __Sticky:__ _(Cost: 0, Charisma Cost: 8)_ Force an entity to make an inner fire saving throw against your spell power. On failure, the entity is rendered uncomfortably sticky. This effect lasts until the entity washes itself or the magic is dispelled.  
* __Summon Flame:__ _(Cost: 0, Charisma Cost: 8)_ As an offhand action, summon a flame to your hand. The flame does 1d6 damage to anyone it touches.  
* __Summon Water:__ _(Cost: 0, Charisma Cost: 8)_ Summon water from your surroundings. Takes about 1 minute per gallon.  
* __Thunderous Voice:__ _(Cost: 0, Charisma Cost: 8)_ Magically magnify your voice so that it can be heard clearly at up to 100 yards.  
* __Transcribe Memory:__ _(Cost: 0, Charisma Cost: 8)_ Given a piece of parchment or paper, instantly render a sketch of a scene that you witnessed.  
  
__Tier 1:__  
* __Bare Knuckle Punch:__ _(Cost: 1, Charisma Cost: 12)_ Make a magically reinforced punching attack. On contact, fire and ice fly from your hand, dealing 1d8 damage to the affected entity.  
* __Beam of Heat:__ _(Cost: 1, Charisma Cost: 12)_ Concentration. Create a beam of heat originating from the source of your spell power. Every turn that the beam is targeted at the object, it does one dice greater of damage. Therefore, the beam does 1d4 damage on the first turn, 1d6 on the second, etc, capping at 1d20 damage. When the beam begins doing 1d20 damage, the target is ignited, and begins taking an additional 1d6 damage per turn.  
* __Become Slime:__ _(Cost: 1, Charisma Cost: 12)_ Transform into a green slime with a radius of one foot. As a slime, you have 10 hit points, and are able to squeeze through tight spaces. You move at a speed of 10 feet per turn, and are able to corrode any organic material, dealing 1d6 damage when you make contact.  
* __Block:__ _(Cost: 1, Charisma Cost: 8)_ Reaction. Make a contested dexterity check against an enemy that is targeting you with an attack. On a success, block their attack.  
* __Blot:__ _(Cost: 1, Charisma Cost: 10)_ Instantly destroy the text within any parchment or book your are holding.  
* __Bounce:__ _(Cost: 1, Charisma Cost: 12)_ Cause an object or entity to become bouncy for 1 turn or six seconds. Objects which are bouncy bounce to half of the height from which they were dropped, and take no fall on the initial impact.  
* __Bubble of Air:__ _(Cost: 1, Charisma Cost: 10)_ Creates a bubble of breathable air around an entity's head. Lasts 1 hour.  
* __Bull Rush:__ _(Cost: 1, Charisma Cost: 10)_ Burst forward ten feet, knocking back all entities in front of you and dealing 1d6 damage. Any affected entities must make an inner fire saving throw against your spell power. On failure, they are knocked prone.  
* __Charm:__ _(Cost: 1, Charisma Cost: 13)_ If an entity fails an inner fire saving throw against your spell power, gain advantage on charisma checks with them. If you fail, they become aware that you were trying to charm them.  
* __Cloak of Shadow:__ _(Cost: 1, Charisma Cost: 12)_ Make an entity that is standing absolutely still invisible. Lasts for 5 minutes or until the entity moves.  
* __Corrode:__ _(Cost: 1, Charisma Cost: 10)_ Concentration. Corrode metal or stone at a rate of one cubic foot per minute.  
* __Create Pit:__ _(Cost: 1, Charisma Cost: 12)_ Summon a 40 foot deep pit with a 5 foot radius to a location anywhere within 30 feet of you. If the pit is summoned beneath an entity, the entity may make a dexterity saving throw against your spell power to avoid falling.  
* __Curse of the Bedwetter:__ _(Cost: 1, Charisma Cost: 10)_ Force an enemy to make an inner fire saving throw against your spell power. On failure, the enemy receives a curse which causes them to wet the bed each night. The curse cannot be removed unless dispelled.  
* __Electrified:__ _(Cost: 1, Charisma Cost: 10)_ Electrify an object or entity. Any entity who touches or attacks the affected entity suffers 1d4 electric damage.  
* __Fireball:__ _(Cost: 1, Charisma Cost: 12)_ Hurl a fireball which does 1d8 damage on all enemies within 15 feet of the point of impact.  
* __Fog Cloud:__ _(Cost: 1, Charisma Cost: 10)_ Summon a fog cloud with a 20 foot radius to your position. The interior of the fog cloud is considered to be lightless.  
* __Freeze or Unfreeze Water:__ _(Cost: 1, Charisma Cost: 8)_ Freeze or unfreeze up to a 40 square foot area of water.  
* __Heat or Cool Air:__ _(Cost: 1, Charisma Cost: 12)_ Heat or cool the air in a room to an uncomfortable or extreme temperature. After a turn of focus, all entities in the room that are not acclimated to the temperature begin taking 1d4 damage per turn.  
* __Hide:__ _(Cost: 1, Charisma Cost: 10)_ Hide something or someone that can fit into a 2 cubic foot box in a pocket dimension. The affected entity must be willing.  
* __High Speed Projectile:__ _(Cost: 0, Charisma Cost: 10)_ Instantly fire an small object you are holding forward at the speed of a bullet. The projectile deals 1d6 damage to a single target, plus the attack damage of the item thrown.  
* __Increase Gravity:__ _(Cost: 1, Charisma Cost: 10)_ Double the gravity effecting an object or entity. If an entity is targeted, it must make an inner fire saving throw against your spell power to determine spell success.  
* __Jelly Arms:__ _(Cost: 1, Charisma Cost: 12)_ Force an entity to make an inner fire saving throw against your spell power. On failure, the entity looses control of its arms, which fall limp to its sides. Each turn, the entity may attempt an inner fire saving throw against your spell power to attempt to break the spell.  
* __Jet of Frost:__ _(Cost: 1, Charisma Cost: 12)_ Fire a 10 foot cone of frost from the source of your magic, dealing 1d6 cold damage to all entities in the cone. Affected entities must make an inner fire saving throw against your spell power, or be slowed. Slowed entities move at half speed, and are forced back one position in the initiative order.  
* __Jet of Water:__ _(Cost: 1, Charisma Cost: 12)_ Fire a get of water from the source of your spell power. The blast of water travels 40 feet, and strikes all entities in a line. Affected entities take 1d6 damage, and must make an inner fire saving throw against your spell power and be knocked prone on failure. You may maintain the stream of water for up to 10 seconds, or two turns, dumping 300 gallons of water per minute.  
* __Lasso:__ _(Cost: 1, Charisma Cost: 10)_ Summon a 20 foot lasso of glowing magic, which attempts to restrain an entity of your choice. The targeted entity must make a dexterity saving throw against your spell power, and is restrained on failure. As an offhand action, you may tug a lassoed entity to you if it is of your size or smaller. Each turn, the lassoed entity may attempt a strength saving throw against your spell power to break the grapple.  
* __Lightning Touch:__ _(Cost: 1, Charisma Cost: 10)_ Electrify your hands so that they deal 1d8 damage to any entity that touches them. Any entity touched must make an inner fire saving throw against your spell power, and is knocked prone on failure.  
* __Lock or Unlock:__ _(Cost: 1, Charisma Cost: 10)_ Lock or unlock an easy lock, tie or untie a knot, or seal something with magic. Lock lasts 24 hours.  
* __Magic Alarm:__ _(Cost: 1, Charisma Cost: 10)_ Create a magic alarm that triggers on a physical event of your choice.  
* __Magically Reinforced Arms:__ _(Cost: 1, Charisma Cost: 12)_ Concentration. Reinforce your arms with a layer of magic. While your arms are reinforced, your strength is treated as +1. A retractable blade of magic can extend from either of your wrists, parallel to your arms. Attacks made with this blade do 1d8 damage.  
* __Melon Headed Wanderer:__ _(Cost: 1, Charisma Cost: 12)_ Concentration. Force an entity to make an inner fire saving throw against your spell power. On failure, the entity's head is replaced with a melon. While an entity's head is a melon, it makes all actions with disadvantage, and is considered blind. The entity may repeat the saving throw each turn as an action.  
* __Minor Ward of Hearing:__ _(Cost: 1, Charisma Cost: 10)_ Create an invisible ward through which you can hear. The ward disappears after one day or if you move more than 1 mile from it.  
* __Minor Ward of Sight:__ _(Cost: 1, Charisma Cost: 10)_ Create an invisible ward through which you can see. The ward disappears after one day or if you move more than 1 mile from it.  
* __Mirror Image:__ _(Cost: 1, Charisma Cost: 12)_ Summon 1d4 false images of yourself that stand near you at an offset. The mirror images copy your actions exactly, but are incapable of interacting with the world in any way.  
* __Paint:__ _(Cost: 1, Charisma Cost: 10)_ Instantly paint up to a 100x100 area any way you desire. Roll a dexterity check to determine the quality of the painting.  
* __Quicksand:__ _(Cost: 1, Charisma Cost: 12)_ Summon a 10 square foot patch of quicksand. Any enemy in the quicksand must make a D14 saving throw to escape it. An entity that is stuck in the quicksand for two consecutive turns begins to drown, taking 1d10 damage per turn. If an entity is drowning, its saving throw increases to 16.  
* __Silence:__ _(Cost: 1, Charisma Cost: 10)_ Stop one entity from being able to make sound. Entity must be within line of sight, and no more than 50 feet away. This spell does not require a saving throw, as it affects the air around the entity, rather than the entity itself. Concentration.  
* __Slackjaw:__ _(Cost: 1, Charisma Cost: 12)_ Force an entity to make an inner fire saving throw against your spell power. On failure, the entity's jaw goes slack, and it is unable to speak. Each turn or every five minutes, the entity may repeat its saving throw.  
* __Strike True:__ _(Cost: 1, Charisma Cost: 8)_ Give a teammate advantage on an upcoming check or attack of their choice.  
* __Terrible Smell:__ _(Cost: 1, Charisma Cost: 12)_ Fill a room with a noxious scent for 1d4 turns. While in the scent, all susceptible entities must make an inner fire saving throw against your spell power at the start of each turn. On failure, they must make all moves on that turn with disadvantage. On critical failure, they vomit and take 1d4 damage.  
* __Tiny Golem:__ _(Cost: 1, Charisma Cost: 12)_ Summon forth a one foot tall fire, water, or lightning golem. The golem lasts for one hour, has 10 health, and can attack for 1d6 damage. You have command of the golem's actions.  
* __Weakness:__ _(Cost: 1, Charisma Cost: 10)_ Force an entity to make an inner fire saving throw against your spell power. On failure, the entity is sapped of 1d4 strength and must make all strength checks with disadvantage. The entity can attempt a saving throw each turn  
  
__Tier 2:__  
* __Acid Rain:__ _(Cost: 2, Charisma Cost: 12)_ Rain acid down on a 25 square foot area, doing 1d6 damage to all enemies affected. Concentration.  
* __Become Ephemeral:__ _(Cost: 2, Charisma Cost: 14)_ Your form flickers as you enter the plane of the ethereal. While you are ephemeral, you cannot be struck by enemies damage, and may pass through any substance less than one inch thick. While ephemeral, you cannot attack, cast spells, or use abilities.  
* __Deep Sleep:__ _(Cost: 2, Charisma Cost: 12)_ If an enemy fails a saving throw against your spell power, put them into a deep sleep. They are awakened if attacked, or if they pass a dc 17 perception check.  
* __Dragons Breath:__ _(Cost: 2, Charisma Cost: 12)_ The air crackles and pops as a jet of flame roars from your mouth. Any entity caught in a ten foot cone in front of you suffers 2d8 fire damage.  
* __Energy Shots:__ _(Cost: 2, Charisma Cost: 12)_ Three balls of crackling yellow energy swirl about you. You may fire them at up to 3 enemies, doing 1d6 damage on each impact.  
* __Frostthrower:__ _(Cost: 2, Charisma Cost: 12)_ With a pop and a hiss, a torrent of frozen air sprays forth from the origin of your magic. This arctic blast hits all entities in a 10 foot cone before you, dealing 3d6 frost damage.  
* __Greater Drain:__ _(Cost: 2, Charisma Cost: 12)_ Take 4 action points from an enemy and do 1d8 damage.  
* __Greater Levitation:__ _(Cost: 2, Charisma Cost: 14)_ Lift an object up to 200 pounds. Levitation works on objects up to 150 feet away.  
* __Greater Rapid Fire Snowballs of Fury:__ _(Cost: 1, Charisma Cost: 12)_ Roll 1d6. Fire that many rock filled ice-balls at up to as many targets. Each snowball does 2 damage.  
* __Hail of Blades:__ _(Cost: 2, Charisma Cost: 14)_ In a rhythmic spiral, eight daggers appear in a halo about you. As one, they hurtle forth dealing 2d8 damage split across as many as eight entities.  
* __Ice Spear:__ _(Cost: 2, Charisma Cost: 14)_ Spear an enemy with a lance of ice for 2d10 damage.  
* __Longband Telepathic Message:__ _(Cost: 2, Charisma Cost: 14)_ Concentrate on an entity that you have met. You are able to telepathically send them a message of up to 14 words, regardless of distance.  
* __Magic Chains:__ _(Cost: 2, Charisma Cost: 14)_ Force an entity to make a dexterity saving throw against your spell power. On failure, chains large enough to subdue the entity crackle into existence, grappling it. The entity may make a strength saving throw against your spell power at the start of each of its turns to attempt to break the grapple.  
* __Magnetic:__ _(Cost: 2, Charisma Cost: 14)_ Point at an object of your choice. That object becomes an incredibly powerful magnet, pulling any piece of metal within 100 feet to it. Entities holding metal weapons must make an strength saving throw against your spell power, or risk loosing their grip. Entities wearing metal armor are pulled five feet towards the magnet on failure, or fly to the magnet if they roll below a five, taking 1d4 damage per five feet that they are carried.  
* __Major Ward of Hearing:__ _(Cost: 2, Charisma Cost: 12)_ Create an invisible ward through which you can hear. The ward disappears if you move more than 5 mile from it.  
* __Major ward of sight:__ _(Cost: 2, Charisma Cost: 12)_ Create an invisible ward through which you can see. The ward disappears if you move more than 5 mile from it.  
* __Mark:__ _(Cost: 2, Charisma Cost: 14)_ Lay your hands on something or someone so that you always know what it is. This spell lasts for 1d6 days, or until the affected entity dispels it.  
* __Platform:__ _(Cost: 2, Charisma Cost: 12)_ Summon a circular  
* __Rainbows:__ _(Cost: 2, Charisma Cost: 12)_ With a mighty explosion, a blinding beam of light flares from your fingertips or mouth, As the light moves further from you, it separates into bands of color, a rainbow! Any entity struck by the rainbow takes 2d6 damage, and must make an inner fire saving throw against your spell power. On failure, the entity instantly begins vomiting rainbows, and makes all moves with disadvantage on it's next turn.  
* __Stone Skin:__ _(Cost: 2, Charisma Cost: 12)_ Harden the skin of an entity, giving it 4 armor for 5 turns or 1 hour.  
* __Summon Cannon:__ _(Cost: 2, Charisma Cost: 14)_ Point at an enemy. A cannon appears at your side in a burst of blackish smoke, and fires a single round, dealing 3d8 siege damage. If the entity is large or smaller, it must make a strength saving throw against your spell power. On failure, it is pushed backwards 1d20 feet.  
* __Turn into Frog:__ _(Cost: 2, Charisma Cost: 14)_ Force an entity to make an inner fire saving throw against your spell power. On failure, they are transformed into a frog. As a frog, their movement speed is 5 feet per round, and they are unable to speak, use abilities, or perform actions. Each turn, the affected entity may repeat its saving throw.  
* __Wall of Stone:__ _(Cost: 2)_ Create a wall up to 40 feet high and 100 feet long of solid stone.  
* __Weaken Metal:__ _(Cost: 2, Charisma Cost: 10)_ Lay your hand on metal to weaken it. Works on up to a 1 cubic foot block of metal and makes it roughly the same strength as wood.  
  
__Tier 3:__  
* __Bubble of Vacuum:__ _(Cost: 3, Charisma Cost: 12)_ Creates a bubble with no air around an enemy's head. On each turn, the enemy may make a saving throw against your spell power to attempt to escape from the bubble. While the bubble is in place, they have disadvantage on any attacks. If the bubble persists for 2 turns, the entity begins taking 2d10 damage per turn.  
* __Chain Lightning:__ _(Cost: 3, Charisma Cost: 15)_ Fire lighting at an enemy for a guaranteed 1d10 damage. Roll a d20, and if 5 or above, chain to an enemy of your choice. Continue until you roll below 5. Lightning may only strike the same entity twice in succession.  
* __Clone:__ _(Cost: 3, Charisma Cost: 14)_ Split a person in two. The clones share a pool of hit points, but each gets its own turn, and acts autonomously. The duplicates remain until both agree to be merged once more or until the magic is dispelled.  
* __Curse of Insanity:__ _(Cost: 3, Charisma Cost: 14)_ Force an entity to make an inner fire saving throw against your spell power. On failure, the entity is cursed, and begins a slip into insanity. Every hour, the entity may make an inner fire saving throw to avoid slipping further. On each failure, the entity looses one intelligence and one inner fire.  
* __Duplicate Object:__ _(Cost: 3, Charisma Cost: 14)_ Concentration. Duplicate any object into two. When the objects are merged, the resulting object is the less valuable of the two. This spell does not work on consumable objects including potions, spell scrolls, or food.  
* __Featherfall:__ _(Cost: 3, Charisma Cost: 14)_ The entity on which you cast this falls as though it is a feather.  
* __Flash fry:__ _(Cost: 3, Charisma Cost: 14)_ With a sizzle, boiling grease envelops an entity of your choice. The entity immediately takes 3d10 damage, and must make an dexterity saving throw against your spell power. On failure, the entity is blinded through its next turn, and must make all actions with disadvantage.  
* __Geyser of Air:__ _(Cost: 3, Charisma Cost: 14)_ In a rush, a gout of air shoots up at a position of your choice, throwing anything of size large or smaller at the position 60 feet into the air.  
* __Greater Animate Object:__ _(Cost: 3, Charisma Cost: 14)_ Bring an object to life to fight for you. The object has 20 health and can do 1d8 damage. Concentration.  
* __Greater Bubble of air:__ _(Cost: 3, Charisma Cost: 15)_ Create bubbles of breathable air around up to 8 entities heads. Lasts 6 hours.  
* __Greater Fireball:__ _(Cost: 3, Charisma Cost: 15)_ Hurl a fireball which does 4d10 damage on all enemies within 20 feet of the point of impact.  
* __Greater Lock/Unlock:__ _(Cost: 3, Charisma Cost: 13)_ Lock a difficult lock, tie or untie a knot, or seal something with magic. Lock lasts 24 hours.  
* __Greater Muffle Footsteps:__ _(Cost: 3, Charisma Cost: 12)_ Give your whole party advantage on stealth checks for 1 hour.  
* __Loathing:__ _(Cost: 3, Charisma Cost: 14)_ Force an entity to make an inner fire saving throw against your spell power. On failure, you may instill that entity with a deep hatred for an individual of your choosing. This hatred stays present until dispelled.  
* __Manifest Bear:__ _(Cost: 3, Charisma Cost: 14)_ May the power of the wilds be with you! Summon a loyal adult bear to any position within eyesight. The bear follows your telepathic orders. For statistics, view the book of known beasts. The bear disappears at the end of your next rest.  
* __Rapid Ice Spear:__ _(Cost: 3, Charisma Cost: 15)_ Spear up to 2 enemies with lances of ice. Deal 2d10 damage to each or 4d10 damage to one.  
* __Shrink Person:__ _(Cost: 3, Charisma Cost: 14)_ Force an entity to make an inner fire saving throw against your spell power. On failure, the entity is reduced to one twentieth of its size. The entity may make an inner fire saving throw against your spell power each turn or once every ten minutes to attempt to revert to its original size.  
* __Siege Blast:__ _(Cost: 3, Charisma Cost: 14)_ With an explosive blast, deal massive damage to a structure of your choosing. Deal 3d20 damage to any building or structure.  
* __Specter of sight:__ _(Cost: 3, Charisma Cost: 15)_ Create an invisible specter through which you can see and hear. The specter moves on your command, and lasts 24 hours.  
* __Summon Bleck:__ _(Cost: 3, Charisma Cost: 14)_ Summon a mighty bleck to fight for you! A bleck is a gooey, little creature with a one inch diameter. Bleck have 1 hit point, and are incapable of attacking. They move at a rate of one foot per minute. Bleck cannot be damaged by crushing force or blades, as they will merely be split and then reform. After five seconds, a bleck splits into two blecks. Each of these blecks wait in five seconds, and then split into two more.  
* __Summon elemental weapon:__ _(Cost: 3, Charisma Cost: 14)_ Summon to yourself a 1d12 elemental weapon with bonus 1d6 elemental damage.  
* __Trade Bodies:__ _(Cost: 2, Charisma Cost: 12)_ Touch an entity. If the entity is unwilling, force it to make an inner fire saving throw against your spell power. On failure, you switch bodies, including all applicable stats and abilities. If either entity's body dies during the swap, the change is permanent. An unwilling entity may repeat its saving throw at the start of each of its turns.  
* __Vortex:__ _(Cost: 3, Charisma Cost: 14)_ With a rush, wind or water of your choice twists into a rushing vortex. Entities within thirty feet must make a dexterity saving throw against your spell power or be pulled in and restrained.  
  
__Tier 4:__  
* __Biting winds:__ _(Cost: 4, Charisma Cost: 16)_ Concentration. Wind howls and whips as you utter an incantation. Driving winds that cut like razors push enemies away from you, dealing 2d10 damage per turn to any entity within a forty foot cone in front of you. Affected entities must make an strength saving throw against your spell power to move in the wind. On success, they move at half their normal speed. Gigantic and larger entities make their check with advantage. Small entities make it with disadvantage.  
* __Cage:__ _(Cost: 4, Charisma Cost: 16)_ Create a 30 cubic foot magical cage around yourself which no one can exit.  
* __Chains of Fire:__ _(Cost: 4, Charisma Cost: 16)_ Concentration. Force an entity to make a dexterity saving throw against your spell power. On failure, fiery chains large enough to restrain them burst into existence, grappling them. Each turn, the affected entity may make a strength saving throw against your spell power in an attempt to break out. Each turn an entity is tethered, it takes 2d10 fire damage.  
* __Deadman's Contingency:__ _(Cost: 0, Charisma Cost: 8)_ Put in place a contingency plan for when you die. The contingency can involve up to three of your spells, and is chained together by an ethereal entity which acts as your proxy, and exists for sixty seconds.  
* __Delayed Explosion:__ _(Cost: 4, Charisma Cost: 16)_ Cast a glyph within 100 feet of yourself which explodes on your command. Does 2d20 damage to all affected enemies.  
* __Flaming Flowers:__ _(Cost: 4, Charisma Cost: 16)_ With a hiss and a crackle, a thousand flours of pure flame sprout in a space up to 100 square feet around you. These flowers do not harm your allies, but deal 1d6 damage for every 10 feet that an enemy moves through them. As a bonus, you are always able to summon a single flaming flower as a tier zero spell.  
* __Greater Block:__ _(Cost: 4, Charisma Cost: 17)_ Block your entire team from taking damage for 1 turn.  
* __I Know Malkizar!:__ _(Cost: 7, Charisma Cost: 16)_ Convince every entity that witnessed an event that there was another person present named Malkizar. In fourteen words or fewer, describe what Malkizar did. Everyone who witnessed the event now earnestly believes that Malkizar was present and performed the action you described.  
* __Implode:__ _(Cost: 4, Charisma Cost: 17)_ Do 3d20 damage to a single target. On death, the enemy explodes, doing 2d10 damage to any adjacent enemies.  
* __Inter-Realm Teleport:__ _(Cost: 4, Charisma Cost: 16)_ Gather up to eight willing entities, and link arms. With a thunderous blast, you are torn through the veil of the realms' alignment, and are transported to a realm of of which you know. On a critical failure, you are transported to a random realm.  
* __Mass Increase Gravity:__ _(Cost: 4, Charisma Cost: 16)_ Quadruple the gravity effecting up to twelve objects or entities. If an entity is targeted, it must make an inner fire saving throw against your spell power to determine spell success.  
* __Pillar of flame:__ _(Cost: 4, Charisma Cost: 17)_ Create a Pillar of flame with a radius of 10 feet and up to 100 feet in height. The pillar does 4d10 damage to any enemies caught inside. Concentration, disappears if you move more than 100 feet away.  
* __Purest Self:__ _(Cost: 4, Charisma Cost: 16)_ Concentration. Cause an object of your choice to become its archetypal self. For example, if you have in your possession a rusty old sword, cause it to become a pristine blade with a keen edge.  
* __Summon Cannons:__ _(Cost: 4, Charisma Cost: 17)_ With a sound like lightning a wall of a dozen cannons appear behind you, stacked high and pointing at up to four entities of your choice. Split 8d12 damage among as many as four enemies. Each affected entity must make an strength saving throw against your spell power. On failure, they are pushed back 4d10 feet.  
* __Tri-beam:__ _(Cost: 4, Charisma Cost: 17)_ Three beams of crackling energy fire forth from the source of your magic. Each of the beam may target an entity of your choice. Roll a d6 for each beam. On 1, the beam is a beam of fire, which deals 4d10 damage and sets the entity aflame. On 2, it is a ray of frost, which deals 3d12 damage and slows the entity if it fails its save, moving it back one space in the initiative order. On a 3, it is a ray of weakness, and causes the entity's strength to decrease by 1d8 until its next rest if it fails its save. On a 4, it is a ray of electricity, and does 3d10 damage and causes the entity to go prone if they fail a save. On a d5, it is a beam of discord, and causes the entity to spontaneously change gender on a failed save. On a 6, it is a ray of death, and causes the entity to take 3d20 damage.  
* __Wall of Steel:__ _(Cost: 3, Charisma Cost: 16)_ Create a wall up to 40 feet high and 100 feet long of steel swords, spears, and axes fused together.  
  
__Tier 5:__  
* __Anti magic ring:__ _(Cost: 5, Charisma Cost: 18)_ Create a 50 foot diameter sphere around yourself in which magic, potions, and divine attacks have no effect.  
* __Explosion!:__ _(Cost: 5, Charisma Cost: 18)_ Darkness blacker than black and darker than dark, I beseech thee, combine with my deep crimson. The time of awakening cometh. Justice, fallen upon the infallible boundary, appear now as an intangible distortion! I desire for my torrent of power a destructive force: a destructive force without equal! Return all creation to cinders, and come from the abyss! This is the mightiest means of attack known to man, the ultimate attack magic! Explosion! Deal 7d20 points of damage to all entities within a 100 foot sphere at a targeted point. Upon casting, you are immediately exhausted, take 10d10 damage, and must make all actions with disadvantage until you have slept.  
* __Quake:__ _(Cost: 5, Charisma Cost: 20)_ Create a thunderous earthquake capable of destroying a house. Enemies affected must make a dexterity saving throw to avoid being knocked prone. On a critical fail, enemies plummet into a fissure, dying. All enemies take 4d10 damage, or half that if they make their saving throw.  
* __Stop Time:__ _(Cost: 5, Charisma Cost: 18)_ Freeze time for everyone but you for 1d4 + Inner Fire turns or 1d20 minutes if out of battle. Tapping a party member returns them to the normal flow of time. Attacking an entity returns it to the normal flow of time.  
* __Strike from the Record:__ _(Cost: 6, Charisma Cost: 19)_ Strike a word, or a phrase of up to 3 words from the record. It becomes impossible for anyone in the world to speak the word or phrase. If they do, they instantly take 4d10 psychic damage. You may ban at most one word or phrase at a time.  

  
### The Sorcerer's Scrolls
  
__Tier 0:__  
* __Hologram:__ _(Cost: 0, Charisma Cost: 8)_ Manifest your thoughts as a hologram standing one foot tall on your palm.  
* __Summon Familiar:__ _(Cost: 0, Charisma Cost: 8)_ Summon a small familiar with 5 health. The familiar obeys your every command and can attack for 1d4 damage. If a familiar dies, it cannot be resummoned until the next day.  
* __Tickle:__ _(Cost: 0, Charisma Cost: 8)_ Utilize your magic to tickle an entity within 30 feet of you. If in combat, the entity must make an inner fire saving throw against your spell power, or be forced to move at disadvantage.  
  
__Tier 1:__  
* __Conjure Minor Illusion:__ _(Cost: 1, Charisma Cost: 10)_ Create an illusory object which cannot move and cannot be bigger than a horse. You must have seen the object you are attempting to create. Concentration.  
* __Disarm:__ _(Cost: 1, Charisma Cost: 10)_ Force an entity to make a dexterity check against your spell power. On failure, the entity looses its grip on its weapon, which flies to your hand.  
* __Hoist:__ _(Cost: 1, Charisma Cost: 10)_ Concentration. Force an average sized or smaller entity to make a dexterity check against your spell power. On failure, the entity is hoisted into the air by its ankle. On its turn, the entity may repeat its save. While hoisted, the entity is treated as grappled. This spell may be attempted on larger creatures with increased difficulty.  
* __Slash:__ _(Cost: 1, Charisma Cost: 10)_ As an offhand action, slash at an enemy up to 15 feet away with an invisible blade, dealing 1d8 damage.  
* __Unseen hand:__ _(Cost: 1, Charisma Cost: 10)_ Conjure an unseen hand which can manipulate objects up to 50 feet away.  
* __Through My Familiar's Eyes:__ _(Cost: 2, Charisma Cost: 12)_ View the world through your familiar's eyes. Increase the difficulty by 2 to hear through your familiar's ears.  
  
__Tier 2:__  
* __Conjure major illusion:__ _(Cost: 2, Charisma Cost: 14)_ Create an illusory object which can move/speak if you tell it to but cannot be bigger than a house. Concentration.  
* __Disarm:__ _(Cost: 2, Charisma Cost: 12)_ Disarm an enemy if they fail a saving throw against your spell power.  
* __Enlarge:__ _(Cost: 2, Charisma Cost: 14)_ Grow an object or entity to up to double its size. Unwilling entities can attempt a saving throw against your spell power each turn. Concentration.  
* __Enter Mind:__ _(Cost: 2, Charisma Cost: 12)_ Force an entity to make an inner fire saving throw against your spell power. On failure, you may break into other entities mind, viewing their memories.  
* __Jet of water:__ _(Cost: 2, Charisma Cost: 12)_ Call forth a powerful jet of water. The spell does 1d10 damage regularly, or 2d10 damage if cast while on or near a body of water. Knocks an enemy over on critical hit.  
* __Minor Familiar:__ _(Cost: 2, Charisma Cost: 14)_ Summon a small familiar to aid you. See the book of known beasts for more information.  
* __Seer:__ _(Cost: 2, Charisma Cost: 10)_ Wave your hand over something to understand its meaning.  
* __Shrink:__ _(Cost: 2, Charisma Cost: 14)_ Shrink an object or entity to a desired size. Unwilling entities can attempt a saving throw every turn. Concentration.  
* __Strange Tongue:__ _(Cost: 2, Charisma Cost: 10)_ You and your party speak in a tongue only you can understand. Concentration.  
* __Telepathic communication:__ _(Cost: 2, Charisma Cost: 10)_ Create a ward on an entity to allow you to communicate with them via thought. Works up to 1 half mile. Lasts 6 hours. Concentration.  
* __Summon Greater Familiar:__ _(Cost: 0, Charisma Cost: 8)_ Summon a moderately sized familiar with 20 health. The familiar obeys your every command, and can attack for 1d8 damage. If a familiar dies, it cannot be resummoned until the next day.  
  
__Tier 3:__  
* __Pocket Dimension:__ _(Cost: 3, Charisma Cost: 15)_ Create a door into your own, private pocket dimension. The dimension is 30x30x30 feet, and persists over time. Once you are in the pocket dimension, you can always exit. For every 10 minutes you are in the pocket dimension, Make a D8 inner fire saving throw. If you fail, you are ejected from the pocket dimension.  
* __Fuse into Familiar:__ _(Cost: 3, Charisma Cost: 14)_ Touch your familiar to fuse with it. Lasts for up to 10 minutes, before you reappear where your familiar stands.  
* __Gateway:__ _(Cost: 3, Charisma Cost: 15)_ Create a doorway from one location to another within 300 feet. Both ends must be in view for the spell to be cast. Concentration.  
* __Mind Blast:__ _(Cost: 3, Charisma Cost: 14)_ Fire a blast of psychic energy at an enemy. Do 1d20 damage and grapple them if you roll above a 10. They can attempt an inner fire saving throw against your spell power each turn at a cost of 1d6 health if they fail. Concentration.  
* __Polymorph:__ _(Cost: 3, Charisma Cost: 15)_ Transform an entity into a medium or small creature of your choice if they fail an inner fire saving throw against your spell power. They can attempt a saving throw every turn.  
  
__Tier 4:__  
* __Blink to Familiar:__ _(Cost: 4, Charisma Cost: 16)_ Instantly teleport to your familiar.  
* __Fly:__ _(Cost: 4, Charisma Cost: 14)_ Allow yourself or another entity to fly. Concentration.  
* __Illusory Terrain:__ _(Cost: 4, Charisma Cost: 12)_ Make 100x100 yards of terrain look any way you choose.  
* __Lift:__ _(Cost: 4, Charisma Cost: 16)_ Force up to four entities to make dexterity saving throws against your spell power. For each success, lift the entity into the air with your magic and hurl them. Impacts cause 3d12 damage.  
* __Living Armor:__ _(Cost: 0, Charisma Cost: 8)_ Infuse your armor with life, so that when you hit zero hit points, it can move on its own. In this state, your armor has 8 hit points, and access to anything on your person.  
  
__Tier 5:__  
* __Black Hole:__ _(Cost: 5, Charisma Cost: 18)_ Lasts 3 turns. Summon a black hole at any point within 100 feet of yourself on the battlefield. Any entity within 50 feet of the black hole must make a strength saving throw or be dragged 15 feet towards it. At the start of its turn, each entity in the black hole's radius must repeat this check. On success, the entity may move five feet away from the black hole. Entities that touch the black hole take 4d20 damage at the start of each turn. A black hole may not be summoned on a space occupied by an enemy.  
* __Control Weather:__ _(Cost: 5, Charisma Cost: 20)_ Change the weather in a region.  
* __Firestorm:__ _(Cost: 5, Charisma Cost: 18)_ Fire bursts from your body, spiraling in every direction. Does 3d20 damage to all entities within 25 feet of you if they fail a dc 10 dexterity saving throw. If the succeed, they take half damage. Enemies that fail a saving throw are burned, and take 1d6 at the start of each turn until they are healed.  
* __Grand Illusion:__ _(Cost: 5, Charisma Cost: 16)_ Conjure an illusory object, which can move/speak, and think for itself. Cannot be bigger than a mountain. Concentration.  
* __Greater Gateway:__ _(Cost: 5, Charisma Cost: 16)_ Create up to a 20x20 foot gateway from your current position to another location within five  miles. The creation of a gateway makes an explosive bang. It takes one full turn or five minutes to cast this spell properly. If improperly cast, the cost of this spell is 12, and the gateway lets out at an undetermined location within one mile. Concentration.  
* __Summon Major Familiar:__ _(Cost: 1, Charisma Cost: 8)_ Summon a large familiar with 40 health. The familiar obeys your every command, and can make 2 attacks for 2d10 damage. If a familiar dies, it cannot be resummoned until the next day.  

  
### The Tome Of The Ancients
  
__Tier 6:__  
* __Massive Levitation:__ _(Cost: 10)_ Requires gemstones worth 200,000 gold and at least five master spellcasters to assist you. Requires 12 hours of casting time. Levitate anything up to the size of a mountain.  
* __True Enchantment:__ _(Cost: 6)_ You are now able to make truly enchanted items. It takes days to make an enchanted object, and may involve multiple roles.  
* __Teleportation Circle:__ _(Cost: 8)_ Requires diamonds, gold, and jewels valuing 50,000 gold. Craft a circle of teleportation. Any circle of teleportation may link to another you have created or have access to.  

  
### The Wizard's Addendum
  
__Tier 0:__  
* __Eat slugs:__ _(Cost: 0)_ Fill a person's mouth with slugs. If they fail an inner fire saving throw against your spell power, they are staggered, and make their next action with disadvantage.  
* __Enchanting:__ _(Cost: 0)_ Once per evening, you may attempt to imbue an object with one of your spells. Works best if the object has at least one gemstone on it. The spell may be one or more use. Duration it is left in the object is dependent on the success of the enchanting. The cost of this spell is equivalent to the cost of the spell being added to the gemstone.  
* __Firecrackers:__ _(Cost: 0)_ Summon firecrackers to a position you can see.  
* __Minor Manifest Will:__ _(Cost: 0)_ Conjure a small, nonliving object of no more than 1 pound. Only one can be conjured at a time. The object must be something you have seen. The object and its effects will disappear when you stop concentrating on it. Concentration.  
* __Summoning Spell:__ _(Cost: 0)_ Summon an object of up to 20 pounds to you.  
  
__Tier 1:__  
* __Catch Soul:__ _(Cost: 1, Charisma Cost: 10)_ Capture a soul in a diamond valued at 100 gold pieces. Soul gems can be used as a power source when creating magic items and in certain rituals. They may also be utilized by necromancers to cast spells.  
* __Greater Manifest Will:__ _(Cost: 1)_ Conjure a small, nonliving object of no more than 20 pounds. Only one can be conjured at a time. The object must be something you have seen. The object and its effects will disappear when you stop concentrating on it. Concentration.  
* __Imitate:__ _(Cost: 1)_ Imitate the voice of a person you have met. Lasts for one hour.  
* __Remove Footprints:__ _(Cost: 1)_ Remove all footprints you and those with you have made over the past 6 hours.  
* __Unburnt:__ _(Cost: 1)_ Allow yourself or another entity to pass through fire unharmed. Concentration. Can be used as a reaction. To use as a reaction, you must succeed in a contested dexterity check.  
  
__Tier 2:__  
* __Invisibility:__ _(Cost: 2)_ Make yourself or another entity or object completely invisible. Gives advantage on stealth checks. Concentration.  
* __Rain of Arrows:__ _(Cost: 2, Charisma Cost: 12)_ With a chorus of twangs, a flight of arrows streak past and around you, targeting all entities within a 20 foot radius of your choosing and dealing 2d10 damage.  
* __Scry:__ _(Cost: 2)_ Using a mirror, pool or water, or other reflective surface, view a person or place that you know as if through a one way window. Concentration.  
* __Statue:__ _(Cost: 2, Charisma Cost: 12)_ Harden to become a statue. While you are a statue, you take one quarter damage from any attacks. On your next turn, you may revert from being a statue at the cost of your movement.  
* __Suppress Item:__ _(Cost: 2, Charisma Cost: 12)_ Concentration. Make a check against a magic item's spell power. On success, suppress the magic item's power.  
  
__Tier 3:__  
* __Dominate:__ _(Cost: 3)_ Dominate an enemy if they fail a contested saving throw against your spell power, causing them to fight for you. Each turn or every hour they can attempt a saving throw, but take 1d10 damage.  
* __Door step:__ _(Cost: 3, Charisma Cost: 14)_ As you place your hand on a door handle, magic flows through you, opening a portal to another door within 100 feet of you.  
* __Greater Imitate:__ _(Cost: 3)_ Imitate the voice of someone or something you haven't met.  
* __Igna Bokak:__ _(Cost: 3)_ Summon a flaming bird to attack your foes. The bird does 1d20 damage, to a randomly selected enemy each turn, and has 20 hit points. It stays for 3 turns. If out of battle, the bird stays for 10 minutes.  
* __Octahedral Barrier:__ _(Cost: 3, Charisma Cost: 14)_ Reaction. In a rush of energy, a barrier with up to a 20 foot radius forms around you and any allies in close proximity, protecting you from an attack.  
* __Wall of Fire:__ _(Cost: 3, Charisma Cost: 14)_ Create a wall up to 40 feet high and 100 feet long of fire. Any entity that moves through the flames takes 2d20 damage.  
  
__Tier 4:__  
* __Banish:__ _(Cost: 4)_ If the target fails an inner fire saving throw against your spell power, it is banished to a pocket dimension. The affected enemy may repeat the saving throw after each turn, or, if out of combat, every 10 minutes.  
* __Inanimate Aid:__ _(Cost: 4, Charisma Cost: 16)_ With a chorus of clangs, every inanimate object within twenty feet comes to life to fight for you, throwing themselves at any enemies in close proximity.  
* __Major manifest will:__ _(Cost: 4)_ Conjure a nonliving object of no more than 200 pounds. Only one can be conjured at a time. The object must be something you have seen. The object and its effects will disappear 5 minutes after you lose concentration on it. Concentration.  
* __Teleport:__ _(Cost: 4)_ Instantly transport yourself and anyone touching you up to 1 mile. In order to cast, you must concentrate for one minute or one round of combat. If concentration is broken, you are immediately teleported to a random location.  
  
__Tier 5:__  
* __Invulnerability:__ _(Cost: 3)_ Make yourself or another entity invulnerable for 3 turns.  
* __Reverse Gravity:__ _(Cost: 3)_ Reverse the gravity in a space up to 1000 square feet.  
* __Storm of Swords:__ _(Cost: 3)_ Conjure 6 swords of pure arcane energy around yourself. Each of the swords has 20 hit points. Each turn, each remaining sword may attack for 1d6 damage. If an enemy physically attacks you, you may make a contested dexterity check to command the remaining swords to parry. On a successful parry, all but the parrying sword may attack the enemy as a reaction.  


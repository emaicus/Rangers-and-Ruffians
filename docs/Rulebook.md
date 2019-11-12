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
   * [Stats](#stats)  
     * [Strength](#strength)  
     * [Dexterity](#dexterity)  
     * [Intelligence](#intelligence)  
     * [Inner Fire](#inner-fire)  
     * [Charisma](#charisma)  
     * [Perception](#perception)  
     * [Luck](#luck)  
     * [Stat Values](#stat-values)  
     * [Diminishing Returns: The Most Confusing Rule in Rangers and Ruffians](#diminishing-returns-the-most-confusing-rule-in-rangers-and-ruffians)  
       * [Why are Diminishing Returns Important?](#why-are-diminishing-returns-important?)  
     * [Bonus Stat: Health Die](#bonus-stat-health-die)  
     * [Abilities](#abilities)  
     * [Action Points](#action-points)  
     * [Spell Power](#spell-power)  
   * [Combat](#combat)  
     * [Initiative](#initiative)  
     * [Your Turn](#your-turn)  
       * [Actions](#actions)  
       * [Offhand Actions](#offhand-actions)  
       * [Movement](#movement)  
       * [Free Actions](#free-actions)  
       * [The Dash Action](#the-dash-action)  
     * [Attacking](#attacking)  
     * [Critical Hits](#critical-hits)  
     * [Weapons](#weapons)  
     * [Combat Abilities](#combat-abilities)  
     * [Hitting Zero Health](#hitting-zero-health)  
       * [Reversible Death](#reversible-death)  
       * [Irreversible Death](#irreversible-death)  
   * [Health, Rest, and Healing](#health,-rest,-and-healing)  
     * [Rest](#rest)  
   * [Magic](#magic)  
     * [Spell Levels](#spell-levels)  
     * [Learning new Spells](#learning-new-spells)  
   * [Leveling Up](#leveling-up)  
     * [Increasing Your Maximum Health](#increasing-your-maximum-health)  
     * [Odd Levels: New Abilities](#odd-levels-new-abilities)  
     * [Even Levels: New Stats](#even-levels-new-stats)  
     * [New Spells](#new-spells)  
   * [Building a Character](#building-a-character)  
     * [Health Dice Pieces](#health-dice-pieces)  
   * [Races](#races)  
   * [Classes](#classes)  
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
```   
Poohbah: The door before you stands locked. The corridors of the castle are quiet, save for the steady dripping of water from the ceilings.   
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
```   
  
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
```   
If the players are having fun, you are doing a good job.   
```   
  

  
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
  

  
## Stats
Characters in RnR are made up of __Stats__ and __Abilities__. __Stats__ attempt   
to capture the physical, mental, and social prowess of a character. A relevant stat   
is almost always added to the result of a check. The seven stats in Rangers and   
Ruffians are as follows:   
  

  
### Strength
__Strength__ is defined as raw power of the body. Strength influences the way that   
you play the game in three ways:   
1. __Strength is added to strength checks.__ You enter a dungeon, and see   
  a friend trapped in a cell. You desperately want to get them out, so you decide   
  to bend the bars. In this scenario, you add your strength to a ```d20``` roll.   
2. __Strength affects strength weapon damage.__ In combat, your strength is added to   
  the amount of damage you do with strength based weapons such as warhammers, great-axes,   
  and clubs.   
3. __Strength affects the type of armor you can wear.__ The stronger you are, the heavier   
  the armor that you can wear.   
  

  
### Dexterity
__Dexterity__ is defined as mobility, nimbleness, and ability with the body.   
Dexterity affects the way that you play the game in two ways:   
1. __Dexterity is added to dexterity checks.__ You are chasing a fleeing thief across   
  the rooftops of a city. You come up to a gap, and have to jump! In this scenario,   
  you would add your dexterity to a ```d20``` roll.   
2. __Dexterity affects your dexterity weapon damage.__ In a combat scenario, dexterity   
  is added to the amount of damage you do with dexterity based weapons, such as spears,   
  daggers, and falchions.   
  

  
### Intelligence
__Intelligence__ is defined as raw aptitude with the mind. Intelligence affects the   
way that you play the game in two key ways.   
1. __Intelligence is added to intelligence checks.__   
2. __Intelligence affects your number of action points.__ In Rangers and Ruffians, action points   
  are treated as a resource which is used to perform special abilities or to cast spells. This means   
  that the more action points you have, the more abilities you can use or spells you can cast. Action   
  points are further detailed in the [Action Points](#action-points) section.   
  

  
### Inner Fire
__Inner Fire__ is defined as mental fortitude, resolve, and strength of will. Inner Fire affects the way   
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
  

  
### Charisma
__Charisma__ is defined as force of personality, or how charming your character can be. Charisma can   
affect the way you play the game in two ways:   
1. __Charisma is added to charisma checks.__ You speak with the local innkeeper and have a feeling that   
  he's keeping something from you. You don't think that he's a dangerous person, but rather that someone   
  or *something* is stopping him. In this scenario, you would want high charisma, so that you can convince   
  him to help you despite the risk.   
2. __(Conditional) If you are playing a Sorcerer, Charisma determines whether or not your spells succeed or   
  fail.__ Further detailed in the [Sorcerer](#sorcerer) section.   
  

  
### Perception
__Perception__ determines how likely it is your character will notice things going on in the world around them.   
It affects the way you play the game in two ways:   
1. __Perception is added to perception checks.__ You are riding through the forest at night. Little do you know,   
   a trio of goblins lie in ambush. In this scenario, you would want high perception.   
2. __Perception is added to combat initiative.__ When in combat, __Initiative__ is rolled to determine turn order.   
  Perception is added to such checks, so that characters who are better at reading a situation tend to go first.   
  Initiative is further detailed in the [Initiative](#initiative) section.   
  

  
### Luck
When all else fails, there's always luck! Luck is a special stat, and is the only stat that cannot go negative.   
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
Every character in Rangers and Ruffians has a __Health Die.__ When a character levels up (detailed in the   
section [Leveling Up](#leveling-up)), they roll their health dice, and ```1d4``` and add the numbers rolled   
to their maximum health.   
  

  
### Abilities
Abilities are special things that a character is capable of. Abilities include special   
[advantages and disadvantages](#advantage-and-disadvantage), as well as special attacks   
that can be made in combat. Some abilities cost one or more [Action Points](#action-points)   
to perform.   
  

  
### Action Points
__Action Points__ can be spent to perform special abilities and to cast spells in Rangers and Ruffians.   
A characters total number of Action Points is equal to ```5 + their Intelligence```. So if a characters   
intelligence is ```-3```, they have ```2``` Action Points. If their intelligence is ```2```, they have ```7```   
Action Points. Spent Action Points are restored after resting. See the [Resting](#resting)   
section for more details.   
  

  
### Spell Power
A character's __Spell Power__ determines how likely it is that an enemy will succumb to the affects   
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
  

  
#### Movement
On each turn, you are able to make 15 feet of movement. This movement can be decomposed however   
you wish. For example, you might drink a potion as an offhand action, walk 5 feet forward, lift   
a cauldron as an action, and then walk ten 10 feet to the right.   
  

  
#### Free Actions
It costs neither an action nor an offhand action to perform very simple actions such as shouting   
out to your allies, pointing at something, or sheathing or unsheathing a blade. It is up to your   
Poohbah's discretion what counts as a Free Action.   
  

  
#### The Dash Action
You are able to spend your action moving an additional 15 feet.   
  

  
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
to cast spells. This section details the different levels of spells, as well as how learning   
new spells works.   
  

  
### Spell Levels
There are 6 spell levels in Rangers and Ruffians, ranging from ```Level 0``` to ```Level 5```.   
In general, lower level spells cost fewer action points to use than higher level spells.   
Access to new spell levels is treated as an ability, which is gained at certain levels upon   
[Leveling Up](#leveling-up).   
  

  
### Learning new Spells
Mages can learn new spells in two ways. First, a mage passively learns new spells upon   
[Leveling Up](#leveling-up). Second, your Poohbah may present you with a spell book as   
during your game. A spell book may contain a specific spell hand selected by the Poohbah.   
If the spell is of a higher level than you could normally learn, you may learn it, but   
you do not learn spells of that level upon leveling up. If the spell book does not contain   
a specific spell, you may use it to learn any one spell of up to the max spell level that you   
are able to learn.   
  

  
## Leveling Up
There are 16 levels in Rangers and Ruffians, ranging from ```Level 0``` to ```Level 15.``` These   
Levels neatly fit into 3, 5 level arcs.   
  
| Level Range    | Arc           |   
| -------------- |---------------|   
| 0 - 5          | Burgeoning adventurer. You are small, and the world is a large, scary place. |   
| 6 - 10         | Hero. You begin to make real change in the land that you are in.             |   
| 11 - 15        | Hero of Legend. You begin fighting ancient evils. The fate of the world may be in your hands. |   
  

  
### Increasing Your Maximum Health
Every time that you level up, you get to roll your health die + ```1d4``` and add add the   
result to your maximum health. For example, if your maximum health is ```26``` and your   
health die is ```1d8``` the following might occur:   
1. You roll a ```3``` on your health die.   
2. You roll a ```2``` on your 1d4.   
3. Your new maximum health is ```26 (your old max health) + 3 (your health die roll) + 2 (your d4 roll) = 31```.   
  

  
### Odd Levels: New Abilities
When you level up, you get better at being your class. That is to say, you are a better _Rouge_ or _Knight_   
or _Gunslinger_ or _Bard_ than you were before. When you reach an odd level, you receive new abilities, allowing   
you to perform all new actions or granting you new advantages.   
  

  
### Even Levels: New Stats
When you reach an even level, you get ```2``` __Stat Points__ to spend. You can spend these to increase your stats.   
Review the [Effective Stats](#effective-stats) section for details on how this works.   
Alternatively instead of increasing your stats, you are able to instead take a new [Skill](#skills). See the   
[Skills](#skills) section for more details.   
  
  

  
### New Spells
If you are a magic user, you are able to learn 1 new spell of _every_ spell level that you know each time you level up.   
This means that if you know level 0, 1, and 2 spells, you get to learn 3 spells: 1 level 0 spell, 1 level 1 spell, and 1 level 2 spell.   
  
  

  
## Building a Character
Now that you understand (or at least glanced at) the rules of Rangers and Ruffians, you can now get started building   
your character. In terms of gameplay, a character is made up of two major components: a __Race__ and a __Class.__   
A Race represents the racial background that your character comes from. Your choice of race grants you base   
abilities and stats, and can greatly affect the way that you interact with the world. If you choose to play a   
tiny _Sprout_, you might ride atop the shoulders of the another player's _Orc_ character.   
  
__Class,__ meanwhile, affects your role within your adventuring party. A _Rouge_ might spend their time   
scouting, skulking, and sneaking. A _Highborn_ might use their high Charisma to barter for goods or   
get information out of an important non-player character. A _Knight_ will spend their time in combat   
shielding and soaking up damage for their more-squishy counterparts.   
When you level up in Rangers and Ruffians, it is your class that grants you new abilities.   
  

  
### Health Dice Pieces
Races and Classes each have ```Health Dice Pieces```. When building a character,   
you add these pieces together to get your total health dice. For example,   
if you race has ```2``` health dice pieces, and your class has ```4```,   
your health dice would be ```6```.   
  

  
## Races

  
## Classes

  
## Races

  
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
  * __Courageous Blow:__ _(Cost 1)_ Add your Inner Fire to an attack. At level 5, double this. At level 8, triple it.   
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
  * __Bellow:__ _(Cost 1)_ On your turn, spend one spell point to unleash a mighty bellow. All who hear must make an Spell Power save of be frightened.   
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
  * __Become Mist:__ _(Cost 1)_ Spend one spell point to become mist to have an attack pass right through you as a reaction.   
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
  * __Expert Fletcher:__ All arrows now cost 1 spell point less.   
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
  * __Learning Spells:__ New spells or techniques are obtained by leveling up or by finding spellbooks or scrolls in the world. A spellbook may contain a specific spell, or a maximum spell level. Spellbooks with a maximum spell level contain one spell of your choice from the spellbooks that you can learn from with a level up to the spellbook's maximum spell level.   
  * __Learn Spells:__ Each time you level up, learn one new spell of each spell level that you have access to. Spells must be learned from one of your spellbooks.   
* __Choices:__   
  * __Spell Choice:__ At the start of your journey, you know 2 extra level zero spells.   
  * __My Father's Oboe:__ You are proficient and start with two instruments of your choice.   
* __General Abilities:__   
  * __Level Zero Spells:__ You have achieved a basic knowledge of the arcane, and may now learn level zero spells from any of your spellbooks.   
* __Starting Items:__   
  * __The Bard's Songbook:__ You can learn spells from the Bard's Songbook.   
* __Advantages:__   
  * __Boozehound:__ You have a very high tolerance for alcohol. Do not take disadvantage when drunk.   
  * __Regular Patron:__ You may add 1d6 to charisma checks made in a tavern.   
  * __Slight of Hand:__ You have advantage when performing slight of hand actions.   
  
__Level 0 Bard__   
  
* __Rules:__   
  * __Learning Spells:__ New spells or techniques are obtained by leveling up or by finding spellbooks or scrolls in the world. A spellbook may contain a specific spell, or a maximum spell level. Spellbooks with a maximum spell level contain one spell of your choice from the spellbooks that you can learn from with a level up to the spellbook's maximum spell level.   
  * __Learn Spells:__ Each time you level up, learn one new spell of each spell level that you have access to. Spells must be learned from one of your spellbooks.   
  
  
* __Choices:__   
  * __My Father's Oboe:__ You are proficient and start with two instruments of your choice.   
  
  
* __General Abilities:__   
  * __Level Zero Spells:__ You have achieved a basic knowledge of the arcane, and may now learn level zero spells from any of your spellbooks.   
  
  
* __Starting Items:__   
  * __The Bard's Songbook:__ You can learn spells from the Bard's Songbook.   
  
  
* __Advantages:__   
  * __Regular Patron:__ You may add 1d6 to charisma checks made in a tavern.   
  * __Slight of Hand:__ You have advantage when performing slight of hand actions.   
  
  
__Level 1 Bard__   
  
* __General Abilities:__   
  * __Level One Spells:__ Your powers are growing. You may now learn level one spells from any of your spellbooks.   
  * __Minor Restful Melody:__ _(Cost 1)_ When your party is resting, you may perform a song for them which grants them an extra 1d8 healing.   
  
  
* __Combat Abilities:__   
  * __One up the Sleeve:__ _(Cost 1)_ You may make a throwing knife attack as an offhand action.   
  
  
__Level 2 Bard__   
  
* __Choices:__   
  * __Stat Increase:__ You gain two stat points to add to a stat or stats of your choosing.   
  
  
__Level 3 Bard__   
  
* __General Abilities:__   
  * __Spell Coin:__ You have one spell coin, which may store a spell of up to first level. Any person who rubs the coin may cast the spell as an offhand action. Each day, you may re-summon the coin to yourself, and may put a spell into it free of cost.   
  
  
* __Advantages:__   
  * __Nimble Fingers:__ You have advantage on dexterity and stealth checks made while stealing.   
  
  
__Level 4 Bard__   
  
* __Choices:__   
  * __Stat Increase:__ You gain two stat points to add to a stat or stats of your choosing.   
  
  
* __General Abilities:__   
  * __Level Two Spells:__ You have graduated from novice to proficient! You may now learn level two spells from any of your spellbooks.   
  
  
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
  * __Level Three Spells:__ Magical energy flows through you. You may now learn level three spells from any of your spellbooks.   
  * __Greater Restful Melody:__ _(Cost 1)_ When your party is resting, you may perform a song for them which grants them an extra 2d8 healing.   
  
  
* __Combat Abilities:__   
  * __Imbue Weapon:__ _(Cost 1)_ As an offhand action, add 1d6 elemental damage to your weapon at the cost of 1 spell point. Lasts 1 battle or 1 hour.   
  
  
__Level 8 Bard__   
  
* __Choices:__   
  * __Stat Increase:__ You gain two stat points to add to a stat or stats of your choosing.   
  
  
__Level 9 Bard__   
  
* __General Abilities:__   
  * __Greater Spell Coin:__ You have learned the art of storing second level spells in your spell coins.   
  
  
* __Combat Abilities:__   
  * __Greater Imbue Weapon:__ _(Cost 1)_ As an offhand action, add 1d8 elemental damage to your weapon at the cost of 1 spell points. Lasts 1d4 turns.   
  
  
__Level 10 Bard__   
  
* __Choices:__   
  * __Stat Increase:__ You gain two stat points to add to a stat or stats of your choosing.   
  
  
* __General Abilities:__   
  * __Level Four Spells:__ You are a master of your spellcraft. You can now learn level four spells from any of your spellbooks.   
  
  
__Level 11 Bard__   
  
* __General Abilities:__   
  * __Major Restful Melody:__ _(Cost 1)_ When your party is resting, you may perform a song for them which grants them an extra 3d8 healing.   
  
  
__Level 12 Bard__   
  
* __Choices:__   
  * __Stat Increase:__ You gain two stat points to add to a stat or stats of your choosing.   
  
  
__Level 13 Bard__   
  
* __General Abilities:__   
  * __Additional Spell Coin:__ You have an additional spell coin.   
  * __Level Five Spells:__ You have achieved the highest form of sorcery, and are a mage to be reckoned with. You can now learn level five spells from any of your spellbooks.   
  
  
__Level 14 Bard__   
  
* __Choices:__   
  * __Stat Increase:__ You gain two stat points to add to a stat or stats of your choosing.   
  
  
__Level 15 Bard__   
  
* __General Abilities:__   
  * __Major Spell Coin:__ You have learned the art of storing third level spells in your spell coins.   
  
  
  
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
  * __Learning Spells:__ New spells or techniques are obtained by leveling up or by finding spellbooks or scrolls in the world. A spellbook may contain a specific spell, or a maximum spell level. Spellbooks with a maximum spell level contain one spell of your choice from the spellbooks that you can learn from with a level up to the spellbook's maximum spell level.   
  * __Learn Spells:__ Each time you level up, learn one new spell of each spell level that you have access to. Spells must be learned from one of your spellbooks.   
* __Spellbooks:__   
  * __The Book of Healing:__ You are able to learn spells from the Book of Healing.   
* __Choices:__   
  * __Spell Choice:__ At the start of your journey, you know 2 extra level zero spells.   
  * __Pledge:__ At the start of your journey, you may select a deity to pledge yourself to.   
* __General Abilities:__   
  * __Level Zero Spells:__ You have achieved a basic knowledge of the arcane, and may now learn level zero spells from any of your spellbooks.   
  
__Level 0 Cleric__   
  
* __Rules:__   
  * __Learning Spells:__ New spells or techniques are obtained by leveling up or by finding spellbooks or scrolls in the world. A spellbook may contain a specific spell, or a maximum spell level. Spellbooks with a maximum spell level contain one spell of your choice from the spellbooks that you can learn from with a level up to the spellbook's maximum spell level.   
  * __Learn Spells:__ Each time you level up, learn one new spell of each spell level that you have access to. Spells must be learned from one of your spellbooks.   
  
  
* __Spellbooks:__   
  * __The Book of Healing:__ You are able to learn spells from the Book of Healing.   
  
  
* __Choices:__   
  * __Pledge:__ At the start of your journey, you may select a deity to pledge yourself to.   
  
  
* __General Abilities:__   
  * __Level Zero Spells:__ You have achieved a basic knowledge of the arcane, and may now learn level zero spells from any of your spellbooks.   
  
  
__Level 1 Cleric__   
  
* __General Abilities:__   
  * __Level One Spells:__ Your powers are growing. You may now learn level one spells from any of your spellbooks.   
  
  
* __Combat Abilities:__   
  * __Purge Decay:__ Gain 1d6 damage when fighting the undead.   
  
  
__Level 2 Cleric__   
  
* __Choices:__   
  * __Stat Increase:__ You gain two stat points to add to a stat or stats of your choosing.   
  
  
__Level 3 Cleric__   
  
* __Actions:__   
  * __Minor Offhand Spell:__ You may cast a level zero spell as an offhand action.   
  
  
* __Combat Abilities:__   
  * __Last Ditch Prayer:__ _(Cost 1)_ Say a fervent prayer to your deity, and add 1d8 to your roll.   
  
  
__Level 4 Cleric__   
  
* __Choices:__   
  * __Stat Increase:__ You gain two stat points to add to a stat or stats of your choosing.   
  
  
* __General Abilities:__   
  * __Level Two Spells:__ You have graduated from novice to proficient! You may now learn level two spells from any of your spellbooks.   
  
  
__Level 5 Cleric__   
  
* __Combat Abilities:__   
  * __Feint:__ _(Cost 1)_ You may roll a d20 against an enemy attack. Reduce the attack by the amount rolled.   
  
  
__Level 6 Cleric__   
  
* __Actions:__   
  * __Greater Offhand Spell:__ You may cast a level one spell as an offhand action.   
  
  
* __Choices:__   
  * __Stat Increase:__ You gain two stat points to add to a stat or stats of your choosing.   
  
  
__Level 7 Cleric__   
  
* __Actions:__   
  * __Offhand Attack:__ You may use an offhand action to make an attack.   
  
  
* __General Abilities:__   
  * __Level Three Spells:__ Magical energy flows through you. You may now learn level three spells from any of your spellbooks.   
  
  
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
  * __Level Four Spells:__ You are a master of your spellcraft. You can now learn level four spells from any of your spellbooks.   
  
  
__Level 11 Cleric__   
  
* __General Abilities:__   
  * __True Heal:__ Re-roll any ones or twos rolled while healing.   
  
  
__Level 12 Cleric__   
  
* __Actions:__   
  * __Major Offhand Spell:__ You may cast a level two spell as an offhand action.   
  
  
* __Choices:__   
  * __Stat Increase:__ You gain two stat points to add to a stat or stats of your choosing.   
  
  
__Level 13 Cleric__   
  
* __General Abilities:__   
  * __Level Five Spells:__ You have achieved the highest form of sorcery, and are a mage to be reckoned with. You can now learn level five spells from any of your spellbooks.   
  
  
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
  
  
Gaurdians of nature, most druids prefer to live in tribes in the forests, mountains, prairie, tundra, or desert. Druid's command powerful nature based magic, which they use to smite those who threaten them, their friends, or their home. Druids utilize intelligence based spell points to cast spells, and are a good match for players interested in playing a mage. As you build your druid, consider where they came from. Why are they so attached to nature? How does their attachment to the natural world change how they think? How do they react to large towns and cities? What do they wear, and how do they speak? How do they feel about other types of magic? Why are they on their adventure? How do they feel about eating meat? What are their values? What do they think the place of people is in the world? How will being a druid change the way you interact with your party?   
  
|STR|DEX|INT|INF|CHR|PER|LUK|HD|   
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|   
|-2|-1|0|2|-3|1|1|4|   
  
__Druid Abilities:__   
* __Rules:__   
  * __Learning Spells:__ New spells or techniques are obtained by leveling up or by finding spellbooks or scrolls in the world. A spellbook may contain a specific spell, or a maximum spell level. Spellbooks with a maximum spell level contain one spell of your choice from the spellbooks that you can learn from with a level up to the spellbook's maximum spell level.   
  * __Learn Spells:__ Each time you level up, learn one new spell of each spell level that you have access to. Spells must be learned from one of your spellbooks.   
* __Spellbooks:__   
  * __Novice Spellbook:__ You are able to learn spells from the Novice Spellbook.   
  * __The Druid's Field Guide:__ You can learn spells from the Druid's Field Guide.   
* __Choices:__   
  * __Spell Choice:__ At the start of your journey, you know 2 extra level zero spells.   
* __General Abilities:__   
  * __Level Zero Spells:__ You have achieved a basic knowledge of the arcane, and may now learn level zero spells from any of your spellbooks.   
  
__Level 0 Druid__   
  
* __Rules:__   
  * __Learning Spells:__ New spells or techniques are obtained by leveling up or by finding spellbooks or scrolls in the world. A spellbook may contain a specific spell, or a maximum spell level. Spellbooks with a maximum spell level contain one spell of your choice from the spellbooks that you can learn from with a level up to the spellbook's maximum spell level.   
  * __Learn Spells:__ Each time you level up, learn one new spell of each spell level that you have access to. Spells must be learned from one of your spellbooks.   
  
  
* __Spellbooks:__   
  * __Novice Spellbook:__ You are able to learn spells from the Novice Spellbook.   
  * __The Druid's Field Guide:__ You can learn spells from the Druid's Field Guide.   
  
  
* __General Abilities:__   
  * __Level Zero Spells:__ You have achieved a basic knowledge of the arcane, and may now learn level zero spells from any of your spellbooks.   
  
  
__Level 1 Druid__   
  
* __General Abilities:__   
  * __Level One Spells:__ Your powers are growing. You may now learn level one spells from any of your spellbooks.   
  
  
__Level 2 Druid__   
  
* __Choices:__   
  * __Stat Increase:__ You gain two stat points to add to a stat or stats of your choosing.   
  
  
__Level 3 Druid__   
  
* __Actions:__   
  * __Minor Offhand Spell:__ You may cast a level zero spell as an offhand action.   
  
  
__Level 4 Druid__   
  
* __Choices:__   
  * __Stat Increase:__ You gain two stat points to add to a stat or stats of your choosing.   
  
  
* __General Abilities:__   
  * __Level Two Spells:__ You have graduated from novice to proficient! You may now learn level two spells from any of your spellbooks.   
  
  
__Level 5 Druid__   
  
* __Advantages:__   
  * __Tracker:__ You are an excellent tracker, and have advantage when looking for trails and sign of passage.   
  
  
__Level 6 Druid__   
  
* __Actions:__   
  * __Greater Offhand Spell:__ You may cast a level one spell as an offhand action.   
  
  
* __Choices:__   
  * __Stat Increase:__ You gain two stat points to add to a stat or stats of your choosing.   
  
  
__Level 7 Druid__   
  
* __Actions:__   
  * __Offhand Attack:__ You may use an offhand action to make an attack.   
  
  
* __General Abilities:__   
  * __Level Three Spells:__ Magical energy flows through you. You may now learn level three spells from any of your spellbooks.   
  
  
__Level 8 Druid__   
  
* __Choices:__   
  * __Stat Increase:__ You gain two stat points to add to a stat or stats of your choosing.   
  
  
__Level 9 Druid__   
  
* __General Abilities:__   
  * __Ascend:__ Once per day, you may enter the ascended state. While ascended you immediately gain 5 spell points. he ascended state lasts for 3 turns or five minutes. When you fall out of the ascended state, you are fatigued. Immediately take 4d10 damage, and have disadvantage in all things until you are able to sleep. If you are killed in the ascended state, you cannot be resurrected.   
  
  
__Level 10 Druid__   
  
* __Choices:__   
  * __Stat Increase:__ You gain two stat points to add to a stat or stats of your choosing.   
  
  
* __General Abilities:__   
  * __Level Four Spells:__ You are a master of your spellcraft. You can now learn level four spells from any of your spellbooks.   
  
  
__Level 11 Druid__   
  
* __General Abilities:__   
  * __Ascended Flight:__ While in the Ascended state, you may take flight as an offhand action.   
  
  
__Level 12 Druid__   
  
* __Actions:__   
  * __Major Offhand Spell:__ You may cast a level two spell as an offhand action.   
  
  
* __Choices:__   
  * __Stat Increase:__ You gain two stat points to add to a stat or stats of your choosing.   
  
  
__Level 13 Druid__   
  
* __General Abilities:__   
  * __Level Five Spells:__ You have achieved the highest form of sorcery, and are a mage to be reckoned with. You can now learn level five spells from any of your spellbooks.   
  
  
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
  * __Bull Rush:__ _(Cost 1)_ Spend 1 spell point to burst forward 15 feet, doing 1d6 damage to everyone you hit and causing them to fall prone if they fail a spell power saving throw.   
  
  
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
  * __Gumption:__ You have gumption points equal to your spell points. Spend one to add 1d10 to a check.   
  
  
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
  * __Learn Fighting Techniques:__ Each time you level up, learn one fighting technique from each fighting technique level you have access to.   
* __Spellbooks:__   
  * __The Book of Chi:__ You may select 2 combat techniques and 2 general techniques from the Book of Chi at the start of your journey.   
* __Choices:__   
  * __Starting Fighting Techniques:__ Begin your journey with two standard fighting techniques.   
* __General Abilities:__   
  * __Fighting Techniques:__ You may learn a new fighting technique from the book of chi.   
  
__Level 0 Monk__   
  
* __Rules:__   
  * __Learn Fighting Techniques:__ Each time you level up, learn one fighting technique from each fighting technique level you have access to.   
  
  
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
  * __Learn Spells:__ Each time you level up, learn one new spell of each spell level that you have access to. Spells must be learned from one of your spellbooks.   
  * __Soul Harvest:__ You may harvest 1 soul from a sentient entity that has died within twenty four hours.   
  * __Learning Spells:__ New spells or techniques are obtained by leveling up or by finding spellbooks or scrolls in the world. A spellbook may contain a specific spell, or a maximum spell level. Spellbooks with a maximum spell level contain one spell of your choice from the spellbooks that you can learn from with a level up to the spellbook's maximum spell level.   
  * __Soul Based Magic:__ To fuel your magic, you use the concentrated essence of life, which you are able to harvest from the dead. These "souls" are stored in your soul jar until they are expended on a spell or by an ability. At that time, they escape to the hereafter.   
* __Spellbooks:__   
  * __The Macabre Manual:__ You are able to learn spells from the Macabre Manual.   
* __Choices:__   
  * __Spell Choice:__ At the start of your journey, you know 2 extra level zero spells.   
  * __Vegan:__ At the start of your journey you may choose to become a 'vegan.' Deduct 1 point from your vitality and strength, and add 2 to your charisma. As a vegan, you swear not to harvest souls from the innocent, but increase the time limit on Mortal Coil to once per month.   
* __General Abilities:__   
  * __Mortal Coil:__ Once every week, you must consume a soul. If you do not, your body begins to rot away, causing fear and horror in those who see you.   
  * __Level Zero Spells:__ You have achieved a basic knowledge of the arcane, and may now learn level zero spells from any of your spellbooks.   
* __Starting Items:__   
  * __Soul Jar:__ You have a soul jar, which produces 1d6 souls each day at midnight, the jar can produce 2 souls at maximum. Your soul jar is capable of holding 20 souls at maximum.   
  
__Level 0 Necromancer__   
  
* __Rules:__   
  * __Learn Spells:__ Each time you level up, learn one new spell of each spell level that you have access to. Spells must be learned from one of your spellbooks.   
  * __Soul Harvest:__ You may harvest 1 soul from a sentient entity that has died within twenty four hours.   
  * __Learning Spells:__ New spells or techniques are obtained by leveling up or by finding spellbooks or scrolls in the world. A spellbook may contain a specific spell, or a maximum spell level. Spellbooks with a maximum spell level contain one spell of your choice from the spellbooks that you can learn from with a level up to the spellbook's maximum spell level.   
  * __Soul Based Magic:__ To fuel your magic, you use the concentrated essence of life, which you are able to harvest from the dead. These "souls" are stored in your soul jar until they are expended on a spell or by an ability. At that time, they escape to the hereafter.   
  
  
* __Spellbooks:__   
  * __The Macabre Manual:__ You are able to learn spells from the Macabre Manual.   
  
  
* __Choices:__   
  * __Vegan:__ At the start of your journey you may choose to become a 'vegan.' Deduct 1 point from your vitality and strength, and add 2 to your charisma. As a vegan, you swear not to harvest souls from the innocent, but increase the time limit on Mortal Coil to once per month.   
  
  
* __General Abilities:__   
  * __Mortal Coil:__ Once every week, you must consume a soul. If you do not, your body begins to rot away, causing fear and horror in those who see you.   
  * __Level Zero Spells:__ You have achieved a basic knowledge of the arcane, and may now learn level zero spells from any of your spellbooks.   
  
  
* __Starting Items:__   
  * __Soul Jar:__ You have a soul jar, which produces 1d6 souls each day at midnight, the jar can produce 2 souls at maximum. Your soul jar is capable of holding 20 souls at maximum.   
  
  
__Level 1 Necromancer__   
  
* __General Abilities:__   
  * __Level One Spells:__ Your powers are growing. You may now learn level one spells from any of your spellbooks.   
  * __Edge of Eternity:__ You can consume a soul to increase a stat by 1 or to give yourself a temporary increase of 1d10 health. If you consume more than 3 in a day, decrease the time limit on Mortal Coil to once per day for three days.   
  
  
__Level 2 Necromancer__   
  
* __Choices:__   
  * __Stat Increase:__ You gain two stat points to add to a stat or stats of your choosing.   
  
  
__Level 3 Necromancer__   
  
* __Actions:__   
  * __Minor Offhand Spell:__ You may cast a level zero spell as an offhand action.   
  
  
__Level 4 Necromancer__   
  
* __Choices:__   
  * __Stat Increase:__ You gain two stat points to add to a stat or stats of your choosing.   
  
  
* __General Abilities:__   
  * __Level Two Spells:__ You have graduated from novice to proficient! You may now learn level two spells from any of your spellbooks.   
  
  
__Level 5 Necromancer__   
  
* __General Abilities:__   
  * __Eyes of the Others:__ Consume a soul to give yourself darkvision and detect life for a day.   
  
  
__Level 6 Necromancer__   
  
* __Rules:__   
  * __Larger Soul Jar:__ Your soul jar can produce at maximum 1 more soul per day.   
  
  
* __Actions:__   
  * __Greater Offhand Spell:__ You may cast a level one spell as an offhand action.   
  
  
* __Choices:__   
  * __Stat Increase:__ You gain two stat points to add to a stat or stats of your choosing.   
  
  
__Level 7 Necromancer__   
  
* __Actions:__   
  * __Offhand Attack:__ You may use an offhand action to make an attack.   
  
  
* __General Abilities:__   
  * __Level Three Spells:__ Magical energy flows through you. You may now learn level three spells from any of your spellbooks.   
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
  * __Level Four Spells:__ You are a master of your spellcraft. You can now learn level four spells from any of your spellbooks.   
  
  
__Level 11 Necromancer__   
  
* __Rules:__   
  * __Larger Soul Jar:__ Your soul jar can produce at maximum 1 more soul per day.   
  
  
* __General Abilities:__   
  * __Phylactery:__ You may remove your soul and put it in a box. If the box is destroyed, are destroyed with it. If your body dies and you have a thrall, your consciousness may be transferred to the thrall. If you have no thralls remaining, your body is regenerated at your phylactery after one day.   
  
  
__Level 12 Necromancer__   
  
* __Actions:__   
  * __Major Offhand Spell:__ You may cast a level two spell as an offhand action.   
  
  
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
  * __Level Five Spells:__ You have achieved the highest form of sorcery, and are a mage to be reckoned with. You can now learn level five spells from any of your spellbooks.   
  
  
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
  * __Learning Spells:__ New spells or techniques are obtained by leveling up or by finding spellbooks or scrolls in the world. A spellbook may contain a specific spell, or a maximum spell level. Spellbooks with a maximum spell level contain one spell of your choice from the spellbooks that you can learn from with a level up to the spellbook's maximum spell level.   
  * __Learn Spells:__ Each time you level up, learn one new spell of each spell level that you have access to. Spells must be learned from one of your spellbooks.   
* __Spellbooks:__   
  * __The Book of Healing:__ You are able to learn spells from the Book of Healing.   
* __Choices:__   
  * __Minor Spell Choice:__ At the start of your journey, you know 1 extra level zero spells.   
  * __Pledge:__ At the start of your journey, you may select a deity to pledge yourself to.   
* __General Abilities:__   
  * __Level Zero Spells:__ You have achieved a basic knowledge of the arcane, and may now learn level zero spells from any of your spellbooks.   
* __Starting Items:__   
  * __Chainmail:__ You begin your journey with a suit of chainmail plate. Take -1 damage on attacks while wearing it.   
  
__Level 0 Paladin__   
  
* __Rules:__   
  * __Learning Spells:__ New spells or techniques are obtained by leveling up or by finding spellbooks or scrolls in the world. A spellbook may contain a specific spell, or a maximum spell level. Spellbooks with a maximum spell level contain one spell of your choice from the spellbooks that you can learn from with a level up to the spellbook's maximum spell level.   
  * __Learn Spells:__ Each time you level up, learn one new spell of each spell level that you have access to. Spells must be learned from one of your spellbooks.   
  
  
* __Spellbooks:__   
  * __The Book of Healing:__ You are able to learn spells from the Book of Healing.   
  
  
* __Choices:__   
  * __Pledge:__ At the start of your journey, you may select a deity to pledge yourself to.   
  
  
* __General Abilities:__   
  * __Level Zero Spells:__ You have achieved a basic knowledge of the arcane, and may now learn level zero spells from any of your spellbooks.   
  
  
__Level 1 Paladin__   
  
* __Combat Abilities:__   
  * __Hammer of Light:__ Any weapon that you wield does an additional dice of damage to undead.   
  * __Bash:__ Stun an enemy on a critical hit, causing them to miss an action and an offhand action on their next turn.   
  
  
__Level 2 Paladin__   
  
* __Choices:__   
  * __Stat Increase:__ You gain two stat points to add to a stat or stats of your choosing.   
  
  
* __General Abilities:__   
  * __Level One Spells:__ Your powers are growing. You may now learn level one spells from any of your spellbooks.   
  
  
__Level 3 Paladin__   
  
* __Combat Abilities:__   
  * __Faithful Weapon:__ After throwing your weapon, you can return it to yourself. You do not take disadvantage when throwing hammers or maces.   
  
  
__Level 4 Paladin__   
  
* __Actions:__   
  * __Minor Offhand Spell:__ You may cast a level zero spell as an offhand action.   
  
  
* __Choices:__   
  * __Stat Increase:__ You gain two stat points to add to a stat or stats of your choosing.   
  
  
__Level 5 Paladin__   
  
* __Combat Abilities:__   
  * __Link Lifeforce:__ As an action, link your lifeforce to that of another. Any damage they take is transferred directly to you. Remove the link as an offhand action.   
  
  
__Level 6 Paladin__   
  
* __Choices:__   
  * __Stat Increase:__ You gain two stat points to add to a stat or stats of your choosing.   
  
  
* __General Abilities:__   
  * __Level Two Spells:__ You have graduated from novice to proficient! You may now learn level two spells from any of your spellbooks.   
  
  
__Level 7 Paladin__   
  
* __Actions:__   
  * __Greater Offhand Spell:__ You may cast a level one spell as an offhand action.   
  * __Offhand Attack:__ You may use an offhand action to make an attack.   
  
  
* __Combat Abilities:__   
  * __Shield of Men:__ Reaction. Once per round of combat, you can throw yourself in front of a teammate, taking their damage for them. Any damage you receive as a result is halved. Works up to 30 feet.   
  
  
__Level 8 Paladin__   
  
* __Choices:__   
  * __Stat Increase:__ You gain two stat points to add to a stat or stats of your choosing.   
  
  
__Level 9 Paladin__   
  
* __General Abilities:__   
  * __Beacon of Hope:__ Passive. All allies within 100 feet of you gain +1 to all saving throws.   
  * __Level Three Spells:__ Magical energy flows through you. You may now learn level three spells from any of your spellbooks.   
  
  
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
  * __Level Four Spells:__ You are a master of your spellcraft. You can now learn level four spells from any of your spellbooks.   
  
  
__Level 13 Paladin__   
  
* __Combat Abilities:__   
  * __Winged Jump:__ _(Cost 1)_ Leap up to 40 feet using ethereal, angelic wings. Counts as an action.   
  
  
__Level 14 Paladin__   
  
* __Choices:__   
  * __Stat Increase:__ You gain two stat points to add to a stat or stats of your choosing.   
  
  
__Level 15 Paladin__   
  
* __General Abilities:__   
  * __Level Five Spells:__ You have achieved the highest form of sorcery, and are a mage to be reckoned with. You can now learn level five spells from any of your spellbooks.   
  
  
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
  * __Ward of Tracking:__ _(Cost 1)_ Costs one spell point. Lay your hand on an opponent. For the next forty-eight hours, you know their position within 100 feet.   
  
  
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
  
  
Sorcerer's draw their magic not from cryptic tomes nor nuanced understanding, but rather through raw force of personality. To perform magic, a sorcerer wrestles with a spirit, natural or otherwise, and convinces them to do their bidding. To this end, Sorcerers have no spell points, but rather must pass a charisma check to perform magic. As you create your sorcerer, consider how they learned magic. Who did they learn it from? How did they first wrestle a spirit to aid them? When they cast a spell, do they always use the same spirit, or different spirits? Is the spirit natural, or the soul of someone who is gone? How will being a sorcerer change the way that you interact with the world and your party?   
  
|STR|DEX|INT|INF|CHR|PER|LUK|HD|   
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|   
|-1|-2|0|1|2|-3|1|4|   
  
__Sorcerer Abilities:__   
* __Rules:__   
  * __Learning Spells:__ New spells or techniques are obtained by leveling up or by finding spellbooks or scrolls in the world. A spellbook may contain a specific spell, or a maximum spell level. Spellbooks with a maximum spell level contain one spell of your choice from the spellbooks that you can learn from with a level up to the spellbook's maximum spell level.   
  * __Learn Spells:__ Each time you level up, learn one new spell of each spell level that you have access to. Spells must be learned from one of your spellbooks.   
  * __Charisma Based Spellcaster:__ To succeed at casting spells, you must convince your familiar to perform it for you. To do this, roll a d20 and add your charisma. The result must beat the difficulty of the spell.   
* __Spellbooks:__   
  * __Novice Spellbook:__ You are able to learn spells from the Novice Spellbook.   
  * __The Sorcerer's Scrolls:__ You are able to learn spells from the Sorcerer's Scrolls.   
* __Choices:__   
  * __Spell Choice:__ At the start of your journey, you know 2 extra level zero spells.   
* __General Abilities:__   
  * __Level Zero Spells:__ You have achieved a basic knowledge of the arcane, and may now learn level zero spells from any of your spellbooks.   
  * __Influence:__ You may use spell points to increase any charisma roll by 2.   
  
__Level 0 Sorcerer__   
  
* __Rules:__   
  * __Learning Spells:__ New spells or techniques are obtained by leveling up or by finding spellbooks or scrolls in the world. A spellbook may contain a specific spell, or a maximum spell level. Spellbooks with a maximum spell level contain one spell of your choice from the spellbooks that you can learn from with a level up to the spellbook's maximum spell level.   
  * __Learn Spells:__ Each time you level up, learn one new spell of each spell level that you have access to. Spells must be learned from one of your spellbooks.   
  * __Charisma Based Spellcaster:__ To succeed at casting spells, you must convince your familiar to perform it for you. To do this, roll a d20 and add your charisma. The result must beat the difficulty of the spell.   
  
  
* __Spellbooks:__   
  * __Novice Spellbook:__ You are able to learn spells from the Novice Spellbook.   
  * __The Sorcerer's Scrolls:__ You are able to learn spells from the Sorcerer's Scrolls.   
  
  
* __General Abilities:__   
  * __Level Zero Spells:__ You have achieved a basic knowledge of the arcane, and may now learn level zero spells from any of your spellbooks.   
  * __Influence:__ You may use spell points to increase any charisma roll by 2.   
  
  
__Level 1 Sorcerer__   
  
* __General Abilities:__   
  * __Level One Spells:__ Your powers are growing. You may now learn level one spells from any of your spellbooks.   
  
  
__Level 2 Sorcerer__   
  
* __Choices:__   
  * __Stat Increase:__ You gain two stat points to add to a stat or stats of your choosing.   
  
  
__Level 3 Sorcerer__   
  
* __Rules:__   
  * __Spell Modification:__ You may make one or more of the following modifications to your spells. Increase difficulty by 2 to double the radius, halve the radius, or change the volume of a spell. Increase difficulty by 4  to add an additional effect dice to the spell (e.g. making a spell that does 1d10 damage do 2d10) or to tie off a spell, making it last 1d20 minutes after casting even if it is a concentration spell.   
  
  
* __Actions:__   
  * __Minor Offhand Spell:__ You may cast a level zero spell as an offhand action.   
  
  
__Level 4 Sorcerer__   
  
* __Choices:__   
  * __Stat Increase:__ You gain two stat points to add to a stat or stats of your choosing.   
  
  
* __General Abilities:__   
  * __Level Two Spells:__ You have graduated from novice to proficient! You may now learn level two spells from any of your spellbooks.   
  
  
__Level 5 Sorcerer__   
  
* __Actions:__   
  * __Prepare Spell:__ At the start of each day, choose a spell to have 2 less difficulty.   
  
  
__Level 6 Sorcerer__   
  
* __Actions:__   
  * __Greater Offhand Spell:__ You may cast a level one spell as an offhand action.   
  
  
* __Choices:__   
  * __Stat Increase:__ You gain two stat points to add to a stat or stats of your choosing.   
  
  
__Level 7 Sorcerer__   
  
* __Actions:__   
  * __Offhand Attack:__ You may use an offhand action to make an attack.   
  
  
* __General Abilities:__   
  * __Level Three Spells:__ Magical energy flows through you. You may now learn level three spells from any of your spellbooks.   
  
  
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
  * __Level Four Spells:__ You are a master of your spellcraft. You can now learn level four spells from any of your spellbooks.   
  
  
__Level 11 Sorcerer__   
  
* __General Abilities:__   
  * __Spiritual Movement:__ While you contain a spirit, you may instantly teleport between patches of darkness as an offhand action or once per ten minutes out of combat.   
  
  
__Level 12 Sorcerer__   
  
* __Actions:__   
  * __Major Offhand Spell:__ You may cast a level two spell as an offhand action.   
  
  
* __Choices:__   
  * __Stat Increase:__ You gain two stat points to add to a stat or stats of your choosing.   
  
  
__Level 13 Sorcerer__   
  
* __General Abilities:__   
  * __Level Five Spells:__ You have achieved the highest form of sorcery, and are a mage to be reckoned with. You can now learn level five spells from any of your spellbooks.   
  
  
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
  
  
Often eccentric, wizards are known to be wayfarers and meddlers. Most keep to themselves, approaching others only to entwine them in schemes only they know about. Wizards arrive precisely when they mean to. To use magic, Wizards use spell points, and begin with a number of spell points equal to their intelligence. Spells cost the same amount of spell points as their level, and are reaquired upon a long rest. Wizards have the least health of any class, but also have more spell points than any other class. As you create your wizard, consider what their past is. How old are they? What kind of family did they come from? How long have they been a wizard? Are they mysterious? Are they competent? How do they interact with others? Who taught them magic? How will being a wizard affect how you interact with your other party members?   
  
|STR|DEX|INT|INF|CHR|PER|LUK|HD|   
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|   
|-1|-3|2|1|0|-2|2|2|   
  
__Wizard Abilities:__   
* __Rules:__   
  * __Learn Spells:__ Each time you level up, learn one new spell of each spell level that you have access to. Spells must be learned from one of your spellbooks.   
  * __Learning Spells:__ New spells or techniques are obtained by leveling up or by finding spellbooks or scrolls in the world. A spellbook may contain a specific spell, or a maximum spell level. Spellbooks with a maximum spell level contain one spell of your choice from the spellbooks that you can learn from with a level up to the spellbook's maximum spell level.   
* __Spellbooks:__   
  * __Novice Spellbook:__ You are able to learn spells from the Novice Spellbook.   
  * __The Wizard's Addendum:__ You are able to learn spells from the Wizard's Addendum.   
* __Choices:__   
  * __Spell Choice:__ At the start of your journey, you know 2 extra level zero spells.   
* __General Abilities:__   
  * __Level Zero Spells:__ You have achieved a basic knowledge of the arcane, and may now learn level zero spells from any of your spellbooks.   
* __Starting Items:__   
  * __The Sword and the Satchel:__ You begin your adventure with a bottomless satchel.   
  * __Walking Stick:__ You begin your adventure with a wizard's staff which gives you 1d4 additional damage to all spells.   
* __Advantages:__   
  * __Historian:__ You have a deep knowledge of the land in which your adventure takes place. You gave advantage on any history or geography checks.   
  
__Level 0 Wizard__   
  
* __Rules:__   
  * __Learn Spells:__ Each time you level up, learn one new spell of each spell level that you have access to. Spells must be learned from one of your spellbooks.   
  * __Learning Spells:__ New spells or techniques are obtained by leveling up or by finding spellbooks or scrolls in the world. A spellbook may contain a specific spell, or a maximum spell level. Spellbooks with a maximum spell level contain one spell of your choice from the spellbooks that you can learn from with a level up to the spellbook's maximum spell level.   
  
  
* __Spellbooks:__   
  * __Novice Spellbook:__ You are able to learn spells from the Novice Spellbook.   
  * __The Wizard's Addendum:__ You are able to learn spells from the Wizard's Addendum.   
  
  
* __Choices:__   
  * __Spell Choice:__ At the start of your journey, you know 2 extra level zero spells.   
  
  
* __General Abilities:__   
  * __Level Zero Spells:__ You have achieved a basic knowledge of the arcane, and may now learn level zero spells from any of your spellbooks.   
  
  
__Level 1 Wizard__   
  
* __General Abilities:__   
  * __Level One Spells:__ Your powers are growing. You may now learn level one spells from any of your spellbooks.   
  
  
* __Advantages:__   
  * __Looming Presence:__ Gain advantage when attempting to intimidate anything of lower intelligence than yourself.   
  
  
__Level 2 Wizard__   
  
* __Choices:__   
  * __Stat Increase:__ You gain two stat points to add to a stat or stats of your choosing.   
  
  
__Level 3 Wizard__   
  
* __Actions:__   
  * __Minor Offhand Spell:__ You may cast a level zero spell as an offhand action.   
  
  
__Level 4 Wizard__   
  
* __Choices:__   
  * __Stat Increase:__ You gain two stat points to add to a stat or stats of your choosing.   
  
  
* __General Abilities:__   
  * __Level Two Spells:__ You have graduated from novice to proficient! You may now learn level two spells from any of your spellbooks.   
  
  
__Level 5 Wizard__   
  
* __Actions:__   
  * __Greater Offhand Spell:__ You may cast a level one spell as an offhand action.   
  
  
__Level 6 Wizard__   
  
* __Choices:__   
  * __Stat Increase:__ You gain two stat points to add to a stat or stats of your choosing.   
  
  
__Level 7 Wizard__   
  
* __Actions:__   
  * __Offhand Attack:__ You may use an offhand action to make an attack.   
  
  
* __General Abilities:__   
  * __Level Three Spells:__ Magical energy flows through you. You may now learn level three spells from any of your spellbooks.   
  
  
* __Combat Abilities:__   
  * __Commit to Memory:__ At the beginning of a day, you may commit one spell to memory of level 2 or greater. For the remainder of the day, that spell costs 1 fewer spell points.   
  
  
__Level 8 Wizard__   
  
* __Choices:__   
  * __Stat Increase:__ You gain two stat points to add to a stat or stats of your choosing.   
  
  
__Level 9 Wizard__   
  
* __Actions:__   
  * __Major Offhand Spell:__ You may cast a level two spell as an offhand action.   
  
  
__Level 10 Wizard__   
  
* __Choices:__   
  * __Stat Increase:__ You gain two stat points to add to a stat or stats of your choosing.   
  
  
* __General Abilities:__   
  * __Level Four Spells:__ You are a master of your spellcraft. You can now learn level four spells from any of your spellbooks.   
  
  
__Level 12 Wizard__   
  
* __Choices:__   
  * __Stat Increase:__ You gain two stat points to add to a stat or stats of your choosing.   
  
  
* __General Abilities:__   
  * __Spell Invention:__ You are advanced enough in magic that you may begin inventing your own spells. To invent a spell, you must have either encountered something like it, or have a jumping off point in your spellbook. It can take long periods of time to craft a spell, and its success and cost will be determined by multiple rolls and saving throws, depending on complexity.   
  
  
__Level 13 Wizard__   
  
* __General Abilities:__   
  * __Level Five Spells:__ You have achieved the highest form of sorcery, and are a mage to be reckoned with. You can now learn level five spells from any of your spellbooks.   
  
  
__Level 14 Wizard__   
  
* __Choices:__   
  * __Stat Increase:__ You gain two stat points to add to a stat or stats of your choosing.   
  
  
__Level 15 Wizard__   
  
* __Spellbooks:__   
  * __Tome of the Ancients:__ You are now able to learn spells from the tome of the ancients.   
  
  
  
___   
  


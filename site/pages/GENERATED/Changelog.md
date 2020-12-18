---

portrait_banner_path: /site/images/backdrops/portrait_changelog.jpg

portrait_banner_link: https://www.deviantart.com/spikedmcgrath/art/Toad-Newmann-803282064

portrait_banner_name: Toad Newmann

portrait_banner_artist:  SpikedMcGrath

portrait_banner_artist_link: https://www.deviantart.com/spikedmcgrath

portrait_banner_license: CC BY-NC-ND 3.0

portrait_banner_license_link: https://creativecommons.org/licenses/by-nc-nd/3.0/

title: The Changelog

description: Keep up to date with all of the changes!

show_download: false

---

  
# Changelog

   * [Rangers and Ruffians 2.4.1: Spell Patch 1](#rangers-and-ruffians-241-spell-patch-1)  
   * [Rangers and Ruffians 2.4.0: The Simplification Update](#rangers-and-ruffians-240-the-simplification-update)  
   * [Miscellaneous](#miscellaneous-1)  
   * [Rangers and Ruffians 2.3.1: The Weapon Skill Update](#rangers-and-ruffians-231-the-weapon-skill-update)  
   * [Rangers and Ruffians 2.3.0: The Weapon Update](#rangers-and-ruffians-230-the-weapon-update)  
   * [Rangers and Ruffians 2.2.0: The New Class Update](#rangers-and-ruffians-220-the-new-class-update)  
   * [Rangers and Ruffians 2.1.3: The Combat Update](#rangers-and-ruffians-213-the-combat-update)  
   * [Rangers and Ruffians 2.1.2: The Action Point Economy Update. December 4, 2019](#rangers-and-ruffians-212-the-action-point-economy-update-december-4-2019)  
   * [Rangers and Ruffians 2.1.1: The Rogues and Rangers Update. November 23, 2019](#rangers-and-ruffians-211-the-rogues-and-rangers-update-november-23-2019)  
   * [Rangers and Ruffians 2.1.0: The Skills Update. November 19, 2019](#rangers-and-ruffians-210-the-skills-update-november-19-2019)  
   * [Pre- Rangers and Ruffians 2.1.0 (Pre- November 2019)](#pre--rangers-and-ruffians-210-pre--november-2019)  

  
## Rangers and Ruffians 2.4.1: Spell Patch 1
  
  
  
  

  
### System Changes:
* __None__
  
  

  
### Balance Changes:
  
  
__Spell Balance:__ This is the first of a number of updates that will be coming to the spells of Rangers and Ruffians with the following goals. This spell affects the `Bard` and `Cleric`.
1. Increase the utility of spells.
2. Decrease spell redundancy
3. Increase the mechanical specificity of spells. Spells can include
    *  __Cost:__ A number of action points required to cast a spell.
    * __Target:__ For internal balance, the type of entity the spell targets (e.g., friend or foe)
    * __Number of targets:__ For internal balance, whether a spell targets one or many entities.
    * __Duration:__ The amount of time that the spell lasts in minutes. Zero duration indicates that the spell is instantaneous.
    * __Description:__ A (hopefully interesting) description of what the spell does.
    * __Range:__ The distance at which the spell may be cast.
    * __Purpose:__ One of `utility`, `buff`, `debuff`, `summon`, `healing` or `damage`.
    * __Dice:__ The amount of damage or healing done by the spell.
    * __Effect Type:__ The damage type of the spell.
    * __Casting Time:__ The length of time a spell requires to cast. Zero indicates that the spell is cast instantaneously.
    * __Components:__ Any physical materials needed to cast the spell.
    * __Upcast:__ Defines if additional action points can be spent on the spell to lend it extra power.
    * __Action Type:__ Whether the spell requires an `Action`, `Offhand Action`, `Free Action`, or `Reaction` to cast.
    * __Effect Radius:__ The radius that the spell effects.
    * __Hit:__ Whether the spell requires a roll to hit.
    * __School:__ The spell's school of magic.
  
  
To do this, spellbooks are being converted to `Spell Decks`, each of which contains `54` spells. These come in the form of
* `14` Tier 0 spells
* `13` Tier 1 spells
* `9` Tier 2 spells
* `8` Tier 3 spells
* `6` Tier 4 spells
* `4` Tier 5 spells.
  
  
This means that the overall _number_ of spells in the game is being decreased, while the _usefulness_ and _power_ of spells should be increasing overall.
  
  

  
#### Bard
Completed the Bard's `Spell Deck`.
  
  

  
#### Cleric
Finished tier 0-3 of the Cleric's `Spell Deck`.
  
  

  
### Website Updates:
* Spellbook pages have been updated.
* Fixed an error which sometimes caused spell `Effects` to be rendered incorrectly.
  
  

  
### Miscellaneous
None

  
## Rangers and Ruffians 2.4.0: The Simplification Update
  
  
  
  

  
### System Changes:
  
  
* __Defense and Accuracy:__ Whenever an attack is made, the attacker must roll `1d20` and add their accuracy (attack stat, e.g., `strength or dex + any item bonuses`) and see if it meets or exceeds the enemy’s defense (`5 + armor worn`). If it does, the attack lands, else it misses. If a `20` is rolled, the attack is a critical hit, and all dice damage is doubled.
* __Diminishing Returns (Stats):__ Through a combination of other changes, stats points now always count as worth 1 point (i.e., they are no longer worth a half point after 3).
* __Weapons:__ The weapon system (i.e., weapon abilities and movement penalties) has been removed for ease-of-use reasons.
* __Skills:__ Skills have been temporarily removed for time reasons, but should be reintroduced in a future update.
  
  

  
### Balance Changes:
  
  
* __Movement:__ Weapons no longer affect movement. Dexterity no longer affects movement. Base movement decreased from 30 feet to 25 feet.
* __Leveling up:__ On level up, players now always receive one stat point, rather than alternating between `+2` and `+1`.
* __Max stat values:__ Stat values may no longer exceed `+5`.
* __Race Balance:__ Races no longer grant stat bonuses.
* __Class Balance:__ The standard stat array for classes has been updated from `[-3, -2, -1, 0, 1, 2]` to `[-2, -1, 0, 1, 1, 2]`.
* __Ability Balance:__ A number of abilities have been updated to integrate with the new Defense/Accuracy system (e.g., dodge previously allowed you a chance to dodge an attack, now it adds a bonus to your defense for the turn, effectively doing the same thing).
* __Mage Balance:__ All spells have been clarified with ranges, schools, and durations. Most damage dealing spells have received a buff to match new weapon handout recommendations. A subset of spells can now be "upcast," allowing the caster to spend extra action points to make the spell more potent.
  
  

  
### Website Update:
The website now prompts you for an update if you are running from a stale cache.
  
  

  
## Miscellaneous
New poohbah guidelines: guidelines added for monster health/damage/accuracy, check difficulty, weapon handouts by gameplay tier, and magic item handouts by gameplay tier.
  
  

  
## Rangers and Ruffians 2.3.1: The Weapon Skill Update
  
  

  
### Overview
Adds a host of new skills that better couple with the new weapon system.
  
## Rangers and Ruffians 2.3.0: The Weapon Update
  
  

  
### Overview
Updates weapons to have abilities and drawbacks, making combat more tactical.
  
  

  
### Weapon List
1. Shortsword
2. Shortspear
3. Dagger
4. Handaxe
5. Spear
6. Katana
7. Quarterstaff
8. Great Sword
9. War Hammer
10. Greataxe 
11. Longbow
12. Shortbow
13. Crossbow
14. Pistol 
15. Carbine Rifle
16. Long Rifle

  
## Rangers and Ruffians 2.2.0: The New Class Update
  
  

  
### Overview
This revision:
1. Redesigns every class to make them more action oriented and engaging to play.
2. Tweaks race mechanics to better match new classes.
  
  

  
## Rangers and Ruffians 2.1.3: The Combat Update
  
  

  
### Overview
A large race and class balance update.
  
  

  
### New Rules:
  
  

  
#### Harrying
A player or creature is considered to be ___harried___ if they have an enemy next to them.
Harried creatures make ranged attacks with disadvantage. The harried condition is used by
some abilities, including the Thief's _Flank_ ability, which gives them advantage when attacking
harried enemies.
  
  
  
  

  
### Race Balance Changes

  
#### Catterwol
* __Abilities__
  * __Changed Fast Paws__ _Gain an extra offhand action_
    * __Change:__ Reverted Fast Paws to its previous, pre-2.1.1 state (Offhand action can be used as an attack again).
    * __Reasoning:__ Allows Catterwol to shine.
  
  

  
#### Hardfoot Halfling
* __Abilities__
  * __Changed Courageous Blow__ _Add your INF to an attack_
    * __Change:__ Now allows you to add twice your INF to an attack.
    * __Reasoning:__ Makes the ability more useful at high levels.
  
  

  
#### Dwarf
* __Abilities__
  * __Changed Very Dangerous Over Short Distances__ _Advantage if you begin your turn next to an enemy_
    * __Change:__ Clarified that this ability negates disadvantage when attacking with a ranged weapon.
    * __Reasoning:__ Clarification.
  
  

  
#### Daemonspawn
* __Abilities__
  * __Changed Fix Your Eyes on Me__ _Force an enemy to see only you. Adv on CHA checks._
    * __Change:__ Added combat use: force enemy to attack only you.
    * __Reasoning:__ Increases the utility of the ability.
  * __Changed Sacrificial Rite__ _Sacrifice half your level in health to make a second action._
    * __Change:__ Round up rather than down.
    * __Reasoning:__ Adds to cost-benefit of ability.
  
  

  
#### Automaton
* __Abilities__
  * __Changed Self Repair__ _During combat, self repair._
    * __Change:__ Now costs an action rather than a turn.
    * __Reasoning:__ Makes automaton more survivable despite its inability to heal via potions.
  * __Changed Armored Exterior__ _Take less damage in combat._
    * __Change:__ Rather than adding a static +1 armor, this ability now allows the automaton to take half damage from piercing, slashing, blunt, fire, and ice attacks. Does not stack with Berserk.
    * __Reasoning:__ This change will make the automaton far more survivable despite its inability to drink potions.
  * __Changed Piston Punch__ _Attempt to knock an opponent down._
    * __Change:__ Increased damage across the board.
    * __Reasoning:__ Makes this attack more viable at all levels.
  
  

  
#### Hissling
* __Abilities__
  * __Changed Chomp Chomp__ _Bite and cling to an enemy._
    * __Change:__ Now costs an offhand action rather than an action.
    * __Reasoning:__ Makes this low damage ability more viable at all levels.
  
  
  
  

  
### Class Balance Changes
  
  

  
#### Barbarian
The Barbarian now has two subclasses, _Path of Rage_ and _Path of Nature_.
  
  

  
#### Path of Rage Barbarian
The Path of Rage Barbarian now gains the following new abilities:
  
  
* __Area Control:__
  * __Taunt:__ Force all enemies within 30ft. to make a SP save or be forced to attack only you.
* __Combat__
  * __Berserk:__ Gain +1 STR, DEX, and +2 INF. Take half damage from piercing and blunt attacks.
  * __Brutal Attack:__ Extra damage dice. Size based contested STR save. Fail: prone or 10ft knockback.
  * __Throw Caution to the Wind:__ Add an extra damage dice, but enemies get advantage on attacks.
  * __Arching Swing:__ Attack all enemies adjacent to you.
  * __Hurl Weapon:__ 2 extra damage dice. 5x STR/DEX distance.
  * __Single Out:__ Single out an enemy. Gain 15 feet of movement when moving towards them and take advantage on all attacks.
* __Combat Passive:__
  * __Furious Blows:__ Two attacks when berserk
  * __Adrenaline:__ When you are below 50% health, gain an extra 10 feet of movement.
  * __Terrify:__ Singled out enemies must make an INF save against your spell power or be scared of you.
__Combo:__
  * __Chained Together:__ After slaying an enemy gain 10 feet of movement and a free attack or Hurl Weapon.
  * __Warrior Spirit:__ When you slay an enemy or land a critical hit, gain 1 action point.
  * __Spirit of Rage:__ (Capstone) After slaying an enemy, gain another full turn.
__Multiplier:__
  * __Savage Critical:__ Additional dice of damage when you crit
  * __Fury:__ On a turn where you have taken damage, add an extra damage dice to all of your attacks.
  * __The Opener:__ Attack an enemy that hasn't gone, 2x damage, contested STR save. Failure: prone.
  * __The Closer:__ Add two dice of damage to prone enemies.
  * __Glory:__ When you hit low health, double your damage (25%)
  
  
The anticipated way to play the Path of Rage Barbarian is as follows:
  
  
__Edge of Death__  
  
  
If a high level Path of Rage Barbarian enters combat with low (< 25%) health, it can stack abilities for enormous damage.
  
  
1. As an offhand action, __Single Out__ an enemy. Use all movement to reach it. (we have an extra 20ft due to __Adrenaline__ and __Single Out__).
2. Using __The Opener__ and __Brutal Attack__ gain 2x damage and an extra damage dice respectively.
3. Because the Barbarian is at low health, _Glory_ is active, gaining us an extra dice of damage.
4. Using __Throw Caution to the Wind__ we gain another dice of damage.
5. Therefore, our first attack deals 2x damage with 4 damage dice.
6. If it is a critical hit, we add 2 more damage dice (due to __Savage Critical__).
7. Using __Furious Blows__ we have a second attack. If the enemy is prone, we deal 2 more damage dice due to __The Closer__.
8. Our second attack deals 2x damage with 6 damage dice or 8 damage dice if it is a critical hit.
  
  
__Mopping Up__  
  
  
A Path of Rage barbarian can chain together many kills in a single turn by targeting weak enemies.
  
  
1. If a Path of Rage Barbarian downs an enemy, __Chain Together__ allows it to instantly gains 10 feet of movement and a free attack or __Hurl Weapon__ action.
2. By decomposing it's movement between attacks, the Path of Rage Barbarian can potentially mop up many low level enemies in a single turn, running from one to the next and slaying them.
  
  
  
  

  
#### Path of Nature Barbarian
The Path of Nature Barbarian is a brand new subclass which uses the power of the spirits of nature to deal heavy damage on the battlefield.
  
  
The Path of Rage Nature now gains the following new abilities:
  
  
* __Core Mechanic:__
  * __Spiritual Infusion:__ (Cost 1) Equip a single one of your aspects.
  * __Greater Spiritual Infusion:__ (Cost 1) Equip 2 of your aspects.
  * __Major Spiritual Infusion:__ (Cost 1) Equip 3 of your aspects.
  * __Legendary Spiritual Infusion:__ (Capstone) (Cost 1) Equip 6 of your aspects.
* __Aspects:__
  * __Elk Aspect:__ Add 15 feet of movement.
  * __Wolf Aspect:__ If you attack an enemy with an ally, gain advantage.
  * __Wildcat Aspect:__ You have the ability to dodge incoming attacks.
  * __Bull Aspect:__ All of your attacks have a chance to knock an enemy prone.
  * __Bear Aspect:__ You take half blunt and piercing damage.
  * __Elemental Aspect:__ Convert your damage to a different type of damage of your choice. Declare when aspect is equipped.
  * __Leech Aspect:__ Recover half your level (round up, min 1) in health whenever you land a blow.
  * __Dolphin Aspect:__ Swim at twice your walking speed and hold your breath for fifteen minutes.
* __Combat:__
  * __Spiritual Strike:__ Use your melee weapon to strike an enemy up to 30 feet away.
  * __Spiritual Shield:__ Block an attack.
  * __Greater Spiritual Shield:__ Block an attack aimed at an ally within 30 feet.
  * __Spiritually Reinforced Blow:__ Extra damage dice + Enemy must make a size based contested STR check or be knocked back 10 feet.
  * __Chain Strike:__ Make an attack that deals an extra dice of spiritual damage and immediately chains to a second enemy within 15 feet. Roll 1d20. On 10 or greater, continue the chain and repeat.
  * __Draining Strike:__ Regain half of the damage you deal as health.
  * __Spiritual Blast:__ Attack all enemies in a 30ft line in front of you.
* __Combat Passive:__
  * __Phase Walk:__ If you kill an enemy with Spiritual weapon, teleport to them.
  * __Greater Phase Walk:__ If hit an enemy with Spiritual weapon, teleport to them.
* __Buff Ally:__
  * __Spiritual Aid:__ Grant an ally advantage on their next action or an extra damage dice on their next attack.
  * __Rouse to Action:__ Grant an ally their full movement and one action.
  * __Infuse Other:__ Grant an ally the benefit of one of your infusions for 1 battle.
* __Non Combat:__
  * __Form Shift:__ Change form to that of one of the aspects you are inhabiting.
  
  
The anticipated core gameplay loops for the Path of Nature Barbarian are as follows:
  
  
__Survivable__  
  
  
By equipping __Leech Aspect__ and using __Draining Strike__ the Path of Nature Barbarian can keep its health up.
By adding __Bear Aspect__ the Path of Nature Barbarian begins taking half damage from many attacks.
  
  
__Mobile__   
  
  
By equipping __Elk Aspect__ and using __Phase Walk__ the Path of Nature Barbarian can move incredibly quickly about the battlefield.
  
  
__Crowd Control__  
  
  
By combining __Bull Aspect__ and __Chain Strike__ or __Spiritual Blast__, the Path of Nature Barbarian can knock many enemies prone.
  
  
__Good Against Everything__  
  
  
By using __Elemental Aspect__ the Path of Nature Barbarian can maximize its damage against any enemy type.
  
  
__Team Player__  
  
  
By using __Spiritual Aid__, __Rouse to Action__, and __Infuse Other__ the Path of Nature Barbarian can buff allies in a number of ways.
Using __Wolf Aspect__, the Path of Nature Barbarian can deal extra damage when cooperating with allies.
  
  

  
#### Knight:
The Knight now gains the following new abilities:
* __Area Control__
  * __Block Movement:__ If you hit an enemy with your exposed attack, they must make a contested STR check or be stopped in their tracks.
  * __Hold the Line:__ Gain a second exposed attack.
* __Ally Buff:__ 
  * __Inspiring Critical:__ When you get a critical hit or slay an enemy, grant an ally of your choice a 1d10 inspiration dice.
  * __Defender Aura: Cost:__ 2 Grant all nearby (30ft) allies half damage from physical attacks for 3 turns.
* __Combat:__
  * __Overwhelming Strike:__ Extra damage dice. Size based contested STR or advantage on next attack.
  * __Shield Bash:__  Offhand: Contested STR check. Fail: loose action. d4 damage LV0 d8 LV4, d10 LV8, d12 LV12.
  * __Ready Stance:__ Allows you to counter-attack
  * __Knight's Challenge:__ Call out an enemy. It must make a INF save against your spell power or be forced to attack you. You gain advantage in all attacks.
  * __Warrior's Vow:__ Gain an extra attack against an entity you have challenged. 
  * __Charge__ Offhand. Charge an extra 10ft. Size STR check. Looser is knocked prone.
  * __Greater Charge:__ Charge an extra 15ft. End in an attack.
  * __Steel Yourself:__ Choose to take half damage.
  * __Shield of Men:__  Take a teammate's damage for them. Halved. 30ft rad.
* __Combat Passive__
  * __Armor Master:__ No penalty from armor
  * __Shield Master:__ No penalty from shields
  * __Last Line of Defense:__ If an ally is down, gain a damage dice.
  * __Cleave:__ Attack two adjacent enemies in front of you with a single attack.
* __Combo__
  * __Press the Advantage:__ If you land a critical hit, gain a free shield bash attack.
* __Movement:__
  * __Pivot:__ Trade spaces with an adjacent ally
  * __Advance:__ If you slay an enemy with a melee attack, you may step into their space.
  * __Controlled Advance:__ When you use the advance ability, gain an action which may be used to either attack again or ready your stance.
* __Survivability:__
  * __Stay on your feet:__ When you hit 0 health, flip a coin. On heads, stay alive with 1 health.
  * __Resilient Defense:__ A single attack can do at most 40 damage to you.
* __Social:__
  * __Kingsmen:__ Advantage speaking with loyal commoners.
  
  
The anticipated core gameplay loops for the knight are as follows:
  
  
__Hold the Line__  
  
  
1. The knight positions itself in front of vulnerable allies.
2. The knight uses __Ready Stance__ as an offhand action, giving it the ability to counter attack.
3. As enemies attempt to pass, it uses __None Shall Pass__ and __Hold the Line__ to stop them.
4. If an enemy gets past, the Knight uses __Shield of Men__ to defend the ally.
5. If the Knight is high enough level and a massive attack is incoming, it can use _Defender Aura_ to halve damage to nearby allies.
  
  
__Charge into Battle__  
  
  
1. The Knight uses __Knight's Challenge__ to challenge an enemy.
2. The Knight uses it's movement and __Charge__ to close with the enemy. If it is at a high enough level, __Greater Charge__ results in an attack.
3. The knight uses __Overwhelming Strike__ for it's first attack, and gains advantage on it's second.
4. The knight uses a normal blow for the second attack. If it score's a critical hit, it can follow up with a __Shield Bash__ using its __Press the Advantage__ Combo.
5. If the Knight is high enough level, it gains another attack against challenged enemies due to its __Warrior's Vow__.
  
  

  
#### Paladin:
The Paladin now gains the following abilities:
* __Movement:__
  * __Pivot__ The Paladin can swap places with an adjacent ally.
* __Special Abilities:__
  * __Pledge:__ The Paladin pledges itself to a deity and receives special boons at levels 0, 5, 10, and 15.
  * __Spellcasting:__ The Paladin retains its ability to cast spells, and now learns them at a normal rate.
* __Combat Passive:__ 
  * __Hammer of Light:__ The paladin deals an extra dice of damage to undead.
  * __Bash:__ The paladin stuns an enemy on a critical hit.
  * __Faithful Weapon:__ Any thrown weapons return to the paladin.
  * __Last Hope:__ Any healing done while an ally is down or dead is doubled.
  * __Warrior Spirit:__ Any time a paladin strikes down an enemy they regain 1 action point.
  * __Beacon of Hope:__ All nearby allies gain +2 to all saves.
* __Combat Active:__
  * __Healing Blow:__ (Cost 1), add a dice of damage to an attack or spell. One quarter of the damage done is restored to allies within 15 feet.
  * __Healing Blast:__ (Cost 1), fire a 30 foot cone of healing energy. All allies struck by it regain half your level (round up) in d4's in health. Deals damage to enemies.
  * __Holy Shield:__ (Cost 1) Give an ally a shield with health equal to 2x your level. At higher levels this shield grants 1 turn of invulnerability.
  * __Guardian Ward:__ (Cost 0) Place a ward on an ally which grants a variety of effects as the paladin levels up:
    * __Armor__ The guardian ward grants 1-3 armor depending on level.
    * __Bonus Healing__ When the paladin heals an ally with a guardian ward it grants an extra dice of health.
    * __Link Lifeforce__ A paladin can take damage for an ally with a guardian ward (halved at high levels.)
    * __Guardian Spirit__ When an ally with a guardian ward strikes down an enemy, the paladin regains an action point.
  * __2 Guardian Wards__ At high levels, a paladin can place 2 guardian wards. At even higher levels, healing 1 of the allies also heals the other for half as much.
  * __Guardian Ward Conversion:__ At high levels, a paladin can convert a guardian ward on an ally to a Holy Shield.
  * __Mass Holy Shield__ (Capstone, Cost 3) Grant a Holy Shield to all allies within 30 feet. 
* __Combos__
  * __Blessing of Protection:__ After landing a critical hit, a paladin may give themself or an ally a holy shield.
  
  
The anticipated core gameplay loops for the knight are as follows:
  
  
__Area of Effect Frontline Healer__
1. The Paladin marks its allies with guardian wards.
2. It then stands amidst the front line, using a mixture of __Healing Blow__, and __Healing Blast__ and its spells to keep its allies alive.
3. The __Guardian Wards__ grant the marked allies an extra dice of health from any healing done.
4. At high levels, __Mass Holy Shield__ and __Ward Conversion__ can be used to grant allies bonus health.
  
  
__The Battery__
1. The Paladin places a __Guardian Ward__ on an ally.
2. The ally then rushes into the fray.
3. The Paladin takes their damage for them using __Link Lifeforce__ or __Greater Link Lifeforce__ for as long as possible possibly granting them health by healing a second __Guardian Ward__ recipient.
4. The Paladin then converts the ally's __Guardian Ward__ to a __Holy Shield__ using __Ward Conversion.__ This grants the ally a turn of invulnerability and 30 health at level 15.

  
## Rangers and Ruffians 2.1.2: The Action Point Economy Update. December 4, 2019
  
  

  
### Overview:
This revision:
1. Adds many abilities to the action point economy.
2. Modifies leveling up so that at each odd level players gain 1 stat point.
3. Fixes a bug which was causing disadvantages not to be displayed on the site.
  
  
  
  

  
### Ability Changes
Added an action point cost to the following abilities: __Berserk__, __Furious Blows__, __Repeating Shot__, __Called Shot__, __Detect Magic__, __From the Hip__, __Minor Medicine__, __Greater Medicine__, __Major Medicine__, __Disengage__, __Wild Sight__, __Penetration__, __Shield Bash__, __Shield of Men__, __Swoon__, __Fix Your Eyes on Me__, __Spirit of Rage__, __Reflexes__, __Disappear__, __Ascended Action__, __Aura of Advantage__, __Angelic Wings__, __Volley__, __Twin Blade Parry__, __Gumption__, __Spurred to Movement__.
  
  

  
## Rangers and Ruffians 2.1.1: The Rogues and Rangers Update. November 23, 2019
  
  

  
### Overview:
This revision brings:
1. Additional Race and Class Balance Tweaks, especially to ```Rouges``` and ```Rangers```.
2. An updated rule regarding player movement speed.
  
  

  
### Rule Changes:
* A character's movement distance on a given turn is now computed via the following formula: ```movement = 15ft + (5ft x dexterity)```,
  where negative dexterity values are treated as ```0```. This makes Dexterity an important stat even for the most ardent knight, and, paired
  with the ```2.1.0```'s update to make perception affect initiative, should make choosing stats on level up far more interesting.
  
  

  
### Additional Clarifications:
* Clarified how armor and shields work in the [Rulebook](Rulebook.md#armor-and-shields).
* Clarified how rest works. [Rulebook](Rulebook.md#rest).
  
  

  
### Race Balance Changes:
  
  

  
#### Catterwol
* __Abilities__
  * __Changed Fast Paws__ _Gain an extra offhand action_
    * __Change:__ The extra offhand action cannot be used as an attack.
    * __Reasoning:__ If the extra offhand was used as an attack, the Catterwol would have the highest damage output of any race by far.
  
  

  
#### Wood Elf
* __Abilities__
  * __Changed Counter Attack__ _Reaction, for 1 Action Point, counter attack when you are attacked_
    * __Change:__ You no longer have to roll to see if the counterattack succeeds.
    * __Reasoning:__ With a cost associated with the counterattack and ```Reaction``` meaning it can only be done once per turn, it felt unnecessarily punishing to force the ability to sometimes fail.
  
  

  
#### High Elf
* __Abilities:__
  * __Added Learned__ _Start with an extra language._
    * __Reasoning:__ In line with erudite High Elf.
  
  

  
#### Orc
* __Abilities:__
  * __Changed Thunderous Blow__ _Add an extra dice of damage to an attack for 1 action point._
    * __Change:__ Reduced cost from 2 to 1 action point.
    * __Reasoning:__ In line with costs for similar abilities.
  
  

  
#### Lizkin
* __Abilities:__
  * __Changed Posion Bite__ _Bite an enemy and have a chance to do poison damage_
    * __Change:__ Damage now scales with level.
    * __Reasoning:__ Ability is now worthwhile to use at higher levels.
  
  
  
  

  
#### Daemonspawn
* __Abilities:__ 
  * __Changed Charm__ _If an enemy fails an SP save, they cannot attack you._
    * __Change:__ You now also gain advantage on CHA checks with the affected entity.
    * __Reasoning:__ This makes sense and gives the ability more utility.
  * __Changed Sacrificial Rite:__ _Spend health to gain an extra action._
    * __Change:__ Amount of health needed is now equal to your level (minimum of 1) rather than a static 10.
    * __Reasoning:__ A static 10 health makes the ability impossible to use until high levels.
  
  
  
  

  
#### Automaton
* __Abilities:__
  * __Changed Piston Punch__ _Throw a powerful punch that could knock enemies prone._
    * __Change:__ Damage now scales with Level. Prone happens on contested Strength rather than critical hit. Chance scales with enemy size.
  * __Changed Overdrive:__ _Spend health to gain extra strength or dexterity._
    * __Change:__ Amount of health needed is now 2x the amount gained rather than a static 10. The maximum amount gained is 10.
    * __Reasoning:__ A static 10 health makes the ability impossible to use until high levels.
  
  

  
#### Sprout
* __Abilities:__
  * __Changed Harden:__ _Lose 2 DEX to gain 2 armor_
    * __Change:__ Now explicitly does not stack with other armor.
    * __Reasoning:__ It is not the intention of this ability to be used to create an un-killable strength based sprout build.
  
  

  
#### Hissling
* __Abilities:__
  * __Changed Tossed Around__ _Take half blunt damage, but be tossed back by the attack._
    * __Change:__ Take full damage if being tossed back makes you hit something.
    * __Reasoning:__ Adds an interesting dynamic to an already cool ability.
  
  

  
### Class Balance Changes:
  
  

  
#### Barbarian:
* __Abilities:__
  * __Merged Blind Rage and Berserk__ _Blind Rage: Advantage at SP saves while berserk._
    * __Reasoning:__ Berserk was already granting a static +1 to inner fire. Removed that and merged
      in blind rage to keep things simpler.
  * __Moved Always angry from level 7 to level 5__ _Go Berserk once per battle (up from 1/day)_
    * __Reasoning:__ Berserk is a core barbarian feature, so it was problematic to wait for it to become 
      consistently good until level 7.
  * __Removed Warmaster__ _Level 11, gain +1 additional strength when going berserk_
    * __Reasoning:__ This ability was underwhelming at best.
  * __Moved Savage Critical from level 5 to level 11__ _Additional damage on critical hit_
    * __Reasoning:__ Replaced Warmaster. Was a little overpowered at early levels when combined with other Barbarian 
      abilities. 
  
  

  
#### Knight:
* __Abilities:__
  * __Removed Shield Up__ _Level 3. Half damage from non-magic ranged attacks when you have a shield_
    * __Reasoning:__ Shields now come with their own abilities and requirements.
  * __Added New Ability Shield Master__ _Level 0. Don't take movement penalties from shield use._
    * __Reasoning:__ With the new shield and movement rules, this ability was a great replacement for ```Shield Up```.
  * __Added New Ability Charge!__ _Offhand. Run an extra 10ft. Contested STR check if you hit someone. Looser is knocked prone._
    * __Reasoning:__ With the move towards ```DEX``` based movement, the knight was being left behind. This new ability helps to make them feel like they have more movement.
  * __Changed Armored__ _You start with a suit of armor._
    * __Change:__ Armor is now Chainmail (```+1```) instead of Light Plate (```+2```).
    * __Reasoning:__ ```+2``` armor is too effective at level 0.
  
  

  
#### Paladin:
* __Abilities:__
  * __Swapped Chainmail with Armored__ _You start with armor_
    * __Reasoning:__ With the change of armored from ```+2``` to ```+1```, the chainmail ability became redundant.
  
  

  
#### Fighter
* __Abilities:__
  * __Renamed Trained Attack to Focused Attack__ _Re-roll an attack_
    * __Reasoning:__ It was confusing to have abilities named ```Trained Attack``` and ```Trained Precision```.
  * __Moved Determination from Level 1 to Level 0__ _Gain a D10 inspiration dice as an offhand_
    * __Reasoning:__ The fighter's level 0 was sparse, and Determination is a core class feature.
  * __Moved Minor Second Wind from Level 3 to level 1__ _Regain 1d6 health for 1 action point as an offhand action_
    * __Reasoning:__ Filled the void left by moving determination.
  * __Added Greater Second Wind to level 5__ _Heal yourself for 1d12 damage as an offhand for 1 action point_
    * __Reasoning:__ It was an oversight that their was a ```Minor``` and ```Major``` second wind but no ```Greater```.
  
  

  
#### Ranger
This was a larger Rework of the Ranger, which had kind of lost its way and become a Jack of all Trades,
Master of None. Now, the Ranger is a very competent fighter with minor magic, who excels at tracking enemies.
In the future, a monster hunter subclass will likely be added.
  
  
* __Abilities:__
  * __Removed Shifting Cloak__ _You begin with a cloak which gives you advantage on stealth checks when still_.
    * __Reasoning:__ Redundant, did the same thing as ```Camouflage```.
  *  __Moved Tracker from Level 3 to Level 0__ _Advantage on tracking checks_.  
    * __Reasoning:__ Tracking is a core ranger feature, and should be present from level 0.
  * __Added New Ability, Embers__ _Shoot fire 10ft. Deals 1d4 dmg. Increases to 1d8 at LV3, 1d10 LV6, 1d12 LV9, 2d12 LV12._
    * __Reasoning:__ The Ranger was missing a solid damage dealing ability. Embers is the solution.
  * __Changed Finesse Strike__ _Add additional damage to an attack, which is extended over two turns if the enemy fails a SP save._
    * __Change:__ The ability used to add an additional dice of damage _and_ then another next turn if the enemy failed an SP save.  Now it adds an additional dice of damage and half as much next turn on a failed SP save.
    * __Reasoning__ This is more balanced at lower levels.
  * __Moved Finesse Strike from Level 5 to Level 3__
    * __Reasoning:__ Rangers gain ```Twin Blades``` at level 5, which overshadowed the value of ```Finesse Strike```.
  * __Removed Monster Slayer__ _Level 9, bonus damage to monsters_
    * __Reasoning:__ Didn't work with the more streamlined Ranger. Will return with new ```Monster Hunter``` subclass later.
  * __Removed Disengage__ _Level 9, Don't provoke exposed attacks as an offhand action._
    * __Reasoning:__ Didn't quite fit the Ranger class.
  * __Added New Ability Elemental Weapon__ _Level 9, Change your weapon's damage type for 1 action point. Lasts until dispelled._
    * __Reasoning:__ Fit well with the capstone ```Fire and Ice```. A good and unique ability.
  * __Moved Spell of Darkvision From Level 11 to Level 3__ _Cast Darkvision on yourself for 1 Action Point_
    * __Reasoning:__ Too late in the game for an ability like this. A great ability at low levels.
  * __Removed Disarming Blow__ _Level 11, Disarm an opponent on a critical hit_
    * __Reasoning:__ Interesting ability, but did not fit with Ranger or Level 11.
  * __Added new Ability Major Medicine__ _Level 11, make 1x per day make a potion equivalent to a greater healing poition. Lasts 24 hours._
    * __Reasoning:__ It was an oversight that there were ```Minor``` and ```Greater``` Medicine abilities, but no ```Major```.
  * __Moved Expert Tracker from Level 13 to Level 11__ _Add 1d6 to tracking checks._
    * __Reasoning:__ This ability is quite useful, and it is better to get it to the player earlier.
  
  

  
#### Rogue
* __Abilities__
  * __Removed Ruffians__ _Base ability, gain advantage when speaking with seedy folk._
    * __Reasoning:__ This may be part of a larger trend. It is in consideration that we may add a new system ```Backgrounds```, which can be chosen from to gain specific (very small) advantages or abilities. This ability would fall under one of those Backgrounds.
  * __Changed Ranged Weapon Proficiency to Thrown Weapon Proficiency__
    * __Reasoning:__ It wasn't the intention of the Rogue design that they would be able to use bows by default.
  * __Added Spell of Darkvision to Assassin Level 5__ _Gain Darkvision for 1 action point_
    * __Reasoning:__ Previously, the Assassin gained regular Darkvision at level 9. This was both too late to be useful and didn't make sense.
  * __Added New Ability Sticky Fingers to Level 5 Thieves__ _Add 1d6 to checks made to steal something_.
    * __Reasoning:__ Thieves didn't actually have many abilities that made them better at thievery.
  * __Added New Ability Spell of Minor Invisibility to Level 9 Assassins__ _Become invisible for 5 minutes for 1 action point_
    * __Reasoning:__ With Darkvision moved from Level 9 to Level 5, a new ability was needed. This will add additional utility to the assassin, and should be very strong paired with their Strike from the Shadows ability.
  * __Returned Assassinate as a Level 15 Assassin Capstone__
  
  

  
#### Archer
* __Abilities__
  * __Removed Arrow Stab__ _Make a 1d6 arrow stab._
    * __Reasoning:__ Better than a bow at low levels, totally useless at high levels. Not needed in the game.
  
  

  
#### Bard
* __Abilities__
  * __Modified Minor, Greater, and Major Restful Melody__ _Bonus health for allies during rest._
    * __Change:__ Instead of granting 1, 2, or 3 d8 extra healing, it grants 1, 2, or 3 rest dies of healing.
    * __Reasoning:__ In line with new rest health rules.
  
  

  
#### Sorcerer
* __Clarification__
  * Finally clarified sorcerer's ```Spell Modification``` Ability. 
  
## Rangers and Ruffians 2.1.0: The Skills Update. November 19, 2019
  
  

  
### New Features:
*  __The Last Oversized Update!__
    *  With the introduction of the changelog, future updates will be more frequent, but much smaller.
*  __The Rangers and Ruffians Rulebook!__
    *  It was long past time for the rules of ```RnR``` to finally get written down, and with new Poohbah's stepping up to the plate,
       we finally did it!
 * __A Brand New Website!__
     * We acquired ```www.rangersandruffians.com``` and are now hosting a website with all of the game rules!
*  __Stat Rebalances__
    *  With the formalization of the Rulebook, it finally became time to also formalize the core "balance" math of Rangers and Ruffians,
       so that new Poohbahs can more easily get up and running. To this end, the following balance changes were made:
    *  All Races now add ```+1``` to 2 stats (or ```+2```  to 1 stat) and ```-1``` to 2 stats (or ```-2``` to 1 stat).
       This means that race plays a little bit less of a role in the stat makeup of a character than it previously did. This
       is great, as it enforces the idea that _any_ race can pair with any _any_ class.
    *  Not including ```Luck``` and ```Health Dice```, classes now assign a ```2```, ```1```, ```0```, ```-1```, ```-2``` and ```-3```
       to their other stats. This keeps an internal logic, so that all classes are good and bad at the same number of things.
    *  These new changes mean that, for the first time ever, we can roll for stats! See the ```Rulebook``` for more info.
    *  ```Luck``` and ```Health Dice``` now vary inversely, so if you have a high ```Health Dice``` you have a low starting
      ```Luck``` and vice versa.
*  __Weapon Balance:__
    *  With new stat balance came new ```health```, ```rest```, ```weapon damage``` and ```magic damage``` balance tweaks.
*  __Renamings__
    *  __Spell Points -> Action Points:__ ```Spell Points``` were renamed to ```Action Points```. This reflects their new use by non-mage classes.
    *  __Spell Levels -> Spell Tiers:__ ```Spell Levels``` were renamed to ```Spell Tiers```. With the character leveling system in place, it is confusing
      to talk about both spell and character levels.
    *  __Opportunity Attacks -> Exposed Attacks__
*  __Introduction of Skills:__
    *  When a player reaches an even level, they may now __choose__ either to gain 2 stat points to spend or to gain a new skill.
    *  Skills are like small abilities that give you new ways to play your character.
    *  For example, a knight might gain access to firearms!
    *  Some skills have stat prerequisites. For example, you need 3 intelligence to gain access to tier zero magic.
    *  Some skills are upgrades of other skills. For example, you need the "Cook" skill before you can get the "Master Chef" skill.
*  __New Race:__
    *  A new challenger approaches! The Kragraven is a bird based race. It has vestigial wings that it can use to jump high or to coast from great heights.
  
  

  
### Rule Changes:
*  Spell Power is now computed as ```12 + INF``` rather than ```10 + (2 x INF)```. Under the previous system, if a player or enemy had even modestly high inner fire, it became nearly impossible to avoid their spells. For example, if an enemy had ```4``` effective inner fire, you would have to roll an ```18``` or greater to avoid their spell ```(10 + (2 x 4))```. Now, you need to beat a ```16``` ```(12 + 4)```.
* Perception is now added to initiative. This makes perception a more viable stat, and makes choosing stats on level-up
  more interesting.
  
  

  
### All Races and Classes:
The stat changes referenced above affected all races and classes, and are not detailed here to save space.
To see the result of the changes, please view the ```Race``` and ```Class``` sections of the ```Rulebook.```
  
  

  
### Race Balance Changes:

  
#### Human:
* __Abilities__
  * __Changed__: __Last Stand__
      * __Change:__ now occurs when health is below 25% rather than 20%. It is easier to calculate a quarter than a fifth.
  * __Removed:__ __Tactics:__ _Double damage for 2 SP._
    * __Reasoning:__ This ability has been overpowered for a while, despite previous nerfs.
  * __Added Adaptable:__ _Humans gain advantage on subsequent saves after a failure._
    * __Reasoning:__ This situational ability makes humans more survivable/interesting under certain conditions.
    * __Concern:__ This ability may be difficult for players to remember to use.
  * __Added Skilled:__ _Humans begin with one extra skill._
    * __Reasoning__ Removing __Tactics__ left human's underpowered. This helps bridge the power gap while also allowing each human to feel more unique.
  
  

  
#### Catterwol:
* __Abilities:__
  * __Changed:__ __Fast Paws__ _Cost 1, Gain an additional action._
    * __Change:__ Now grants a bonus action rather than an action.
    * __Reasoning:__ Balances low level the Catterwol, which can't yet attack as an offhand action.
  
  
  
  

  
#### High Elf:
* __Abilities:__
  * __Added Inherent Magic__ _grants a tier zero spell regardless of class_
    * __Reasoning:__ Always intended but forgotten. Part of what makes a High Elf unique from other elven subraces.
  
  

  
#### Fleetfoot Halfling:
* __Abilities:__
  * __Removed Bull Rush__ _Charge an enemy for a chance to grapple_
    * __Reasoning:__ Not in line with small, sneaky, fleetfoot halfling.
  * __Added Nimble Fingers__ _Advantage when stealing_
    * __Reasoning:__ In line with small, sneaky fleetfoot halfling.
  
  
  
  

  
#### Lizkin:
* __Abilities:__
  * __Combined Camouflage and Color Choice__
  * __Changed Color Choice__
    * __Change:__ Now costs 1 SP and can explicitly be used for stealth.
    * __Reasoning:__ Cost increase due to added benefit.
  * __Changed Poison Bite__ _1d6 bite with potential to poison_
    * __Change:__ Cost increased from 0 to 1.
    * __Reasoning:__ In line with other race ability costs.
  * __Changed Shed Tail__ _Shed your tail to break a grapple_.
    * __Change:__ Now once per week rather than once per day.
    * __Reasoning:__ Logic of growing a new tail.
  
  

  
#### Orc:
* __Abilities:__
  * __Thunderous Blow__
    * __Change:__ Now adds 1 attack dice rather than double damage.
    * __Reasoning:__ Unbalanced at high levels.
  
  

  
#### Dwarf:
* __Abilities:__
  * __Combined Miner's Eye and Mending into Forgeborn__
    * __Reasoning:__ Ability Consolidation.
  * __Removed Natural Sprinter__ _Advantage on attacks after running a short distance_
    * __Reasoning:__ Difficult to arbitrate in practice.
  * __Replaced Stone Skin with Incombustible__
    * __Reasoning:__ Stone skin granted dwarves half damage when attacked by blunt weapons, which could be unbalanced in many situations, especially when paired with a class like a heavily armored knight. Incombustible grants dwarves half damage from fire. This is also useful, but not in quite as many situations. It also helps establish a lore reason for the dwarves affinity for forges.
  
  

  
#### Daemonspawn:
* __Abilities:__
  * __Renamed Infernal Blood to Sacrificial Rite__
  * __Added Incombustible__ _Half Fire Damage_
    * __Reasoning:__ Makes sense due to lore.
  
  

  
#### Sprout:
* __Abilities:__
  * __Removed Mantel__ _Advantage on Climbing_
    * __Reasoning:__ Redundant. __Scurry__ grants the same advantages.
  
  

  
#### Automaton:
* __Abilities:__
  * __Changed Self Repair__ _Spend a full turn to heal_
    * __Change:__ Can now be done every turn rather than every 3 turns.
    * __Reasoning:__ Because Automata can't drink potions and self repair takes a full turn, the situations where using this ability two turns in a row are necessary should be more common than situations where it is abused.
  
  

  
#### Hissling:
* __Abilities:__
  * __Removed And this part goes here...__ _Craft things with garbage._
    * __Reasoning:__ While this ability was fun, it devalued the gnome, and the hissling already has many cool abilities.
  * __Changed Tossed Around__ _Half blunt damage, but tossed back_
    * __Change:__ Distance now scales with enemy size.
    * __Reasoning:__ Balanced and much more interesting.
  
  

  
#### Waterborn:
* __Abilities:__
  * __Changed Water Healing__ _Extra Healing when sleeping in Water_
    * __Change:__ No longer applies to short rests.
    * __Reasoning:__ Treating short rest as a full sleep was unbalanced.
  * __Removed Beast Form__ _For 1 Action Point, gain +1 STR, DEX, INF and extra HP_
    * __Reasoning:__ While a cool idea, there was no reason not to spam beast form in every encounter. This could be rectified by adding costs, but the waterborn already has a tight set of abilities, so it was cut instead.
  * __Renamed Unbreathing to Water Breating__
  * __Combined Dry up and Water Breating__
  
  

  
### Class Balance Changes:
  
  

  
#### All:
*  All classes now have 15 levels. Abilities were redistributed accordingly.
*  Multi-class option is no longer listed as an ability.
*  Spell Power is no longer listed as an ability.
  
  

  
#### Barbarian:
* __Abilities:__
  * __Changed Glory__ _When you are at low health, double your damage._
    * __Change:__ Now activates at 25% health instead of 10% health.
    * __Reasoning:__ Even at high level, 10% health isn't much. Increasing the activation percentage to 25% makes this ability actually useful.
  * __Changed Taunt:__ _SP save. On failure, force all within 30ft. to attack only you._
    * __Change:__ Now costs 1 action point.
    * __Reasoning:__ Makes taunt use more tactical.
  * __Clarified Taunt:__ _Force enemies to attack you if they fail an Spell Power Save._
    * __Change:__ Clarified 30 foot radius.
    * __Reasoning:__ Ability was non-specific about range of use.
  * __Ruffians is now a base ability__
    * __Reasoning:__ It doesn't make sense for a character who multi-classes to Barbarian to suddenly have advantage when speaking with ruffians.
  
  

  
#### Knight:
  * __Abilities:__
    * __Changed Trained Precision:__ _Add extra damage to an attack._
      * __Change:__ Damage now scales with the weapon you are holding rather than just being +1d6.
      * __Reasoning:__ Scales better to higher levels.
    * __Changed Shield Up:__ _Half damage from targeted ranged attacks._
      * __Change:__ Clarified that Shield Up works for non-magic, targeted attacks (e.g. not a lightning bolt).
      * __Reasoning:__ This was the intention of the ability.
    * __Removed Hold the Line:__ _Advantage on attacks when an ally is down._
      * __Reasoning:__ Redundant with Last Line of Defense _Extra damage when an ally is down_. Rolling more damage is easier than advantage.
    * __Changed Steel Yourself:__ _Choose to take half damage from an attack._
      * __Change:__ Now costs 1 action point instead of 2.
      * __Reasoning:__ While steel yourself is strong, the knight has many other options, and using this ability often will still drain action points quickly, especially if an enemy has multi-attack.
    * __Changed Cleave__
      * __Change:__ Cleave no longer grants bonus damage, but now allows knights to passively hit an second enemy that is adjacent to the first.
      * __Reason:__ The new iteration of Cleave is more interesting on a grid.
    * __Added Ready Stance:__ ___Level 6, Spend an offhand action to gain +1d6 armor for one turn.___
    * __Added Stalwart Defender:__ ___Level 11, Allies within 30 feet gain 1 armor.___
  
  

  
#### Paladin:
  * __Abilities:__
    * __Changed Hammer of Light:__ _Extra damage to undead._
      * __Change:__ Damage now scales with the weapon you are holding rather than just being +1d6.
      * __Reasoning:__ Scales better to higher levels.
    * __Removed Sinner's Bane:__ _Extra damage to undead._
      * __Reasoning:__ Redundant with Hammer of Light _Extra damage to undead._
  
  

  
#### Beastmaster:
* __Abilities__
  * __Changed Leaping Strike__ _Leap forward to deal extra damage. LV0 1d6, LV5 2d6, LV10 3d6._
    * __Change:__ Now costs 1 action point rather than 0.
    * __Reason:__ In line with new action point rules.
  * __Inseparable__  _Offhand. Teleport yourself to your animal or vice versa._
    * __Change:__ Now costs 1 action point rather than 0.
    * __Reason:__ In line with new action point rules.
  
  

  
#### Sorcerer:
* __Abilities:__
  * __Changed Prepare Spell__
    * __Change:__ Instead of spending a minute to cast a spell at -2, now allows sorcerer to pick 1 spell per day to be at lower SP.
    * __Reason:__ Old ability was redundant with spell modifications. New ability requires more interesting planning.
  
  

  
#### Fighter:
* __Abilities__
  * __Changed Whirlwind of Blades__ _Level 15, Make an additional 3 attacks on your turn._
    * __Change:__ Decreased cost from 3 action points to 2.
    * __Reasoning:__ While Whirlwind of Blades is a very powerful ability, at level 15, a fighter has many options, and a cost of 3 is too prohibitive to see the ability used.
  * __Changed Find Center__ _Level 11, Free Action. Gain advantage on all things for 1 turn._
    * __Change:__ Find action is now a free action rather than an offhand action, but now costs 1 action point.
    * __Reasoning:__ Using an offhand action to use find center limits the things that a fighter can do on their turn. Adding the ability to the action point economy but allowing a full turn is more interesting.
  * __Changed Major Second Wind__ _Level 8, Heal yourself for 2d10 damage as an offhand._
    * __Change:__ Decreased cost from 2 to 1.
    * __Reasoning:__ Major second wind is meant as a replacement for Minor second wind (_Level 2, Heal yourself for 1d6 as an offhand_ ), not an alternative.
  * __Changed Resolve__ _Level 3, When your health is low, all attacks do half damage against you._
    * __Change:__ Activates at 25% instead of 20%.
    * __Reasoning:__ It is easier for players to compute 1/4 than 1/5. Works better at lower levels.
  
  

  
#### Highborn:
* __Abilities:__
  * __Changed Rally Cry__ _Level 13, Allow all allies to do extra damage on their next attack_
    * __Change:__ now costs 1 action point, rather than free use once every three turns. Now grants an extra damage dice rather than +1d6
    * __Reasoning:__ Matches new action point scheme, scales better.
  * __Changed Aura of Peace__ _Level 14, Grants nearby allies bonus health_
    * __Change:__ Now grants a flat 10 health rather than 1 vitality.
    * __Reasoning:__ Vitality is no longer a stat.
  * __Changed Beauty Incarnate__
    * __Change:__ Now a base ability.
    * __Reasoning:__ Multi-classing to a highborn no longer makes you more attractive.
  * __Changed Feeling Lucky__ _Level 7, spend a action point to get bonus damage based on your luck._
    * __Change:__ Grants a number of d4's equal to luck rather than raw luck to an attack.
    * __Reasoning:__ Scales better with increased luck.
  * __Added Strike First__ _Level 15, Reaction. When an enemy attacks you, attack them first._
    * __Reasoning:__ Highborn lacked a strong capstone ability.
  * __Changed Disarming__ _Level 4, Reaction. Force enemy to make an attack at disadvantage on a failed CHA vs INF save._
    * __Change:__ Failure now possible, but can be done once per turn.
  * __Added Lionhearted__ _Level 12, Advantage on Spell Power saves_
  * __Added Ability Side By Side__ _Level 8, advantage when adjacent to an ally._
  
  

  
#### Ranger:
* __Abilities:__
  * __Removed Trap Master__ _Able to create simple traps._
    * __Reasoning:__ Not in line with other ranger abilities. Too difficult to use in play.
  * __Changed Fire and Ice__ _Level 15, Add 1d6 elemental damage to each of your swords._
    * __Change:__ Now costs 1 action point instead of 2.
    * __Reasoning:__ Increases the value of this capstone ability.
  * __Changed Minor Medicine:__ _Level 0, Create a health potion once per day (lasts 24 hours)_
    * __Change:__ Removed requirement that you must be in your favorite terrain. Ability now creates a _Salve_ (heals 1d6+2 at
      the time of this writing). The ability previously created a 1d20 health potion.
    * __Reasoning:__ Favorite terrain requirement was restrictive. New health regained is in line with level system health.
      Creating a _Salve_ means that the ability will scale more easily with any future health balancing changes.
  * __Changed Greater Medicine:__ _Level 7, Create a health potion once per day (lasts 24 hours)_
    * __Change:__ Removed requirement that you must be in your favorite terrain. Ability now creates a _Minor Health Potion_ (heals 1d12+3 at
      the time of this writing). The ability previously created 2 1d20 health potions.
    * __Reasoning:__ Favorite terrain requirement was restrictive. New health regained is in line with level system health.
      Creating a _Minor Health Potion_ means that the ability will scale more easily with any future health balancing changes.
  * __Changed Monster Slayer:__ _Additional damage vs monsters._
    * __Change:__ Rather than dealing a static 1d10 additional damage, monster slayer now awards an additional dice of damage.
    * __Reasoning:__ In line with other such abilities. Additional damage dice scale better than static values.
  
  

  
#### Rouge:
* __Abilities:__
  * __Added Subclass Thief Ability Soft Landing:__ _Level 7, Reduce any falling damage by 20 feet._
  
  

  
#### Bard:
* __Abilities:__
  * __Added Imbue Weapon:__ _Level 5, Costs 1 action point. Add a dice of elemental damage to your weapon for 1 battle/hr._
    * __Reasoning:__ Imbue weapon was a holdover from the battle mage, and makes the bard more versitle.
      The ability was updated to add a dice of damage rather than a static 1d6.
  * __Added Greater Imbue Weapon:__ _Level 5, Costs 2 action points. Add 2 dice of elemental damage to your weapon for 1 battle/hr._
    * __Reasoning:__ Imbue weapon was a holdover from the battle mage, and makes the bard more versitle.
      The ability was updated to add a 2 dice of damage rather than a static 1d10.
  * __Boozehound is now a base ability:__
    * __Reasoning:__ Subclassing to bard no longer gives you increased alcohol tolerance.
  * __Removed multi-action__ _Grants the wielder an extra action every 3 turns._
    * __Reasoning:__ Multi-action been replaced with offhand attacks and spells.
  * __Changed Restful Melody:__ _Grant your party extra health when resting._
    * __Change:__ Restful Melody has been split into three abilities tiers (lesser, greater, major)
      gained at levels 1, 9, 11, which grant the party 1d4, 1d10 and 2d10 extra health respectively. All tiers cost 1 action point.
    * __Reasoning:__ Splitting Restful Melody into tiers means that it scales much better with new health
      balancing. Giving restful melody a cost means that players must make a choice about whether to do it.
  
  

  
#### Cleric:
* __Abilities:__
  * __Changed Last Ditch Prayer:__ _Level 3: Your deity helps you with a roll._
    * __Change:__ Now lets you add 1d8 to a roll rather than advantage. Cost changed from 1/3 turns
      to 1 action point.
    * __Reasoning:__ Old advantage based ability conflicts with the new _Luck_ system. Cost is in
      line with other such abilities.
  
  

  
#### Druid
* __Abilities:__
  * __Changed Ascended Action:__ _Level 15, take an extra action out of turn when in the ascended state._
    * __Change:__ Ascended action is now an extra action _and_ a movement.
    * __Reasoning:__ Increases utility of the capstone.
  
  

  
#### Wizard:
* __Abilities:__
  * __Changed Walking Stick:__ _You start with an staff that adds extra damage to magic attacks._
    * __Change:__ The magic staff now adds +1 damage rather than +1d4 damage.
    * __Reasoning:__ This is in line with current enemy balancing.
  * __Wizards learn new spell tiers one level earlier than other casters.__
    * __Reasoning:__ Helps to make wizards stand out among other casters.
  
  

  
#### Archer:
* __Abilities:__
  * __Changed Focus:__ _Level 0, Spend 1 Action point to gain advantage on an attack._
    * __Change:__ Focus now costs 1 action point, up from 1/3 turns.
    * __Reasoning:__ In line with new action point ability costs.
  * __Dual Shot:__ _Level 3, Spend 1 Action point to fire two arrows at once._
    * __Change:__ Dual Shot now costs 1 action point, up from 1/3 turns.
    * __Reasoning:__ In line with new action point ability costs.
  * __Dual Shot:__ _Level 3, Spend 1 Action point to fire two arrows at once._
    * __Change:__ Dual Shot now costs 1 action point, up from 1/3 turns.
    * __Reasoning:__ In line with new action point ability costs.
  * __Added Expert Fletcher:__ _Level 13 Reduce all arrow costs by 2._
    * __Reasoning:__ Allows better arrows to be used more freely at higher levels.
  * __Tuned Arrow Economy:__
    * __Change:__ With the introduction of expert fletcher, revisited arrow action point costs.
  
  

  
#### Gunslinger:
* __Abilities:__
  * __Changed Flash Grenades:__ _Blind enemies who fail a Dex check._
    * __Change:__ Now cost 1 action point, rather than 3/day.
    * __Reasoning:__ In line with action point economy.
  * __Added Marksman Ability Bull Rush:__ _Level 1 Rush forward at least 10 feet to deal an extra dice of melee damage to an enemy (Bayonet Charge)._
  
  

  
#### Spellbooks:
  * __Balance Changes:__ Spell damage was balanced as part of the health/rest/monster/weapon damage re-balancing.

  
## Pre- Rangers and Ruffians 2.1.0 (Pre- November 2019)
* This changelog was first established in Rangers and Ruffians 2.1.0. For details
  about prior releases, please review the Github commit history.


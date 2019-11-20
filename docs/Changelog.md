# Changleog
## Rangers and Ruffians Version 2.1.0

### New Features:
0. __The Last Huge Update!__
  1. With the introduction of the changelog, future updates will be more frequent, but much smaller.
1. __The Rangers and Ruffians Rulebook!__
  1. It was long past time for the rules of ```RnR``` to finally get written down, and with new Poohbah's stepping up to the plate,
     we finally did it! Please see ```docs/Rulebook.md``` to read through the (hopefully) complete rules of Rangers and Ruffians!
2. __Stat Rebalances__
  1. With the formalization of the Rulebook, it finally became time to also formalize the core "balance" math of Rangers and Ruffians,
     so that new Poohbahs can more easily get up and running. To this end, the following balance changes were made:
  2. All Races now add ```+1``` to 2 stats (or ```+2```  to 1 stat) and ```-1``` to 2 stats (or ```-2``` to 1 stat).
     This means that race plays a little bit less of a role in the stat makeup of a character than it previously did. This
     is great, as it enforces the idea that _any_ race can pair with any _any_ class.
  3. Not including ```Luck``` and ```Health Dice```, classes now assign a ```2```, ```1```, ```0```, ```-1```, ```-2``` and ```-3```
     to their other stats. This keeps an internal logic, so that all classes are good and bad at the same number of things.
  4. These new changes mean that, for the first time ever, we can roll for stats! See the ```Rulebook``` for more info.
  5. ```Luck``` and ```Health Dice``` now vary inversely, so if you have a high ```Health Dice``` you have a low starting
    ```Luck``` and vice versa.
3. __Weapon Balance:__
  1. With new stat balance came new ```health```, ```rest```, ```weapon damage``` and ```magic damage``` balance tweaks.
4. __Renamings__
  1. __Spell Points -> Action Points:__ ```Spell Points``` were to ```Action Points```. This reflects their new use by non-mage classes.
  2. __Spell Levels -> Spell Tiers:__ ```Spell Levels``` were renamed to ```Spell Tiers```. With the character leveling system in place, it is confusing
    to talk about both spell and character levels.
  3. __Opportunity Attacks -> Exposed Attacks__ 
5. __Introduction of Skills:__
    1. When a player reaches an even level, they may now __choose__ either to gain 2 stat points to spend, or to gain a new skill.
    2. Skills are like small abilities that give you new ways to play your character.
    3. For example, a knight might gain access to firearms!
    4. Some skills have stat prerequisites. For example, you need 3 intelligence to gain access to tier zero magic.
    5. Some skills are upgrades of other skills. For example, you need the "Cook" skill before you can get the "Master Chef" skill.
6. __New Race:__
    A new challenger approaches! The Kragraven is a bird based race. It has vestigial wings that it can use to jump high or to coast from great heights.

### Rule Changes:
1. Spell Power is now computed as 12 + INF rather than 10 + (2 x INF). Under the previous system, if a player or enemy had even modestly high inner fire, it became nearly impossible to avoid their spells. For example, if an enemy had 4 inner fire, you would have to roll an 18 or greater to break their spell (10 + (2 x 4)). Now, you need to beat a 16 (12 + 4).

### All Races and Classes:
The stat changes referenced [above](#new-features) affected all races and classes, and are not detailed here to save space.
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
    * __Reasoning:__ Balances the Catterwol, where they can't yet attack as an offhand action.


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
  * __Combined Camouflage and Color Choice_
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
    * __Reasoning:__ Because Automaton's can't drink potions and self repair takes a full turn, the situations where using this ability two turns in a row are necessary should be more common than situations where it is abused.

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
    * __Reasoning:__ Even at low level, 10% health isn't much. Increasing the activation percentage to 25% makes this ability actually useful.
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
    * __Removed Taunt:__ _Force enemies to attack you if they fail a Spell Power Save._
      * __Reasoning:__ Ability bloat. May add a knight subclass and add taunt to it in the future.
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
      * __Reasoning:__ Redundant with Hammer of Light _Extra damage to undead._.

#### Beastmaster:
* __Abilities__
  * __Changed Leaping Strike__ _Leap forward to deal extra damage. LV0 1d6, LV5 2d6, LV10 3d6._
    * __Change:__ Now costs 1 action point rather than 0.
    * __Reason:__ In line with new action point rules.
  * __Inseparable___  _Offhand. Teleport yourself to your animal or vice versa._
    * __Change:__ Now costs 1 action point rather than 0.
    * __Reason:__ In line with new action point rules.

#### Sorcerer:
* __Abilities:__
  * __Changed Prepare Spell__
    * __Change:__ Instead of spending a minute to cast a spell at -2, now allows sorcerer to pick 1 spell per day to be at lower SP.
    * __Reason:__ Old ability was redundant with spell modifications. New ability requires more interesting planning.

#### Fighter:
* __Abilities__
  * __Changed Whirlwind of Blades__ ___Level 15, Make an additional 3 attacks on your turn.___
    * __Change:__ Decreased cost from 3 action points to 2.
    * __Reasoning:__ While Whirlwind of Blades is a very powerful ability, at level 15, a fighter has many options, and a cost of 3 is too prohibitive to see the ability used.
  * __Changed Find Center__ ___Level 11, Free Action. Gain advantage on all things for 1 turn.___
    * __Change:__ Find action is now a free action rather than an offhand action, but now costs 1 action point.
    * __Reasoning:__ Using an offhand action to use find center limits the things that a fighter can do on their turn. Adding the ability to the action point economy but allowing a full turn is more interesting.
  * __Changed Major Second Wind__ _Level 8, Heal yourself for 2d10 damage as an offhand._
    * __Change:__ Decreased cost from 2 to 1.
    * __Reasoning:__ Major second wind is meant as a replacement for Minor second wind (_Level 2, Heal yourself for 1d6 as an offhand_ ), not an alternative.
  * __Changed Resolve__ _Level 3, When your health is low, all attacks do half damage against you._
    * __Change:__ Activates at 25% instead of 20%.
    * __Reasoning:__ It is easier for players to compute 1/4 than 1/5. Works better at lower levels.

##### Highborn:
* __Abilities:__
  * __Changed Rally Cry__ ___Level 13, Allow all allies to do extra damage on their next attack___
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
  * __Removed Trap Master__ ___Able to create simple traps.___
    * __Reasoning:__ Not in line with other ranger abilities. Too difficult to use in play.
  * __Changed Fire and Ice__ ___Level 15, Add 1d6 elemental damage to each of your swords.___
    * __Change:__ Now costs 1 action point instead of 2.
    * __Reasoning:__ Increases the value of this capstone ability.
  * __Changed Minor Medicine:__ ___Level 0, Create a health potion once per day (lasts 24 hours)___
    * __Change:__ Removed requirement that you must be in your favorite terrain. Ability now creates a _Salve_ (heals 1d6+2 at
      the time of this writing). The ability used to create a 1d20 health potion.
    * __Reasoning:__ Favorite terrain requirement was restrictive. New health regained is in line with level system health.
      Creating a _Salve_ means that the ability will scale more easily with any future health balancing changes.
  * __Changed Greater Medicine:__ ___Level 7, Create a health potion once per day (lasts 24 hours)___
    * __Change:__ Removed requirement that you must be in your favorite terrain. Ability now creates a _Minor Health Potion_ (heals 1d12+3 at
      the time of this writing). The ability used to create 2 1d20 health potions.
    * __Reasoning:__ Favorite terrain requirement was restrictive. New health regained is in line with level system health.
      Creating a _Minor Health Potion_ means that the ability will scale more easily with any future health balancing changes.
  * __Changed Monster Slayer:__ ___Additional damage vs monsters.___
    * __Change:__ Rather than dealing a static 1d10 additional damage, monster slayer now awards an additional dice of damage.
    * __Reasoning:__ In line with other such abilities. Additional damage dice scale better than static values.

#### Rouge:
* __Abilities:__
  * __Added Subclass Thief Ability Soft Landing:__ ___Level 7, Reduce any falling damage by 20 feet.___

#### Bard:
* __Abilities:__
  * __Added Imbue Weapon:__ ___Level 5, Costs 1 action point. Add a dice of elemental damage to your weapon for 1 battle/hr.___
    * __Reasoning:__ Imbue weapon was a holdover from the battle mage, and makes the bard more versitle.
      The ability was updated to add a dice of damage rather than a static 1d6.
  * __Added Greater Imbue Weapon:__ ___Level 5, Costs 2 action points. Add 2 dice of elemental damage to your weapon for 1 battle/hr.___
    * __Reasoning:__ Imbue weapon was a holdover from the battle mage, and makes the bard more versitle.
      The ability was updated to add a 2 dice of damage rather than a static 1d10.
  * __Boozehound is now a base ability:__
    * __Reasoning:__ Subclassing to bard no longer gives you increased alcohol tolerance.
  * __Removed multi-action__ ___Grants the wielder an extra action ever 3 turns.___
    * __Reasoning:__ Multi-action been replaced with offhand attacks and spells.
  * __Changed Restful Melody:__ ___Grant your party extra health when resting.___
    * __Change:__ Restful Melody has been split into three abilities tiers (lesser, greater, major)
      gained at levels 1, 9, 11, which grant the party 1d4, 1d10 and 2d10 extra health respectively. All tiers cost 1 action point.
    * __Reasoning:__ Splitting Restful Melody into tiers means that it scales much better with new health
      balancing. Giving restful melody a cost means that players must make a choice about whether to do it.

#### Cleric:
* __Abilities:__
  * __Changed Last Ditch Prayer:__ ___Level 3: Your deity helps you with a roll.___ 
    * __Change:__ Now lets you add 1d8 to a roll rather than advantage. Cost changed from 1/3 turns
      to 1 action point.
    * __Reasoning:__ Old advantage based ability conflicts with the new _Luck_ system. Cost is in
      line with other such abilities.

#### Druid
* __Abilities:__
  * __Changed Ascended Action:__ ___Level 15, take an extra action out of turn when in the ascended state.___
    * __Change:__ Ascended action is now an extra action _and_ a movement.
    * __Reasoning:__ Increases utility of the capstone.

#### Wizard:
* __Abilities:__
  * __Changed Walking Stick:__ ___You start with an staff that adds extra damage to magic attacks.___
    * __Change:__ The magic staff now adds +1 damage rather than +1d4 damage.
    * __Reasoning:__ This is in line with current enemy balancing.
  * __Wizards learn new spell tiers one level earlier than other casters.__
    * __Reasoning:__ Helps to make wizards stand out among other casters.

#### Archer:
* __Abilities:__
  * __Changed Focus:__ ___Level 0, Spend 1 Action point to gain advantage on an attack.___
    * __Change:__ Focus now costs 1 action point, up from 1/3 turns.
    * __Reasoning:__ In line with new action point ability costs.
  * __Dual Shot:__ ___Level 3, Spend 1 Action point to fire two arrows at once.___
    * __Change:__ Dual Shot now costs 1 action point, up from 1/3 turns.
    * __Reasoning:__ In line with new action point ability costs.
  * __Dual Shot:__ ___Level 3, Spend 1 Action point to fire two arrows at once.___
    * __Change:__ Dual Shot now costs 1 action point, up from 1/3 turns.
    * __Reasoning:__ In line with new action point ability costs.
  * __Added Expert Fletcher:__ ___Level 13 Reduce all arrow costs by 2.___
    * __Reasoning:__ Allows better arrows to be used more freely at higher levels.
  * __Tuned Arrow Economy:__
    * __Change:__ With the introduction of expert fletcher, revisited arrow action point costs.

#### Gunslinger:
* __Abilities:__
  * __Changed Flash Grenades:__ ___Blind enemies who fail a Dex check.___
    * __Change:__ Now cost 1 action point, rather than 3/day.
    * __Reasoning:__ In line with action point economy.
  * __Added Marksman Ability Bull Rush:__ ___Level 1 Rush forward at least 10 feet to deal an extra dice of melee damage to an enemy (Bayonet Charge).___

#### Spellbooks:
  * __Balance Changes:__ Spell damage was balanced as part of the health/rest/monster/weapon damage re-balancing.

## Pre- Rangers and Ruffians 2.1.0
* This changelog was first established in Rangers and Ruffians 2.1.0. For details
  about prior releases, please review the Github commit history.
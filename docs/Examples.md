  
# The Book of Examples
_Version 2.1.0_  

   * [Additional Dice Information](#additional-dice-information)  
     * [Types of Dice Used](#types-of-dice-used)  
     * [When Are Checks Called?](#when-are-checks-called)  
     * [When Is Advantage or Disadvantage Granted?](#when-is-advantage-or-disadvantage-granted)  
   * [Diminishing Returns](#diminishing-returns)  
     * [Diminishing Returns Explained](#diminishing-returns-explained)  
     * [Why are Diminishing Returns Important?](#why-are-diminishing-returns-important)  
   * [Initiative](#initiative)  
     * [Initiative Example](#initiative-example)  
   * [Stat Computation Examples](#stat-computation-examples)  
     * [Method 1 (Easiest) Use Pre-generated Stats:](#method-1-easiest-use-pre-generated-stats)  
     * [Method 2 (Easy) Standard Array:](#method-2-easy-standard-array)  
     * [Method 3 (High Risk, High Reward) Roll:](#method-3-high-risk-high-reward-roll)  

  
## Additional Dice Information
  
  

  
### Types of Dice Used
There are a total of seven dice that are used in RnR, all of which can
be purchased online as a set or at your local hobby shop. These dice are
the ```d4```, ```d6```, ```d8```, ```d10```, ```d12```, ```d20```, and
the ```percentile``` die (a ```d10``` with two digits on each side).
We name dice with ```d``` and then the number of sides on the die.
Therefore, a ```d4``` has 4 sides, a ```d6``` is the 6 sided die with
which you are most familiar, a ```d8``` has 8 sides, and so on and so forth.
  
  
In some cases, it is necessary to roll a ```d100```. Since we
don't actually have a 100 sided die, we instead roll a ```percentile```
and a ```d10```. When we do this, the ```percentile``` represents the tens
place, and the ```d10``` the ones place. The minimum roll, then, is
a ```0``` (where we roll a ```0``` on both the ```d10``` and the ```percentile```)
and the maximum roll is a ```99``` (where we roll a ```90``` on the ```percentile```
and a ```9``` on the ```d10```).
If we rolled a ```60``` on the ```percentile```, and a ```4``` on the ```d10```,
we would say that we rolled a ```64```.
  
  

  
### When Are Checks Called?
It is left entirely to the Poohbah's discretion for which actions a check
should or should not be called for. For example, if a player is playing
a Rogue (a dexterous, sneaky character) and they say that they want to
climb a small wall, the Poohbah may not ask for a check, as it is reasonable
to say that the player could easily perform that action without failure.
If a player playing a heavily armored Hardfoot Halfling (a short, stocky race)
asked to climb the same wall, the Poohbah may call for a check. Similarly,
if the wall was slick with rain, even the Rogue may have to make a check
due to the increased difficulty of the task at hand.
  
  

  
### When Is Advantage or Disadvantage Granted?
For example, the
sneaky Rogue mentioned earlier earlier is good at hiding, so it has advantage.
This means that, when the rogue tries to hide, they get to roll a ```d20``` twice,
and keep the higher roll. So if the rogue rolled a ```10``` followed by a ```15```,
they would keep the ```15```. __Disadvantage__ is similar, but the player keeps the
_worse_ of the two rolls. So in the case above, if the rogue had disadvantage,
they would keep the ```10```. When you build your character, your advantages and
disadvantages will be explicitly listed out for you. However, your Poohbah
may sometimes call for a role with advantage or disadvantage even though
the rules of the game do not explicitly give you advantage or disadvantage
in that scenario. There is no concept of "double advantage" or "double disadvantage"
in Rangers and Ruffians. If you are performing a task and are gaining advantage
from multiple abilities, you still only role twice. If you have advantage and
disadvantage at the same time, they cancel out.
  
  

  
## Diminishing Returns
  
  

  
### Diminishing Returns Explained
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
  
  
  
  
  
  
  
  

  
### Why are Diminishing Returns Important?
__Diminishing Returns__ are very important to [Leveling Up](#leveling-up) in Rangers and Ruffians
in two ways:
  
  
  
  
1. __They provide a buffer against values getting to high.__ Because players can increase whatever
   stat they want when leveling up, a buffer is needed to avoid stat values getting out of hand.
2. __They encourage stat diversification upon level up.__ Diminishing returns incentivize players
   to spend stat points on stats that they wouldn't ordinarily take, promoting well rounded characters.
  
  

  
## Initiative
  
  

  
### Initiative Example
Let's say that we have 2 players and 1 enemy goblin. Each player and
the goblin roll initiative. Let's say the first player rolls a ```10``` and has
a perception of ```0```. Their initiative value for this combat is ```10```. The second
player rolls a ```14``` and has ```2``` perception, so their initiative is ```16```.
Finally, the goblin rolls a ```15``` but has a perception of ```-3```, so its initiative
is ```12```. So, in this combat, player 2 would go first (as ```16``` is highest),
then the goblin with ```12```, then player 1 with ```10``` initiative.
  
  
  
  

  
## Stat Computation Examples
  
  

  
### Method 1 (Easiest) Use Pre-generated Stats:
  
  
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
In rangers and Ruffians, every class has a standard array of stat values,
that is to say, each class has one stat with each of the following values,
not including its ```Health Dice``` and ```Luck```: ```2```, ```1```, ```0```, 
```-1```, ```-2```, and ```-3```. When creating a character we are allowed to 
swap these values for our class.
  
  
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
We are allowed to randomly generate our class stats when building our character.
  
  
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


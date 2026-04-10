######################################################################
# The following code is ai-generated, and is a result of me asking Grok
# to explain how the class keyword in Python works.
# This exists purely for educational purposes for me to understand how this works
# I don't vibecode i swear lol, i just want info about how this works
######################################################################
# Initial Prompt:
#
# I've been learning python recently. However there are only so many things I've learned so far,
# as I'm a novice. I know the words if, elif, else, while, for, isinstance, global, def, try,
# except, return, continue, break, range, del, strip, lower. The basic stuff like thatI know how
# to use booleans, strings, ints, floats, lists and arrays. I also know how turn a string into a
# list.I know enough to import the modules random and time, though not the full extent of everything
# they do.Basically, I know a couple of the important things, enough that I can make some basic
# scripts. But not anything too advanced. However, I'd like to learn what a class is in python
# and how to use them.
######################

# Classes in Python are one of the most powerful tools once you get the hang of them.
# They let you group data (like variables) and actions
# (like functions) together into a single "thing" — an object.
# Think of a class as a blueprint.
# You use the blueprint to build as many actual objects as you want.
#
# Simple Analogy
# Class = Recipe for a cake  
# Object (instance) = An actual cake you baked using that recipe
# You can bake many cakes from the same recipe, and each cake can be slightly different (different flavor, size, etc.).
#
# Why Would You Use a Class?
# Right now you probably store data in separate variables or lists, and write separate functions that work on that data.
# A class lets you bundle the data and the functions that belong to it together. It keeps your code cleaner and easier to reuse.

# Basic Structure of a Class
#############################################

class Dog:                    # This is the blueprint
    def __init__(self, name, age):   # Special method that runs when you create a new dog
        self.name = name         # Store the name inside this dog object
        self.age = age           # Store the age inside this dog object

    def bark(self):              # A method (a function that belongs to the dog)
        print(f"{self.name} says Woof!")

# How to Create and Use Objects (Instances)
###################################

# Create two different dogs from the same blueprint
my_dog = Dog("Buddy", 5)      # my_dog is now an object/instance
your_dog = Dog("Luna", 3)

print(my_dog.name)            # Output: Buddy
print(your_dog.age)           # Output: 3

my_dog.bark()                 # Output: Buddy says Woof!
your_dog.bark()               # Output: Luna says Woof!

#########################

# What is self?
# self is Python's way of saying "this particular object".
# When you write self.name = name, you're saying "store this name inside me (this specific dog)".
# You must put self as the first parameter in every method inside a class. Python automatically
# passes it for you when you call the method.
# 
# You Already Use Classes Without Realizing It!

#########################

my_list = [1, 2, 3]           # my_list is an instance of the 'list' class
my_list.append(4)             # .append() is a method that belongs to the list class
print(my_list.upper())        # Wait, strings have .upper() method too!

#################################################

# Lists, strings, integers — everything in Python is actually an object created from a class!
# 
# A More Useful Example You Can Build On
# Let’s make a simple Player class for a game (you already know random, so this will feel natural):

#########################

import random

class Player:
    def __init__(self, name, health=100):
        self.name = name
        self.health = health
        self.inventory = []          # Every player starts with an empty list

    def take_damage(self, amount):
        self.health -= amount
        print(f"{self.name} took {amount} damage! Health now: {self.health}")

    def heal(self):
        heal_amount = random.randint(10, 25)
        self.health += heal_amount
        print(f"{self.name} healed {heal_amount} health! Health now: {self.health}")

    def add_item(self, item):
        self.inventory.append(item)
        print(f"{self.name} picked up: {item}")

    def show_inventory(self):
        print(f"{self.name}'s inventory: {self.inventory}")
        

# Now you can use it like this:
####################################################################

hero = Player("Bloona", 120)      # Create your player
hero.take_damage(30)
hero.heal()
hero.add_item("Magic Sword")
hero.add_item("Health Potion")
hero.show_inventory()

enemy = Player("Goblin", 50)
enemy.take_damage(40)             # Different player, completely separate data

##############################################################
# Follow up #1
# What do you mean "extends" a class, I don't know what you mean by inheritance.
#####################################################################

# Inheritance is a way to make a new class that automatically gets everything from an existing class —
# without copying and pasting any code.
# 
# It’s like saying:
# “I already have a Player class that works great. Now I want a special kind of player called Warrior.
# The Warrior should do everything a normal Player can do… plus some extra warrior stuff.”
# 
# Simple Analogy
# Player = The basic “Human” blueprint (has arms, legs, can walk, can talk).  
# Warrior = A new blueprint that says “I’m still a Human, but I also have a sword and can swing it
# really hard.”
# 
# The Warrior inherits all the Human stuff and then adds its own special features.
# In Python we don’t usually say “extends” (that’s more of a Java word).
# We just put the parent class name in parentheses like this:

class Warrior(Player):     # Warrior inherits from Player
    ...
    
# Full Example Using the Player Class You Already Have
# I’m going to use the exact same Player class from my last message (so you can copy-paste everything
# together). Then I’ll show you the Warrior subclass.

import random

class Player:                          # ← Parent / Superclass
    def __init__(self, name, health=100):
        self.name = name
        self.health = health
        self.inventory = []

    def take_damage(self, amount):
        self.health -= amount
        print(f"{self.name} took {amount} damage! Health now: {self.health}")

    def heal(self):
        heal_amount = random.randint(10, 25)
        self.health += heal_amount
        print(f"{self.name} healed {heal_amount} health! Health now: {self.health}")

    def add_item(self, item):
        self.inventory.append(item)
        print(f"{self.name} picked up: {item}")

    def show_inventory(self):
        print(f"{self.name}'s inventory: {self.inventory}")
        
# Now the new child class:

class Warrior(Player):                 # ← Child / Subclass (inherits everything above)
    
    def __init__(self, name, health=100, strength=30):
        # First, let the Player class do its normal setup
        super().__init__(name, health)     # ← This calls Player's __init__
        
        # Now add the extra warrior-only stuff
        self.strength = strength           # New attribute only Warriors have

    # New method that only Warriors can do
    def powerful_attack(self, target):
        damage = random.randint(self.strength, self.strength + 20)
        print(f"{self.name} swings their sword for a POWERFUL attack!")
        target.take_damage(damage)         # We can still use the inherited take_damage

    # We can even change (override) a method from the parent if we want
    def heal(self):                        # This replaces Player's heal
        heal_amount = random.randint(15, 35)   # Warriors heal a bit better
        self.health += heal_amount
        print(f"{self.name} roars and heals {heal_amount} health! Health now: {self.health}")
        
# How to Use It

# Create a normal player and a warrior
hero = Player("Bloona", 120)
warrior = Warrior("Thorn", 150, strength=35)   # extra strength value

# Both can use the normal Player methods
hero.take_damage(20)
warrior.take_damage(20)          # ← inherited from Player

# Warrior has extra stuff
warrior.powerful_attack(hero)    # ← new method only Warrior has
warrior.heal()                   # ← uses the improved Warrior heal

print(f"{warrior.name} has {warrior.strength} strength")  # only Warrior has this

# What Actually Happens
# Warrior automatically gets: name, health, inventory, take_damage, add_item, show_inventory  
# It can add new things (strength, powerful_attack)  
# It can change things that already existed (heal is now better for warriors)  
# super().__init__(...) is how the child says “Hey parent, do your setup first, then I’ll add my own stuff.”
# 
# Why This Is Awesome for You
# You don’t have to rewrite all the player code again.
# If you later improve the Player class (maybe add a level_up method), every subclass
# (Warrior, Mage, Archer, etc.) automatically gets the improvement for free.
# 
# Quick Practice You Can Try Right Now
#    Copy the whole thing above into a new file and run it.
#    Add a second subclass called Mage that inherits from Player.Give it a mana attribute.
#    Add a method called cast_spell(self, target) that does random damage.
#    Create one Warrior and one Mage and have them fight each other.
# 
# Want me to write the Mage class for you as an example?
# Or should we go through it together line-by-line?
# Just say the word and we’ll keep building! 
########################################################################333
# Follow up #2
#
# You're using the word __init__, but I don't know that word if its a preexisting keyword,
# is that a custom keyword?Also, sure go ahead and make a mage if you think its demonstrative.
# Additionally, lets say this was a fantasy game where the race of the character also gives
# you some kind of attributes. Like lets say this was a game in which the sex, race, background,
# etc of the character has some kinds of statistical implications to represent as well.
# so I don't just want to go from player to fighter, I want to go from player to female
# player to female elf to female elf druid to female elf hermit with a hermit background.
# I'm not asking because I intend to make such a game I'm focused on the programming here.
# like would you essentially just make a series of classes that inherit off of the previous
# classes to make them work?
#
#######################################################################################
#
# __init__ is NOT a keyword — great question!
# Python’s keywords are the special reserved words you already know (like def, class, if, for,
# return, etc.). You can’t use those as variable names.
# 
# __init__ is completely different.
# It is a special method name (sometimes called a “dunder” method because of the double underscores: double underscore).
# Python has a small list of these special names that it automatically recognizes and calls for you at the right time.
# When you write:

hero = Warrior("Thorn")

# Python secretly does this for you:
#     1. Creates a blank Warrior object  
#     2. Immediately calls Warrior.__init__(self, "Thorn")
# 
# So __init__ is just the official name Python expects for “the method that sets up a new object.”
# It is not something you invented — every Python class uses it (or inherits it). You can think of it as the
# “constructor” or “setup” method.You already used it without realizing it when you created lists or strings
# — those classes have their own __init__ under the hood.

# Updated Full Example with Mage
# Here is the complete code so far (Player + Warrior from before + the new Mage class you asked for).
# Everything builds on what you already know.

import random

class Player:                          # Base class
    def __init__(self, name, health=100):
        self.name = name
        self.health = health
        self.inventory = []

    def take_damage(self, amount):
        self.health -= amount
        print(f"{self.name} took {amount} damage! Health now: {self.health}")

    def heal(self):
        heal_amount = random.randint(10, 25)
        self.health += heal_amount
        print(f"{self.name} healed {heal_amount} health! Health now: {self.health}")

    def add_item(self, item):
        self.inventory.append(item)
        print(f"{self.name} picked up: {item}")

    def show_inventory(self):
        print(f"{self.name}'s inventory: {self.inventory}")


class Warrior(Player):                 # Inherits from Player
    def __init__(self, name, health=100, strength=30):
        super().__init__(name, health)     # Let Player do the basic setup
        self.strength = strength

    def powerful_attack(self, target):
        damage = random.randint(self.strength, self.strength + 20)
        print(f"{self.name} swings their sword for a POWERFUL attack!")
        target.take_damage(damage)

    def heal(self):                        # Overrides Player's heal
        heal_amount = random.randint(15, 35)
        self.health += heal_amount
        print(f"{self.name} roars and heals {heal_amount} health! Health now: {self.health}")


class Mage(Player):                    # Also inherits directly from Player
    def __init__(self, name, health=80, mana=100):
        super().__init__(name, health)     # Player's setup
        self.mana = mana                   # Mage-only attribute

    def cast_spell(self, target):
        if self.mana >= 20:
            damage = random.randint(25, 40)
            self.mana -= 20
            print(f"{self.name} casts a fireball!")
            target.take_damage(damage)
        else:
            print(f"{self.name} is out of mana!")

    def heal(self):                        # Mages heal with magic
        heal_amount = random.randint(20, 30)
        self.health += heal_amount
        self.mana -= 10
        print(f"{self.name} channels magic to heal {heal_amount} health! Health now: {self.health}")
        
# You can now do:

bloona = Mage("Bloona", health=90, mana=120)
thorn  = Warrior("Thorn")

bloona.cast_spell(thorn)
thorn.powerful_attack(bloona)

# Your Main Question: Multi-level inheritance
# (Player → Female Player → Female Elf → Female Elf Druid → Female Elf Hermit)
# 
# Yes — exactly.
# You can create a chain of classes where each one inherits from the one before it.
# Each new class gets everything from its parent, then adds or changes whatever it wants.
# 
# Here’s how it looks for your fantasy example (I kept it short and clean so you can see the pattern easily):

# ─────────────────────────────────────────────────────────────
# 1. Base class (same as before)
class Player:
    def __init__(self, name, health=100):
        self.name = name
        self.health = health
        self.inventory = []
        self.sex = "unknown"      # default
        self.race = "human"       # default
        self.background = "none"  # default

    def take_damage(self, amount):
        self.health -= amount
        print(f"{self.name} took {amount} damage! Health now: {self.health}")

    # (heal, add_item, show_inventory stay the same - omitted here for space)

# ─────────────────────────────────────────────────────────────
# 2. Female Player (adds sex-specific bonus)
class FemalePlayer(Player):
    def __init__(self, name, health=100):
        super().__init__(name, health)      # Let Player set up first
        self.sex = "female"
        self.health += 5                    # example: females start with +5 health

# ─────────────────────────────────────────────────────────────
# 3. Female Elf (adds race bonus)
class FemaleElf(FemalePlayer):
    def __init__(self, name, health=100):
        super().__init__(name, health)      # FemalePlayer does its setup
        self.race = "elf"
        self.agility = 15                   # elf bonus attribute

    def quick_dodge(self):
        print(f"{self.name} gracefully dodges using elven agility!")

# ─────────────────────────────────────────────────────────────
# 4. Female Elf Druid (adds class abilities)
class FemaleElfDruid(FemaleElf):
    def __init__(self, name, health=100):
        super().__init__(name, health)
        self.background = "druid"           # or you could set this later

    def nature_heal(self):
        heal_amount = random.randint(25, 40)
        self.health += heal_amount
        print(f"{self.name} calls on nature spirits to heal {heal_amount} health!")

# ─────────────────────────────────────────────────────────────
# 5. Female Elf Hermit Druid (adds background bonus)
class FemaleElfHermit(FemaleElfDruid):
    def __init__(self, name, health=100):
        super().__init__(name, health)
        self.background = "hermit"
        self.health += 10                   # hermit survival bonus

    def meditate(self):
        print(f"{self.name} meditates in solitude and regains strength.")

# Every level automatically calls super().__init__() so the setup bubbles up from the very top (Player).
# 
# Quick Tips for This Style
# This is called inheritance chaining (or a class hierarchy).  
# It works great for learning and for simple games.  
# If you had 20 races and 10 classes and 5 backgrounds, you would end up with hundreds of classes — that gets messy.
# In real games, most programmers switch to composition (e.g. one Character class that has a Race object, has a Background object, etc.).
# But that’s an intermediate topic — we can cover it later when you’re ready.
# 
# Would you like me to:
#     Add the missing methods (heal, add_item, etc.) back into the chain so you can copy-paste a full working file?
# Show you how to add random stat bonuses based on race/sex/background inside __init__?
# Or give you a tiny exercise where you create one more subclass (e.g. a Male Dwarf Warrior)?
# 
# Just tell me what you want to try next — we’re going exactly at your pace!
########################################################################333
# Follow up #2
#
# 
# Okay but you used more words I don't know. I gave you a list of all the python keywords I knew at the beginning
# of this conversation. What is this super() function you called?
# Additionally, if this WERE a character in a game,
# from this class once you create these "class objects". This character would obviously need to have its specific
# values updated dynamically, for example, they could lose health, they could level up, they could have a pair of
# magic gauntlets that give them 2 more 'strength'. At the end of this chain of classes. Does this store a unique
# 'character' instance of that class at the end?Also, one thing I do not know in python yet is how to have it read
# and write data to a file. Whenever I start a script currently, they must start from SCRATCH. This obviously limits
# the kinds of programs I'm capable of writing. I'm sure there must be keywords for reading/writing from a file right?
###################################################
# super() is NOT a Python keyword — it's a built-in function (just like print(), len(), or random.randint() that you already use).
# 
# You can use it anywhere inside a class method. Its only job is:
# “Call the same method from my parent class.”
# 
# That’s why we use it in __init__:

class FemaleElf(FemalePlayer):
    def __init__(self, name, health=100):
        super().__init__(name, health)   # ← This says: “Hey FemalePlayer, run your __init__ first”
        self.race = "elf"
        self.agility = 15

# 
# Without super(), the parent classes (Player → FemalePlayer) would never set up name, health, inventory, etc.
# 
# Python does not automatically call the parent’s __init__ for you — you have to ask it with super().
# Think of it like this:
# You’re building a sandwich. super() tells the parent recipe “make the bread and meat first”, then you
# add your own toppings.
# 
# You’ll see super() a lot when you do inheritance. It’s one of the most common things you learn right after classes.
# 
# Yes — each character you create is a unique instance
# When you do this at the end of the chain:

my_hero = FemaleElfHermit("Lirael", health=110)

# my_hero is now a completely separate object that lives in your computer’s memory.
# It contains all the attributes from every class in the chain:my_hero.name
# my_hero.health
# my_hero.sex
# my_hero.race
# my_hero.background
# my_hero.agility
# my_hero.inventory (the list you already know how to use)
# 
# And because it’s just a normal object, you can change any value whenever you want (exactly like you already change variables):

my_hero.health -= 25                    # lost health in battle
my_hero.health += 40                    # leveled up or used a potion
my_hero.inventory.append("Magic Gauntlets")   # found new item

# You can even add brand-new attributes on the fly if you want:
my_hero.strength = 35                   # magic gauntlets gave +2 strength

# All of these changes stay on that specific my_hero object.
# If you create a second character:

friend = FemaleElfHermit("Elara")

# friend has its own separate health, inventory, etc. They don’t affect each other at all.
# So yes — at the end of the inheritance chain you get one unique “character instance” that you
# can keep modifying forever (until the script ends).

# Reading and Writing Data to Files (so your character doesn’t reset every time)
# 
# You’re right — right now every script starts fresh.
# Python has built-in tools for this. The main keyword/function you need is open().
# 
# Here’s the absolute simplest way (using only things you already know + one new pattern):

# === SAVING data to a file ===
with open("character_save.txt", "w") as file:   # "w" = write (creates/overwrites the file)
    file.write("Lirael\n")                      # write one line at a time
    file.write("120\n")                         # health
    file.write("female\n")
    file.write("elf\n")
    # ... you could write the whole inventory as a string too
    
# === LOADING data from a file ===
with open("character_save.txt", "r") as file:   # "r" = read
    lines = file.readlines()                    # reads every line into a list

name = lines[0].strip()                         # you already know .strip()
health = int(lines[1].strip())                  # turn string back into number
sex = lines[2].strip()

# The with open(...) as file: line is the modern, safe way.
# It automatically closes the file when you’re done (you don’t have to remember to close it).
# 
# But saving a whole character object is a bit annoying with plain text.
# There’s a much better way using a module you can import (just like you already import random and time).
# 
# The easy way: Use the json module (built-in, no extra install)
# Add this at the top of your script:

import json          # ← new import, exactly like random

# Then give your final class two simple methods:

class FemaleElfHermit(FemaleElfDruid):
    # ... all your other code ...

    def save(self, filename="character_save.json"):
        data = {
            "name": self.name,
            "health": self.health,
            "sex": self.sex,
            "race": self.race,
            "background": self.background,
            "agility": self.agility,
            "inventory": self.inventory          # lists save perfectly
            # add any other stats you want
        }
        with open(filename, "w") as file:
            json.dump(data, file)                # writes the whole thing in one line
        print(f"Saved {self.name} to {filename}!")

    def load(self, filename="character_save.json"):
        with open(filename, "r") as file:
            data = json.load(file)               # reads it back
        self.name = data["name"]
        self.health = data["health"]
        self.sex = data["sex"]
        # ... copy every other attribute the same way
        self.inventory = data["inventory"]
        print(f"Loaded {self.name} from save file!")
        
# Now your game can do this:

hero = FemaleElfHermit("Lirael")
# play the game, fight, level up, get items...
hero.health -= 30
hero.inventory.append("Magic Gauntlets")

hero.save()                     # saves everything to a file

# --- later, when you run the script again ---
hero = FemaleElfHermit("Temp")  # temporary placeholder
hero.load()                     # now hero is exactly how you left it!
print(hero.inventory)           # shows the gauntlets you picked up last time

# This is how almost every simple game saves progress.
# 
# 1. Would you like me to:Give you the complete, copy-paste-ready file that includes the whole class chain + the save()
# and load() methods?
# 2. Or walk through turning your current character into a save/load version step-by-step?
# 
# Just say which one (or anything else that’s still confusing) and we’ll do it next. You’re picking this up really fast!
#################################################
# Follow up #3
# 
# I'm not actually picking this up really fast I'm just having you elaborate so I can read this later on.
# It's more efficient to ask follow up questions, study them afterwards and then ask follow up questions.
# You mentioned earlier that inheritance chaining is not actually efficient for games with large numbers of characters,
# and that most programmers switch to something called composition. Where a character contains a race, background,
# class object, etc. So lets explore that a little more.To be clear, I'm NOT actually making a game, at least not
# right now. I'm learning programming. This is simply the mechanism by which I'm explaining what I'm asking because
# you used it first. But if I were, I'd imagine you'd need more efficient ways to do this. A player character would
# obviously be a complex object (im not sure if thats the right word in this context) for sure. But a game would also
# need to have like npcs. Like if I entered a dungeon and there were multiple undead guarding an imprisoned damsel. 
# These skeletons themselves would have their own characteristics to keep track of. They themselves could
# be male or female, have had different classes in life, be elves, dwarves half-orcs, wielding different weapons,
# etc. this could quickly increase the amount of potential class objects this hypothetical game would require, so
# I imagine when you're using this tool frequently efficiency becomes important fast. Both on a computer processing
# and tedium for the human programmer levels.
##########################################
# Composition is exactly the more efficient way most real games (and most Python programs) handle complex characters like players,
# NPCs, skeletons, etc.
# 
# You already understand the problem with deep inheritance:
# If you have 5 races × 2 sexes × 10 backgrounds × 8 classes = hundreds of classes.
# Every new combination needs its own class. That’s a nightmare to write and maintain.
# 
# Composition fixes this by flipping the idea:
# Instead of “a FemaleElfHermitDruid is a special kind of Player”, we say:
# “A Character has a race, has a sex, has a background, has a job/class, has weapons, etc.”
# 
# It’s like building with Lego blocks. You have one main Character class, and you plug
# in different small pieces (Race object, Background object, etc.).
# You only ever need a handful of tiny classes instead of hundreds of big ones.
# 
# Simple Analogy
# Inheritance = “I am a super-special sandwich with 10 layers of bread and toppings baked together.”  
# Composition = “I have a plate, and I can put any bread + any toppings on it whenever I want.”
# 
# How Composition Looks in Code
# We’ll create a few small, reusable classes first (these are like your Lego blocks).
# Then one main Character class that holds them.

import random
import json   # for saving/loading later if you want

# ─── Small reusable pieces (these never change much) ───
class Race:
    def __init__(self, name, health_bonus=0, agility_bonus=0):
        self.name = name
        self.health_bonus = health_bonus
        self.agility_bonus = agility_bonus

class Background:
    def __init__(self, name, bonus_stat="none", bonus_value=0):
        self.name = name
        self.bonus_stat = bonus_stat   # e.g. "strength" or "mana"
        self.bonus_value = bonus_value

class Job:                         # "class" is a Python keyword, so we use Job
    def __init__(self, name):
        self.name = name

# ─── The main Character class (only ONE class for players AND NPCs) ───
class Character:
    def __init__(self, name, race, background, job, sex="unknown", health=100):
        self.name = name
        self.sex = sex
        self.race = race                  # ← this is a Race object
        self.background = background      # ← this is a Background object
        self.job = job                    # ← this is a Job object
        
        # Apply bonuses from race and background
        self.health = health + race.health_bonus + background.bonus_value
        self.agility = 10 + race.agility_bonus
        self.inventory = []
        self.strength = 20                # default, can be changed later

    def take_damage(self, amount):
        self.health -= amount
        print(f"{self.name} took {amount} damage! Health now: {self.health}")

    def add_item(self, item):
        self.inventory.append(item)
        print(f"{self.name} picked up: {item}")

    def show_status(self):
        print(f"\n=== {self.name} ===")
        print(f"Sex: {self.sex} | Race: {self.race.name} | Background: {self.background.name}")
        print(f"Job: {self.job.name} | Health: {self.health} | Agility: {self.agility}")
        print(f"Inventory: {self.inventory}")

    # Easy to add more methods later: heal, attack, level_up, etc.

# Creating Characters (Player or NPC — same code!)

# Pre-make the Lego blocks once
elf_race      = Race("elf", health_bonus=5, agility_bonus=15)
hermit_bg     = Background("hermit", bonus_stat="health", bonus_value=10)
druid_job     = Job("druid")
warrior_job   = Job("warrior")

# Create your player exactly how you described
player = Character(
    name="Lirael",
    race=elf_race,
    background=hermit_bg,
    job=druid_job,
    sex="female",
    health=100
)

# Create an NPC skeleton (totally different stats, same Character class!)
skeleton_race = Race("undead", health_bonus=-10, agility_bonus=5)
former_knight = Background("fallen knight", bonus_stat="strength", bonus_value=15)
undead_job    = Job("skeleton guard")

skeleton1 = Character(
    name="Bonecrusher",
    race=skeleton_race,
    background=former_knight,
    job=undead_job,
    sex="male",
    health=60
)

# Create the imprisoned damsel
damsel = Character(
    name="Princess Elara",
    race=Race("human"),
    background=Background("noble"),
    job=Job("none"),
    sex="female",
    health=30
)

# Now watch them all work the same way
player.show_status()
skeleton1.show_status()
damsel.show_status()

# Dynamic changes still work exactly like before
player.health += 25                  # level up or potion
player.add_item("Magic Gauntlets")
player.strength += 2                 # gauntlets give bonus

skeleton1.take_damage(35)            # player attacks the skeleton

# Why This Is Way Better for a Game (or Any Program)
# 
# 1. Only 4 classes total (Race, Background, Job, Character) no matter how many combinations you have.
# 2. Want a female dwarf barbarian? Just make new Race/Background/Job objects and pass them in.
# No new class needed.
# 3. Want 50 different skeletons? Same Character class, different pieces plugged in.
# 4. Easy to add new things later: Weapon class, Spell class, Faction class — just plug them into Character.
# 5. Much less typing and debugging for you (the programmer).
# 6. Computer runs it faster because there’s no giant chain of super() calls.
# 
# This “has-a” style (composition) is what almost every modern game uses for characters, items, enemies, etc.
# 
# You can still mix a little inheritance if you want (e.g. make Player(Character) if you want player-only methods),
# but most of the time pure composition is cleaner.
# 
# Would you like me to:
# 1. Give you the full copy-paste script with the save/load methods updated for composition?
# 2. Show how to add a simple level_up() or attack() method that uses the bonuses?
# 3. Or turn this into a tiny interactive loop where you can fight the skeleton a few times?
# 
# Just tell me which direction feels useful for your studying and we’ll keep going.
# You’re asking exactly the right questions — this is how real programmers think about design. 
###################################
# Follow Up #4
#
# 
Lets use an example from a custom roleplaying game, my old friend Caramel made a ttrpg called "TropicOS".
# He had me participate in a 'combat test' for this game. Now, Caramel's roleplaying game has a few unusual features.

# He did not use a class system, the max level was 30, and characters could actually get jobs instead of classes.
# Every level in a job would immediately bestow some kind of active or passive benefit for the player character.
# Jobs could only have 3 levels before there were no more to get. For your first level there was a list of 7 starter
# jobs, and your first level must be one of those. After that you could choose from the wider list. However some
# jobs would require others. For example, to get Knight 1, you must have had at least Squire 1 beforehand, to get
# Cleric 1 you had to be Devotee 1 beforehand, to get Paladin you must fulfill any 2 of 4 requirements
# (having 1 level in Knight, Cleric or Magician, or having a PIETY stat of at least 40.) You could also get
# "job medallions", which, while worn, could give you the ability of the corresponding job.

# Obviously, this is a system that not only encourages, but requires multiclassing and building for synergies.

# He also had a mutations system. Upon character creation, depending on your race, you would get a certain number
# of "mutation points". These could either be converted to stat points or used to buy racial advantages of a race
# that you are NOT. You could also give up your own racial advantages or take racial disadvantages to buy more.
# 
# My character was a level 3 human who went by the alias "Queenfisher". She had Squire 1, Acrobat 1 and
# Apprentice 1. She had the "human" (which are slightly different in this setting traits of:
# "Adaptive Blood", "Primal Grip", "Walker", "Prehensile Tail", "Omnivore".
# She also had a lot of mutations, she gave up a human bonus to Piety from a trait called "Born of Chaos",
# along with taking the downsides "Hollow Bones" and "Voracious Appetite".
# However, she had "Back Wings", "Hydrophobic Feathers", "Hunter Eyes", "Slick", "Natural Swimmer" and
# "Gills".What she was designed to be was the best mobility character I could've made at
# the time. Because this was a playtest and I wanted to see if a character that went all in on movement would
# cause any gameplay problems. The idea was that she was a slippery and inescapable huntress that could follow
# you anywhere. A rushdown character that could always be wherever on the board they wanted to be, and also a bit
# of a spellblade. Her name was wordplay, a chess queen is the strongest piece because it has the most freedom of
# movement on the board, and a kingfisher is a bird that dives underwater to catch fish.She had some pretty severe
# weaknesses though. Hollow bones made her more vulnerable to crushing attacks, her gills actually made her more
# vulnerable to gas attacks, while she was versatile, she wasn't high enough level to have the bridge piece jobs
# to really make her split focus start to synergize with itself. She was uncharismatic because her greatest strength
# is freedom of movement, and having to rely on allies shackled her to others that can't go where she can, but most
# damningly, her advantages are worthless inside a building or underground. Which actually made her a significantly
# WEAKER then average character in some of the most common dungeon crawling environments.
#
# Now, this game by its verystructure relies on these racial and job characteristics not being that restrictive. Obviously,
# Queenfisher pickedmutations giving her the traits of birdlike and fishlike races that exist in this setting, and the
# job system means you have to pick more then one job, obviously.  One new job or rank in a job you already have per
# level up. So how would we solve these problems from a technical perspective? Your established method of doing this
# relies on the ideawe only need to decide the characters class or race once, but multiclassing and mutations
# challenge this perspective.
##########################################################3
# 
# Composition still works perfectly here — we just make it more flexible to handle the exact complexity you described from TropicOS.
# 
# The key insight is:
# Instead of giving Character one job and one set of racial traits, we give it:
#     1. A dictionary of jobs → their current level (supports multiclassing + leveling each job up to 3)
#     2. A list/set of traits (your mutations, including advantages from other races + disadvantages you took)
# 
# Everything else (stats, bonuses, prerequisites, synergies) is calculated dynamically whenever you need it.
# 
# No giant inheritance chains. No hundreds of classes. Just one Character class + a few small helper classes/data structures.
# 
# This is exactly how real game engines and TTRPG digital tools handle multiclassing and mutation systems.
# 
# Updated Code Design (copy-paste ready)

import json  # if you want save/load later

# ─── Small helper classes (your "Lego blocks") ───
class Race:
    def __init__(self, name, base_traits=None):
        self.name = name
        self.base_traits = base_traits or []   # e.g. ["Adaptive Blood", "Primal Grip"]

class Trait:
    def __init__(self, name, is_advantage=True, stat_bonuses=None):
        self.name = name
        self.is_advantage = is_advantage
        self.stat_bonuses = stat_bonuses or {}   # e.g. {"agility": 5, "piety": -10}

class Job:
    """Just holds the name. All benefits and prerequisites live in data below."""
    def __init__(self, name):
        self.name = name

# ─── Data for the whole game (easy to expand) ───
# These could later come from a JSON file if you want
JOB_PREREQUISITES = {
    "Knight":       [("Squire", 1)],           # must have Squire at least level 1
    "Cleric":       [("Devotee", 1)],
    "Paladin":      [("Knight", 1), ("Cleric", 1), ("Magician", 1), "piety>=40"],
    # add more as needed
}

JOB_BENEFITS = {
    "Squire": {
        1: {"passive": "mobility +5", "stat": {"agility": 5}},
        2: {"passive": "armor training", "stat": {"strength": 3}},
        3: {"passive": "mounted charge"}
    },
    "Acrobat": {
        1: {"passive": "dodge +10", "stat": {"agility": 8}},
        # etc.
    },
    "Apprentice": {
        1: {"active": "basic spellblade attack", "stat": {"magic": 4}}
    },
    # ... add every job in the game here
}

# ─── The main Character class (handles everything) ───
class Character:
    def __init__(self, name, base_race):
        self.name = name
        self.base_race = base_race
        
        self.job_levels = {}          # e.g. {"Squire": 1, "Acrobat": 1, "Apprentice": 1}
        self.traits = []              # list of Trait objects (mutations + base race traits)
        self.stats = {                # base stats — everything else is added on top
            "health": 100,
            "agility": 10,
            "strength": 20,
            "piety": 20,
            "magic": 15,
            # add any other stats TropicOS uses
        }
        
        # Add base race traits automatically
        for trait_name in base_race.base_traits:
            self.traits.append(Trait(trait_name))

    # ─── Adding jobs with prerequisite checks ───
    def can_add_job(self, job_name, target_level=1):
        if job_name in self.job_levels and self.job_levels[job_name] >= 3:
            return False, "Job already at max level 3"
        
        prereqs = JOB_PREREQUISITES.get(job_name, [])
        for req in prereqs:
            if isinstance(req, tuple):          # e.g. ("Squire", 1)
                req_job, req_lvl = req
                if self.job_levels.get(req_job, 0) < req_lvl:
                    return False, f"Requires {req_job} level {req_lvl}"
            elif req == "piety>=40" and self.get_current_stats()["piety"] < 40:
                return False, "Requires Piety 40+"
        return True, "OK"

    def add_job(self, job_name, level=1):
        can, reason = self.can_add_job(job_name, level)
        if not can:
            print(f"Cannot add {job_name} level {level}: {reason}")
            return False
        
        self.job_levels[job_name] = level
        print(f"{self.name} gained {job_name} level {level}!")
        return True

    # ─── Adding mutations / racial traits ───
    def add_trait(self, trait):
        self.traits.append(trait)
        print(f"{self.name} gained trait: {trait.name}")

    # ─── Calculate final stats on the fly (this is the magic) ───
    def get_current_stats(self):
        final = self.stats.copy()
        
        # 1. Add bonuses from all jobs
        for job_name, lvl in self.job_levels.items():
            benefits = JOB_BENEFITS.get(job_name, {}).get(lvl, {})
            stat_bonus = benefits.get("stat", {})
            for stat, value in stat_bonus.items():
                final[stat] += value
        
        # 2. Add bonuses from all traits (mutations)
        for trait in self.traits:
            for stat, value in trait.stat_bonuses.items():
                final[stat] += value
        
        return final

    def show_sheet(self):
        stats = self.get_current_stats()
        print(f"\n=== {self.name} ===")
        print(f"Race: {self.base_race.name}")
        print(f"Jobs: {self.job_levels}")
        print(f"Traits/Mutations: {[t.name for t in self.traits]}")
        print("Stats:")
        for stat, value in stats.items():
            print(f"  {stat.capitalize()}: {value}")

# Creating Queenfisher Exactly as You Described

# Create the base race and character
human_race = Race("human", base_traits=["Adaptive Blood", "Primal Grip", "Walker", "Prehensile Tail", "Omnivore"])
queenfisher = Character("Queenfisher", human_race)

# Add her jobs (multiclassing with prerequisites — the check would pass here)
queenfisher.add_job("Squire", 1)
queenfisher.add_job("Acrobat", 1)
queenfisher.add_job("Apprentice", 1)

# Add all her mutations (advantages + disadvantages)
queenfisher.add_trait(Trait("Back Wings", stat_bonuses={"agility": 12}))
queenfisher.add_trait(Trait("Hydrophobic Feathers"))
queenfisher.add_trait(Trait("Hunter Eyes", stat_bonuses={"agility": 8}))
queenfisher.add_trait(Trait("Slick", stat_bonuses={"agility": 5}))
queenfisher.add_trait(Trait("Natural Swimmer"))
queenfisher.add_trait(Trait("Gills"))
# Disadvantages she took
queenfisher.add_trait(Trait("Hollow Bones", is_advantage=False, stat_bonuses={"health": -15}))
queenfisher.add_trait(Trait("Voracious Appetite", is_advantage=False))
# She gave up the "Born of Chaos" piety bonus by simply not adding it

# See the full character
queenfisher.show_sheet()

# This prints her exact build with all synergies already applied.
# 
# Why This Solves the Problems You Mentioned
# 
# Multiclassing / jobs → job_levels dictionary lets her have as many jobs as she wants, each at its own level.
# Prerequisites are checked automatically.
# 
# Mutations / racial mixing → traits list can hold any combination of advantages, disadvantages,
# and borrowed racial traits. You can even add a “mutation points” system later by giving Character
# a mutation_points counter and a method to spend them.
# 
# Synergies & dynamic stats → get_current_stats() recalculates everything fresh every time. If she levels
# up a job or gains a new trait, the bonuses appear instantly.
# 
# Leveling up → You could add a method level_up(self, job_name) that does self.job_levels[job_name] += 1
# and checks the new benefits.
# 
# Efficiency → Only one Character class no matter how many weird combinations players make. Adding a new job
# or trait is just adding one line to the data dictionaries — no new classes needed.
# 
# NPCs / monsters → Same class! A skeleton guard would just have different race + different job_levels + different traits.
# 
# This is the professional way to build exactly the kind of flexible, synergy-heavy system TropicOS uses.
# 
#     1. Want me to:Add the level_up() method with the “one new job or rank per level” rule?
#     2. Show how to turn the JOB_BENEFITS and JOB_PREREQUISITES into a saveable JSON file?
#     3. Or make a tiny combat test loop where Queenfisher fights a skeleton using her mobility bonuses?
# 
# Just say the word — we’ll keep building exactly what helps you understand it best. You’re thinking like a real systems designer now. 
##############################################################################
# Follow Up #5
#
# 
Well obviously I can't just AI generate the code to make game code for me for someone else's game.
# He's my friend and that wouldn't make me any better at programming. It was an example. I can however
# do whatever I want with Queenfisher, since she's my character. Which is why she was the example and
# not the games rulebook. Remember this is a conversation about teaching ME to program here.
# 
# In terms of how this actually works though, I find your proposed solution strange for the reason that.
# If I picked that I WAS a human, I should already have any traits a human have. I shouldn't have to
# select for them. Choosing mutations afterwards would be choosing traits I don't have / converting them
# to stats / giving up my existing traits. So there would have to be a way this program KNEW what traits
# a human specifically had already, you can't just rely on the player selecting all the human traits.
# They might not even know what they are, one of them was a tail.
################################################################################3
# You're absolutely right — that's a sharp observation, and exactly the kind of thinking that makes someone
# a better programmer.
# 
# The code I showed you technically worked, but it had a bad design smell: it forced the person using the
# program (the player) to remember and type every human trait every single time they made a character.
# That’s not realistic, and it’s not how real game tools work.
# 
# The fix: Make the program know the defaults
# We store the “what does each race get by default?” information once, in a big dictionary at the top
# of the file (just like we did with JOB_BENEFITS).
# 
# Then when you create a character you only say “this is a human” — the code automatically gives her
# every human trait without the player having to list them.
# 
# Mutations then become changes on top of that default list:
#     1. Add new traits (from other races)
#     2. Remove or replace some of her own racial traits
# 3. Convert unused mutation points into raw stat points, etc.
# 
# Here’s the cleaned-up version that does exactly that:

# ─── Data that the program "knows" forever ───
RACES = {
    "human": {
        "base_traits": [
            "Adaptive Blood",
            "Primal Grip",
            "Walker",
            "Prehensile Tail",
            "Omnivore",
            "Born of Chaos"          # the piety bonus she later gave up
        ],
        "mutation_points": 8         # example starting points for humans
    },
    # You can add "elf", "dwarf", "undead", etc. later — just one entry each
}

# (Trait and Job classes stay exactly the same as last time — no need to repeat them)

# ─── The Character class, now smarter about defaults ───
class Character:
    def __init__(self, name, race_name="human"):
        self.name = name
        self.race_name = race_name
        
        # Look up the default traits and points automatically
        race_data = RACES.get(race_name.lower(), RACES["human"])
        self.base_traits = race_data["base_traits"].copy()   # copy so we can modify later
        self.mutation_points = race_data["mutation_points"]
        
        self.job_levels = {}
        self.traits = []                     # will hold Trait objects
        self.stats = {"health": 100, "agility": 10, "strength": 20, "piety": 20, "magic": 15}
        
        # Automatically give every default racial trait
        for trait_name in self.base_traits:
            self.traits.append(Trait(trait_name))
        
        print(f"{self.name} created as a {self.race_name}. Default traits loaded automatically.")

    # ─── Mutation / trait editing (this is what the player actually chooses) ───
    def spend_mutation(self, trait_name, is_advantage=True, stat_bonuses=None):
        """Add a brand-new trait using mutation points"""
        if self.mutation_points <= 0:
            print("No mutation points left!")
            return False
        self.mutation_points -= 1
        new_trait = Trait(trait_name, is_advantage=is_advantage, stat_bonuses=stat_bonuses or {})
        self.traits.append(new_trait)
        print(f"{self.name} gained mutation: {trait_name}")
        return True

    def remove_trait(self, trait_name):
        """Give up one of your own racial traits to gain a mutation point back"""
        for i, trait in enumerate(self.traits):
            if trait.name == trait_name:
                del self.traits[i]
                self.mutation_points += 1
                print(f"{self.name} gave up the trait '{trait_name}' (+1 mutation point)")
                return True
        print(f"Trait '{trait_name}' not found")
        return False

    # (get_current_stats and show_sheet stay exactly the same as before)
    def get_current_stats(self):
        final = self.stats.copy()
        for job_name, lvl in self.job_levels.items():
            benefits = JOB_BENEFITS.get(job_name, {}).get(lvl, {})
            for stat, value in benefits.get("stat", {}).items():
                final[stat] += value
        for trait in self.traits:
            for stat, value in trait.stat_bonuses.items():
                final[stat] += value
        return final

    def show_sheet(self):
        stats = self.get_current_stats()
        print(f"\n=== {self.name} ===")
        print(f"Race: {self.race_name} | Mutation points left: {self.mutation_points}")
        print(f"Jobs: {self.job_levels}")
        print(f"Current traits: {[t.name for t in self.traits]}")
        print("Stats:")
        for stat, value in stats.items():
            print(f"  {stat.capitalize()}: {value}")

# Creating Queenfisher — exactly as you described

queenfisher = Character("Queenfisher", race_name="human")

# Add her three jobs (same as before)
queenfisher.add_job("Squire", 1)
queenfisher.add_job("Acrobat", 1)
queenfisher.add_job("Apprentice", 1)

# Now the mutations she actually chose:
queenfisher.spend_mutation("Back Wings", stat_bonuses={"agility": 12})
queenfisher.spend_mutation("Hydrophobic Feathers")
queenfisher.spend_mutation("Hunter Eyes", stat_bonuses={"agility": 8})
queenfisher.spend_mutation("Slick", stat_bonuses={"agility": 5})
queenfisher.spend_mutation("Natural Swimmer")
queenfisher.spend_mutation("Gills")

# She gave up two of her own human traits for more points:
queenfisher.remove_trait("Born of Chaos")      # gave up the piety bonus
queenfisher.remove_trait("Prehensile Tail")    # (example — you said she had it, but you can remove any)

queenfisher.show_sheet()

# Now the player never has to type the human traits themselves.
# The program already knows what a human gets, and only the mutations are the player’s choices.
# 
# This is called data-driven design — all the game rules live in the big dictionaries at the top (RACES, JOB_BENEFITS, etc.).
# If your friend later adds a new race, you just add one more entry to RACES. You don’t touch the Character class at all.
# 
# That’s the professional pattern.
# 
# Would you like me to:
#     1. Add the missing add_job, JOB_BENEFITS, and JOB_PREREQUISITES pieces so you have a complete working file?
#     2. Show how to turn mutation points into raw stat points instead of buying traits?
#     3. Or add a simple level_up(job_name) method that follows the “one new job or rank per level” rule?
# 
# Just tell me which part you want to study next and we’ll keep going at whatever speed helps you most. You’re asking the exact right questions.
##############################
# Follow Up #6
# 
# There's an additional part of the process I didn't specify.Humans get a choice to be either Herbivores, Omnivores or Carnivores
# they also get a choice to be
# In God's Image or Born of Chaos
# You can also only give up ONE of your own racial traits for mutation points.
# This mutation CANNOT be adaptive blood (since adaptive bloods effect IS it gives you a mutation point)
# it also cannot be Herbivore, Omnivore or Carnivore (since your character obviously has to eat SOMETHING.)
# this would require a character to make a choice about what their human is before they even mutate at all.
# Additionally, while the diet traits can't be removed, In God's Image or Born of Chaos CAN be, and Queenfisher did.
# As stated before I don't actually want you to AI generate my friends game for me. But the technical details of the
# game aren't fully captured by the process your describing either, and I want to know how you'd account for these
# choices that require a decision before imposing the preset traits for the race, before applying the mutation choices.
# Mostly just to understand the logic process of the code, not because I want you to make this game for me.
##########################################
# Got it — this is exactly the kind of detail that turns “it mostly works” into “it actually follows the rules.”
# You’re learning the real programming skill here: how to turn a set of rules into code logic that enforces them automatically.
# The new requirements mean we have to change the order of operations inside __init__:
#     Player tells us their choices (diet and origin) first.
#     The code builds the full default list of human traits based on those choices.
#     Only after that does mutation logic run.
#     Certain traits are marked “protected” (cannot be removed) and the player can only remove one trait total.
# 
Here’s how we do it cleanly:
#     
# Updated Code (only the parts that changed)

# ─── Data the program knows about humans ───
RACES = {
    "human": {
        "fixed_traits": [          # traits every human always gets
            "Adaptive Blood",
            "Primal Grip",
            "Walker",
            "Prehensile Tail"
        ],
        "mutation_points": 8
    }
    # other races would go here later
}

# Trait class (same as before)
class Trait:
    def __init__(self, name, is_advantage=True, stat_bonuses=None):
        self.name = name
        self.is_advantage = is_advantage
        self.stat_bonuses = stat_bonuses or {}

# ─── Character class with the new logic ───
class Character:
    def __init__(self, name, race_name="human", diet="Omnivore", origin="Born of Chaos"):
        self.name = name
        self.race_name = race_name
        self.diet = diet                  # player's choice 1
        self.origin = origin              # player's choice 2
        
        race_data = RACES.get(race_name.lower(), RACES["human"])
        
        # Step 1: Build the default traits using the player's choices
        self.base_traits = race_data["fixed_traits"].copy()
        self.base_traits.append(self.diet)      # Herbivore / Omnivore / Carnivore
        self.base_traits.append(self.origin)    # In God's Image / Born of Chaos
        
        self.mutation_points = race_data["mutation_points"]
        self.job_levels = {}
        self.traits = []                     # will hold Trait objects
        
        # These stats start the same for everyone
        self.stats = {"health": 100, "agility": 10, "strength": 20, "piety": 20, "magic": 15}
        
        # Step 2: Automatically give every default racial trait
        for trait_name in self.base_traits:
            # Special case: Born of Chaos gives a piety bonus
            bonuses = {"piety": 10} if trait_name == "Born of Chaos" else {}
            self.traits.append(Trait(trait_name, stat_bonuses=bonuses))
        
        # Step 3: Mark which traits can NEVER be removed
        self.protected_traits = {"Adaptive Blood", self.diet}   # diet can never be removed
        self.removed_count = 0          # tracks how many traits have been given up
        self.max_removals = 1
        
        print(f"{self.name} created as a {self.race_name}.")
        print(f"   Diet: {self.diet} | Origin: {self.origin}")
        print(f"   Default traits loaded automatically.")

    # ─── Mutation methods (now with rules enforced) ───
    def spend_mutation(self, trait_name, stat_bonuses=None):
        if self.mutation_points <= 0:
            print("No mutation points left!")
            return False
        self.mutation_points -= 1
        new_trait = Trait(trait_name, stat_bonuses=stat_bonuses or {})
        self.traits.append(new_trait)
        print(f"   + Gained mutation: {trait_name}")
        return True

    def remove_trait(self, trait_name):
        """Only ONE removal allowed, and never protected traits"""
        if self.removed_count >= self.max_removals:
            print(f"Cannot remove more than {self.max_removals} racial trait!")
            return False
        
        if trait_name in self.protected_traits:
            print(f"Cannot remove protected trait: {trait_name}")
            return False
        
        # Find and remove the trait
        for i, trait in enumerate(self.traits):
            if trait.name == trait_name:
                del self.traits[i]
                self.removed_count += 1
                self.mutation_points += 1
                print(f"   - Gave up racial trait '{trait_name}' (+1 mutation point)")
                return True
        
        print(f"Trait '{trait_name}' not found")
        return False

    # (get_current_stats and show_sheet are unchanged from last time)
    def get_current_stats(self):
        final = self.stats.copy()
        # job bonuses + trait bonuses code stays exactly the same
        for job_name, lvl in self.job_levels.items():
            # ... (same as before)
            pass
        for trait in self.traits:
            for stat, value in trait.stat_bonuses.items():
                final[stat] += value
        return final

    def show_sheet(self):
        stats = self.get_current_stats()
        print(f"\n=== {self.name} ===")
        print(f"Race: {self.race_name} | Diet: {self.diet} | Origin: {self.origin}")
        print(f"Mutation points left: {self.mutation_points}")
        print(f"Jobs: {self.job_levels}")
        print(f"Current traits: {[t.name for t in self.traits]}")
        print("Stats:")
        for stat, value in stats.items():
            print(f"  {stat.capitalize()}: {value}")

# Creating Queenfisher — now with the exact rules you described

queenfisher = Character(
    name="Queenfisher",
    race_name="human",
    diet="Omnivore",           # her choice
    origin="Born of Chaos"     # her choice
)

# Add jobs (unchanged)
queenfisher.add_job("Squire", 1)
queenfisher.add_job("Acrobat", 1)
queenfisher.add_job("Apprentice", 1)

# Mutations she bought
queenfisher.spend_mutation("Back Wings", stat_bonuses={"agility": 12})
queenfisher.spend_mutation("Hydrophobic Feathers")
queenfisher.spend_mutation("Hunter Eyes", stat_bonuses={"agility": 8})
queenfisher.spend_mutation("Slick", stat_bonuses={"agility": 5})
queenfisher.spend_mutation("Natural Swimmer")
queenfisher.spend_mutation("Gills")

# She gave up ONE allowed trait
queenfisher.remove_trait("Born of Chaos")   # this is allowed

# These would be blocked by the code:
# queenfisher.remove_trait("Adaptive Blood")   # → protected
# queenfisher.remove_trait("Omnivore")         # → protected (diet)
# queenfisher.remove_trait("Primal Grip")      # would work, but she only gets ONE removal

queenfisher.show_sheet()

# What the logic is actually doing (the part you’re learning)__init__ forces
# the player to make the two choices before anything else.
# 
# The default traits list is built on the fly from the choices.
# 
# Protected traits are stored in self.protected_traits so the program can check rules automatically.
# 
# remove_trait now refuses anything that breaks the rules — the computer enforces the game rules
# instead of trusting the player to remember them.
# 
# This pattern (make choices first → build defaults → then allow modifications with checks) is
# used in almost every character creator, video game, or TTRPG tool.
# 
# You now have a clear mental model for “how do I turn complicated game rules into code that
# can’t be broken accidentally?”
# 
# Would you like me to:
#     Add the missing add_job / JOB_BENEFITS pieces so the whole thing runs as one file?
#     Show how to turn the remaining mutation points into raw stat bonuses instead of buying traits?
#     Or explain what would change if humans had even more choices (e.g. a third choice for “starting location”)?
# 
# Just tell me which piece of the logic you want to study next.
#############################################################################
# Follow up number i didnt check.
# 
# This game example is in the weeds anyways.
# 
# Secondary questions, I remember something about writing 'import time' and 'import random' where writing just
# 'import random' is supposed to import ALL of randoms functions. I remember I did that or something alot like
# that once and it works, but I can't get it to work now. So I've been writing 'from random import randint'.
# Is there a way to just import the whole thing at once?
# 
# Additionally, lets say I was making an idle game,something simple you do x thing and x value increases by 1.
# However in games like that, normally, you'd want to be able to have things happen seperately from the actual
# user input, such as if the user was a blacksmith forging ignots, but you hire an apprentice and he does it
# too every 10 seconds. It would be basically unplayable at a certain point of the constant loops prevented
# user input entirely. Is there a simple way to do that, or isthat something that requires some kind of far
# off advanced concepts.
###############################################################################
# Importing modules — you remembered correctly!
# The short answer is: yes, you can import the whole module at once with the simple line you already know:

import random
import time

# After that line, you use the module name as a prefix:

number = random.randint(1, 10)   # this works
print(time.time())               # this works

# That’s the normal, recommended way. It imports everything inside the module, but you have to type
# random. or time. in front of each function. That’s why it feels like “it works but I have to type more.”
# 
# You can also do what you’ve been doing:

from random import randint   # only brings in randint

# Then you can call it directly:

number = randint(1, 10)      # no "random." needed

# There is a third way that does what you were thinking of — importing all functions so you don’t need the prefix:

from random import *         # the asterisk means "everything"

# Now you can write randint(1, 10) directly.
# This is what you probably did once that “worked.”
# But it’s usually not recommended because if two modules have a function with the same name, they
# can fight each other and cause bugs. Most programmers stick with import random or the specific from
# random import randint style.
# 
# So in your scripts, just keep using import random (or import time) — that’s the cleanest and what
# everyone expects to see.
# 
# 
Idle games and background actions (the apprentice forging every 10 seconds)
# You’re exactly right — a plain while True: loop with time.sleep(10) would freeze the whole program
# and make it impossible for the player to type commands. That’s because sleep() stops everything.
# 
# The simple solution that still works with only things you already know (plus one new built-in module)
# is called threading.
# A “thread” is just Python running two pieces of code at the same time. One thread handles the player
# typing commands, the other thread quietly runs the apprentice in the background.
# 
# Here’s a complete tiny idle-game example using a class (exactly like we’ve been practicing):

import time
import threading   # ← new module, just like random or time

class Blacksmith:
    def __init__(self, name):
        self.name = name
        self.ingots = 0
        self.last_forge_time = time.time()   # used if you ever want offline progress too

    def forge(self):
        self.ingots += 1
        print(f"   🔥 {self.name} forged 1 ingot! Total: {self.ingots}")

    def status(self):
        print(f"\n=== {self.name}'s Forge ===")
        print(f"Ingots: {self.ingots}")
        print("Type 'forge', 'status', or 'quit'")

# Background worker that runs forever in its own thread
def apprentice_work(blacksmith):
    while True:
        time.sleep(10)           # apprentice forges every 10 seconds
        blacksmith.forge()

# ─── Main game loop (this is what the player interacts with) ───
blacksmith = Blacksmith("Queenfisher's Apprentice")

# Start the apprentice in the background
apprentice_thread = threading.Thread(target=apprentice_work, args=(blacksmith,), daemon=True)
apprentice_thread.start()

print("Welcome to the idle forge! The apprentice works even while you type.")
blacksmith.status()

while True:
    cmd = input("\n> ").strip().lower()
    
    if cmd == "forge":
        blacksmith.forge()           # you can still forge manually
    elif cmd == "status":
        blacksmith.status()
    elif cmd == "quit":
        print("Saving and quitting...")
        break
    else:
        print("Unknown command. Try 'forge', 'status', or 'quit'.")
        
# How to run it
# Copy the whole thing into a file and run it.
# You can type commands any time — the apprentice will still print “forged 1 ingot!”
# every 10 seconds without ever freezing your typing.

# Why this works so well for idle games
# 
# The apprentice_work function runs completely separately.
# daemon=True means the thread automatically stops when you type “quit”.
# You can add as many background systems as you want (gold per second, mana regen, etc.)
# — just make more threads or one big timer thread.
# 
# If you later want offline progress (so the apprentice keeps working even when the game
# is completely closed), we can add a simple save() / load() using json and time.time()
# the same way we did for characters earlier — no threads needed for that part.
# 
# Would you like me to:
#     Add save/load so the ingot count remembers between runs?
#     Show how to make the apprentice’s speed improve when you level him up (using the job
#     system ideas from before)?
#     Or turn this into a tiny loop that also prints a message every 5 seconds automatically?
# 
# Just say what you want to try next — we’re still going at whatever pace helps you most.
# You’re asking great questions that real game programmers deal with every day. 



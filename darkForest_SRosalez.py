from random import randrange
from random import randint

# Modular grid that equalizes spacing of displayed index
# IMPORTANT - a and b variables must be ODD NUMBERS

a = 21		# board length - vertical
b = 21		# board length - horizontal        
c = 0 		# max array value size
d = 0		# border adjustment

# amount of trees to spawn

if a > 20 or b > 20:
    trees = ((3 * a) // 2) + ((3 * b) // 2) * 2
else:
    trees = ((3 * a) // 2) + ((3 * b) // 2)

# This board is the actual board, its where everythings supposed to actually be.
board = [ [a * j + i + 1 for i in range(b)] for j in range(a) ]

# This board records whether the empty ground underneath the symbols is a "," or a "."
# So that when the player or an enemy passes through, the symbol underneath can be replaced.
ground = [ [" " for i in range(b)] for j in range(a) ]

# A dictionary to handle different kinds of directional player input.
compass = { "w":0,"d":1,"a":2,"s":3,
            "north":0, "east":1,"west":2,"south":3,
            "up":0,"right":1,"left":2,"down":3,
            "skip":4, "pass":4, "rest":4, "wait":4, "skip turn":4, "z":4,
            "controls":64, "control":64,
            "done":108, "finish":108, "finished":108, "exit":108, "quit":108,
            "start":128, "beginning":128, "begin":128, "intro":128,
            "help":333,
            "enemies":666, "enemy":666
    }

# Agree/Disagree lists for when the player is asked if they would like to replay the game.
agree		= ["y", "yes", "okay", "ok", "sure", "alright", "agree", "accept", "do", "yeah", "ok fine", "okay fine", "fine"]
disagree	= ["n", "no", "nope", "nah", "never", "stop", "quit", "exit", "don't", "disagree", "object", "protest"]

# The victory, defeat and replay flags are used to tell when to end the game, whether it was a win or a loss, and whether to replay.
victory = False
replay = True
defeat = False

# I forget what this does, but I know its relevant for setting up the board somehow.
respace = []

# Enemy's current distance from player using shortest possible path.
j_dist = 0
d_dist = 0
bm_dist = 0
c_dist = 0

wander = False

###################
# DELAYS
# In order to make the game more fair, the enemies have different stamina counters, which once reach certain
# thresholds, trigger recovery timers before they can move again. Along with chances to hesitate.

# John B. Treyl: Moves 10 turns, Recovers 1 turn, 20% chance to hesitate.
# Having the simplest AI, he has the most stamina.
# However, he also has a chance to skip his own turn.
# Or even completely fuck up and have to rest at any time.
j_stamina = 10
j_fatigue = 0
j_recover = 1
j_rest    = 0

# Doppelganger: Moves 8 turns, Recovers 2 turns.
# In exchange for having smarter ai, he has lower stamina and longer stops.
# d_stamina = 8
# d_fatigue = 0
# d_recover = 2
# d_rest    = 0

# Bloody Mary: Moves 1 turn, Recovers 1 turn, 5% chance to hesitate.
mary = True

# Compound
fortress = [
    ["#", "#", "#", "#", "#", "#", "#"],
    ["#", "▒", "▒", "▒", "▒", "▒", "#"],
    ["#", "▒", "▒", "▒", "▒", "▒", "#"],
    ["#", "▒", "▒", "⚑", "▒", "▒", "#"],
    ["#", "▒", "▒", "▒", "▒", "▒", "#"],
    ["#", "▒", "▒", "▒", "▒", "▒", "#"],
    ["#", "#", "#", "#", "#", "#", "#"]
]

# Current positions of important board symbols.
you = []		# Player coords
flag = []		# Goalpost coords
forest = []		# list of all tree coords
enemy = []		# John B. Treyl coords
twoman = []		# Doppelganger coords
ghost = []		# Bloody Mary coords
dog = []		# Cerberus coords
doors_dist = [] # All fortress door distances
doors_pos = [] # All fortress door positions

####################################################################
# To-do list:
#
# 1. Thinking about it, I'm not sure if there's any benefit at all to most of
# the functions that call ver and hor doing so? Like, I think I could've just
# had them all read the global variable right? You only need to declare a global
# variable in a function if you intend to modify it right? Idk, I need to double
# check if any of that was necessary.
#
# 2. Maze structure. I would like to add a second structure to the map, a small maze.
# Unfortunately, while I've seen examples of how to do so, I don't currently understand
# the code involved to be able to meaningfully adapt it to my purposes.
#
####################################################################
# Enemy list:
#
# Enemy #1: John B. Treyl "♞" (COMPLETE)
# 'YOU ARE BETRAYED!'
#
# Walks directly towards the player.
# After 10 turns of chasing, takes a 2 turn break.
# 2 in 20 chance of skipping his turn.
# 1 in 20 chance of skipping his turn and immediately taking the 2 turn break.
#
# Enemy #2: Doppelganger "A" (COMPLETE?)
# 'two man'
#
# Attempts to anticipate the best path from player to flag.
# Then attempts to get in the way.
# If he's already in the way, moves towards the player instead.
#
# Enemy #3: Bloody Mary "\033[1;37m♛\033[0m" (COMPLETE)
# 'bloody mary bloody mary bloody mary'
# 'hey check out how hard I can pee'
#
# Intangible - Walls and Trees don't block her
# But she can only move every other turn.
# 1/20 chance to think of something gross and get distracted.
#
# Enemy #4: Cerberus "щ" (COMPLETE) 
# 'you encounter a dog, what do you do?'
#
# 1 in 10 chance to teleport randomly.
# 1 in 3 chance to remember it's supposed to move towards you.
# 2 in 3 chance to wander aimlessly.
####################################################################
# Known bugs/oversights:
# 1. The only thing stopping chase() from making the enemy move off the board
# and wrapping around to the other side is it will never logically try to.
# Because it is not possible for it to decide to do something that would trigger
# this as of now, I'm ignoring it unless it becomes a problem.
#
# 2. intercept() is still fucked. Doppelganger still has problems with camping the flag
# becoming unresponsive and no longer moving at all. etc etc.
#
# I really really fuckin' hope that that bug is finally fixed.
#
# 3. It appears both bloody mary and the doppelganger are not able to actually kill the player
# if they reach them. idfk why.
#
# I think this issue is already fixed but I'm not sure
#
# 4. Because the only thing John B. Treyl can do is move towards the player. If theres
# no path to the player, his ai breaks. This is less a bug and more a "there literally just
# not code that accounts for that condition."
#
# 5. Cerberus can teleport into a position incapable of reaching the player rarely. This likely could be fixed with
# trivially easily with a ring map, I just haven't yet.
#
# 6. On the turn after john b. treyl eats shit, he doesnt properly display a message
# that hes resting even though he is
###############################################################
# DISCLAIMER:
#
# I am not actually smart enough to understand the fuckin ANSII format of instructions.
# Seriously, that formats ancient, noone actually believes I understand that kind of special
# instruction shit lmfao. I looked that up.
# I just wanted to make sure the more important symbols stood out better without having to
# use only symbols that are bold by default. If you quiz me on how ANSII works later I don't
# fuckin know lmfao. Its good qol tho, just take it as that and nothing more.
####################################################################

# Displays initial scenario and rules on game start
def rules():
    print("""
    ╔═══════════════════════════════════════════════════════════════╗
    ║ You have entered a Dark Forest deep in enemy territory.       ║
    ║                                                               ║
    ║ Your objective is to make your way to the flag without        ║
    ║ being captured by members of the enemy clan, the wicked       ║
    ║ and sinister Treyl Clan!                                      ║
    ║                                                               ║
    ║ "\033[1;37m@\033[0m" is (You).                                                 ║
    ║                                                               ║
    ║ "⚑" is the flag of the enemy,                                 ║
    ║ If you reach the flag safely, you win.                        ║
    ╚═══════════════════════════════════════════════════════════════╝
    """)

def controls():
    print("""
    ╔═══════════════════════════════════════════════════════════════╗
    ║ CONTROLS:                                                     ║
    ║                                                               ║
    ║ You can move by typing the direction you want to go:          ║
    ║ "w", "0", "up", or "north" will move up.                      ║
    ║ "d", "1", "right", or "east" will move right.                 ║
    ║ "a", "2", "left", or "west" will move left.                   ║
    ║ "s", "3", "down", or "south" will move down.                  ║
    ║                                                               ║
    ║ "z", "4", "wait", "skip", "pass", or "rest" will skip         ║
    ║ your turn.                                                    ║
    ╚═══════════════════════════════════════════════════════════════╝
    """)

def enemies():
    print("""
    ╔═══════════════════════════════════════════════════════════════╗
    ║ THE TREYL CLAN:                                               ║
    ║                                                               ║
    ║ "T" and "#" are the forests trees and fortress walls of the   ║
    ║  Treyl Clan's hideout. They are both harmless but impassable. ║
    ║                                                               ║
    ║ "\033[38;2;40;149;253m♞\033[0m" is John B. Treyl. If he catches you he will slash you     ║
    ║ with his magic sabre!!! You must not let this happen!         ║
    ║ Fortunately, he only knows how to go straight for you!        ║
    ║                                                               ║
    ║ "\033[1;37m♛\033[0m" is Bloody Mary, this haunting apparition slowly stalks    ║ 
    ║ these cursed grounds. But her incorporeal nature means that   ║
    ║ the forest's trees aren't enough to stop her!                 ║
    ║                                                               ║
    ║ "\033[1;37mA\033[0m" is a Doppelganger, this dubious pretender will tear your  ║
    ║ pelt from your bones. Wearing it sloughed over his form as he ║
    ║ takes the flag for himself!                                   ║
    ║ Be careful where you run, this mimic is crafty, and knows     ║
    ║ about your quest. He may try to predict your chosen path!     ║
    ║                                                               ║
    ║ "\033[1;37mщ\033[0m" is Cerberus. This deadly hound wanders                    ║
    ║ around the board aimlessly. Only 1 of its heads is smart      ║
    ║ enough to remember its supposed to attack intruders.          ║
    ╚═══════════════════════════════════════════════════════════════╝
    """)
    
def explain():
    while True:
        x = input("""
    ╔═══════════════════════════════════════════════════════════════╗
    ║ What specifically do you need help with?                      ║
    ║                                                               ║
    ║ >Type "intro" to see the intro text again.                    ║ 
    ║ >Type "controls" for the list of commands.                    ║
    ║ >Type "enemies" for a description of your adversaries!        ║
    ║                                                               ║
    ║ >Type "done" when you want to return to the game.             ║
    ╚═══════════════════════════════════════════════════════════════╝
    """)
        x = translate(x)
        if x == 64:
            controls()
        if x == 128:
            rules()
        elif x == 666:
            enemies()
        elif x == 108:
            break
        else:
            print("    Didn't quite catch that.\n    ")

# This is basically so the size of the board can vary based
# on a couple preset variables.
def detectLen(ver, hor):
    global c,d 
    for i in range(ver):
        for j in range(hor):
            value = board[i][j]
            value = str(value)
            list(value)
            value2 = len(value)
            if value2 > c:
                c = value2
                d = c + 1

# I don't 100% remember what this does, but I think its just
# to make it not look like shit, shouldn't normally matter.
# Don't ask me how it works I dont remember lol.
def adjust(ver, hor, area):
    for h in range(ver):
        for i in range(hor):
            value = board[h][i]
            square = value
            square = str(square)
            list(square)
            space = area - len(square)
            square = "".join(square)
            y = (" " * space, square)
            y = "".join(y)
            respace.append(y)
            squareSpace = respace[i]
            board[h][i] = squareSpace
        del respace[:]

# Displays current board state
def world(ver, hor, bord):
    print("    ╔═", "═" * hor * bord, "╗", sep="", end="")
    for x in range (ver):
        print("")
        print("    ║ ", end="")
        for y in range (hor):
            print(board[x][y], " ", sep="", end="")
        print("║", end="")
    print("")
    print("    ╚═", "═" * hor * bord, "╝", sep="", end="")
    print("")

# Fills empty spaces with ","s and "."s
# Really just an aesthetic feature.
def topsoil(ver, hor):
    for x in range (ver):
        for y in range (hor):
            a = randint(0,1)
            if a == 1:
                board[x][y] = ","
                ground[x][y] = ","
            else:
                board[x][y] = "."
                ground[x][y] = "."

# A helper function to reduce the size of spawn(), its very repetative.
def summon(ver, hor, symb, sol):
    symbols = ["T", "⚑", "\033[38;2;40;149;253m♞\033[0m", "\033[1;37m@\033[0m", "\033[1;37m♛\033[0m", "\033[1;37mщ\033[0m", "\033[1;37mA\033[0m", "#", "╍", "▒", "╏"]
    
    while True:
        a = randint(0,ver-1)
        b = randint(0,hor-1)
        
        if board[a][b] not in symbols:
                board[a][b] = symb
                sol.append(a)
                sol.append(b)
                break

# Populates board with game objects
def spawn(ver, hor, area):    
    symbols = ["T", "⚑", "\033[38;2;40;149;253m♞\033[0m", "\033[1;37m@\033[0m", "\033[1;37m♛\033[0m", "\033[1;37mщ\033[0m", "\033[1;37mA\033[0m", "#",]
    tree_symbols = ["T", "⚑", "\033[38;2;40;149;253m♞\033[0m", "\033[1;37m@\033[0m", "\033[1;37m♛\033[0m", "\033[1;37mщ\033[0m", "\033[1;37mA\033[0m", "#", "╍", "▒", "╏"]
    
    while True:
        # Treyl Fortress
        while True:
            rand_ver = randint(0,ver-1)
            rand_hor = randint(0,hor-1)
            
            if board[rand_ver][rand_hor] not in symbols and 3 < rand_ver < ver-3 and 3 < rand_hor < hor-3:
                see, d = rand_ver-3,rand_hor-3
                e = randint(2,3)
                
                flag.append(rand_ver)
                flag.append(rand_hor)
                for x in range (7):
                    for y in range (7):
                        board[see+x][d+y] = fortress[x][y]
                        ground[see+x][d+y] = fortress[x][y]
                
                door_count = [] 
                while len(door_count) != e:
                    f = randint(0,3)
                    if f not in door_count:
                        door_count.append(f)
                        
                for _ in range(e):
                    if door_count[_] == 0:    
                        board[rand_ver+3][rand_hor] = "╍"
                        ground[rand_ver+3][rand_hor] = "╍"
                        doors_pos.append([rand_ver+3, rand_hor])
                        
                    elif door_count[_] == 1:
                        board[rand_ver][rand_hor+3] = "╏"
                        ground[rand_ver][rand_hor+3] = "╏"
                        doors_pos.append([rand_ver, rand_hor+3])
                    
                    elif door_count[_] == 2:
                        board[rand_ver][rand_hor-3] = "╏"
                        ground[rand_ver][rand_hor-3] = "╏"
                        doors_pos.append([rand_ver, rand_hor-3])
                    
                    elif door_count[_] == 3:    
                        board[rand_ver-3][rand_hor] = "╍"
                        ground[rand_ver-3][rand_hor] = "╍"
                        doors_pos.append([rand_ver-3, rand_hor])
                        
                break
        
        # Trees - this doesnt use summon() bc theres more then 1.
        t = 0
        while t != trees:
            rand_ver = randint(0,ver-1)
            rand_hor = randint(0,hor-1)
            
            if board[rand_ver][rand_hor] not in tree_symbols:
                board[rand_ver][rand_hor] = "T"
                ground[rand_ver][rand_hor] = "T"
                forest.append([rand_ver,rand_hor])
                t += 1
        
        # You
        summon(ver, hor, "\033[1;37m@\033[0m", you)
 
        # John B. Treyl
        summon(ver, hor, "\033[38;2;40;149;253m♞\033[0m", enemy)
        
        # Doppelganger
        summon(ver, hor, "\033[1;37mA\033[0m", twoman)
        
        # Bloody Mary
        summon(ver, hor, "\033[1;37m♛\033[0m", ghost)
        
        # Cerberus
        summon(ver, hor, "\033[1;37mщ\033[0m", dog)
            
        #######################################################
        # SOFTLOCK CHECK:
        #
        # Part 1: Generate ring map from player.
        # Part 2: Check distance values of John B. Treyl, Doppelganger and Flag.
        # Part 3: If any dist value > 0, regenerate, else, continue
        #
        # For obvious reasons, Bloody Mary doesn't need the check.
        
        player_rings = [[-1 for _ in range(hor)] for _ in range(ver)] # temp list of lists, used for pathfinding
        ppos = []
        
        ring_mapper(ver, hor, ppos, you, player_rings, ["T", "#"])

        j_dist = player_rings[enemy[0]][enemy[1]]
        j_dist = int(j_dist)
        
        f_dist = player_rings[flag[0]][flag[1]]
        f_dist = int(f_dist)
        
        d_dist = player_rings[twoman[0]][twoman[1]]
        d_dist = int(d_dist)
        
        # The goal of this section is to scan if any doorway can't reach
        # the player without going through a different door.
        player_rings = [[-1 for _ in range(hor)] for _ in range(ver)]
        ppos = []
        ring_mapper(ver, hor, ppos, you, player_rings, ["T", "#", "▒"])

        for _ in range(len(doors_pos)):
            x, y = doors_pos[_][0], doors_pos[_][1]
            z = player_rings[x][y]
            doors_dist.append(z)
        
        if j_dist > 0 and f_dist > 0 and d_dist > 0 and -1 not in doors_dist:
            break
        else:
            purge(a,b,c)

# Helper function for user input error handling
def translate(a):
    try:
        a = int(a)
    except:
        pass
    if isinstance(a, str) and a.lower() in compass:
        babble		= a.lower()
        evilBabble	= compass[babble]
        a	= int(evilBabble)
    return a

# This is what handles player movement.
def move(ver, hor, area, bord):
    global defeat
    while True:
        x = input("    Which direction? (North, South, East, West or Wait?)\n    Type 'help' if you need any assistance.\n    ")      
        x = translate(x)
        
        current_row, current_col = you[0], you[1]
        under = ground[current_row][current_col]
        
        symbols = ["T", "#", "\033[38;2;40;149;253m♞\033[0m", "\033[1;37mA\033[0m", "\033[1;37m♛\033[0m", "\033[1;37mщ\033[0m"]
        directions = [[-1, 0], [0, 1], [0, -1], [1, 0], [0, 0]]
        
        try:
            if 0 <= x <= 3:
                dy, dx = directions[x]
                target_row = current_row + dy
                target_col = current_col + dx
                
                if 0 <= target_row < ver and 0 <= target_col < hor:
                    
                    if board[target_row][target_col] not in symbols:
                        you[0] = target_row
                        you[1] = target_col
                        board[current_row][current_col] = under
                        board[target_row][target_col] = "\033[1;37m@\033[0m"
                        break
                        
                    elif board[target_row][target_col] == "T":
                        print("    A sturdy tree blocks your path.")
                    
                    elif board[target_row][target_col] == "#":
                        print("    A sturdy wall blocks your path.")
                        
                    elif board[target_row][target_col] == "\033[38;2;40;149;253m♞\033[0m":
                        print("    Your head was cleaved from your shoulders.")
                        defeat = True
                        break
                    
                    elif board[target_row][target_col] == "\033[1;37mA\033[0m":
                        print("    Your reflection shatters you.")
                        defeat = True
                        break
                    
                    elif board[target_row][target_col] == "\033[1;37m♛\033[0m":
                        print("    You were never seen again.")
                        defeat = True
                        break
                    
                    elif board[target_row][target_col] == "\033[1;37mщ\033[0m":
                        print("    The true mastermind of the Treyl Clan pressed a button on its remote,")
                        print("    and you get drawn into its UFO's tractor beam!")
                        defeat = True
                        break
                else:
                    print("    That would be outside the board.")
            
            elif x == 4:
                print(f"    You take a moment to catch your breath...")
                break
            elif x == 333:
                explain()
                world(ver, hor, bord)
            else:
                print("    Invalid move, try again.\n    ")
        except:
            print("    Invalid move, try again.\n    ")

# Checks if player has won the game
def win():
    global victory
    a = you[0]
    b = you[1]
    c = flag[0]
    d = flag[1]
    if a == c and b == d:
        victory = True

# Checks if player wants to play again
def playAgain():
    global replay, victory, defeat
    while True:
        a = input("    Would you like to play again?\n    ")
        if a in agree:
            print("    Alright, regenerating the map.\n    ")
            replay = True
            victory = False
            defeat = False
            break
        elif a in disagree:
            replay = False
            break
        else:
            print("    Didn't quite catch that.\n    ")

# Clears the board to be reset for a new game/board regeneration
def purge(ver, hor, area):
    del you[:]
    del enemy[:]
    del twoman[:]
    del ghost[:]
    del dog[:]
    del flag[:]
    del forest[:]
    del doors_pos[:]
    del doors_dist[:]
    
    board[:] = [ [" " for i in range(hor)] for j in range(ver) ]
    ground[:] = [ [" " for i in range(hor)] for j in range(ver) ]
    
    topsoil(a,b)
    detectLen(a,b)
    adjust(a,b,c)

########################################################################
# PATHFINDING LOGIC - HELPER FUNCTIONS moveTWO(), ring_mapper(), backtracer()

# The previous enemy movement code sucked so I rewrote it
def moveTWO(nme, symb, target_row, target_col, ver, hor):
    global defeat, wander
    
    current_row, current_col = nme[0], nme[1]
    under = ground[current_row][current_col]
    
    directions = [[-1, 0], [0, 1], [0, -1], [1, 0]]
    
# enumerate() explanation
# okay so the explanation online for enumerate() is overcomplex to the point of
# completely obscuring the meaning. tl;dr what it does is when you're looping over
# a list (or something else iterable) and you need both an item AND its position
# at the same time.
#
# EXAMPLE:
#     for index, value in enumerate(directions):
#         print(index, value)
#
# OUTPUTS:
#     0 [-1, 0]
#     1 [0, 1]
#     2 [0, -1]
#     3 [1, 0]
    
    # == This check ensures a single valid step ==
    way = None
    for i, (dy, dx) in enumerate(directions):
        if current_row + dy == target_row and current_col + dx == target_col:
            way = i
            break
        
    if way is None:
        # It shouldn't be possible for this to trigger, but if does, pick any legal neighbor.
        print(f'Error: {nme} ({symb}) could not find a valid step to {target_row}, {target_col}!')
        return
    
    # == Move preparation ==
    dy, dx = directions[way]
    target_row = current_row + dy
    target_col = current_col + dx
    
    # == Defeat check ==
    if board[target_row][target_col] == "\033[1;37m@\033[0m":
        if nme == enemy:
            print("    You run right into your pursuers blade...\n    He informs you that you have been John Betrayed...")
        elif nme == twoman:
            print("    The thing wearing your face will take their flag in your place...")
        elif nme == ghost:
            print("    You collapse to the forest floor with a blood curdling scream...")
        elif nme == dog:
            print("    The dog lets out a really, really SCARY bark and you die of death disease...")
        defeat = True
        return
    
    # == Actual move ==
    nme[0], nme[1] = target_row, target_col
    board[current_row][current_col] = under
    board[target_row][target_col] = symb
    
    # == normal movement messages ==
    if nme == dog and wander == True:
        msg = "    An adversary wanders aimlessly..."
    else:
        msg = "    An adversary approaches..."   

    if way == 0:   print(f"{msg} ({symb}) (N) ({nme})")
    elif way == 1: print(f"{msg} ({symb}) (E) ({nme})")
    elif way == 2: print(f"{msg} ({symb}) (W) ({nme})")
    elif way == 3: print(f"{msg} ({symb}) (S) ({nme})")

####################################################################################
# Defining the trail backwards part of all this pathfinding into a helper function.
# Used for chase() and intercept()
def backtracer(ver, hor, dist, ring_map, symb, path):
    
    directions = [[-1, 0], [0, 1], [0, -1], [1, 0]]
    
    for _ in range(dist):
        counter = 0 # simply prevents it from writing more then one valid lower position.
        row, col = path[-1][0], path[-1][1]
        
        for d in directions:
            nr, nc = row + d[0], col + d[1] # new row, new column
            
            if (0 <= nr < ver) and (0 <= nc < hor):
                chk_rng = ring_map[nr][nc] # ring number of neighbor being checked
                old_pos = ring_map[path[-1][0]][path[-1][1]] # old position
                
                if (0 <= nr < ver) and (0 <= nc < hor) and chk_rng == old_pos - 1 and board[nr][nc] not in symb and counter == 0:
                    path.append([nr, nc])
                    counter += 1
                    # I'm not sure if I need to use return here when the values are being appended to a list like this.

####################################################################################
# Defining the ring mapping part of all this pathfinding into a helper function.
# Used for spawn(), chase() and intercept().
def ring_mapper(ver, hor, _pos, sol, ring_map, symb):
    
    directions = [[-1, 0], [0, 1], [0, -1], [1, 0]]
    
    _pos.append(sol[:]) # filling list
    ring_map[sol[0]][sol[1]] = 0 # placing 0 at enemy pos
    
    while len(_pos) > 0:
        current = _pos.pop(0)
        row = current[0]
        col = current[1]
        rings = ring_map[row][col]
        
        for d in directions:
            nr = row + d[0] # new row
            nc = col + d[1] # new column
             
            if (0 <= nr < ver) and (0 <= nc < hor) and ring_map[nr][nc] == -1 and board[nr][nc] not in symb:
                ring_map[nr][nc] = rings + 1
                _pos.append([nr,nc])
                # I'm not sure if I need to use return here when the values are being appended to a list like this.
                
                # Okay, afaik .append() refers to the original list, not a copy, so _pos should update input values correctly?        

########################################################################
# ENEMY PATHFINDING LOGIC - chase(), intercept(), haunt() and encounter()

# John B. Treyl's pathfinding and movement.
def chase(ver, hor, forest_trees):
    global enemy, defeat, you, j_dist, j_fatigue, j_stamina, j_rest, j_recover

    # Step 1: Create ring map relative to enemy position.
    # Step 2: Create list of coordinates that lead from player position to enemy position
    # Step 3: Have enemy move to space marked at the end of list of coordinates
    
    # To be 100% clear, it is INTENDED BEHAVIOR that the lists are backwards.

    #####################################################################

    symbols = ["T", "⚑", "\033[38;2;40;149;253m♞\033[0m", "\033[1;37mA\033[0m", "\033[1;37m♛\033[0m", "\033[1;37mщ\033[0m", "#"]
    
    # north, east, west, south
    directions = [[-1, 0], [0, 1], [0, -1], [1, 0]]
    
    #####################################################################
    # Enemy Chasing Behavior - Addon: Staming and Stumbling
    #
    # With multiple enemies, the game becomes much more difficult, to
    # make the game more fair, I'm going to limit how long john can chase the player.
    # This code simply isn't fully written.
    
    d20 = randint(1, 20)
    
    if j_fatigue != j_stamina and d20 > 4:
        j_fatigue += 1
            
        #####################################################################
        # Enemy Chasing Behavior - Part 1: Ring Map Generation        

        betray_ring = [[-1 for _ in range(hor)] for _ in range(ver)] # temp list of lists, used for pathfinding
        jpos = [] # list for holding copy of enemy position
        
        ring_mapper(ver, hor, jpos, enemy, betray_ring, symbols)
            
        #####################################################################
        # Enemy Chasing Behavior - Part 2: Path from "@" to "♞"
        # God pathfinding is hell to write
        
        player_to_john = [] # pathing from player to enemy
        player_to_john.append([you[0], you[1]]) # append initial player position (necessary to start loop)
        
        j_dist = betray_ring[you[0]][you[1]] # the number that is in this position on pathfinder is what i want
        j_dist = int(j_dist)
        
        backtracer(ver, hor, j_dist, betray_ring, symbols, player_to_john)
                    
        #####################################################################
        # Enemy Chasing Behavior - Part 3: Enemy Movement
        
        current_row, current_col = enemy[0], enemy[1]
        
        target_row, target_col = player_to_john[-1][0], player_to_john[-1][1]
        # -1 in a list index picks the last entry of the list.
        
        print("    You hear someone cleaving through tree branches with a blade behind you.")
        moveTWO(enemy, "\033[38;2;40;149;253m♞\033[0m", target_row, target_col, ver, hor)
        
    elif j_fatigue == j_stamina and j_rest != j_recover and d20 > 3:
        j_rest += 1
        print(f"    John B. Treyl needs a moment to John Breathe Treyl. (\033[38;2;40;149;253m♞\033[0m) ({enemy})")
        
    elif j_fatigue == j_stamina and j_rest == j_recover and d20 > 3:
        j_fatigue, j_rest = 0, 0
        print(f"    John B. Treyl has recovered his stamina! (\033[38;2;40;149;253m♞\033[0m) ({enemy})")
        
    elif d20 <= 3 and d20 != 1 and j_fatigue != j_stamina:
        print(f"    John B. Treyl trips on a dead branch and loses his footing. (\033[38;2;40;149;253m♞\033[0m) ({enemy})")
        
    elif d20 == 1 and j_fatigue != j_stamina:
        print("    John B. Treyl eats shit and trips face first into the forest floor,")
        print(f"    narrowly managing not to impale himself on his own sword. (\033[38;2;40;149;253m♞\033[0m) ({enemy})")
        j_fatigue = j_stamina

#     # view ring map for debugging
#     for row in pathfinder:
#         print(row)

# Doppelganger's pathfinding and movement.
def intercept(ver, hor, forest_trees):
    global twoman, defeat, d_dist, d_fatigue, d_stamina, d_rest, d_recover
    
    # Unlike John B. Treyl, the Doppelganger is supposed to flank the player.
    
    # The intention of intercept() is that "A" will try stand in the way of
    # the players best possible path to the flag. Then, use that path to move
    # towards the player.    
    
    # Step 1: Generate Ring Map from Player.
    # Step 2: Generate Path from Flag to Player.
    # Step 3: Generate Ring Map from Doppelganger.
    # Step 4: Finding Closest Position in Path from Flag to Player to Doppelganger.
    # Step 5: Determine if Doppelganger is to chase or flank Player.
        # Step 5A: If Doppelgangers already in players way, move towards player.
        # Step 5B: If Doppelgangers not in players way...
            # Step 5B1: Generate path from Best Position to Doppelganger.
            # Step 5B2: Move towards path.
            
    # This code is however incredibly difficult for me to bugfix, idk why its not
    # working. It has problems with camping the flag and becoming unresponsive and just
    # not making any moves anymore. I'm tried to set it so it couldnt path to the fortress
    # floor using its flanking logic, only its chasing logic. But that didn't work. idk.
    # shits fucked. I'm still working on it.

    # north, east, west, south
    directions = [[-1, 0], [0, 1], [0, -1], [1, 0]]
    
    player_symbols = ["\033[38;2;40;149;253m♞\033[0m", "\033[1;37mщ\033[0m", "\033[1;37m♛\033[0m", "T", "#"]
    doppel_symbols = ["\033[38;2;40;149;253m♞\033[0m", "\033[1;37mщ\033[0m", "\033[1;37m♛\033[0m", "T", "#", "⚑", "\033[1;37mA\033[0m",]  
    
    best_dist = 9999 # just a stupid high number
    best_pos = None # Storing which position in fpos_to_ppos is closest to dpos

# I wanted to give it stamina mechanics like John has, but given how buggy
# its code is as it is. I don't want to introduce another complicating factor.
#     
#     if d_fatigue != d_stamina:
#         d_fatigue += 1
    
    # Part 1: Ring Map Generation (Player)
    player_rings = [[-1 for _ in range(hor)] for _ in range(ver)]
    ppos = [] # player position
    
    ring_mapper(ver, hor, ppos, you, player_rings, player_symbols)
                
    # Part 2: Path from "F" to "@"
    fpos_to_ppos = [] # path from flag to player
    fpos_to_ppos.append([flag[0], flag[1]])
    
    p_dist = player_rings[flag[0]][flag[1]]
    p_dist = int(p_dist)
    
    backtracer(ver, hor, p_dist, player_rings, player_symbols, fpos_to_ppos)
    
    # Part 3: Ring Map Generation (Doppel)
    doppel_rings = [[-1 for _ in range(hor)] for _ in range(ver)]
    dpos = [] # doppelganger position
    
    ring_mapper(ver, hor, dpos, twoman, doppel_rings, doppel_symbols)
                
    # Part 4: Finding Closest Position in fpos_to_ppos to dpos.
    for pos in fpos_to_ppos:
    # I wasn't aware you could make for loops this way, maybe it was explained before, I forgor.
        
        row, col = pos[0], pos[1]    
        dist = player_rings[row][col]
        
        # Previously, this section used:
            # dist = doppel_rings[row][col]
            
        # But because that minimizes distance from Doppelganger instead of the Player
        # it can lead to behavior where the Doppelganger camps the flag. By using
        # player_rings instead, he focuses on parts of the path closer to the player
        # making him easier to kite.
        
        # tbh this didn't fix the issue so I question if it was ever correct lmfao.
        
        if dist < best_dist and dist != -1 and board[row][col] != "⚑":
            best_dist = dist
            best_pos = pos
    
    ###########################
    current_row, current_col = twoman[0], twoman[1]
    
    # This is where I learned how to use any()
    # any() returns True if at least one element would return True in a list
    
    # Chasing player behavior
    if any(twoman == pos for pos in fpos_to_ppos): 
        target_row, target_col = you[0], you[1]
        print("    You hear your own voice calling from right behind you!")   # chase message
        
    # Flanking player behavior
    else:   
        ############################################
        # Path from best_pos to "A".
        # This used to be part 5, but was moved into this else branch because
        # when the path from player to flag is extremely short (ie: theyre right next to it)
        # the game would simply crash. So this code should only run conditionally, when
        # flanking is actually desired.
        
        # The most persistent crash bug I haven't been able to fix is best_pos
        # somehow getting set to None. If the path is very short or theres no valid square
        # is my current theory, it happens more the closer you get to the flag.
        #
        # Until I deal with it. if that occurs, we set it to this so that it just
        # defaults to chasing instead of flanking.
        
        if best_pos is None:
            # Fallback for edge cases (very short path or no valid square)
            # This just makes it chase the player anyways instead of flanking.
            
            target_row, target_col = you[0], you[1]   # player's exact position
            print("    You hear your own voice calling from right behind you!")   # chase message
            
        else:
            # This is the real flanking code
            bpos_to_dpos = []
            bpos_to_dpos.append([best_pos[0], best_pos[1]])
           
            d_dist = doppel_rings[best_pos[0]][best_pos[1]]
            d_dist = int(d_dist)
            
            backtracer(ver, hor, d_dist, doppel_rings, doppel_symbols, bpos_to_dpos)
            
            target_row, target_col = bpos_to_dpos[-1][0], bpos_to_dpos[-1][1]
            print("    You hear your own voice calling for you in the distance.")
    
    moveTWO(twoman, "\033[1;37mA\033[0m", target_row, target_col, ver, hor)
        
    # == Distance from player for print() purposes ==
    dpos = [] # doppelganger position
    ring_mapper(ver, hor, dpos, twoman, doppel_rings, doppel_symbols)
    d_dist = doppel_rings[you[0]][you[1]]
    d_dist = int(d_dist)
    print(f"    Doppelganger's distance from (You): {d_dist}")
    print()
         
#     elif j_fatigue == d_stamina and d_rest != d_recover:
#         d_rest += 1
#         print("    Your mirror image is waiting for you to blunder into its trap.")
#         
#     elif j_fatigue == d_stamina and d_rest == d_recover:
#         d_fatigue, d_rest = 0, 0
#         print("    Your mirror image has decided on a better position.")

# Bloody Mary's pathfinding and movement.
def haunt(ver, hor):
    global ghost, mary, bm_dist, defeat
    
    # Bloody Mary's ai is alot simpler then Doppelganger's
    # She gets to move through trees as if they arent there.
    # But she only gets to move every other turn.
    # She just moves directly towards the player like John though.
    
    # north, east, west, south
    directions = [[-1, 0], [0, 1], [0, -1], [1, 0]]
    symbols = ["\033[38;2;40;149;253m♞\033[0m", "\033[1;37mA\033[0m", "\033[1;37mщ\033[0m", "⚑", "\033[1;37m♛\033[0m"]
    d20 = randint(1,20)
    
    if d20 != 1:
        # I'm very sick of writing pathfinding logic lmfao
        bloody_ring = [[-1 for _ in range(hor)] for _ in range(ver)]
        bmpos = []
        ring_mapper(ver, hor, bmpos, ghost, bloody_ring, symbols)
        bm_to_u = [] 
        bm_to_u.append([you[0], you[1]])
        bm_dist = bloody_ring[you[0]][you[1]] 
        bm_dist = int(bm_dist)
        backtracer(ver, hor, bm_dist, bloody_ring, symbols, bm_to_u)
        
        if mary == True:
            print(f"    A moment of calm. (♛) ({ghost})")
            print(f"    Mary's distance from (You): {bm_dist}")
            print()
            mary = False
            
        elif mary == False:
            current_row, current_col = ghost[0], ghost[1]
            target_row, target_col = bm_to_u[-1][0], bm_to_u[-1][1]
            
            print("    What a horrible night.")
            moveTWO(ghost, "\033[1;37m♛\033[0m", target_row, target_col, ver, hor)
            
            bmpos = []
            ring_mapper(ver, hor, bmpos, ghost, bloody_ring, symbols)
            bm_to_u = [] 
            bm_to_u.append([you[0], you[1]])
            bm_dist = bloody_ring[you[0]][you[1]] 
            bm_dist = int(bm_dist)
            backtracer(ver, hor, bm_dist, bloody_ring, symbols, bm_to_u)
            
            print(f"    Mary's distance from (You): {bm_dist}")
            print()
            mary = True
    
    elif d20 == 1:
        print("    Bloody Mary pauses for a moment, remembering something gross")
        print(f"    and letting out a sigh of dissapointment. (♛) ({ghost})")
        print(f"    Mary's distance from (You): {bm_dist}")
        print()
        mary = True

# Cerberus's "pathfinding" and movement.
def encounter(ver, hor):
    global dog, defeat, c_dist, wander

    directions = [[-1, 0], [0, 1], [0, -1], [1, 0]]
    symbols = ["\033[38;2;40;149;253m♞\033[0m", "\033[1;37mA\033[0m", "\033[1;37mщ\033[0m", "⚑", "\033[1;37m♛\033[0m", "T", "#"]
    
    distractions = ["the sounds of the forest", "their tail", "a glimmer in the corner of his eye", "spite", "literally nothing",
                    "a distraction", "hunger\n    for a choccy dog with pilk", "the futility of it all", "political intrigue",
                    "AI generated slop videos", "skepticism\n    whether the other heads are also dogs", "the grindset",
                    "wanting\n    to show off to Bloody Mary", "the\n    realization that they're a dog",  "hatred\n    towards the doppelganger",
                    "worries\n    about their mother's worsening dementia", "a strange rat", "envy\n    over John's cool sabre",
                    "insecurity\n    that hes holding the team back", "an\n    unrequited crush on the left head"]
      
    canine_ring = [[-1 for _ in range(hor)] for _ in range(ver)]
    cpos = [] 
    ring_mapper(ver, hor, cpos, dog, canine_ring, symbols)
    player_to_dog = [] 
    player_to_dog.append([you[0], you[1]]) 
    c_dist = canine_ring[you[0]][you[1]] 
    c_dist = int(c_dist)
    backtracer(ver, hor, c_dist, canine_ring, symbols, player_to_dog)
    current_row, current_col = dog[0], dog[1]
    
    d10 = randint(1, 10)
    d20 = randint(1, 19)
       
    if d10 <= 5:
        print("    A faint light flickers behind Cerberus's left head's eyes.")
        target_row, target_col = player_to_dog[-1][0], player_to_dog[-1][1]
        
        wander = False
        moveTWO(dog, "\033[1;37mщ\033[0m", target_row, target_col, ver, hor)
        
        print(f"    Cerberus's distance from (You): {c_dist}")
        
    elif 5 < d10 <= 8:
        print("    A wild smirk adorns Cerberus's center head's face...")
        
        adjacent = [] # available open spaces
    
        # The intention here is I'm reusing some of backtracer()'s code to check if
        # adjacent positions are free and writing them into a list.
        for d in directions:
            nr, nc = current_row + d[0], current_col + d[1] # new row, new column
            
            if (0 <= nr < ver) and (0 <= nc < hor):
                chk_rng = canine_ring[nr][nc] # ring number of neighbor being checked
                
                if (0 <= nr < ver) and (0 <= nc < hor) and chk_rng not in [0, -1] and board[nr][nc] not in symbols:
                    adjacent.append([nr, nc])
                    
        dLen = randint(1, len(adjacent)) -1
        target_row, target_col = adjacent[dLen][0], adjacent[dLen][1]
        
        wander = True
        moveTWO(dog, "\033[1;37mщ\033[0m", target_row, target_col, ver, hor)

        print(f"    Cerberus's distance from (You): {c_dist}")
        
    elif 8 < d10 :
        print(f"    Cerberus's right head gets distracted by {distractions[d20]}.")
        print(f"    ...before he forgets where he is entirely! (\033[1;37mщ\033[0m) (?) ({dog})")
        
        under = ground[current_row][current_col]
        del dog[:]
        summon(ver, hor, "\033[1;37mщ\033[0m", dog)
        board[current_row][current_col] = under
        
        canine_ring = [[-1 for _ in range(hor)] for _ in range(ver)]
        cpos = [] 
        ring_mapper(ver, hor, cpos, dog, canine_ring, symbols)
        player_to_dog = [] 
        player_to_dog.append([you[0], you[1]]) 
        c_dist = canine_ring[you[0]][you[1]] 
        c_dist = int(c_dist)
        
        print(f"    Cerberus's distance from (You): {c_dist}")

########################################################################
# THE MASTER LOOP

def master():
    topsoil(a,b)
    detectLen(a,b)
    adjust(a,b,c)
    spawn(a,b,c)
    rules()
    while True:
        world(a,b,d)
        print(f"    You are currently standing at {you}")
        move(a,b,c,d)
        win()
        
        if victory == True:
            world(a,b,d)
            print("    ===YOU WIN===")
            playAgain()
            if replay == False:
                input("    Alright, press enter to close game.")
                break
            elif replay == True:
                purge(a,b,c)
                spawn(a,b,c)
        
        # John B. Treyl's Turn
        if defeat == False:
            chase(a, b, forest)
            print(f"    John's distance from (You): {j_dist}")
            print()
        if defeat == True:
            world(a,b,d)
            print("    ===YOU LOSE===")
            playAgain()
        
        # Doppelganger's Turn
        if defeat == False:
            intercept(a,b,forest)
        if defeat == True:
            world(a,b,d)
            print("    ===YOU LOSE===")
            playAgain()
            
        # Bloody Mary's Turn
        if defeat == False:
            haunt(a,b)
        if defeat == True:
            world(a,b,d)
            print("    ===YOU LOSE===")
            playAgain()
        
        # Cerberus's Turn
        if defeat == False:
            encounter(a,b)
        if defeat == True:
            world(a,b,d)
            print("    ===YOU LOSE===")
            playAgain()
            
            if replay == False:
                input("    Alright, press enter to close game.")
                break
            elif replay == True:
                purge(a,b,c)
                spawn(a,b,c)
        
master()
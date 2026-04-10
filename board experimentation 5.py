from random import randrange
from random import randint

# def display_board(board):
# 	print("+-------" * 3,"+", sep="")
# 	for row in range(3):
# 		print("|       " * 3,"|", sep="")
# 		for col in range(3):
# 			print("|   " + str(board[row][col]) + "   ", end="")
# 		print("|")
# 		print("|       " * 3,"|",sep="")
# 		print("+-------" * 3,"+",sep="")

# 12x12 grid, squares all seperated, randomly either commas or periods
# for x in range (12):
#     print("")
#     print("+---" * 12, "+", sep="")
#     for y in range (12):
#         a = randint (0, 1)
#         if a == 1:
#             print("| , ", end="")
#         else:
#             print("| . ", end="")
#     print("|", end="")
# print("")
# print("+---" * 12, "+", sep="")

###############################################

# # Modular enclosed ascii board
# 
# a = 12 # vertical
# b = 14 # horizontal
# 
# print("+", "-" * b, "+", sep="", end="")
# for x in range (a):
#     print("")
#     print("|", end="")
#     for y in range (b):
#         z = randint (0, 1)
#         if z == 1:
#             print(",", end="")
#         else:
#             print(".", end="")
#     print("|", end="")
# print("")
# print("+", "-" * b, "+", sep="")

###############################################

# Modular grid that equalizes spacing of displayed index

a = 9		# vertical
b = 19		# horizontal        
c = 0 		# max array value size
d = 0		# border adjustment

trees = (a // 2) + (b // 2)

enemies = trees // 2
        
board = [ [a * j + i + 1 for i in range(b)] for j in range(a) ]
ground = [ [" " for i in range(b)] for j in range(a) ]

betrayal = [ [" " for i in range(enemies)] for j in range(2) ]

tokens = ["@", "F", "T", "J"]

compass = { "w":0,"d":1,"a":2,"s":3, "north":0,"east":1,"west":2,"south":3, "up":0,"right":1,"left":2,"down":3}

agree		= ["y", "yes", "okay", "ok", "sure", "alright", "agree", "accept", "do", "yeah", "ok fine", "okay fine", "fine"]
disagree	= ["n", "no", "nope", "nah", "never", "stop", "quit", "exit", "don't", "disagree", "object", "protest"]

victory = False
replay = True
defeat = False

respace = []
you = []
flag = []

enemy = []

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
            
def adjust(ver, hor, area):
    for h in range(ver):
        for i in range(hor):
            value 		= board[h][i]
            square		= value
            square = str(square)
            list(square)
            space		= area - len(square)
            square = "".join(square)
            y = (" " * space, square)
            y = "".join(y)
            respace.append(y)
            squareSpace	= respace[i]
            board[h][i] = squareSpace
        del respace[:]

def world(ver, hor, bord):
    print("+-", "-" * hor * bord, "+", sep="", end="")
    for x in range (ver):
        print("")
        print("| ", end="")
        for y in range (hor):
            print(board[x][y], " ", sep="", end="")
        print("|", end="")
    print("")
    print("+-", "-" * hor * bord, "+", sep="", end="")
    print("")
    
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
    
def spawn(ver, hor):
    global you, flag, enemy
    a = randint(0,ver-1)
    b = randint(0,hor-1)
    board[a][b] = "@"
    you.append(a)
    you.append(b)
    
    # Flag
    while True:
        c = randint(0,ver-1)
        d = randint(0,hor-1)
        
        if c == a and d == b:
            continue
        else:
            board[c][d] = "F"
            flag.append(c)
            flag.append(d)
            break
    
    # Trees
    t = 0
    while t != trees:
        c = randint(0,ver-1)
        d = randint(0,hor-1)
        e = board[c][d]
        
        if e != "@" and e != "F" and e != "T":
            board[c][d] = "T"
            t += 1
            
#     # Enemies plural (unfinished)
#     t = 0  
#     while len(betrayal) != enemies:
#         c = randint(0,ver-1)
#         d = randint(0,hor-1)
#         e = board[c][d]
#         if e not in tokens:
#             board[c][d] = "J"
#             counter += 1
#             betrayal[0][t] = c
#             betrayal[1][t] = d
    
    # For just one enemy
    while True:
        if e != "@" and e != "F" and e!= "T":
            board[c][d] = "J"
            enemy.append(c)
            enemy.append(d)
            break

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

def rules():
    print(
        """
    +================================+
    | "@" is (You).                  |
    | "F" the flag of the enemy,     |
    | acquiring it is your reason    |
    | for being.                     |
    | "T" are the forest's trees     |
    | blocking your path.            |
    | "J" are the enemies men, you   |
    | must avoid them at all costs!  |
    | Input the direction you want   |
    | to move to reach the end.      |
    | a=left, w=up, s=down, d=right  |
    +================================+
          """)

def move(ver, hor, bord):
    global defeat
    while True:
        x = input("Which direction? (North, South, East or West)\n")
        x = translate(x)
        y = you[0]
        z = you[1]
        q = ground[y][z]
        
        try:
            # north
            if x == 0 and 0 <= y-1 < len(board) and 0 <= z < len(board[0]):           
                
                if board[y-1][z] != "T" and board[y-1][z] != "J":
                    me = you[0]
                    me = me - 1
                    you[0] = me
                    board[y][z] = q
                    board[y-1][z] = "@"
                    break
                
                elif board[y-1][z] == "T":
                    print("A sturdy tree blocks your path.")
                
            # east
            elif x == 1 and 0 <= y < len(board) and 0 <= z+1 < len(board[0]):     
                
                if board[y][z+1] != "T" and board[y][z+1] != "J":
                    me = you[1]
                    me = me + 1
                    you[1] = me
                    board[y][z] = q
                    board[y][z+1] = "@"
                    break
                
                elif board[y][z+1] == "T":
                    print("A sturdy tree blocks your path.")
            
            # west
            elif x == 2 and 0 <= y < len(board) and 0 <= z-1 < len(board[0]):
                if board[y][z-1] != "T" and board[y][z-1] != "J":                  
                    me = you[1]
                    me = me - 1
                    you[1] = me
                    board[y][z] = q
                    board[y][z-1] = "@"
                    break
                
#                 elif board[y][z-1] != "J":
#                     defeat = True:
#                     print = 
                
                elif board[y][z-1] == "T":
                    print("A sturdy tree blocks your path.")
                
            #south
            elif x == 3 and 0 <= y+1 < len(board) and 0 <= z < len(board[0]):         
                if board[y+1][z] != "T" and board[y+1][z] != "J":                
                    me = you[0]
                    me = me + 1
                    you[0] = me
                    board[y][z] = q
                    board[y+1][z] = "@"
                    break
                
                elif board[y+1][z] == "T":
                    print("A sturdy tree blocks your path.")
                
            # North - out of bounds (works)
            elif x == 0 and y-1 < 0:
                print("That would be outside the board.")
                
            # South - out of bounds (works)
            elif x == 3 and y+1 > (len(board)-1):
                print("That would be outside the board.")
                
            # East - out of bounds (works)
            elif x == 1 and z+1 > (len(board[0])-1):
                print("That would be outside the board.")
                
            # West - out of bounds (works)
            elif x == 2 and z-1 < 0:
                print("That would be outside the board.")
                           
        except:
            print("Invalid move, try again.\n")

def enemyNorth(ver, hor, under):
    global enemy, defeat
    john = enemy[0]
    john = john - 1
    enemy[0] = john    
    board[ver][hor] = under
    if board[ver-1][hor] == "@":
        print("You have been slain by your pursuer...")
        defeat = True
    else:
        print("Your adversary approaches... (N)")
    board[ver-1][hor] = "J"
    
def enemyEast(ver, hor, under):
    global enemy, defeat
    john = enemy[1]
    john = john + 1
    enemy[1] = john
    board[ver][hor] = under
    if board[ver][hor+1] == "@":
        print("You have been slain by your pursuer...")
        defeat = True
    else:
        print("Your adversary approaches... (E)")
    board[ver][hor+1] = "J"

def enemyWest(ver, hor, under):
    global enemy, defeat
    john = enemy[1]
    john = john - 1
    enemy[1] = john
    board[ver][hor] = under
    if board[ver][hor-1] == "@":
        print("You have been slain by your pursuer...")
        defeat = True
    else:
        print("Your adversary approaches... (W)")
    board[ver][hor-1] = "J"
    
def enemySouth(ver, hor, under):
    global enemy, defeat
    john = enemy[0]
    john = john + 1
    enemy[0] = john
    board[ver][hor] = under
    if board[ver+1][hor] == "@":
        print("You have been slain by your pursuer...")
        defeat = True
    else:
        print("Your adversary approaches... (S)")
    board[ver+1][hor] = "J"


def chase():
    global enemy, defeat
    while True:
        b = enemy[0]
        c = enemy[1]
        y = you[0]
        z = you[1]
        q = ground[b][c]
        
        try:
            # north
            if b > y and board[b-1][c] != "T" and board[b-1][c] != "F":
                enemyNorth(b,c,q)
                break
            # east
            elif z > c and board[b][c+1] != "T" and board[b][c+1] != "F":
                enemyEast(b,c,q)
                break
            # west
            elif z < c and board[b][c-1] != "T" and board[b][c-1] != "F":
                enemyWest(b,c,q)
                break
            # south
            elif b < y and board[b+1][c] != "T" and board[b+1][c] != "F":
                enemySouth(b,c,q)
                break
            # emergency
            else:
                while True:
                    huh = []
                    if board[b-1][c] != "T" and board[b-1][c] != "F" and 0 <= b-1 < len(board) and 0 <= c < len(board[0]):
                        huh.append(0)
                    if board[b][c+1] != "T" and board[b][c+1] != "F" and 0 <= b < len(board) and 0 <= c+1 < len(board[0]):
                        huh.append(1)
                    if board[b][c-1] != "T" and board[b][c-1] != "F" and 0 <= b < len(board) and 0 <= c-1 < len(board[0]):
                        huh.append(2)
                    if board[b+1][c] != "T" and board[b+1][c] != "F" and 0 <= b+1 < len(board) and 0 <= c < len(board[0]):
                        huh.append(3)
                        
                    why = len(huh)-1
                    how = randint(0, why)
                    idk = huh[how]
                    idk = int(idk)
                    
                    if idk == 0:
                        enemyNorth(b,c,q)
                        break
                    elif idk == 1:
                        enemyEast(b,c,q)
                        break
                    elif idk == 2:
                        enemyWest(b,c,q)
                        break
                    elif idk == 3:
                        enemySouth(b,c,q)
                        break
                    else:
                        print("Your pursuer has been flummoxed, you are free.")
                        break
        except:
            continue
        
def win():
    global victory
    a = you[0]
    b = you[1]
    c = flag[0]
    d = flag[1]
    if a == c and b == d:
        victory = True
        
def playAgain():
    global replay, victory, defeat
    while True:
        a = input("Would you like to play again?\n")
        if a in agree:
            print("Alright, regenerating the map.\n")
            replay = True
            victory = False
            defeat = False
            break
        elif a in disagree:
            replay = False
            break
        else:
            print("Didn't quite catch that.\n")
            
def purge(ver, hor, area, bord):
    del you[:]
    del flag[:]
    del enemy[:]
    del board[:][:]
    del ground[:][:]
    
    topsoil(a,b)
    detectLen(a,b)
    adjust(a,b,c)
    spawn(a,b)
    rules()

def master():
    topsoil(a,b)
    detectLen(a,b)
    adjust(a,b,c)
    spawn(a,b)
    rules()
    while True:
        world(a,b,d)
        move(a,b,d)
        print(f"You: {you[0]}, {you[1]}")
        win()
        if victory == True:
            world(a,b,d)
            print("===YOU WIN===")
            playAgain()
            if replay == False:
                input("Alright, press enter to close game.")
                break
            elif replay == True:
                purge(a,b,c,d)
        chase()
        print(f"Enemy: {enemy[0]}, {enemy[1]}")
        if defeat == True:
            world(a,b,d)
            print("===YOU LOSE===")
            playAgain()
            if replay == False:
                input("Alright, press enter to close game.")
                break
            elif replay == True:
                purge(a,b,c,d)
        
master()
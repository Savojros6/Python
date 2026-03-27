from random import randint
secret_number = randint (1, 10)
counter 		= 0

# Lists for strings the script is intended to be able to respond to.

agree		= [ "y", "yes", "okay", "ok", "sure", "alright", "agree", "accept", "do", "yeah", "ok fine", "okay fine"]
disagree	= [ "n", "no", "nope", "nah", "never", "stop", "quit", "exit", "don't", "disagree"]
explicit	= ["fuck you", "kys", "gay", "bitch", "bitche", "kill yourself", "go fuck yourself", "i hate you"]
funny		= ["67"]

# This list tracks your previous guesses, prevents duplicates from
# incrementing the counter.

prevGuess	= []

# These variables will only come into play in the event I get
# The ability to choose whether or not you want to replay the
# game at the end working. They are currently unused.

consent 		= 0
victory 		= False
secretJewels 	= 0

# This is just the function that plays when the player actually wins or loses.
# Its intended to clear prevGuess and reset the counter in the event the user
# replays the number game.

def gameOver():
    print(f'Previous guesses: {prevGuess}')
    del prevGuess[:]
    counter = 0

print(
"""
+================================+
| Welcome to my game, mortal!    |
| Enter an integer number        |
| and guess what number I've     |
| picked for you.                |
| The number is between 1 and 10.|
| But you only get 3 guesses!    |
| If you win, you get some of my |
| Secret Jewels, but if you lose,|
| you DIE to my MAJYKK >:)       |
| So, care to play my game?      |
+================================+
""")

# The requirement that you consent to the wizards game
# was implemented so that there would be a choice that preceded
# the loop of the game. The idea is that if I define the loop of the entire game
# into a function initiated as a result of a choice preceding the game
# I might be able to get the replayability of the game working?
# This is probably the right idea but I havent worked out the specifics yet.

while True:
    consent = input("Play the wizards game?: ")
    if consent in agree:
        print("""
+================================+
| Great, now, what is your first |
| guess mortal? >:)              |
+================================+
        """)
        break
    
    elif consent in disagree:
        print("""
+================================+
| WRONG, TRY AGAIN DUMBASS >:(   |
+================================+
        """)
        
    else:
        print("""
+================================+
| Speak Normal EDIOT >:(         |
+================================+
        """)

# This is the section where it responds to strings in lists it has responses too.

while True:
    try:
        guess = input("Guess a number: ").strip()
        # .strip() removes extra spaces from the input.
        # not from the center though, only leading and trailing.
        
        # .lower() takes whatever the input actually is.
        # then converts it to entirely lowercase.
        # It's helpful when looking for specific strings.
        
        if guess.lower() in disagree:
            print("""
+================================+
| Stupid BITCHE... Guess your    |
| number... Before I draw my     |
| bladde..."                     |
+================================+
        """)
            continue
        
        elif guess.lower() in agree:
            print("""
+================================+
| Ver naisu. Now, let's begin! :)|
+================================+
        """)
            continue
        
        elif guess.lower() in explicit:
            print("""
+================================+
| wtfug! mean!!! D:              |
+================================+
        """)
            continue
        
        elif guess in funny:
            print("""
+================================+
| You've posted CRINGE mortal... |
| You are UNWORTHY of my game... |
| DIE...                         |
+================================+
        """)
            print("You have been cut down by the wizards kata anna...")
            gameOver()
            break
                
        # The reason this has to end w/ 'elif' and not 'else' is I think 'else' can't have conditions?
        
    except ValueError:
        continue

    try:
        guess = int(guess)

# I thought it'd be nice to acknowledge if you ruined the wizards game by guessing it immediately.

        if guess == secret_number and counter == 0:
            prevGuess.append(guess)
            print("""
+================================+
| Gadzooks! How could you have   |
| known the Legendary Secret     |
| Number already?! You MUST have |
| cheated!                       |
+================================+
        """)             
            print("The wizard malds impotently as he slowly transmogrifies into a corn cob.")
            gameOver()
            victory = True
            break
        
        elif guess == secret_number and counter > 0:
            prevGuess.append(guess)
            print("""
+================================+
| Argh, drats! Curse you mortal, |
| now I shall disintegrate into  |
| comsic ash! AAAAAAAAAAAAAAAAAAA|
+================================+
        """)                        
            print("You have killed the wizard...")
            gameOver()
            victory = True
            break
        
        elif counter == 2 and guess != secret_number:
            prevGuess.append(guess)
            print("""
+================================+
| Too late FOOL, you LOSE!       |
| Prepare to face my OMEGA       |
| BEANS!!!                       |
+================================+
        """)
            print("You were disintegrated by the wizards majykks...")
            gameOver()
            break

# This is mostly so that repeat guesses can't increment the counter.

        elif guess in prevGuess:
            print("""
+================================+
| You already SAID that one! >:( |
+================================+
        """)
        
# This was something already covered by other parts of the cascade
# but I thought it was something that deserved its own response.
            
        elif guess <= 0 or guess >= 11:
            print("""
+================================+
| FOOLE, it OBVIOUSLY can't be   |
| that one! Are you even listen- |
| -ing to me?!                   |
+================================+
        """)
            prevGuess.append(guess)

# The original idea that prompted me to keep developing this script was that
# the original example code for this would just loop until you said '777'
# which I don't think qualifies as a game. So I made it 3 tries, within
# the range of 1 and 10, and it tells you higher or lower. Which makes it
# an incredibly lame game, but it makes it a game.

# It might be funny if the wizard calls you stupid if you guess higher
# after he already told you to guess lower or vice versa.

# The wizard should totally accuse you of being a metafag if you
# guess 5 or 6 first.

        elif guess > secret_number:
            print("""
+================================+
| Too high mortal, guess again!  |
+================================+
        """)            
            prevGuess.append(guess)
            counter += 1
            
        elif guess < secret_number:
            print("""
+================================+
| Too low mortal, guess again!   |
+================================+
        """)       
            prevGuess.append(guess)
            counter += 1

# I genuinely can't think of a way to trigger this condition, but I guess thats the point.

        else:
            print("???")

# If the input isn't a number or a string the loop can respond to this is what you get.

    except ValueError:        
            print("""
+================================+
| Foolish mortal! That's not even|
| a real number! Try again!!!    |
+================================+
        """)   
    
# ====================================================================#
# 'try' and 'except' are an exception handling mechanism.             |
# 'try' attempts to run subsequent code, but if it fails              |
# instead of the whole program failing, it immediately                |
# executes the corresponding 'except' conditions instead.             |
# It has to be formatted kind of like an else/if statement.           |
#                                                                     |
# 'ValueError' is a built-in exception class in Python.               |
# It is raised when a function or operation receives an argument      |
# of the correct type but with an inappropriate value.                |
# e.g. attempting to turn a string into an integer when it can't be.  |
#                                                                     |
# 'ValueError' being there isn't actually necessary its just clearer. |
# ====================================================================#   

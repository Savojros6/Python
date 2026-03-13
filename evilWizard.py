from random import randint
secret_number = randint (1, 10)
counter = 0

agree		= ["yes", "okay", "ok", "sure", "alright", "agree", "accept", "do", "yeah"]
disagree	= ["no", "nope", "nah", "never", "stop", "quit", "exit", "don't", "disagree"]
explicit	= ["fuck you", "kys", "gay", "bitch", "kill yourself", "go fuck yourself"]
prevGuess	= []

print(
"""
+================================+
| Welcome to my game, muggle!    |
| Enter an integer number        |
| and guess what number I've     |
| picked for you.                |
| The number is between 1 and 10.|
| But you only get 3 guesses!    |
| So, what is the secret number? |
+================================+
""")

while True:
    try:
        guess = input("Guess a number: ").strip()
        # .strip() removes extra spaces from the input.
        # not from the center though, only leading and trailing.
        
        # .lower() takes whatever the input actually is.
        # then converts it to entirely lowercase.
        # It's helpful when looking for specific strings.
        
        if guess.lower() in disagree:
            print("Stupid BITCHE... Guess your number... Before I draw my bladde...")
            continue
        
        elif guess.lower() in agree:
            print("Ver naisu. Now, let's begin! :)")
            continue
        
        elif guess.lower() in explicit:
            print("wtfug! mean!!!")
            continue
                
        # The reason this has to end w/ 'elif' and not 'else' is I think 'else' can't have conditions?
        
    except ValueError:
        continue

    try:
        guess = int(guess)
        
        if guess == secret_number and counter == 0:
            print('"Gadzooks! How could you have know the Legendary Secret Number already?! You MUST have cheated!"\n"The wizard malds as he slowly transmogrifies into a corn cob"')
            break
        
        elif guess == secret_number and counter > 0:
            print('"Argh, drats! Curse you mortal, now I shall disintegrate into comsic ash! AAAAAAAAA"\nYou have killed the wizard...')
            break
        
        elif counter == 2 and guess != secret_number:
            print('"Too late FOOL, you LOSE! Prepare to face my OMEGA BEANS!!!"\nYou were disintegrated by the wizards majykks...')
            break
        
        elif guess in prevGuess:
            print("You already SAID that one!! >:(")
        
        elif guess > secret_number:
            print("Too high muggle, guess again!")
            prevGuess.append(guess)
            counter += 1
            
        elif guess < secret_number:
            print("Too low muggle, guess again!")
            prevGuess.append(guess)
            counter += 1
        
        else:
            print("???")
            
    except ValueError:
        print("Foolish muggle! That's not even a real number! Try again!!!")        

# It would be nice if it prompted you to try again.
    
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

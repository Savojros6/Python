from random import randint
secret_number = randint (1, 10)
counter = 0

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
        guess = int(input("Guess a number: "))
        if guess == secret_number and counter == 0:
            print('"Gadzooks! How could you have know the Legendary Secret Number already?! You MUST have cheated!"\n"The wizard malds as he slowly transmogrifies into a corn cob"')
            break
        elif guess == secret_number and counter > 0:
            print('"Argh, drats! Curse you mortal, now I shall disintegrate into comsic ash! AAAAAAAAA"\nYou have killed the wizard...')
            break
        elif counter == 2 and guess != secret_number:
            print('"Too late FOOL, you LOSE! Prepare to face my OMEGA BEANS!!!"\nYou were disintegrated by the wizards majykks...')
            break
        elif guess > secret_number:
            print("Too high muggle, guess again!")
            counter += 1
        else:
            print("Too low muggle, guess again!")
            counter += 1
    except ValueError:
        print("Foolish muggle! That's not even a real number! Try again!!!")
        
# It would also be desirable to add the ability to account for certain
# special strings, ie; saying no and refusing to play.

# It would be nice if the wizard refused to accept guesses of the same number multiple times.
    
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

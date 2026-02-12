from random import randint
secret_number = randint (1, 10)

# I don't fully understand random, but randint allows me to generate a random integer in a range.

print(
"""
+================================+
| Welcome to my game, muggle!    |
| Enter an integer number        |
| and guess what number I've     |
| picked for you.                |
| So, what is the secret number? |
+================================+
""")

# 'try' and 'except' are an exception handling mechanism.
# 'try' attempts to run subsequent code, but if it fails
# instead of the whole program failing, it immediately
# executes the corresponding 'except' conditions instead.
# It has to be formatted kind of like an else/if statement.

# 'ValueError' is a built-in exception class in Python.
# It is raised when a function or operation receives an argument
# of the correct type but with an inappropriate value.
# e.g. attempting to turn a string into an integer when it can't be.

# 'ValueError' being there isn't actually necessary its just clearer.

while True:
    try:
        guess = int(input("Guess a number: "))
        break
    except ValueError:
        print("Foolish muggle! That's not even a real number! Try again!!!")
    
while guess != secret_number:
    if guess > secret_number:
        print("Too high muggle, guess again!")
        guess = int(input("Guess a number: "))
    else:
        print("Too low muggle, guess again!")
        guess = int(input("Guess a number: "))
        
print('"Argh, drats! Curse you mortal, now I shall disintegrate into comsic ash! AAAAAAAAA"\nYou have killed the wizard...')

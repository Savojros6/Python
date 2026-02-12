import random
secret_number = random.randint (1, 10)

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

guess = int(input("Guess a number: "))

while guess != secret_number:
    if guess > secret_number:
        print("Too high muggle, guess again!")
        guess = int(input("Guess a number: "))
    else:
        print("Too low muggle, guess again!")
        guess = int(input("Guess a number: "))
        

print('"Argh, drats! Curse you mortal, now I shall disintegrate into comsic ash! AAAAAAAAA"\nYou have killed the wizard...')

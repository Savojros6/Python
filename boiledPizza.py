# Create a list of at least five ingredients
# Use a for loop to:
# Print a preparation instruction for each ingredient
# Use a second loop to:
# Modify each ingredient to include the word "prepared"
# Print the final list
# Add a while loop that simulates a cooking countdown from 3

import time

ingred = ["tomato", "mushroom", "cheese", "pepperoni", "pineapple"]

i = 0

def prepare():
    global i
    time.sleep(1)
    for seconds in range(1, 4):
        print(f"{seconds} seconds.")
        time.sleep(1)
    print(f"Prepared {ingred[i]}.")
    i += 1
    time.sleep(1)
    
# Without the words 'global i', this code will break
# The reason it breaks is it decides i is local to the function
# due to the 'i += 1' line. Preventing it from reading and writing
# to the globally declared 'i' variable already declared.

while True:
    if i == 0:
        print(f"First, we boil {ingred[i]} into the soup.")        
        prepare()
    elif i > 0 and i < len(ingred):
        print(f"Then we boil {ingred[i]} into the soup.")
        prepare()
    elif i == len(ingred) - 1:
        print(f"Finally, we boil {ingred[i]} into the soup.")
        prepare()
    else:
        print("Mama mia, don't you just love authentic italian cuisine?")
        break

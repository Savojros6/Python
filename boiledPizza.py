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

while i < 99:
    if i == 0:
        print(f"First, we boil {ingred[i]} into the soup.")
        time.sleep(1)
        for seconds in range(1, 4):
            print(f"{seconds} seconds.")
            time.sleep(1)
        print(f"Prepared {ingred[i]}.")
        i += 1
        time.sleep(1)
    elif i > 0 and i < len(ingred):
        print(f"Then we boil {ingred[i]} into the soup.")
        time.sleep(1)
        for seconds in range(1, 4):
            print(f"{seconds} seconds.")
            time.sleep(1)
        print(f"Prepared {ingred[i]}.")
        i += 1
        time.sleep(1)
    elif i == len(ingred) - 1:
        print(f"Finally, we boil {ingred[i]} into the soup.")
        time.sleep(1)
        for seconds in range(1, 4):
            print(f"{seconds} seconds.")
            time.sleep(1)
        print(f"Prepared {ingred[i]}.")
        i += 1
        time.sleep(1)
    else:
        print("Mama mia, don't you just love authentic italian cuisine?")
        break

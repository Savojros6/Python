# Create a list of at least five ingredients
# Use a for loop to:
# Print a preparation instruction for each ingredient
# Use a second loop to:
# Modify each ingredient to include the word "prepared"
# Print the final list
# Add a while loop that simulates a cooking countdown from 3

ingred = ["tomato", "mushroom", "cheese", "pepperoni", "pineapple"]
prep = "prepared"

i = 0
i2 = 0

while i == 0:
    if i2 < 5:
        print(f"first we boil {ingred[i2]} into the soup")
        i2 += 1
    else:
        break

for i in range(0, len(ingred)):
    print(prep, ingred[i])
    i += 1
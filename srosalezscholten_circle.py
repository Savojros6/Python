#I don't believe that netacad told me how to input Pi into Python, so I looked it up.
from math import pi
#It's my understanding doing this instead of "import math" is cleaner because I only need pi and not the other stuff it does.

# Just a test

# print(f"π ≈ {pi:.10f}")   # π ≈ 3.1415926536

# Also, Netacad.com instructions on how to comment out multiple lines are incorrect in Thonny.
# It's actually alt+3 and alt+4 to comment/uncomment

print("This is a program that calculates the area and circumference of a circle.")

radius			= float(input("Enter the radius: "))

# I was already aware of importing functions from my attempts to learn C++
# That being said, I don't exhaustively know what can be imported or what those functions do.

area			= pi * radius ** 2
circumference	= 2 * pi * radius

# I also looked up the fstring thing, apparently it's more efficient?
# I'm going to use it, but I hope that's not defeating the point of anything.
# I'd imagine the other ways of writing strings are important to learn for their own reasons.
# However it seems ideal in this case and I already had to look up one thing on my own.

print(f"The area of your circle is {area}.")
print(f"The circumference of your circle is {circumference}.")

# Obviously, if this were well coded, it would need a way of avoiding failure in the event the user inputs letters or special characters.
# But idk how to do that, I could look up how to do that, but then we start getting a bit too chinese room about this.
# And it risks me no longer understanding what my code is doing lmao.



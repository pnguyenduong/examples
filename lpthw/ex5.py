"""
	Example using "format string" 
"""

name = "Phong Nguyen Duong"
age = 27 # not a lie 
height = 172 # centimeter
weight = 70 # lbs
eyes = "Black"
teeth = "White"
hair = "Black"

print(f"Let's talk about {name}.")
print(f"He's {height} meters tall.")
print(f"He's {weight} pounds heavy.")
print("Actually that's not too heavy.")
print(f"He's got {eyes} eyes and {hair} hair.")
print(f"His teeth are usually {teeth} depending on the coffee.")

# this line is tricky, try to get it exactly right
total =  age + height + weight
print(f"If I add {age}, {height}, and {height} I get {total}.")
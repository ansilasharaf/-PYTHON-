import math
from pack_main import rect
from pack_main import circle
from pack_main.pack_sub import cuboid
from pack_main.pack_sub import sphere

# Prompt the user for input
length = float(input("Enter the length of the rectangle: "))
width = float(input("Enter the width of the rectangle: "))
height = float(input("Enter the height of the cuboid: "))
radius = float(input("Enter the radius of the circle and sphere: "))

# Rectangle calculations
print("Area and perimeter of rectangle:")
print("Area:", length * width)
print("Perimeter:", 2 * (length + width))

# Circle calculations
print("Area and perimeter of circle:")
print("Area:", math.pi * radius ** 2)
print("Perimeter (Circumference):", 2 * math.pi * radius)

# Cuboid calculations
print("Surface Area and Volume of cuboid:")
print("Surface Area:", 2 * (length * width + length * height + width * height))
print("Volume:", length * width * height)

# Sphere calculations
print("Surface Area and Volume of sphere:")
print("Surface Area:", 4 * math.pi * radius ** 2)
print("Volume:", (4 / 3) * math.pi * radius ** 3)

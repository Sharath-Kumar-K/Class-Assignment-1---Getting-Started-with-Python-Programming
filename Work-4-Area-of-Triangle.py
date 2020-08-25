"""
Modify the program of Project 4 to compute the area of a triangle. Issue
the appropriate prompts for the triangle’s base and height, and change
the names of the variables appropriately. Then, use the formula
.5 * base * height to compute the area. Test the program from
an IDLE window.
"""

base = int(input("Enter the base of Triangle: "))
height = int(input("Enter the height of Triangle: "))

if base<=0 or height<=0 : print("Base or Hight of Triangle can have only positive values!!!!!")
else:
    area = 0.5 * base * height
    print("The area is", area, "square units")


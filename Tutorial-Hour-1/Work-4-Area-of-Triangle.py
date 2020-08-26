"""
Write a Python code to Calculate the Area of a Triangle
"""

base = float(input("Enter the base of triangle : "))
height = float(input("Enter the height of triangle : "))
if base<=0.0 or height<=0.0 : print("Base or Height of triangle cannot have zero or negative values!!!!")

else:
    area = base * height
    print(f"Area of triangle is {area} sq.unit.")

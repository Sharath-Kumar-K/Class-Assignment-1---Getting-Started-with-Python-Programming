"""
Write and test a program that computes the area of a circle. This pro-
gram should request a number representing a radius as input from the

user. It should use the formula 3.14 * radius ** 2 to compute the
area, and output this result suitably labeled.
"""

radius = float(input("Enter the radius of Circle: "))
if radius<=0 : print("Radius of Circle cannot have zero or negative!!!!")
else:
    area = 3.14 * (radius ** 2)
    print("Area of circle is ", area)


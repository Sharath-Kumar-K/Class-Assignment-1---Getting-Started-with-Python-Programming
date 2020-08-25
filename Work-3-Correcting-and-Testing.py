"""
Open an IDLE window, and enter the program from Figure 1.7 that
computes the area of a rectangle. Load the program into the shell by
pressing the F5 key, and correct any errors that occur. Test the program
with different inputs by running it at least three times.
"""

width = int(input("Enter the width: "))
height = int(input("Enter the height: "))

if width<=0 or height<=0 : print("Width or Hight of rectangle can have only positive values!!!!!")
else:
    area= width * height
    print("The area is", area, "square units")

"""
Test 1 :
    Enter the width: 34
    Enter the height: 43
    The area is 1462 square units
Test 2 :
    Enter the width: 0
    Enter the height: 33
    Width or Hight of rectangle can have only positive values!!!!!
Test 3 :
    Enter the width: -13
    Enter the height: 64
    Width or Hight of rectangle can have only positive values!!!!!
"""

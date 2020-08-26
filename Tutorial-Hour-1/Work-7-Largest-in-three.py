"""
Write a Python code to Find the Largest Among Three Numbers
"""
n1 = int(input("Enter number 1: "))
n2 = int(input("Enter number 2: "))
n3 = int(input("Enter number 3: "))

if n1>n2 and n1>n3 : print(f"{n1} is Lagest number.")
elif n2>n3 : print(f"{n2} is Lagest number.")
else : print(f"{n3} is Lagest number.")



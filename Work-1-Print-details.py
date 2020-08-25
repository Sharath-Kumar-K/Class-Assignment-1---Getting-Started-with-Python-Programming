"""
Question : Write a Python program that prints (displays) your name, address, and
telephone number.
"""

name = input("Enter your name : ")
print("Enter Your ADDRESS\n")
house = input("House : ")
post = input("Post : ")
via = input("Via : ")
dist = input("District : ")
pin = input("Pin : ")
phone = input("Phone : ")

print("\n\nPrinting your details....\n")
print(f"Name   \t\t:{name}")
print(f"Address\t\t:{house}(H)\n",
        f"\t\t {post}(P.O)\n",
        f"\t\t {via}(Via)\n",
        f"\t\t {dist}\n",
        f"\t\t PIN   : {pin}\n",
        f"\t\t Phone : {phone}\n"
        )


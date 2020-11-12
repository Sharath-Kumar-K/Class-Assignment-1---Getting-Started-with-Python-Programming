"""
Question :
    Write a program to read numbers sorted in one file and store the sorted numbers in
 another file after deleting duplicates.
"""
sorted_numbers = []
with open("sorted.dat", "r") as sorted :
    loop = True
    while loop :
        num = sorted.readline()
        if not num :
            loop = False
        else:
            num = int(num)
            if num not in sorted_numbers :
                sorted_numbers.append(num)

with open("sorted_without_duplicate.dat", "w") as nodupl :
    for i in sorted_numbers :
        store = str(i)+"\n"
        nodupl.write(store)
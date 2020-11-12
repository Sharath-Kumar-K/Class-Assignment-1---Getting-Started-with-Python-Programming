"""
Question :
    Write a Python code to read a text file, copy the contents to another file after
removing the blank lines.
"""
tmp = []
with open("file1.dat", "r") as file :
    data = file.read()
    if data is "" :
        print("The file is empty.")
    else :
        lines = data.split("\n")
        for line in lines :
            if line == "" :
                continue
            else :
                tmp.append(line+"\n")
    with open("stripped-file.dat", "w") as sfile :
        for i in tmp :
            # data = data + "\n"
            sfile.write(i)
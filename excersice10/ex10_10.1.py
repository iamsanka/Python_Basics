import os.path
#name of the text file needs to be created
filename="name.txt"
name=input("Enter your Name : ")
#while the length of the input is greater than 0 loop will continue
while len(name)> 0:
    if(os.path.exists(filename)) :
        file=open(filename, "a")
        file.write("\n"+name)
    else :
        file=open(filename, "w")
        file.write(name)
    name=input("Enter your Name : ")

file.close()

#read the file
lines=[""]
file=open(filename,"r")
lines=file.readlines()

print(lines)
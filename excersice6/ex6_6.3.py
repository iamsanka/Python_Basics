#Get names as input then show how many names are there and the output

name=input("Enter student name : ")
names=[]

#adding names to the list untill a blank input comes
while len(name) > 0 :
    names.append(name)
    name=input("Enter student name : ")

#setting the output
output=''
#reading the each name and set to output string and separate them in commas 
for name in names :
    output += name + ","

#delete the last comma in output string and replace it with blank
output = output[:-1]
output += ''

print("Student Count : ",len(names))
print(output)

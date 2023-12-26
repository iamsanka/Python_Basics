#Ask the name and print excersice
fName=input("Enter First Name : ")
lName=input("Enter Last Name : ")

#get the fName length
fname_length=len(fName)

#initialize the fnameOutput
fnameOutput=''
#loopin the first letter of the fname to the output
while fname_length > 0 :
    fnameOutput += fName[0]
    fname_length = fname_length-1

#getting the length of the lName
lName_length=len(lName)
#Declare the lName Output
lnameOutput=''
#looping to get the out put from last to first 
while lName_length > 0 :
    lnameOutput += lName[lName_length-1]
    lName_length = lName_length - 1

#Displaying the output 
print(fnameOutput+" "+lnameOutput)
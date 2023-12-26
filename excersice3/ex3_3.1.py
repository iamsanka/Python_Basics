#program about persons age
age=input("How old are you? ")

#Checking the age 
if int(age)<13 :
    print("Child")
elif int(age)<=19 :
    print("Teen")
elif int(age)<=65 :
    print("Adult")
else :
    print("Senior")
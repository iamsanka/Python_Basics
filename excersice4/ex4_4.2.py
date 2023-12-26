#Importing Random module in python
import random

#Random lottory no generator
sets=input("How many sets of lottory numbers to generate : ")
sets=int(sets)
#Declaring the no's in a set
noInSet = 7
setOutput=[]

while sets > 0 :
    while noInSet > 0 :
        setOutput.append(random.randrange(1,40))
        noInSet = noInSet -1
        
    print(setOutput)
    setOutput=[]
    noInSet=7
    sets =sets -1


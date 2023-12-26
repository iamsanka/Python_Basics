#Compare Numbers
inp1=input("Input Integer : ")
inp2=input("Input another Integer : ")
inp3=input("One more : ")

inp1=int(inp1)
inp2=int(inp2)
inp3=int(inp3)

#compare the Integers
if inp1 > inp2 :
    if inp1 > inp3 :
        print ("Max Value : ",inp1)
    else :
        print ("Max Value : ",inp3)
else :
    if inp2 > inp3 :
        print("Max Value : ",inp2)
    else :
        print("Max Value : ",inp3)
 
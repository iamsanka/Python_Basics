#Checking the list outofbound error
list=[1,2,3,4]

try:
    list[4]=6
    print(list)
except IndexError :
    print("Index trying to modify is incorrect")

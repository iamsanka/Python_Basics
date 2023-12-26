#ski jumping results


i=1
values=[]
while 5 >= i :
    inp=int(input("Give points from judge "+str(i)+" : "))
    #Insert the input values to a list
    values.append(inp)
    i += 1

max_no=max(values)
min_no=min(values)
total_sum=sum(values)

print("Total points are : ",(total_sum-(max_no+min_no)))
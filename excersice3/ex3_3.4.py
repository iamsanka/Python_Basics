#Program to get the 5 numbers sum but only if number is greater than 0

a=input("Input Number : ")
b=input("Input Number : ")
c=input("Input Number : ")
d=input("Input Number : ")
e=input("Input Number : ")

#converting to int
a=int(a)
b=int(b)
c=int(c)
d=int(d)
e=int(e)

#declare the sum
sum=0

#condition checking
if a > 0 :
    sum=sum+a
if b > 0 :
    sum=sum+b
if c > 0 :
    sum=sum+c
if d > 0 :
    sum=sum+d
if e > 0 :
    sum=sum+e

print("Sum is : ", sum)
#making the collection with 5 strings
li=["a","b","c","d","e"]

#true loop
while True :
    indx=int(input("Insert an Index : "))
    strng=input("Enter a text : ")
    len_li=len(li)

    #in the condition is matched then show the output other wise ask again
    if(indx <= len_li):
        li.insert(indx, strng)
        break
    else :
        print("Entered index is out of the List, current length is : ",len_li)
    

print(li)

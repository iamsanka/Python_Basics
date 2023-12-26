#print the deck of cards to the console

#defining the suits
suits=["clubs","hearts","diamonds","spades"]
#defining the range of numbers
nos=[1,2,3,4,5,6,7,8,9,10,11,12,13]

#checking the lengths
suits_len=len(suits)
nos_len=len(nos)

i=0
j=0
final=[]
#now we need to loops to get the data stack
while i < suits_len:
    while j < nos_len :
        final.append(suits[i]+" "+str(nos[j]))
        j+=1
    j=0
    i+=1
    print(final)
    final=[]

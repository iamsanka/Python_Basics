#Program of bank balance

#declaring Intial Balance
initMoney=2000
print("Bank Account Balance : "+str(initMoney)+" EUR")

#Get the new adding balances
money1=input("How many euros will be added to the balance : ")
money2=input("How many cents will be added to the balance : ")

#adding the integers
money3=int(money1)+int(initMoney)

#concating the cents amount
finalBalance=str(money3)+"."+money2

#Display the final balance
print("Bank Account Balance : ", finalBalance)
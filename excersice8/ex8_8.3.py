#Program to stroe car details and print them

cars=["Skoda,ABC-123","Toyota,ABC-345","Honda,BCD-876","Volvo,KLD-9876","Ferrari,HYT-8976","Toyota,TEF-8765",
"Susuki,LMN-8765","Kia,HGT-6598","MG,OUY-0987","Hyndai,FRT-789",]

length_cars=len(cars)

#print the car details sorted with car model
cars=sorted(cars)
#Sorted with make
print("Cars sorted with Make : ") 
print(cars)

print("")

print("Cars sorted with Registration No :")
print(sorted(cars, key=lambda x: x.split(",")[-1]))

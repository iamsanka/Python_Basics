#Declaring a car class to hold car propoeties
import random

class car :
    def __init__(self, brand, model, price) :
        self.brand=brand
        self.model=model
        self.price=price

    def __str__(self) :
        return str(self.brand)+self.model+str(self.price)

    def add(self):
        return self.price

    def random():
        cars=["Audi", "BMW", "Skoda","Volvo","Ford"]
        cars=random.choice(cars)
        ran = random.randint(1000, 10000)
        return "' Brand : "+cars+" Price : ",str(ran)+" ',"

car1=car("car1 : Skoda", "Octavia", 3000)
car2=car("car2 : Audi", "A4", 4000)
car3=car("car1 : Volvo", "V70", 5000) 

#adding car price
total=car1.add()
total+=car2.add()
total+=car3.add()

collection=[]
for i in range(5):
    cars=car.random()
    collection+=cars
print(*collection)
print()

print(car1)
print(car2)
print(car3)
print("Total price is :",total)



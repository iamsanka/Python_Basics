#implement the function

def show_info():
    print("I'm utills.info")


#5.2 Subtract Function
def subtract(number1, number2):
    return number1-number2

#5.2 average function
def average(number1, number2, number3):
    avg=round(float((number1+number2+number3)/3),1)
    return avg

#5.3 calc_consumption 
def calc_consumption(dist, price, consumption):
    fuel_consumed=round((consumption/100)*dist, 2)
    cost=round(price*fuel_consumed,2)

    print("Fuel consumed : "+str(fuel_consumed)+" liters")
    print("Cost : "+str(cost))

    return fuel_consumed, cost
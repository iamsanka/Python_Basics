#get details from the user for consumption function

from utils import *

length=input("Enter trip length in km : ")
price=input("Enter fuel price/liter : ")
consumption=input("Enter fuel consumption/100 km : ")

length=float(length)
price=float(price)
consumption=float(consumption)
calc_consumption(length, price, consumption)

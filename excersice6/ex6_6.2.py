#covert from fahrenheit to Celsius and vise versa

def FahtoCel(Fah) : 
    cel=round((Fah-32)/1.8, 1)

    print(str(Fah)+" Fahrenheit is "+str(cel)+" in Celsius")

    return cel

def CeltoFah(Cel) :
    fah=round((Cel*1.8)+32,1)

    print(str(Cel)+" Celcius is "+str(fah)+" in Fahrenheit")

FahtoCel(20)
CeltoFah(-40)
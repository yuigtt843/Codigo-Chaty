def grados_Fahrenheit(Celcius):
    return (Celcius * 9/5)+32
def grados_Celcius(Fahrenheit):
    return (Fahrenheit-32)*8/9


while True:
    print("""Que conversion quiere hacer?
      1.Celcius a Fahrenheit
      2.Fahrenheit a Celsius
      3.Salir del Programa""")
    opcion=input("1 o 2?---->")
    
    if opcion == "1":
        Celcius=float(input("Ingrese su temperatura en grados Celsius"))
        print(grados_Fahrenheit(Celcius),"grados Fahrenheit")
        
    if opcion=="2":
        Fahrenheit=float(input("Ingrese su temperatura en graos Fahrenheit"))
        print(grados_Celcius(Fahrenheit),"grados Celsius")
        
    if opcion == "3":
        print("adios")
        break
    
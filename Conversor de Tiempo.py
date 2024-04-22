def segundos():
    segundos = int(input("Ingrese su cantidad en segundos: "))
    minutos = segundos / 60
    print(f"Los segundos {segundos} equivale a {minutos} en minutos")


def minutos():
    minutos = int(input("Ingrese su cantidad en minutos"))
    horas = minutos / 60
    print(f"Los minutos {minutos} equivale a {horas} en horas")


def horas():
    horas = int(input("Ingrese su cantidad en minutos"))
    seg = minutos / 3600
    print(f"Las horas {horas} equivale a {seg} en segundos")

print("1. Segundos a minutos")
print("2. Minutos a horas")
print("3. Horas a segundos")
eleccion=input("Ingrese la conversion que quiere hacer: ")


if eleccion =="1":
    print(segundos())

if eleccion =="2":
    print(minutos())

if eleccion =="3":
    print(horas())
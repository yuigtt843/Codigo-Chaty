medida=0
cm=0
inch=0
ft=0
cm=float(input("Ingrese la medida en cm: "))
medida=(input("A que medida quiere convertir la cantidad ingresada, ft o inch?: "))
if medida=="inch":
    print(cm*2.54)
    print("Esta es la conversion de cm a inch")

if medida=="ft":
    print(cm/30.40)    
    print("Esta es la conversion de: cm a ft ")
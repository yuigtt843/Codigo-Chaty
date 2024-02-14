
for _ in range(10):
    carne=input("Ingrese numero de carmé: ") 
    if len(carne)==8:
        nombre=input("Ingrese nombre y apellido del alumno: ")
        print("Nombre y carne de lo alumnos son: ", carne, nombre)
    else:
        print("Carne invalido")
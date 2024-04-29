
             
def found_vel(distancia, tiempo):
    result=distancia/tiempo
    print("La velocidad seria", str(result),"metros por segundo")

def found_dis(velocidad, tiempo):
    result=velocidad*tiempo
    print("La Distancia seria:",str(result),"metros")

def found_time(distancia,velocidad):
    result=distancia/velocidad
    print("El tiempo seria:",str(result),"segundos")

def fisica():
    Fisica=input("""Que variable quiere encontrar?
             1.Velocidad
             2.Distancia
             3.Tiempo
             Que variable quiere encontrar?: """)
    
    if Fisica =="1":
        time=float(input("Ingrese el tiempo en segundos: "))
        distance=float(input("Ingrese su distancia en metros: "))
        found_vel(distance, time)

    if Fisica =="2":
        speed=float(input("Ingrese su velocidad en metros por segundo: "))
        time=float(input("Ingrese su tiempo en segundos: "))
        found_dis(speed, time)

    if Fisica =="3":
        distance=float(input("Ingrese su distancia en metros: "))
        time=float(input("Ingrese su tiempo en segundos: "))
        found_dis(distance, time)


def area_cuadradro(base, altura):
    resultado=base*altura
    print("El area del cuadrado seria:", str(resultado),"metros cuadrados")

def area_triangulo(base,altura):
    resultado=base*altura/2
    print("El area de su triangulo seria:",str(resultado),"metros cuadrados")

def perimetro(lado1, lado2, lado3, lado4):
    resultado=lado1+lado2+lado3+lado4
    print("El perimetro de su figura sera:",str(resultado),"metros")

def mate():
    math=input("""Que operacion matemática quiere realizar
            1. Area de un Cuadrado
            2. Area de un triagulo
            3. Perimetro de un una figura de 4 lados
                                            : """)
    if math=="1":
        base=float(input("Ingrese la base de su figura en metros: "))
        altura=float(input("Ingrese su altura en metros: "))
        area_cuadradro(base, altura)
    
    if math=="2":
        base=float(input("Ingrese su base en metros: "))
        altura=float(input("Intgrese su altura en metros: "))
        area_triangulo(base, altura)

    if math=="3":
        lado1=("Ingrese la medida del lado 1: ")
        lado2=("Ingrese la medida del lado 2: ")
        lado3=("Ingrese la medida del lado 3: ")
        lado4=("Ingrese la medida del lado 4: ")
        perimetro(lado1, lado2, lado3, lado4)

    


 

lista_funciones_ope=[]
#Funciones de Fisíca
Fisica=""
#Operaciones Matematicas
Mate=""

Inicio=input("""Sobre que materia quiere resolver su problema?
      1.Fisica
      2.Matematicas
             : """)

if Inicio=="1":
    print(fisica())


elif Inicio =="2":
    print(mate())
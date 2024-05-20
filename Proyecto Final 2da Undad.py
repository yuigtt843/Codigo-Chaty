          
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
        lado1=float(input(("Ingrese la medida del lado 1: ")))
        lado2=float(input(("Ingrese la medida del lado 2: ")))
        lado3=float(input(("Ingrese la medida del lado 3: ")))
        lado4=float(input(("Ingrese la medida del lado 4: ")))
        perimetro(lado1, lado2, lado3, lado4)



def masa_molar(masaAto, moleculas):
    resultado= masaAto*moleculas
    print("El compuesto de la masa molar seria:", str(resultado),"masas molares")

def moles_a_gramos(moles, masa_molar):
    resultado= moles*masa_molar
    print("El resultado de su conversion seria: ", str(resultado),"gramos")
 
def concentracion_solucion(moles, litros_de_solucion):
    resultado= moles/litros_de_solucion
    print("La concentracion de su solucion es de:", str(resultado),"m/L")

def quimica():
    Quimica=input("""
                Que operacion desea realizar?
                  1. Masa Molar
                  2. Moles a gramos
                  3. Concentracion de una Solucion
                                            : """
                                    )
    if Quimica=="1":
        masaAto=float(input("Ingrese el numero de masa atomica: "))
        moleculas=float(input("Ingrese el numero de moleculas: "))
        masa_molar(masaAto, moleculas)

    if Quimica=="2":
        moles=float(input("Ingrese la cantidad de moles: "))
        masa_molar1=float(input("Ingrese la masa molar: "))
        moles_a_gramos(moles, masa_molar1)
    
    if Quimica=="3":
        moles=float(input("Ingrese la cantidad de moles: "))
        litros_de_solucion=float(input("Ingrese los litros de su solucion: "))
        concentracion_solucion(moles, litros_de_solucion) 

lista_funciones_ope=[]
#Funciones de Fisíca
Fisica=""
Mate=""
Quimica=""
Inicio=input("""Sobre que materia quiere resolver su problema?
      1.Fisica
      2.Matematicas
      3.Quimica
             : """)

if Inicio=="1":
    print(fisica())

elif Inicio =="2":
    print(mate())

elif Inicio =="3":
    print(quimica())

    
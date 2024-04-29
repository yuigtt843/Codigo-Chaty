lista_funciones_ope=[]
#Funciones de Fisíca
Fisica=""
Inicio=input("""Sobre que materia quiere resolver su problema?
      1.Fisica
      2.Matematicas
             : """)
             
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

if Inicio=="1":
    print(fisica())
 
#Operaciones Matematicas

Mate=""
def mate():
    math=input("""Que operacion matemática quiere realizar
            1. Area de un Cuadrado
            2. Area de un triagulo
            3. Ecuacion General
            4. Perimetro de un una figura de 4 lados
                                            : """)
    
if Inicio =="2":
    print(mate())


 





def calcular_tarifa(distancia, tiempo_minutos, hora):
    tarifa_base = 5.00
    tarifa_por_km = 2.50
    tarifa_por_minuto = 0.50

    costo_viaje = tarifa_base + (distancia * tarifa_por_km) + (tiempo_minutos * tarifa_por_minuto)

    if (7 <= hora < 9) or (17 <= hora < 19):
        costo_viaje *= 1.20 

    return costo_viaje

try:
    distancia = float(input("Ingrese la distancia del destino en kilómetros: "))
    tiempo_minutos = int(input("Ingrese el tiempo de viaje en minutos: "))
    hora = int(input("Ingrese la hora actual (formato 24 horas): "))

    if distancia < 0 or tiempo_minutos < 0 or hora < 0 or hora >= 24:
        print("Por favor, ingrese valores válidos.")
    else:
        costo_total = calcular_tarifa(distancia, tiempo_minutos, hora)
        print("El costo total del viaje es: Q{:.2f}".format(costo_total))

except ValueError:
    print("Por favor, ingrese valores numéricos válidos.")

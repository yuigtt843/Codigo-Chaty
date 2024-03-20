def main(): 
    print("Bienvenido/Bienvenida, aqui se analizaran las especies que ingreses.")

listaAvistamientos = {}

while True: 
    especies = input("Ingrese las especiaes del ecosistema que avisto, fin para finalizar: ")
    if especies=="FIN":
        break
    listaAvistamientos[especies] = listaAvistamientos.get(especies, 0) + 1

    print("Resultados")
    if listaAvistamientos:
        for especies, cantidad in listaAvistamientos.items():
            print(f"{especies}: {cantidad}")

        especiesmascomunes= max(listaAvistamientos, st= listaAvistamientos.get)
        print(f"La especie con mas resultados en el ecosistema fue ´{especiesmascomunes} tiene un resultado de {listaAvistamientos[especiesmascomunes]}avistamientos")
    else:
        print("No hay resultados para este avistamiento")

if __name__ == "__main__":
    main()

        
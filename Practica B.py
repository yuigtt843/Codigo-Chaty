listaItems=[]
while True:
    menu_tienda=input("""Que desea gestionar en la lista de productos
        1. añadir un producto
        2. eliminar un producto
        3. mostar la lista      
        4. salir          :""")


    def añadir_item():
        while True:
            item=input("ingrese un item: ")
            if item== "fin":
                print(listaItems)
                break
            else:
                listaItems.append(item)

    def elimiar_item():
        while True:
            elim=input("Desea eliminar algun item?: ")
            if elim=="si":
                itemelim=int(input("Que item desea eliminar?: "))
                if itemelim=="fin":
                    break
                else:
                    listaItems.pop(itemelim)
            else:
                print(listaItems)
                break

    if menu_tienda =="1":
        añadir_item()
        
    if menu_tienda =="2":
        elimiar_item()
        
    if menu_tienda =="3":
       for indice, item in enumerate(listaItems, start=0):
            print(str(indice)+" "+item)
        
    if menu_tienda =="4":
        print("gracias por visitarnos")
        break
    
    

        
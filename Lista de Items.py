listaItems=[]
while True:
    item=input("ingrese un item: ")
    if item== "fin":
        break
    else:
        listaItems.append(item)

print(listaItems)

while True:
    elim=input("Desea eliminar algun item?: ")
    if elim=="si":
        itemelim=input("Que item desea eliminar?: ")
        if itemelim=="fin":
            break
        else:
            listaItems.remove(itemelim)
    else:
        print(listaItems)
        break
    

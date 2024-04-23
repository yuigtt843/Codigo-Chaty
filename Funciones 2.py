lista=[]
def lista_de_items():
    for _ in range(50):
        items=input("Ingrese los items que quiere agregar a la lista: ")
        if items== "Fin":
            break
        else:
            lista.append(items)

lista_de_items()
print(lista)
def agregaritem():
    while True:       
        agregar_item=input("desea agregar un item?: ")
        if agregar_item=="si":
            agregar_item=input("Agregue sus items: ")
            
        if agregar_item=="Fin":
            break
            print(lista)
        else:
            lista.append(agregar_item)
    else:
        print(lista)
agregaritem()

def elimitem():
    while True:
        itemelim=input("Desea eliminar algun item?: ")
        if itemelim=="si":
            print("Estos son los item de la lista"), print(lista)
            itemelim=input("que item desea eliminar?: ")
        if itemelim=="Fin":
            print(lista)
            break
        else:
            lista.remove(itemelim)
    else:
        print(lista)
elimitem()
from contacto.gestion import lista_contacto 


def buscar_contacto(nombre):
    for contacto  in lista_contacto:
        if nombre in contacto[0]:
            print(f"Nombre: {contacto[0]}, Email: {contacto[1]}")



"""
Comparadores

Igualdad ==
Distinción !=
Mayor que >
Menor que <
Mayor o igual que >=
Menor o igual que <=
"""
#     contacto1[1]                contacto1[1]
#print(lista_contacto[0][1]==("Juan", "juan@ejemplo.com")[1])

#print("Juan" == lista_contacto[0][0])


from contacto import gestion, busqueda

print("Todos los contactos:",end="\n---------------------\n")
for contacto in gestion.lista_contacto:
    print(f"Nombre: {contacto[0]}, Email: {contacto[1]}")


print("A continuación, podrás registrar un nuevo contacto\n")
x = input("Ingresa el nombre del contacto que deseas agregar: ")
y = input("Ingresa el email del contacto que deseas agregar: ")
gestion.agregar_contacto(x, y)

print("Acá está la lista de contactos actualizada:\n")
for contacto in gestion.lista_contacto:
    print(f"Nombre: {contacto[0]}, Email: {contacto[1]}")

nombre_buscado = input("Ingresa el nombre que deseas buscar en la lista de contactos")
busqueda.buscar_contacto(nombre_buscado)
#1
precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva':
1450}

precios_frutas["Naranja"] = 1200;
precios_frutas["Manzana"] = 1500;
precios_frutas["Pera"] = 2300;

print(precios_frutas)

#2
precios_frutas["Banana"] = 1330;
precios_frutas["Manzana"] = 1700;
precios_frutas["Melón"] = 2800;

#3
lista_frutas = []
for fruta in precios_frutas:
    lista_frutas.append(fruta)

print(lista_frutas)

#4
i = 0;
agenda = dict()
while(i < 5):
    nombre_contacto = input("Ingrese un nombre para el contacto teléfonico: ")
    if agenda.get(nombre_contacto) != None:
        print("El nombre de contacto ingresado ya existe, intente con otro nombre")
    else:
        numero_contacto = input("Ingrese el número de teléfono del contacto teléfonico: ")
        agenda[nombre_contacto] = numero_contacto
        i += 1
nombre_contacto = input("Ingrese el nombre del contacto que desee buscar: ")

if agenda.get(nombre_contacto) != None:
        print(agenda.get(nombre_contacto))
else:
    print("El nombre de contacto ingresado no se encuentra en la agenda")


#5
frase = input("Ingrese una frase: ")
lista_palabras = list(frase.split(" "))
palabras_unicas = set(lista_palabras)
aparicion_palabras = dict()
for palabra in lista_palabras:
    if aparicion_palabras.get(palabra) is None:
        aparicion_palabras[palabra] = 1
    else:
        aparicion_palabras[palabra] = aparicion_palabras[palabra] + 1
print(palabras_unicas)
print(aparicion_palabras)


#6
j = 0
alumnos_notas = dict()
while(j < 3):
    nombre = input("Introduzca el nombre del alumno:")
    notas = []
    for i in range(3):
        nota = input("Introduzca una nota:")
        notas.append(nota)
    alumnos_notas[nombre] = tuple(notas)
    j += 1

print(alumnos_notas)


#7
aprobados_parcial_uno = [1,2,6,8,9]
aprobados_parcial_dos = [1,3,4,5,6,8]

aprobados_al_menos_un_parcial = set(aprobados_parcial_uno+aprobados_parcial_dos)
aprobados_solo_un_parcial = set(aprobados_parcial_uno) ^ set(aprobados_parcial_dos)
aprobados_ambos_parciales = set(aprobados_parcial_uno) & set(aprobados_parcial_dos)

print("Aprobados en ambos parciales: ", end="")
print(aprobados_ambos_parciales)
print("Aprobados solo un parcial: ", end="")
print(aprobados_solo_un_parcial)
print("Aprobados en al menos un parcial: ", end="")
print(aprobados_al_menos_un_parcial)


#8
stock = dict()
opcion = -1

def presentar_menu():
    opcion = -1
    print("Ingrese el número de la acción que desea realizar")
    print("1 - Agregar producto")
    print("2 - Consultar stock de un producto")
    print("3 - Agregar unidades de un producto")
    print("4 - Salir")
    try:
        opcion = int(input())
        return opcion
    except ValueError:
        return -1

#agregar productos
def agregar_producto():
    nombre_producto = input("Ingrese el nombre del producto: ")
    if (stock.get(nombre_producto) is not None):
        print("El producto ya se encuentra registrado")
        print("")
    else:
        stock_producto = -1
        while(stock_producto < 0):
            try:
                stock_producto = int(input("Ingrese las unidades en stock: "))
                stock[nombre_producto] = stock_producto
                print("Producto agregado exitosamente")
                print("")
            except ValueError:
                print("Ingrese un valor válido")
            
#consultar stock de un producto
def consultar_stock():
    nombre_producto = input("Ingrese el nombre del producto del que desea consultar el stock: ")
    if stock.get(nombre_producto) is None:
        print("No se encontro un producto con este nombre")
    else:
        print("La cantidad de unidades de este producto es: " + str(stock[nombre_producto]))
        print("")

#agregar unidades producto
def agregar_unidades_producto():
    unidades = -1
    while(unidades == -1):
        producto = input("Ingrese el nombre del producto: ")
        if stock.get(producto) is not None:
            print(f"El stock actual de este producto es de {str(stock[producto])} unidades")
            unidades = -1
            while(unidades == -1):
                try:
                    unidades = int(input("Ingrese la cantidad de unidades que desea agregar: "))
                    if unidades <= 0:
                        print("Debe ingresar un valor mayor que cero")
                        unidades = -1
                    else:
                        stock[producto] = stock[producto] + unidades
                        print(f"Se han añadido las unidades al stock exitosamente (stock: {stock[producto]})")
                        print("")
                except ValueError:
                    print("Debe ingresar un número válido")
        else:  
            print("El producto ingresado no existe en el stock")
            

while(opcion != 4):
    opcion = presentar_menu()
    match opcion:
        case 1:
            agregar_producto()
        case 2:
            consultar_stock()
        case 3:
            agregar_unidades_producto()


#9
agenda = {
    ("lunes", "10:00"): "Reunión",
    ("martes", "15:00"): "Clase de inglés"
}

dia = input("Ingrese el dia: ")
hora = input("Ingrese la hora: ")

if agenda.get((dia,hora)):
    print(agenda[(dia,hora)])
else:
    print("No se encontro una actividad que coincida con el dia y hora")

#10
original = {"Argentina":"Buenos Aires", "Chile":"Santiago"}
invertido = dict()

for k in original:
    invertido[original[k]] = k

print(invertido)

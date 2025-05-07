#Ej 1
lista = []
for i in range(4,101,4):
    lista.append(i)

#Ej 2
lista_de_elementos = ["gato","chocolate","sol","dormir","pizza"]

#Ej 3
lista_vacia = []
lista_vacia.append("calor")
lista_vacia.append("frio")
lista_vacia.append("noche")
print(lista_vacia)

#Ej 4
animales = ["perro", "gato", "conejo", "pez"]
animales[1] = "loro"
animales[3] = "oso"
print(animales)

#Ej 5
"""
max busca el numero mayor dentro de la lista
remove busca el argumento dentro de la lista y lo elimina (en esta caso el numero mayor que es lo que devuelve max)
print imprime los numeros de la lista que ya no incluye el que originalmente era el mayor de ellos
"""

#Ej 6
lista_del_10_al_30 = []
for i in range(10,31, 5):
    lista_del_10_al_30.append(i)

print(lista_del_10_al_30[0],lista_del_10_al_30[1])

#Ej 7
autos = ["sedan", "polo", "suran", "gol"]
autos[1] = "casa"
autos[2] = "algodon"

#Ej 8
dobles = []
dobles.append(5*2)
dobles.append(10*2)
dobles.append(15*2)
print(dobles)

#Ej 9
compras = [["pan", "leche"], ["arroz", "fideos", "salsa"], ["agua"]]

#a
compras[2].append("jugo")
#b
compras[1][compras[1].index("fideos")] = "tallarines"
#c
compras[0].pop(0)
#d
print(compras)

#Ej 10
lista_anidada = [15,True,[25.5,57.9,30.6],False]
print(lista_anidada)

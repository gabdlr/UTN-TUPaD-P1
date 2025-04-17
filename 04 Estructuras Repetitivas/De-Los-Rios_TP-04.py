import random
msj_valor_entero = "Ingrese un número entero: "
msj_cantidad_numeros = "La cantidad de números"

#Ej 1
for i in range(0,101):
    print(i)


#Ej 2
numero_entero = input("Ingrese un numero entero: ")
if numero_entero.isnumeric():
    print(f"El número tiene {len(str(numero_entero))} digitos")

#Ej 3
valor_1 = input(msj_valor_entero);
valor_2 = input(msj_valor_entero);

if valor_1.isnumeric() and valor_2.isnumeric():
    valor_1 = int(valor_1)
    valor_2 = int(valor_2)

    if valor_1 > valor_2:
        for i in range(valor_2, valor_1 + 1):
            print(i)
    else:
        for i in range(valor_1, valor_2 + 1):
            print(i)

#Ej 4
acumulador = 0
pedir_numero = True

while(pedir_numero):
    num_ej4 = input(msj_valor_entero)
    if num_ej4.isnumeric():
        num_ej4 = int(num_ej4)
        if num_ej4 == 0:
            pedir_numero = False
        else:
            acumulador += int(num_ej4)
print(acumulador)

#Ej 5
intentos = 0
numero_azar = random.randrange(0,9,1)
ha_acertado = False
while(not ha_acertado):
    intento = input(msj_valor_entero)
    if intento.isnumeric():
        intentos += 1
        if numero_azar == int(intento):
            ha_acertado = True
            print(f"Necesitaste {intentos} intento{intentos > 1 and 's' or ''} para acertar el número!")

#Ej 6
for i in range(100,-1, -1):
    if i%2 == 0:
     print(i)

#Ej 7
num_ej7 = input('Ingrese un número entero positivo: ')
if num_ej7.isnumeric() and int(num_ej7) > 0:
    acumulador_ej7 = 0
    for i in range(0, int(num_ej7) + 1):
        acumulador_ej7 = i + acumulador_ej7
    print(f"La suma de todos los numeros entre 0 y {num_ej7} es {str(acumulador_ej7)}")

#Ej 8
numeros_ej8 = []
max_input_ej8 = 100
for i in range(max_input_ej8):
    num_ej8 = input(msj_valor_entero)
    try:
        numeros_ej8.append(int(num_ej8))
    except:
        None
        
contador_pares = 0
contador_impares = 0
contador_positivos = 0
contador_negativos = 0

for i in range(0, len(numeros_ej8)):
    if numeros_ej8[i] % 2 == 0:
        contador_pares += 1
    else:
        contador_impares += 1
    if numeros_ej8[i] >= 0:
        contador_positivos += 1
    else:
        contador_negativos += 1

print(f"{msj_cantidad_numeros} pares fue {contador_pares}")
print(f"{msj_cantidad_numeros} impares fue {contador_impares}")
print(f"{msj_cantidad_numeros} positivos fue {contador_positivos}")
print(f"{msj_cantidad_numeros} negativos fue {contador_negativos}")

#Ej 9
numeros_ej9 = []
max_input_ej9 = 100
for i in range(max_input_ej9):
    num_ej8 = input(msj_valor_entero)
    try:
        numeros_ej9.append(int(num_ej8))
    except:
        None

acumulador_ej9 = 0
len_input = len(numeros_ej9)

for i in range(len_input):
    acumulador_ej9 += numeros_ej9[i]

if len_input > 0:
    media = acumulador_ej9 / len_input
    print(f"La media de los valores ingresados es {media}")

#Ej 10
try:
    num_ej10 = int(input("Ingrese un número: "))
    num_como_string = str(num_ej10)
    num_al_reves = ""
    for i in range(len(num_como_string) - 1,-1,-1):
        num_al_reves += num_como_string[i]
    print(num_al_reves)
except:
    None
import random
from statistics import mode, median, mean

#1
edad_ej1 = int(input("Ingrese su edad: "))

if edad_ej1 > 18:
    print("Es mayor de edad")

#2
nota_ej2 = int(input("Ingrese su nota: "))
if nota_ej2 >= 6:
    print("Aprobado")
else:
    print("Desaprobado")

#3
numero_ej3 = int(input("Ingrese un número par: "))

if numero_ej3 % 2 == 0:
    print("Ha ingresado un número par")
else:
    print("Por favor, ingrese un número par")

#4
edad_ej4 = int(input("Ingrese su edad: "))

if edad_ej4 < 12:
    print("Niño")
elif edad_ej4 >= 12 and edad_ej4 < 18:
    print("Adolescente")
elif edad_ej4 >= 18 and edad_ej4 < 30:
    print("Adulto joven")
else:
    print("Adulto")

#5
contrasena_ej5 = input("Ingrese una contraseña de entre 8 y 14 carácteres: ")
len_contrasena = len(contrasena_ej5)
if len_contrasena >= 8 and len_contrasena <= 14:
    print("Ha ingresado una contraseña correcta")
else:
    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")

#6
numeros_aleatorios = [random.randint(1,100) for i in range(50)]
list_mode = mode(numeros_aleatorios)
list_median = median(numeros_aleatorios)
list_mean = mean(numeros_aleatorios)

if list_mode == list_mean and list_mode == list_median:
    print("Sin sesgo")
elif list_mean > list_median and list_median > list_mode: 
    print("Sesgo positivo")
elif list_mean < list_median and list_median < list_mode: 
    print("Sesgo negativo")

#7
frase_o_palabra_ej7 = input("Ingrese una frase o palabra: ")
indice_ultima_letra = len(frase_o_palabra_ej7) - 1
if indice_ultima_letra >= 0:
    vocales = ['a','e','i','o','u']
    if frase_o_palabra_ej7[indice_ultima_letra] in vocales:
        print(frase_o_palabra_ej7 + "!")
    else:
        print(frase_o_palabra_ej7)

#8
nombre_ej8 = input("Ingrese su nombre: ")
opcion_ej8 = input("Ingrese: " \
"\n1. Si quiere su nombre en mayúsculas. Por ejemplo: PEDRO. " \
"\n2. Si quiere su nombre en minúsculas. Por ejemplo: pedro." \
"\n3. Si quiere su nombre con la primera letra mayúscula. Por ejemplo: Pedro.\n")
if opcion_ej8 == "1":
    print(nombre_ej8.upper())
elif opcion_ej8 == "2":
    print(nombre_ej8.lower())
elif opcion_ej8 == "3":
    print(nombre_ej8.title())

#9
magnitud_ej9 = int(input("Ingrese la magnitud del terremoto: "))

if magnitud_ej9 < 3:
    print('"Muy leve" (imperceptible).')
elif magnitud_ej9 >= 3 and magnitud_ej9 < 4:
    print('"Leve" (ligeramente perceptible).')
elif magnitud_ej9 >= 4 and magnitud_ej9 < 5:
    print('"Moderado" (sentido por personas, pero generalmente no causa daños).')
elif magnitud_ej9 >= 5 and magnitud_ej9 < 6:
    print('"Fuerte" (puede causar daños en estructuras débiles).')
elif magnitud_ej9 >= 6 and magnitud_ej9 < 7:
    print('"Muy Fuerte" (puede causar daños significativos).')
else:
    print('"Extremo" (puede causar graves daños a gran escala).')

#10
meses = {
    "enero": 1,
    "febrero": 2,
    "marzo": 3,
    "abril": 4,
    "mayo": 5,
    "junio": 6,
    "julio": 7,
    "agosto": 8,
    "septiembre": 9,
    "octubre": 10,
    "noviembre": 11,
    "diciembre": 12   
}

hemisferio_ej10 = input("Ingrese el hemisferio en que se encuentra (norte/sur): ")
mes_ej10 = input("Ingrese el mes del año: ")
dia_ej10 = int(input("Ingrese el dia del mes: "))
if meses.get(mes_ej10) is not None:
    mes_ej10 = meses[mes_ej10]
    if mes_ej10:
            if (mes_ej10 >= 1 and mes_ej10 <= 2) or (mes_ej10 == 3 and (dia_ej10 >= 1 and dia_ej10 <= 20)) or (mes_ej10 == 12 and (dia_ej10 >= 21 and dia_ej10 <= 31)):
                    if hemisferio_ej10 == "norte":
                        print("Invierno")
                    if hemisferio_ej10 == "sur":
                        print("Verano")
            if (mes_ej10 == 3 and (dia_ej10 >= 21 and dia_ej10 <= 31)) or (mes_ej10 >= 4 and mes_ej10 <= 5) or (mes_ej10 == 6 and (dia_ej10 >= 1 and dia_ej10 <= 20)):
                    if hemisferio_ej10 == "norte":
                        print("Primavera")
                    if hemisferio_ej10 == "sur":
                        print("Otoño")
            if (mes_ej10 == 6 and (dia_ej10 >= 21 and dia_ej10 <= 30) or (mes_ej10 >= 7 and mes_ej10 <= 8)) or (mes_ej10 == 9 and (dia_ej10 >= 1 and dia_ej10 <= 20)):
                    if hemisferio_ej10 == "norte":
                        print("Verano")
                    if hemisferio_ej10 == "sur":
                        print("Invierno")
            if (mes_ej10 == 9 and (dia_ej10 >= 21 and dia_ej10 <= 31) or (mes_ej10 >= 10 and mes_ej10 <= 11) or (mes_ej10 == 12 and (dia_ej10 >=1 and dia_ej10 <= 20))):
                    if hemisferio_ej10 == "norte":
                        print("Otoño")
                    if hemisferio_ej10 == "sur":
                        print("Primavera")
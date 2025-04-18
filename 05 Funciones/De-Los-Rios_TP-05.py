from math import pi
msj_ingrese = "Ingrese su "
msj_ingrese_numero = "Ingrese un número: "

#Ej 1
def imprimir_hola_mundo():
    print("Hola Mundo!")

#Ej 2
def saludar_usuario(nombre):
    print(f"Hola {nombre}!")

#Ej 3
def informacion_personal(nombre, apellido, edad, residencia):
    print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}")

#Ej 4
def calcular_area_circulo(radio):
    return pi * radio**2

def calcular_perimetro_circulo(radio):
    return 2 * pi * radio

#Ej 5
def segundos_a_horas(segundos):
    return segundos/3600

#Ej 6
def tabla_multiplicar(numero):
    for i in range(1,11):
        print(f"{numero} * {i} = {numero*i}")

#Ej 7
def operaciones_basicas(a, b):
    suma = a + b
    resta = a - b
    multiplicacion = a * b
    division = 0
    if b != 0:
        division = a / b
    return (suma,resta,multiplicacion,division)

#Ej 8
def calcular_imc(peso, altura):
    return peso / altura**2

#Ej 9
def celsius_a_fahrenheit(celsius):
    return celsius * 1.8 + 32

#Ej 10
def calcular_promedio(a, b, c):
    return (a + b + c) / 3

#Programa principal
imprimir_hola_mundo()

nombre_ej2 = input(msj_ingrese + "nombre: ")
saludar_usuario(nombre_ej2)


nombre_ej3 = input(msj_ingrese + "nombre: ")
apellido_ej3 = input(msj_ingrese + "apellido: ")
edad_ej3 = input(msj_ingrese + "edad: ")
residencia_ej3 = input(msj_ingrese + "lugar de residencia: ")

informacion_personal(nombre_ej3,apellido_ej3,edad_ej3,residencia_ej3)


try:
    radio_ej4 = int(input("Ingrese el radio: "))
    print(f"area: {calcular_area_circulo(radio_ej4)}, perimetro: {calcular_perimetro_circulo(radio_ej4)}")
except:
    pass  

try:
    segundos_ej5 = float(input("Ingrese los segundos que desea convertir en horas: "))
    print(f"Eso son {segundos_a_horas(segundos_ej5)} horas.")
except:
    pass

try:
    numero_ej6 = int(input(msj_ingrese_numero))
    tabla_multiplicar(numero_ej6)
except:
    pass

try:
    numero1_ej7 = int(input(msj_ingrese_numero))
    numero2_ej7 = int(input(msj_ingrese_numero))
    resultados = operaciones_basicas(numero1_ej7,numero2_ej7)
    print(f"Suma: {resultados[0]}, resta: {resultados[1]}, multiplicación: {resultados[2]}, división: {resultados[3]}")
except:
    pass
    
try:
    peso_ej8 = float(input(msj_ingrese + "peso en kilogramos: "))
    altura_ej8 = float(input(msj_ingrese + "altura en metros: "))
    print(f"Su IMC es {round(calcular_imc(peso_ej8,altura_ej8), 2)}")
except:
    pass
    
try:
    temperatura_ej9 = float(input("Ingrese la temperatura en grados celsius: "))
    print(f"La tempertura equivale a {celsius_a_fahrenheit(temperatura_ej9)} Fahrenheit")
except:
    pass
    

try:
    numero1_ej10 = float(input(msj_ingrese_numero))
    numero2_ej10 = float(input(msj_ingrese_numero))
    numero3_ej10 = float(input(msj_ingrese_numero))
    print(f"El promedio de los números ingresados es: {calcular_promedio(numero1_ej10,numero2_ej10,numero3_ej10)}")
except:
    pass

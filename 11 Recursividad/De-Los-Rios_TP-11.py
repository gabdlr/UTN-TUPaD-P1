from math import floor

#1
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

max = input("Ingrese el número máximo a calcular: ")

try:
    max = int(max)
    for i in range(max + 1):
        print(factorial(i))
except ValueError:
    print("Debe ingresar un número válido")

#2
def fibonacci(n):
    if n == 0 or n == 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

try:
    pos = int(input("Ingrese una posición: "))
    print(fibonacci(pos))
    for i in range(pos + 1):
        print(fibonacci(i))
except ValueError:
    print("Debe ingresar un número válido")

#3
def calcular_potencia(base, exponente):
    if exponente == 0:
        return 1
    return base * calcular_potencia(base, exponente - 1)

try:
    base = int(input("Ingrese la base: "))
    exp = int(input("Ingrese el exponente: "))
    print(calcular_potencia(base,exp))
except ValueError:
    print("Debe ingresar un número válido")

#4
def decimal_a_binario(dec, bin=""):
    if dec == 0 and bin == "":
        return "0" 
    if dec == 0:
        return ""
    resto = dec % 2  
    bin = str(resto)
    return decimal_a_binario(floor(dec/2), bin) + bin

try:
    decimal = int(input("Ingrese un número entero positivo: "))
    if decimal < 0:
        print("Ingrese un número válido")
    else:
        print(decimal_a_binario(decimal)) 
except ValueError:
    print("Ingrese un número válido")

#5
def es_palindromo(palabra):
    if len(palabra) <= 1:
        return True
    if palabra[0].lower() != palabra[-1].lower():
        return False
    return es_palindromo(palabra[1:-1])
print(es_palindromo("kayak"))

#6
def suma_digitos(numero_entero_positivo):
    suma = 0;
    if numero_entero_positivo < 1:
        return suma
    return suma + numero_entero_positivo%10 + suma_digitos(int(numero_entero_positivo/10))

#7
def contar_bloques(n):
    suma = 0 + n
    if n == 0:
        return suma
    return suma + contar_bloques(n - 1)

#8
def contar_digito(numero, digito):
    contador = 0
    if numero < 1:
        return contador
    if str(digito) in str(numero)[-1]:
        contador = 1
    return contador + contar_digito(int(numero/10), digito)

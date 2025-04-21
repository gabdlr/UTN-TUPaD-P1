from collections import deque
from math import pi

#Ej 1
precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva':
1450}

precios_frutas['Naranja'] = 1200
precios_frutas['Manzana'] = 1500
precios_frutas['Pera'] = 2300

#Ej 2
precios_frutas['Banana'] = 1330
precios_frutas['Manzana'] = 1700
precios_frutas['Melón'] = 2800

#Ej 3
lista_frutas = list(precios_frutas.keys())

#Ej 4
class Persona:
    def __init__(self):
        self.nombre = "Carlos"
        self.pais = "Argentina"
        self.edad = 22

    def saludar(self):
        print(f"¡Hola! Soy {self.nombre}, vivo en {self.pais} y tengo {self.edad} años.")
    
carlos = Persona()
carlos.saludar()

#Ej 5
class Circulo:
    radio = 5
    
    def calcular_area(self):
        return pi * self.radio**2

    def calular_perimetro(self):
        return 2 * pi * self.radio

circulo = Circulo()

print(circulo.calcular_area())
print(circulo.calular_perimetro())

#Ej 8
class Pila:
    def __init__(self):
        self.elementos = []

    def apilar(self, elemento):
        self.elementos.append(elemento)

    def desapilar(self):
        return self.elementos.pop() if not self.esta_vacia() else "La pila está vacía"  # 🔄 Quitamos el último elemento

    def esta_vacia(self):
        return len(self.elementos) == 0

    def ver_tope(self):
        return self.elementos[-1] if not self.esta_vacia() else "La pila está vacía"

def balanceado(string):
    pila = Pila()
    
    for letra in range(len(string)):
        pila.apilar(string[letra])

    if not pila.desapilar() == ")":
        return False
    if not pila.desapilar() == "}":
        return False
    if not pila.desapilar() == "]":
        return False
    if not pila.desapilar() == "[":
        return False
    if not pila.desapilar() == "{":
        return False
    if not pila.desapilar() == "(":
        return False    
    return True

print(balanceado("({[]})"))
print(balanceado("({[}))"))

class Cola:
    msj_no_mas_clientes = "No hay mas clientes"
    
    def __init__(self):
        self.clientes = deque()

    def agregar_cliente(self, cliente):
        self.clientes.append(cliente)

    def atender_cliente(self):
        return self.clientes.popleft() if not self.no_hay_clientes() else self.msj_no_mas_clientes

    def no_hay_clientes(self):
        return len(self.clientes) == 0  
    
    def mostrar_siguiente(self):
        return self.clientes[0] if not self.no_hay_clientes() else self.msj_no_mas_clientes

cola_banco = Cola()
cola_banco.agregar_cliente("101")
cola_banco.agregar_cliente("102")
print(cola_banco.atender_cliente())
print(cola_banco.mostrar_siguiente())

#Ej 8
class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None

class ListaEnlazada:
    def __init__(self):
        self.cabeza = None

    def insertar(self, dato):
        nuevo_nodo = Nodo(dato)
        nuevo_nodo.siguiente = self.cabeza
        self.cabeza = nuevo_nodo

    def mostrar(self):
        actual = self.cabeza
        while actual:
            print(actual.dato, end=' ➡️ ')
            actual = actual.siguiente
        print("None")

#Ej 9
def invertir_lista(lista, nodo, nodo_anterior):
    if nodo == None:
        return
    if nodo.siguiente == None:
        nodo.siguiente = nodo_anterior
        lista.cabeza = nodo
        return
    invertir_lista(lista, nodo.siguiente, nodo)
    nodo.siguiente = nodo_anterior
        
lista_enlazada = ListaEnlazada()
lista_enlazada.insertar(1)
lista_enlazada.insertar(2)
lista_enlazada.insertar(3)
lista_enlazada.mostrar()
invertir_lista(lista_enlazada, lista_enlazada.cabeza, None)
lista_enlazada.mostrar()
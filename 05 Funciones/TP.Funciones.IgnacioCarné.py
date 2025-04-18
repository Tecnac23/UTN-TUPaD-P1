"""# Ejercicio 1 #

# Definicion de Funciones
def imprimir_hola_mundo():   # Función sin parámetro
    print("\"Hola Mundo!\"")

# Programa principal
imprimir_hola_mundo()


# Ejercicio 2 #

# Definicion de Funciones
def saludar_usuario(nombre):
    return (f"Hola {nombre}!")  # Devuelve una cadena que es tomada por la variable saludo

# Programa principal
nombre = input("Ingrese su nombre: ")
saludo = saludar_usuario(nombre)
print(saludo)


# Ejercicio 3 #

# Definicion de Funciones
def informacion_personal(nombre, apellido, edad, residencia):
    print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}.")
# Programa principal
nombre = input("Ingresá tu nombre: ")  
apellido = input("Ingresá tu apellido: ")
edad = input("Ingresá tu edad: ")
residencia = input("Ingresá tu residencia: ")

informacion_personal(nombre, apellido, edad, residencia)


# Ejercicio 4 #

from math import pi   # Importo pi desde la librería math
# Definicion de Funciones
def calcular_area_circulo(radio):
    return pi*(radio**2)

def calcular_perimetro_circulo(radio):
    return pi*radio*2

# Programa principal

radio = float(input("Ingrese el valor del radio en centímetros: "))
area_circulo = calcular_area_circulo(radio)   # Guardo el valor del area en una variable
perimetro_circulo = calcular_perimetro_circulo(radio)   # Guardo el valor del perímetro en una variable
print(f"El área del circulo es: {area_circulo}")
print(f"El perímetro del circulo es: {perimetro_circulo}")


# Ejercicio 5 #

# Definicion de Funciones
def segundos_a_horas(segundos):
    return segundos // 3600   # debuelvo el favorl de un cálculo

# Programa principal
segundos = int(input("Ingrese la cantidada de segundos: "))
horas = segundos_a_horas(segundos)     # Guardo el valor que devuelve la funcione la variable "horas"
print(f"{segundos} segundos corresponden a {horas} horas.")


# Ejercicio 6 #

# Definicion de Funciones
def tabla_multiplicar(numero):
    for i in range(1, 11):
        print(f"{numero}x{i} = {numero*i} ")

# Programa principal
numero = int(input("Ingrese un número entero: ")) # Pido número al usuraio
tabla_multiplicar(numero)  # LLamo a la funcion con el argumento ingresado por el usuario


# Ejercicio 7 #

# Definicion de Funciones
def operaciones_basicas(a, b):
    suma = a + b
    resta = a - b
    multiplicacion = a * b
    division = a / b if b != 0 else 'No se puede dividir por cero'  # operador ternario para evitar un error en el programa.
    resultados = (suma, resta, multiplicacion, division) # Guardo los redultados en una tupla
    return resultados 

# Programa principal
a = float(input("Ingrese un  número: "))
b = float(input("Ingrese otro número: "))
resultados = operaciones_basicas(a, b)
print(f"El resultado de la Suma es: {resultados[0]}")  # Imprimo los resultados de manera separada refiriendo a la posición dentro de la tupla.
print(f"El resultado de la Resta es: {resultados[1]}")
print(f"El resultado de la Multiplicación es: {resultados[2]}")
print(f"El resultado de la División es: {resultados[3]}")


# Ejercicio 8 #

# Definicion de Funciones
def calcular_imc(peso, altura): #Calcula el índice de masa corporal (IMC).
    return peso / (altura ** 2)

# Programa principal
peso = float(input("Ingrese su peso en kilogramos: "))  # Solicito al usuario el peso y la altura
altura = float(input("Ingrese su altura en metros: "))
imc = calcular_imc(peso, altura)  # Guardo el IMC
print(f"Su índice de masa corporal (IMC) es: {imc}") # Muestro el resultado 


# Ejercicio 9 #

# Definicion de Funciones
def celsius_a_fahrenheit(celsius): # Función que convierte la temperatura enviada en Celsius a Fahrenheit
  return (celsius * 9/5) + 32


# Programa principal
celsius = float(input("Ingrese la temperatura en grados Celsius: ")) # Pido al usuario la temperatura en Celsius
fahrenheit = celsius_a_fahrenheit(celsius) # Guardo la temperatura a Fahrenheit 
print(f"La temperatura en grados Fahrenheit es: {fahrenheit}")  # Se muestra el resultado de la conversión

"""
# Ejercicio 10 #

# Definicion de Funciones
def calcular_promedio(a, b, c):   # Funcion que calcula en promedio de 3 valores recibidos
  return (a+b+c)/3

# Programa principal
a = float(input("Ingrese el primer valor a promediar: ")) # Pido al usuario que ingrese los valores a promediar
b = float(input("Ingrese el segundo valor a promediar: "))
c = float(input("Ingrese el tercer valor a promediar: "))

promedio = calcular_promedio(a, b, c)

print(f"El promedio es: {promedio}")
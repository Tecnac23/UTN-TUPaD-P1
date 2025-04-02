# Práctico 3. Estructuras condicionales. Ignacio Carné

"""# Ejercicio 1
edad = int(input("Ingrese su edad, por favor: "))
if edad > 18:
    print("Es mayor de edad.")

# Ejercicio 2
nota = int(input("Ingrese su nota: "))
if nota >= 6:
    print("Aprobado")
else:
    print("Desaprobado")

# Ejercicio 3
numero = int(input("Ingrese un número, por favor:"))
if numero % 2 == 0:
    print("Ha ingresado un número par.")
else:
    print("Por favor ingrese un número par.")

#Ejercicio 4

edad = int(input("Ingrese su esdad, por favor: "))
if edad < 12:
    print("Ud pertenece a la categoría niño/a.")
elif 12 <= edad < 18:
    print("Ud pertenece a la categoría adolescente.")
elif 18 <= edad < 30:
    print("Ud pertenece a la categoría adulto/a jóven.")
else:
    print("Ud pertenece a la categoría adulto/a.")

# Ejercicio 5
contrasenia = input("Ingrese una contraseña que tenga entre 8 y 14 (incluídos) caracteres: ")
if 8 <= len(contrasenia) <= 14:
    print("Ha ingresado una contraseña correcta")
else:
    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres.")

# Ejercicio 6 
import random
from statistics import mode, median, mean
numeros_aleatorios = [random.randint(1,100) for i in range (25)]
media = mean(numeros_aleatorios)
mediana = median(numeros_aleatorios)
moda = mode(numeros_aleatorios)

if moda < mediana < media:
    print("El sesgo en los valores es Positivo.")
elif media < mediana < moda:
    print("El sesgo en los valores es Negativo.")
elif media == moda == mediana:
    print("No existe sesgo en los valores.")

# Ejercicio 7
cadena = input("Ingrese una frase o palabra, por favor: ").lower()

if cadena[-1] == "a" or cadena[-1] == "e" or cadena[-1] == "i" or cadena[-1] == "o" or cadena[-1] == "u":
    print(f"{cadena}!")
else:
    print(cadena)
 
#Ejercicio 8
nombre = input("Ingrese su nombre, por favor: ")
opcion = int(input("Ingrese el número 1 si quiere su nombre en MAYÚSCULAS; 2 si quiere su nombre en minúsculas o 3 si quiere su nombre con la primer letra mayúscula: "))
if opcion == 1:
    print(nombre.upper())
elif opcion == 2:
    print(nombre.lower())
elif opcion == 3:
    print(nombre.title())

# Ejercicio 9
magnitud_terremoto = float(input("Ingrese la magnitud del terremoto en escala Richter: "))

if magnitud_terremoto < 3:
    print("\"Muy leve\" (imperceptible)")
elif 3 <= magnitud_terremoto < 4:
    print("\"Leve\" (ligeramente perceptible)")
elif 4 <= magnitud_terremoto < 5:
    print("\"Moderado\" (sentido por personas pero generalmente no causa daños)")
elif 5 <= magnitud_terremoto < 6:
    print("\"Fuerte\" (puede causar daños en estructuras débiles)")
elif 6 <= magnitud_terremoto < 7:
    print("\"Muy fuerte\" (puede causar daños significatifos)")

elif magnitud_terremoto >= 7:
    print("\"Extremo\" (puede causar grandes daños a gran escala)")"""

# Ejercicio 10
hemisferio = input("¿En qué hemisferio se encuentra? Ingrese N ó S: ").upper()
mes = input("¿Qué mes es ahora?: ").lower()
dia = int(input("Qué dia (número) es ahora?: "))

if (21 <= dia and mes == "diciembre" and hemisferio == "N") or (1 <= dia <= 31 and mes == "enero" and hemisferio == "N" ) or (1 <= dia <= 31 and mes == "febrero" and hemisferio == "N" ) or (dia <= 20 and mes == "marzo" and hemisferio == "N"):
    print("Usted está en Invierno")
elif (21 <= dia and mes == "diciembre" and hemisferio == "S") or (1 <= dia <= 31 and mes == "enero" and hemisferio == "S") or (1 <= dia <= 31 and mes == "febrero" and hemisferio == "S" ) or (dia <= 20 and mes == "marzo" and hemisferio == "S"):
    print("Usted está en Verano")
elif (21 <= dia and mes == "marzo" and hemisferio == "N") or (1 <= dia <= 30 and mes == "abril" and hemisferio == "N" ) or (1 <= dia <= 31 and mes == "mayo" and hemisferio == "N" ) or (dia <= 20 and mes == "junio" and hemisferio == "N"):
    print("Usted está en Primavera")
elif (21 <= dia and mes == "marzo" and hemisferio == "S") or (1 <= dia <= 30 and mes == "abril" and hemisferio == "S" ) or (1 <= dia <= 31 and mes == "mayo" and hemisferio == "S" ) or (dia <= 20 and mes == "junio" and hemisferio == "S"):
    print("Usted está en Otoño")
elif (21 <= dia and mes == "junio" and hemisferio == "N") or (1 <= dia <= 31 and mes == "julio" and hemisferio == "N" ) or (1 <= dia <= 31 and mes == "agosto" and hemisferio == "N" ) or (dia <= 20 and mes == "septiembre" and hemisferio == "N"): 
    print("Usted está en Verano")
elif (21 <= dia and mes == "junio" and hemisferio == "S") or (1 <= dia <= 31 and mes == "julio" and hemisferio == "S" ) or (1 <= dia <= 31 and mes == "agosto" and hemisferio == "S" ) or (dia <= 20 and mes == "septiembre" and hemisferio == "S"):
    print("Usted está en Invierno") 
elif (21 <= dia and mes == "septiembre" and hemisferio == "N") or (1 <= dia <= 31 and mes == "octubre" and hemisferio == "N" ) or (1 <= dia <= 30 and mes == "noviembre" and hemisferio == "N" ) or (dia <= 20 and mes == "diciembre" and hemisferio == "N"):
    print("Usted está en Otoño")
elif (21 <= dia and mes == "septiembre" and hemisferio == "S") or (1 <= dia <= 31 and mes == "octubre" and hemisferio == "S" ) or (1 <= dia <= 30 and mes == "noviembre" and hemisferio == "S" ) or (dia <= 20 and mes == "diciembre" and hemisferio == "S"):
    print("Usted está en Primavera")
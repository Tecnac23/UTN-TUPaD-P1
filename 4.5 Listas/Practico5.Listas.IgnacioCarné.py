# Practica 5: Listas  Ignacio Carné

"""# Ejercicio 1      Crear una lista con los números del 1 al 100 que sean múltiplos de 4. Utilizar la función range.

lista = list(range(1,101)) # Genero los elementos de la lista con la función range. Comienza en 1 y termina en 100.
print(lista)


# Ejercicio 2    Crear una lista con cinco elementos (colocar los elementos que más te gusten) y 
# mostrar el penúltimo. ¡Puedes hacerlo como se muestra en los videos o bien investigar cómo funciona el indexing con números negativos!

lista = ["Nacho", 8, "fútbol", [], 3.14]
print(lista[-2])

# Ejercicio 3    Crear una lista vacía, agregar tres palabras con append e imprimir la lista resultante por pantalla. Pista: para crear 
                # una lista vacía debes colocar los corchetes sin nada en su interior. Por ejemplo: lista_vacia = []
lista = []
lista.append("Hola") # Agrego el primer elemento
lista.append("Mundo") # agrego el segundo elemento, a continución del primero
lista.append("Cruel")  # agrego el tercer elemento, a continuaci´pn del segundo
print(lista)

# Ejercicio 4   Reemplazar el segundo y último valor de la lista “animales” con las palabras “loro” y “oso”, respectivamente. Imprimir la lista resultante por pantalla. 
#               ¡Puedes hacerlo como se muestra en los videos o bien investigar cómo funciona el indexing con números negativos! animales = ["perro", "gato", "conejo", "pez"]
animales = ["perro", "gato", "conejo", "pez"]
animales[1] = "loro"  # Reemplazo el segundo elemento "gato" por "loro"
animales[3] = "oso"  # Reemplazo el último elemento "pez" por "oso"
print(animales)


# Ejercicio 5  Analizar el siguiente programa y explicar con tus palabras qué es lo que realiza.
numeros = [8, 15, 3, 22, 7] # Lista con elementos del mismo tipo
numeros.remove(max(numeros)) # max(argumento) devuelve el valor mas grande de un conjunto de números
                             # remove(argumento) borra el elemento que pasamos como argumento
                             # por lo tanto .remove(max(numeros)) borra el mayor valor de la lista numeros
print(numeros)


# Ejercicio 6   Crear una lista con números del 10 al 30 (incluído), 
#               haciendo saltos de 5 en 5 y mostrar por pantalla los dos primeros.
lista = list(range(10,31,5)) # creación de la lista con los valores pedidos
print(lista[0:2]) # imprime los dos primeros valores de la lista


# Ejercicio 7  Reemplazar los dos valores centrales (índices 1 y 2) de la lista “autos” por 
#              dos nuevos valores cualesquiera. autos = ["sedan", "polo", "suran", "gol"]
autos = ["sedan", "polo", "suran", "gol"]
autos[1] = "Virtus" # Reemplazo "polo"
autos[2] = "Kardian"  # Reemplazo "suran"
print(autos) # Imprimo la lista final

# Ejercicio 8   Crear una lista vacía llamada "dobles" y agregar el doble de 5, 10 y 15 
#               usando append directamente. Imprimir la lista resultante por pantalla.
dobles = []
dobles.append(2*5)
dobles.append(2*10)
dobles.append(2*15)
print(dobles) 


# Ejercicio 9  Dada la lista “compras”, cuyos elementos representan los productos 
#              comprados por diferentes clientes:
#              compras = [["pan", "leche"], ["arroz", "fideos", "salsa"], ["agua"]]

#a) Agregar "jugo" a la lista del tercer cliente usando append.
#b) Reemplazar "fideos" por "tallarines" en la lista del segundo cliente.
#c) Eliminar "pan" de la lista del primer cliente.
#d) Imprimir la lista resultante por pantalla

compras = [["pan", "leche"], ["arroz", "fideos", "salsa"], ["agua"]]
compras[2].append("jugo") # Consigna a)
compras[1][1] = "tallarines" # Consigna b)
compras[0].remove("pan") # Consigna c)
print(compras) # Consigna d) """

# Ejercicio 10   Elaborar una lista anidada llamada “lista_anidada” que 
#                contenga los siguientes elementos:
#● Posición lista_anidada[0]: 15
#● Posición lista_anidada[1]: True
#● Posición lista_anidada[2][0]: 25.5
#● Posición lista_anidada[2][1]: 57.9
#● Posición lista_anidada[2][2]: 30.6
#● Posición lista_anidada[3]: False
#Imprimir la lista resultante por pantalla. 
 
lista_anidada = []
lista_anidada.append(15) #● Posición lista_anidada[0]: 15
lista_anidada.append(True) #● Posición lista_anidada[1]: True
lista_anidada.append([25.5]) #● Posición lista_anidada[2][0]: 25.5
lista_anidada[2].append(57.9) #● Posición lista_anidada[2][1]: 57.9
lista_anidada[2].append(30.6) #● Posición lista_anidada[2][2]: 30.6
lista_anidada.append([False]) #● Posición lista_anidada[3]: False
print(lista_anidada) # Imprimo la lista final
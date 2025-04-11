# TP 4. Estructuras repetitivas. Ignacio Carné

"""
# Ejercicio 1 #

for i in range(101):       # Imprime los números enteros de 0 a 100, ambos incluídos.
    print(i)


# Ejercicio 2 #

nro = abs(int(input("Ingrese un número entero, por favor: "))) # Utilizo la funcion abs() por si el usuario ingresa un nro negativo.
cont = 0
while nro >= 1: # Si el resuñtad de dividir el número ingresado por el usuarios entre 10 > 1, entonces entra al ciclo y vuelve a dividir por 10, además suma 1 en cada iteración

    nro = nro / 10 # Divide el número ingresado por el usuario entre 10 
                    #y el resultado es asignado nuevamente a la variable nro.
    cont += 1
print(f"La cantidad de cifras del número ingresado es: {cont}")


# Ejercicio 3 #
 
nro1 = int(input("Ingrese un número entero, por favor: "))  
nro2 = int(input("Ingrese otro número entero, por favor: "))
suma = 0

# Creo un bloque  condicional para representar las posibles combinaciones de 
# números de entrada y considerar los extremos del intervalo, que no estén contenidos.
if nro1<0 and nro2>0:
    for i in range(nro1+1, nro2):
        suma += i
    print(suma)

elif nro1<0 and nro2<0:
    if nro1 > nro2:
        for i in range(nro2+1, nro1):
            suma += i
        print(suma)
    elif nro1 < nro2:
        for i in range(nro1+1, nro2):
            suma += i
        print(suma)

elif nro1>0 and nro2<0:
    for i in range(nro2+1, nro1):
        suma += i
    print(suma)

elif nro1>0 and nro2>0:
    if nro1 > nro2:
        for i in range(nro2+1,nro1):
            suma += i
        print(suma)
    elif nro1 < nro2:
        for i in range(nro1+1,nro2):
            suma += i
        print(suma)                    

# Ejercicio 4 #

nro = int(input("Ingrese números enteros para sumar o 0 (cero) para terminar: "))
suma = 0
while nro != 0:
    suma += nro
    nro = int(input("Ingrese números enteros para sumar o 0 (cero) para terminar: "))
print(f"El total acumulado es {suma}")


# Ejercicio 5 #

nro = int(input("Adivine el número escondico. Su valor está entre 0 y 9: "))
adivina = 7  # Ingreso el número a adivinar
contador = 1
while nro != adivina:
    contador += 1
    nro = int(input(f"Incorrecto!, el número escondido no es {nro}. Ingresá otro:  "))
print(f"Felicitaciones! Adivinaste el número en {contador} intentos.")

# Ejercicio 6 #

for i in range(100, -1, -2):
    print(i)


# Ejercicio 7 #
suma = 0
nro = int(input("Ingrese un número entero positivo: "))
for i in range(0, nro+1):  # Al número ingreasdo por el usuario le sumo 1 para que sea tenido en cuenta.
    suma += i


# Ejercicio 8 #

contador_par = 0
contador_impar = 0
contador_pos = 0
contador_neg = 0
contador_total = 0 

nro = int(input("Ingrese un número entero: "))

while contador_total < 5:  # Condicion a cumplir. En este caso permite ingresar 5 números. Se puede cambiar ese número 5  por cualquier cantidad. 
    # En realidad el usuario ingresa un número mas del que pide la condicion. Los que se analizan sí son los de la condición.
    if nro % 2 == 0:
        contador_par += 1 
        if nro > 0:
            contador_pos += 1       
        elif nro < 0:
            contador_neg += 1
        
    elif nro % 2 != 0:
        contador_impar += 1
        if nro > 0:
            contador_pos += 1       
        elif nro < 0:
            contador_neg += 1
    
    contador_total += 1
    nro = int(input("Ingrese un número entero: "))
    
    
print(f"La cantidad de números pares es: {contador_par}") 
print(f"La cantidad de números impares es: {contador_impar}")
print(f"La cantidad de números positivos es: {contador_pos}")
print(f"La cantidad de números negativos es: {contador_neg}") 
print(f"Total de números ingresados: {contador_total}") 


# Ejercicio 9 #

contador = 0
nro = int(input("Ingrese un número entero: "))
suma = 0
ciclos = 0
while contador < 3:
    suma += nro
    ciclos += 1
    promedio = suma / ciclos
    contador += 1
    nro = int(input("Ingrese un número entero: "))
print(f"La media de los valores ingresados es: {promedio}")"""


# Ejercicoi 10 #
nro = int(input("Ingrese un número: "))
while nro > 0:
    
    resto = nro % 10 # Guardo el resto de la division por 10
    nro = nro // 10  # El número original / 10 va a ser el nuevo número a calcular el módulo.
    print(resto, end = "")  # Imprime sin salto de línea.
    
    
#Esto es una pequeña guia de como escribir codigo en python

# Operadores
# ** Exponente 2 ** 3 = 8 (elevado)
# % Modulo 22 % 8 = 6 (es el resto que se obtiene de la división)
# // Division entera 22 // 8 = 2 (Te devuelve el resultado de la division sin deciamles)
# / Divison 22 / 8 = 2.75
# * Multiplicacion 3 * 5 = 15
# - Resta 5 - 3 = 2
# + Suma 5 + 2 = 7

# Tipo de datos
# Integers (int) numero enteros positivos y negativos
# Foating-pint numbers (float) numero decimales tambien numeros exactos deciamles 1.0
# Strings cualquier dato (no variable) que este entre ''
# 'Alice' + 'Bob' Cunado se ejecute dara 'AliceBob'
# 'a' * 5 Cuando se ejecuto dara 'aaaaa'

# Declarar variables
# variable = 1
# Para imprimir una variable solo tenemos que llamarla y se impirimira sola ejemplo variable

# Funciones
# Las funciones sirven para declarar lo que se va a ultilizar 
# print()
# print ('Hello wolrd') esto se utiliza para monstrar por consola
# input()
# variable = input() con esto introducimos datos desde consola a una variable
# Imprimir un string mas una variable
# print ('Hola' + variable) a la hora de imprimir algo se le puede añadir una variable de esta manera para que nos aparezca su contenido
# len()
# print (len(variable)) con el atributo len podemos decir el numero de caracteres de una palabra o una variable 
# str y int
# print ('hola' + str(int(varibale2) + 1) + ' adios') con str(int(varibale2) + 1) nos dice que es un string por el 1 y ademas matiza que la variable2 va a ser un numero entero
# float
# print ('hola' + str(float(varibale2) + 1) + ' adios') con float(varibale2) nos indica que la variable2 va a ser un numero decimal

# Equivalencia de texto y numero
# Para hacer que haga una equivalencia tenemos que poner == (se pueden comparar todo tipo de datos)
#Ejemplos
# 42 == '42' No, porque uno es un int y el otro un str 
# 42 == 42.0 Si, aunque una es un int y el otro un float 
# 42 == 42 Si, son los dos numeros e iguales 

# Como convertir una variable que contiene un string en un int cuando le asignas un input()
# spam = input ()
# spam es igual a '101'
# Entonces tu le dices que spam = int(spam)
# Y al ejecutarlo te dara que spam es igual a 101
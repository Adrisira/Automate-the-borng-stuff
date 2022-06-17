# Operadores de comparacion
# == Es igual que
# != Es diferente que
# < Es menor que
# > Es mayor que
# <= Es menor o igual que
# >= Es mayor o igual que

# Operadores Booleandos binarios and operator
# True and True = True
# True and False = False
# False and False = False
# False and True = False

# Operadores Booleandos binarios or operator
# True or True = True
# True or False = True
# False or False = False
# False or True = True

# Operadores Booleandos binarios not operator
# not True = False
# not Flase = True

# Se pueden combinar comparadores booleanos y comparadores
# Ejmpplo: (4 < 5) and (5 < 6) = True


# Flow control statements

# If statements
# En Python, una declaración if consiste en seguir
# La palabra clave if
# Una condición (es decir, una expresión que se evalúa como verdadera o falsa)
# Dos puntos
# Comenzando en la siguiente línea y bloque de código sangrado (llamado cláusula if) 
# Ejemplo: 
# If name == 'Alice':
#   print('Hi, Alice.')

# Else statements
# Una instrucción else no tiene una condición, y en el código, una instrucción else siempre consta de lo siguiente:
# La palaba else
# Dos puntos
# Comenzando en la siguiente línea, un bloque de código sangrado (llamado la cláusula else) 
# Ejemplo:
# If name == 'Alice':
#   print('Hi, Alice.')
# else:
#   print('Hello, stranger.')

# Elif statements
# La palabra elif
# Una condicion (una expresion que puede ser falsa o verdadera)
# A partir de la siguiente línea, un bloque de código con sangría (llamado la elif clausula)
# if name == 'Alice':
#   print('Hi, Alice.')
# elif age < 12:
#   print('You are not Alice, Kiddo.')

# While Statements
# La palabra whiel
# Una condicion (una expresion que puede ser falsa o verdadera)
# Dos puntos
# A partir de la siguiente línea, un bloque de código con sangría (llamado la while clausula)
# Ejemplo
# spam = 0
# while spam < 5:
#    print('Hola')
#    spam = spam +1

# Break y continue son usados dentro de los loops como while y for
# Break Statements
# La palabre break
# Ejemplo
# while True:
#    print('Por favor introduce tu nombre')
#    name = input()
#    if name == 'Adrian':
#        break
# print('Gracias')

# Continue Statements
# La palabra continue
# Ejemplo
# while True:
#    print('¿Quien eres?')
#    name = input()
#    if name != 'Adrian':
#        continue
#    print('Hola, Adrian, ¿Cual es tu contraseña?')
#    password = input()
#    if password == 'Josefa05050505':
#        break
# print('Acceso Aceptado')

# For loops and the range() function
# La palabra for
# El nombre de la variable
# La palabra in
# Una llamada al método range () con hasta tres enteros pasados 
# Dos puntos
# A partir de la siguiente línea, un bloque de código con sangría (llamado la for clausula)
# Ejemplo
# for i in range(5):
#    print('Adrian cinco veces (' + str(i) + ')')
# Para ver todos los tipos de usos de range() ir a la carpeta forrange

#Importing modules
# La plabra import
# El nombre del modulo
# Los modulos se importan de uno en uno hacia abajo siempre de la misma manera
# Ejemplo de modulos
# import random Y luego donde lo necesitemos random.randint()
# import sys Y luego donde lo necesitemos sys.exit()
# import os
#import math
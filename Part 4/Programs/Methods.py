spam = ['hello', 'hi', 'howdy', 'heyas']
# Todo esto tambien se puede ejecutar de manera individual ya que se queda guardado en la memoria, por ejemplo, cuando introduxcamos
# spam.sort(), solo tenemos que llamar a spam. 
def index():
    print(spam.index('hello')) # Te dice donde esta el elemento en la lista.

def append():
    print(spam.append('moose')) # Añade un elemento al final de la lista.

def insert():
    print(spam.insert(1, 'chicken')) # Añade un elemento en la posicion que le digamos.

def remove():
    print(spam.remove('hello')) # Borra el elemento que le digamos, pero solo ese, esto quiere decir que si se repite, solo te borra
    # el primero, el segundo no.

def sort():
    print(spam.sort()) # Ordena la lista, de menor a mayor en números y por le abecedario con la primera letra de la palabra.
    print(spam.sort(reverse=True)) # Ordendar al reves.
    # Recuerda que no puedes ordenar una lista que tenga int y str a la vez.
    print(spam.sort(key=str.lower)) # Es un simple ejemplo para ordenador primera las minusculas y luego las mayusculas.

def reverse():
    print(spam.reverse()) # Le da la vuelta a la lista.
    
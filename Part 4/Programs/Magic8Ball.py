import random

mensajes = [
    'It is certain',
    'It is decidedly so',
    'Yes definitley',
    'Reply hazy try again',
    'Ask again later',
    'Concentrate and ask again',
    'My reply is no',
    'Outlook not so goog',
    'Very doubtful'
]

print(mensajes[random.randint(0, len(mensajes) -1)]) # No te asustes de esto es muy simple, basicamente vas a obtener un numero entre
# 0 que es el primer elemento de la lista y -1 que es el ultimo, imprime el que te toque 
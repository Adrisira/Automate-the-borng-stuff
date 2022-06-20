catNames = [] # Declaramos siempre primero la lista 

while True:
    print('Introduce el nombre del gato ' + str(len(catNames) + 1) + ' (O introduce nada para salir.):') # Aqui nos dice el tamaño de la lista por eso al imprimirlo sale gato 1 o gato 2
    name = input()
    if name == '':
        break
    catNames = catNames + [name] # Concetenacion de las listas

print('Los nombres de los gatos son:')
for name in catNames:
    print('' + name)
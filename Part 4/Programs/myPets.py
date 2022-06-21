# Ejemplo de como utilizar los operadores in and not con listas.

def mascotas():
    myPets = ['Zophie', 'Pooka', 'Fat-tail']
    print('Enter a pet name:')
    name = input()
    if name not in myPets:
        print('Io not haver a pet named ' + name)
    else:
        print(name + ' is my pet.')

mascotas()
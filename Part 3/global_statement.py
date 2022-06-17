from pkg_resources import EGG_DIST


def spam():
    global eggs 
    eggs = 'spam' # Global scope por lo de arriba

def bacon():
    eggs = 'bacon' # Local scope

def ham():
    print(eggs) # Global scope

eggs = 42 # Global scope pero se omite porque la que esta en la funcion tiene prioridad al ir antes en la ejecucion
#print(eggs) Como siempre tiene prioridad lo que se ejecute antes, si ambos son global scope
spam()
#print(eggs)

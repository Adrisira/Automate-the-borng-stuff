# Local Scopes Cannot Use Variables in other Local Scopes
def spam(): # Local scope
    eggs = 99 #Local varaible
    bacon()
#   print(eggs) Prueba a ejecutarlo dos veces en ambas funciones 

def bacon(): # Local scope
    ham = 101 # Local variable
    eggs = 0  # Local variable
    print(eggs)

#spam()

# Aunque vemos que la varibale eggs esta definida dos veces en dos funciones diferentes, la que se imprime es donde esta el print y la otra se oprime por compelo



# ----------------------------------------------------------------------------------------------------------------------------------------------------------------- #

# Local Variables Cannot Be Used in the Global Scope
def huevos(): # Local Scope 
    huevos = 99999 # Local Variable

#huevos()
#print(eggs) Global Scope

# ----------------------------------------------------------------------------------------------------------------------------------------------------------------- #

# Gobal Variables Can Be Read froma a Local Scope
def jamon(): #Local Scope
    print(jam)
jam = 9999 # Global Scope
#jamon() 
#print(jam) Global Scope
# Ejemplo típico del bucle for con listas, muy practico 

def suministros():
    supplies = ['pens', 'staples', 'flametheowers', 'binders']
    for i in range(len(supplies)):
        print('Index ' + str(i) + ' in supplies is: ' + supplies[i])
    
suministros()
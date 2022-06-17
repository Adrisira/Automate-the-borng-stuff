import time
import sys

indent = 0 # Cuantos espacios de sangrias
indentIncreasing = True # Si la sangria esta aumentando o no

try:
    while True:
        print(' ' * indent, end='') #Tienes que dejar en el string un espacio porque sino no hay movimiento 
        print('********')
        time.sleep(0.1) #Pausa de 1/10 de segundo

        if indentIncreasing:
            # Incrementa el numero de espacios
            indent = indent + 1
            if indent == 20:
                #Cambia la direccion
                indentIncreasing = False
        

        else:
            # Disminuye el numero de espacios
            indent = indent - 1
            if indent == 1:
                #Cambia de direccion
                indentIncreasing = True


except KeyboardInterrupt:
    sys.exit()
    # Recuerda pulsar control + c para pausar el programa 
     
while True:
    print('¿Quien eres tu?')
    name = input()
    if name == 'Adrian':
        continue
    print('Hola, Adrian. ¿Cual es tu contraseña?') 
    #A partir de aqui hay un error que nose identificar, el loop se reinicia sin sentido cuando lo hago continuar y vuelve a preguntarte tu nombre pero tambien imprime el ultimo print
    contraseña = input()
    if contraseña != 'contraseña':
        break
print('Acceso garantizado')
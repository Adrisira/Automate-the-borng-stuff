#Este codigo explica como funcionan los call stack en las funciones en python, basicamente cuando definimos una funcion esta se ejecuta hasta que es referenciada a 
# otra donde ejecuta esta segunda entera y luego vuelve a seguir ejecutando a la primera

def a():
    print('a() starts')
    b()
    d()
    print('a() retunrs')

def b():
    print('b() starts')
    c()
    print('b() returns')

def c():
    print('c() starts')
    print('c() returns')

def d():
    print('d() starts')
    print('d() returns')


a() #Recuerda siempre llamar a la funcion 
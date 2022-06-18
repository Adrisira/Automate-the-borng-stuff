# Wirte a function named collatz() thas has one parameter named number. If number even, then collatz() shoul print number // 2 and return this value.
# If number is odd, then collatz() shlound print and return 3 * number + 1
# Then write a program that lets the user type in an integer and that keep calling collatz() on that number until the function returns the value 1.

def collatz(number):
    
    if number % 2 == 0:
        print(number // 2)
        return number // 2

    elif number % 2 == 1:
        result = 3 * number + 1
        print(result)
        return result
        

try:
    number = input("Introduce un numero: ")
    while number != 1:
        number = collatz(int(number))
except ValueError:
    print('Introduce un valor valido')
    
collatz(number)

# El ejercicio en teoria está bien pero, nose porque en vez de terminar en 1, termina en cuatro, no tiene sentido, y como ahora no entiendo porque es así, lo dejare para más adelante cuando lo entienda.
import random

def getAnswer(answerNumber):
    if answerNumber == 1:
        return 'It is certain'
    elif  answerNumber == 2:
        return 'It is decidedly so'
    elif  answerNumber == 3:
        return 'Yes'
    elif  answerNumber == 4:
        return 'Reply hazy try again'
    elif  answerNumber == 5:
        return 'Ask again later'
    elif  answerNumber == 6:
        return 'Concentrate and ask again'
    elif  answerNumber == 7:
        return 'My reply is no'
    elif  answerNumber == 8:
        return 'Outlook not so goo'
    elif  answerNumber == 9:
        return 'Very doubtful' 

r = random.randint(1, 9) #Esto es simplemente una variable que almacena un numero aleatorio entre 1 y 9
print(getAnswer(r)) # Aqui imprimimos la funcion getAnswer que tiene atribuida el argumento answerNumber combinado con r y nos devolvera el str con el que concuerde el numero

# Este codigo se puede escribir de dos manera mas

# Segunda manera
#r = random.randint(1, 9)
#fortune = getAnswer(r)
#print(fortune)

# Tercera manera
#print(getAnswer(random.randint(1, 9)))
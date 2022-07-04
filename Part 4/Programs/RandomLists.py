import random

def choice():
    pets = ['Dog', 'Cat', 'Moose']
    print(random.choice(pets))
   
def shuffle():
    people = ['Alice', 'Bob', 'Carol', 'David']
    random.shuffle(people)
    print(people)

choice()
shuffle()
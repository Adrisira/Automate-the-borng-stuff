def Indiviadual():
    spam = ['cat', 'bat', 'rat', 'elephant']
    print('The ' + spam[1] + ' ate the ' + spam[0] + '.')

def TwoList():
    spam = [['cat', 'bat'], [10, 20, 30, 40, 50]]
    print(spam[0][1]) #En el primer corchete decirme que lista queremos y en el segundo el valor de esta

def Negative():
    spam = ['cat', 'bat', 'rat', 'elephant']
    print(spam[-1])

def GettingList():
    spam = ['cat', 'bat', 'rat', 'elephant']
    print(spam[0:4]) # Es lo mismo que [:4], [:] con esto se imprime entera

def Changing():
    spam = ['cat', 'bat', 'rat', 'elephant']
    spam[1] = 'Dog'
    print(spam)

def Length():
    spam = ['cat', 'bat', 'rat', 'elephant']
    len(spam)

def Concatenation():
    spam = ['cat', 'bat', 'rat', 'elephant']
    print(spam * 3)
    spam = spam + ['Dog', 'moose']
    print(spam)

def remove():
    spam = ['cat', 'bat', 'rat', 'elephant']
    del spam[2]
    print(spam)
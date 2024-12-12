import numpy as np

a = []

with open("input_2.txt", 'r') as file:
    a= file.read().splitlines()
    
a = list(map(lambda x: x.split(' '), a))

def test(lista):
    direction = 0
    for i in range(len(lista)-1):
        dif = int(lista[i])-int(lista[i+1])
        if (dif == 0) or (abs(dif)>3):
            return False
        direction_old = direction
        direction = abs(dif)/dif
        if (direction_old!=direction) and (direction_old!= 0):
            return False
    return True

def test_2(lista):
    if test(lista):
        return True
    for i in range(len(lista)):
        if test(lista[:i] + lista[i+1:]):
            return True
    return False

b = list(map(lambda x: test(x), a))
    
sum(b)

c = list(map(lambda x: test_2(x), a))

sum(c)

lista=a[500].copy()

test_2(lista)
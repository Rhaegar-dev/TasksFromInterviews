'''
Задана функция pair(a,b), которая создает пару, а first(pair) и second(pair) возвращает первый и последний элемент объекта, т.е. first(pair(10,12) возвращает 10, а second(pair(10,12) возвращает 12. 

Задана следующая имплементация функции pair:

def pair(a, b):
    return lambda f : f(a, b)

Напишите имплементацию методов first и second
'''

def pair(a, b):
    return lambda f: f(a, b)

def first(f):
    z = lambda x, y: x
    return f(z)

def second(f):

z = lambda x, y: y
    return f(z)
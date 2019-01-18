#!/usr/bin/env python

def add(a,b):
    return a+b

print(add(3,6))

input_params = (4,7)
print(add(input_params[0], input_params[1]))

print(add( *input_params ))

d_params = {'a':10, 'b':12}
print(add(b=12, a=10))
print(add(a=d_params['a'], b=d_params['b']))
print(add( **d_params ))

persona = {'name':'Leszek',
            'surname':'Tarkowski',
            'age':41,
            'city':'KRK'}

def print_person(name, surname, age, *args, **kwargs):
    print(name, surname, age)

print_person(**persona)


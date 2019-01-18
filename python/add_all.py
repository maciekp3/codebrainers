#!/usr/bin/env python



def add_all(*args):
    sum = 0
    for i in args:
        sum += i
    return sum

print(add_all(1,2,3,4,5))
print(add_all(1,2,3))

l= (1,2,3,4,5,6)
print(add_all(*l))

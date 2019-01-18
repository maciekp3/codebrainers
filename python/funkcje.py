#!/usr/bin/env python
#side effects

l = 10

def add5(a):
    return a + 5

# def addinplace5(a):
#     global l
#     a += 5

print(add5(10))

#addinplace5()
#print(l)

#this causes side effect
def add_element(l):
    l.append(5)

li = []

add_element(li)
add_element(li)
print(li)



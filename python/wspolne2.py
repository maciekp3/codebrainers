#!/usr/bin/env python

lista1 = [x**2 for x in range(1,100000)]
lista2 = [x**3 for x in range(1,100000)]

print(lista1,lista2)

print("dlugosc listy pierwszej{}, a drugiej to {}".format(len(lista1), len(lista2)))
print("dlugosc listy pierwszej", len(lista1), ",a drugiej to", len(lista2))

wspolne = []

# to jest petla po elementach listy lista1
for el in lista1:
    #wpisyjemy element listy
    if el in lista2:
        wspolne.append(el)

#dostalismy wyniki ale  wolno
print("Elementy wspólne list to:", wspolne, "jest ich ", len(wspolne))

for el in lista1:
    #wpisyjemy element listy
    if el in lista2:
        print(el)

# sprobojemy przez sety

set1 = set(lista1)
set2 = set(lista2)
 
wspolne = set1 & set2
print("Elementy wspólne list to:", wspolne, "jest ich ", len(wspolne))

for el in wspolne:
    print("wynik działania: {}, to szescian {} oraz kwadrat". format(el, int(el**(1/3)), int(el**(0,5)) 
    


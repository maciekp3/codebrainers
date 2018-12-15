#!/usr/bin/env python

lista1 = [x**2 for x in range(1,100)]
lista2 = [x**3 for x in range(1,50)]

print(lista1,lista2)

print("dlugosc listy pierwszej{}, a drugiej to {}".format(len(lista1), len(lista2)))
print("dlugosc listy pierwszej", len(lista1), ",a drugiej to", len(lista2))

wspolne = []

# to jest petla po elementach listy lista1
for el in lista1:
    #wpisyjemy element listy
    if el in lista1:
        wspolne.append(el)
    else:
        continue

#definiujemy liczbe
liczba = 30

#instrukcja warunkowa. Sprawdzamy czy liczna wystepuje w lista2
if 25 in lista2:
    #jeśli tak to wypisz
    print(liczba, " jest w lista2")
else :
    #jesli nie to wpisz
    print(liczba, " nie ma w lista2")

#!/usr/bin/env python

""" Program losuje liczbe całkowita z zakresu 1 do 100.
Uzytkownik na 7 próbna zgadnięcie tej liczby."""

from random import randint

zagadka = randint(1,100)

liczba = "0"
proba = 0
maksymalna_prob = 3


while(liczba != zagadka):
    print("Podaj liczbę:")
    liczba = int(input())
    proba += 1

    if liczba == zagadka:
        print("Sukces, zgadłeś w {1} próbie {0}!". format(zagadka, proba))
    else:
        if liczba > zagadka:
            print("wybierz mniejszą liczbe")
        else:
            print("wybierz wiekszą liczbe")
        #print("Niestety! Wylosowano liczbe {}.". format(zagadka))
        if proba >= maksymalna_prob:
            print("Nie udało się w {1} probach. Wylosowano liczbe {0}.". format(zagadka, proba))
            break

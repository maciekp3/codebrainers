#!/usr/bin/env python

def sprawdz_typ(variable):
    print("Zmienna jest typu", type(variable), "i zawiera:'", variable, "'.", sep=" _ ", end= '\n kaboom!!!\n')


zmienna = "jest sobota i uczymy sie Pythona"
sprawdz_typ(zmienna)

zmienna = 35//5
sprawdz_typ(zmienna)

zmienna = zmienna/387
sprawdz_typ(zmienna)

liczba = 60
sprawdz_typ(liczba)

zmienna = zmienna + liczba
sprawdz_typ(zmienna)

napis = "To jest zmienna znakowa tj. string"
sprawdz_typ(napis)

zmienna = str(zmienna) + " " + napis
sprawdz_typ(zmienna)
#!/usr/bin/env python

def wyszukiwanie_slow(slowo, gdzie):
    for line in gdzie:
        for word in line.split():
            if slowo in word:
                print(word, line)

plik = open("../../../linux/texty/william.sheakespeare", "r")

imiona = ["Hamlet", "Macbeth", "Ophelia", "Henry"]

text = william.sheakespeare

for imie in imiona:
    wyszukiwanie_slow(imie)

grep -c -w $name $text

echo -n $imiona ":"

if not plik.closed:
    plik.closed

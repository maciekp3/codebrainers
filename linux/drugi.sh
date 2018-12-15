#!/usr/bin/env bash
mkdir -p 2018.12.15.cwiczenia
cd 2018.12.15.cwiczenia

echo "To jest nasz skrypt"

#przekierwianie do pliku przez > gdy nadpisujemy lub >> gdy dodajemy do końca
echo "A to zostanie zapisane w pliku stdout.txt o godzinie " $(date) >> stdout.txt

echo "Sprawdzimy czy rzeczywiście plik stdout.txt zawiera nasz zapis"

date

more stdout.txt
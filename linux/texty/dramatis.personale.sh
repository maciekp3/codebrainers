#!/usr/bin/env bash

#grep -c Hamlet william.sheakespeare
#grep -c Ophelia william.sheakespeare
#grep -c Macbeth william.sheakespeare
#grep -c Lady william.sheakespeare
#grep -c "Lady\ Macbeth" william.sheakespeare
#grep -c 'Lady\ Macbeth' william.sheakespeare
#grep -c Lady\ Macbeth william.sheakespeare


#definiujemy plik
text=william.sheakespeare

#definiujemy liste imion
names="Hamlet Macbeth Ohphelia Henry"

#robimy petle po kolejnym  imionach
for name in $names
#zawartosc petli pod spodem
do
# wyslwietlamy nazwe zmiennej
echo -n $name ": "
# sprawdzamy ile razy zmienna wystepuje w pliku
grep -E -c $name $text
grep -E -c -w $name $text
done

echo $text

text="praca skończona"

echo $text

wc -l william.sheakespeare    

head -15 william.sheakespeare

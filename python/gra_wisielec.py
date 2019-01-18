#!/usr/bin/env python3

import random
import sys

print("Witaj w WISIELCU!")

with open("words_alpha.txt", "r") as f:
    lines = f.readlines()   
    nl_number = len(lines)
    rand_line = random.randint(0, nl_number)
    word = lines[rand_line-1].strip()

word_length = len(word)
covered = "_"*word_length
chances = 10

print (covered, "[", word_length, "liter ]")
print ("Podaj literki by zgadnąć słowo.\n")


while chances:
    letter = input ("Twoja literka: ") 
    if letter in word:
        for i in range(len(word)):
            if letter == word[i]:
                covered_list = list(covered)
                covered_list[i] = word[i]
                covered = "".join(covered_list)
            if not "_" in covered:
                print("WOOHOOO! Wygrałeś!")
                sys.exit("Szukanym słowem było: "+covered)
    else:
        chances -= 1
        print ("Zła literka. Tracisz szansę (masz obecnie:", chances, "szans)")
    print(covered)

print ("PRZEGRAŁES. Szukanym słowem było:", word)
# import dict_eng
# losowanie
# _ _ _ _ _
# j
# j _ _ _ _ 
# ile szans 5 jak zgadł to nie zmienia ilości szans

# read english words py
# word alpha.txt

# import random
# random.randint(0, len(dict))

# letter = input ("give mi a letter: ")
# print(letter)

# czy litera wystepuje w słowie i na którym miejsciu.

# funkcja która zwraca słowo

# funkcja która pokazuje czy litera wystepuje w słowie i ile razy
#!/usr/bin/env python

import random

def load_dictionary(fname):
    words = []
    for line in open(fname):
        words.append(line.strip())
    return words

def draw_word(words):
    choice = random.randint(0, len(words))
    return word[choice]

def get_char(words):
    while True:
        char = input("guess one character")
        if len(char) == 1 and char.isalpha() and char not in good_chars:
            char = char.lower()
            return char

def print_word(word, good_chars):
    for char in word:
        if char in good_chars:
            print(char, end='')
        else:
            print("_", end='')
    print()

def char_in_word(char, word):
    return char in word

def check_win(word, good_chars):
    for char in word:
        if char not in good_chars:
            return False
    return True


if __name__ == "__main__":
    words = load_dictionary("words_alpha.txt")
    word = draw_word(words)
    good_chars = []
    chances = 10
    while chances:
        print_word(word, good_chars)
        char = get_char(good_chars)
        if char_in_word(char, word):
            good_chars.append(char)
            if check_win(word, good_chars):
                break
        else:
            chances -= 1
            print("you have{} chances left".format(chances))
    print("the word was {}". format(word))


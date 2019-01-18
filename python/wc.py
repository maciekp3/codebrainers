#!/usr/bin/env python3

import sys

#if len(sys.argv) > 1
#print(sys.argv)
char = 0
lines = 0
words = 0


try:
    f = open(sys.argv[1])
    for line in f:
        lines += 1
        char += len(line)
        words += len(line.split())

    print(lines, words, char, sys.argv[1])
        
except IndexError:
    print("too few arguments")
except FileNotFoundError:
    print("wrong filenme")

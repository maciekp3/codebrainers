#!/usr/bin/env python

for line in open("hosts.txt"):
    first = line.split('@')
    name = first[0].split(".")
    if len(name) <2:
        name.append(" ")
    print("{:<15} {:<15} email: {}".format(name[0], name[1], first[1]))

for line in open("hosts.txt"):
    try:
        name, addres = line.split('@')
        firstname, surname = name.split(".")
        print(firstname, surname, addres)
    except ValueError:
        pass
#!/usr/bin/env python

def print_board():
    for i in range(0,3):
        for j in range(0,3):
            print map[2-i][j],
            if j != 2:
                print "|",
        print ""


def check_done():
    for i in range(0,3):
        if map[i][0] == map[i][1] == map[i][2] != " " \
        or map[0][i] == map[1][i] == map[2][i] != " ":
            print turn, "wygrales!"
            return True

    if map[0][0] == map[1][1] == map[2][2] != " " \
    or map[0][2] == map[1][1] == map[2][0] != " ":
        print turn, "wygrales!"
        return True

    if " " not in map[0] and " " not in map[1] and " " not in map[2]:
        print "remis"
        return True


    return False

turn = "X"
map = [[" "," "," "],
       [" "," "," "],
       [" "," "," "]]
done = False

while done != True:
    print_board()

    print turn, "sie teraz rusza"
    print

    moved = False
    while moved != True:
        print "Wpisz numer pola miedzy 1-9, ponizej sa rozpisane numery pol..."
        print "7|8|9"
        print "4|5|6"
        print "1|2|3"
        print

        try:
            pos = input("Wybierz: ")
            if pos <=9 and pos >=1:
                Y = pos/3
                X = pos%3
                if X != 0:
                    X -=1
                else:
                     X = 2
                     Y -=1

                if map[Y][X] == " ":
                    map[Y][X] = turn
                    moved = True
                    done = check_done()

                    if done == False:
                        if turn == "X":
                            turn = "O"
                        else:
                            turn = "X"


        except:
            print "tylko warosci liczbowe"
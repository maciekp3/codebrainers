#!/usr/bin/env python

def draw_board(game):
    for i in range(3):
        for j in range(3):
            print(game[i][j], " " , end='')
        print()
    print()

def put_mark(player, position, game):
    x, y = position
    game[y-1][x-1] = player

if __name__ == "__main__":
    game = [["_", "_", "_"],["_", "_", "_"],["_", "_", "_"]]
    draw_board(game)
    put_mark("o", (1,1), game)
    put_mark("o", (1,2), game)
    draw_board(game)


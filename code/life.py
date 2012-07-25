#!/usr/bin/env python

# This is copied from Jack Diederich's enjoyable talk
# http://pyvideo.org/video/880/stop-writing-classes

# I changed it only by making the board toroidal and printing the
# board out on each iteration and putting three well-known entities in
# the initial board.

from __future__ import print_function
import itertools, time

size = 15

def neighbours(point):
    x, y = point
    yield x, (y+1)%size
    yield x, (y-1)%size
    yield (x+1)%size, (y+1)%size
    yield (x+1)%size, y
    yield (x+1)%size, (y-1)%size
    yield (x-1)%size, (y+1)%size
    yield (x-1)%size, y
    yield (x-1)%size, (y-1)%size

def advance(board):
    newstate = set()
    # only currently-live points and neighbours of currently-live
    # points need be considered.
    recalc = board | set(itertools.chain(*map(neighbours, board)))
    for point in recalc:
        # how many neighbours?
        count = sum((neigh in board)
                    for neigh in neighbours(point))
        # if 3 neighbours, or 2 + self, live!
        if count == 3 or (count == 2 and point in board):
            newstate.add(point)
    return newstate

def print_board(board):
    print("-" * (2*size+3)) # print top border
    for x in range(size):
        print("| ", end="") # print left-hand border
        for y in range(size):
            if (x, y) in board:
                # living cell
                print("* ", end="")
            else:
                # dead cell
                print("  ", end="")
        print("|") # print right-hand border
    print("-" * (2*size+3)) # print bottom border

def main():
    glider = set([(0, 0), (1, 0), (2, 0), (0, 1), (1, 2)])
    blinker = set([(12, 2), (11, 2), (10, 2)])
    beacon = set([(2, 10), (3, 10), (2, 11), (4, 13), (5, 12), (5, 13)])
    board = glider | blinker | beacon

    for i in range(1000):
        print_board(board)
        board = advance(board)
        time.sleep(0.1)

if __name__ == "__main__": main()

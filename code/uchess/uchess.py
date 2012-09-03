#!/usr/bin/env python

from __future__ import print_function

pieces = "King Queen Rook Bishop Springer Pawn".split()

white_pieces = [piece[0] for piece in pieces]
black_pieces = [piece.lower() for piece in white_pieces]

def board_from_string(s, to_move="White",
                      may_castle=(False, False), en_passant=None):
    """Given a string s representing a board graphically, convert it
    to a dict-representation. The to_move argument specifies which side
    is to move. The may_castle argument specifies whether castling is
    allowed for both sides. The en_passant argument, if not None, gives
    the column number of a pawn which the to_move side may capture
    en-passant."""
    d = {}
    i = 7
    for line in s.split("\n"):
        if len(line) < 8:
            continue
        for j, c in enumerate(line):
            if c not in ". ":
                d[i, j] = c
        i -= 1
    d["to_move"] = to_move
    d["may_castle"] = may_castle
    d["en_passant"] = en_passant
    return d

def print_board(d):
    for i in range(7, -1, -1):
        for j in range(8):
            if (i, j) in d:
                s = d[i, j]
            else:
                s = "."
            print(s, end="")
        print("")

            
initial = board_from_string("""
rsbqkbsr
pppppppp
........
........
........
........
PPPPPPPP
RSBQKBSR
""")


non_pieces = "to_move", "en_passant", "may_castle"

def successors(d):
    retval = []
    to_move = d["to_move"]
    if to_move == "Black":
        d = rotate(d)
    for pos, piece in d.items():
        if piece in non_pieces: continue
        if is_white(piece):
            retval.extend(piece_successors[piece.lower()](d, pos))
    if to_move == "Black":
        retval = [rotate(d) for d in retval]

    # TODO this might be the right place to put checking for checks etc
    return retval

def rotate_board(d):
    """Rotate the board so that it is white to move, playing
    upwards."""
    d["may_castle"] = d["may_castle"][1], d["may_castle"][0]
    d["to_move"] = other_side(d["to_move"])
    for i in range(8):
        for j in range(4):
            rot_ij = rotate(i, j)
            if (i, j) in d and rot_ij in d:
                d[i, j], d[rot_ij] = d[rot_ij], d[i, j]
            elif (i, j) in d:
                d[rot_ij] = d[i, j]
                del d[i, j]
            elif rot_ij in d:
                d[i, j] = d[rot_ij]
                del d[rot_ij]
    return d

def rotate(i, j):
    return 7-i, 7-j

def pawn_successors(board, pos):
    """Assumes that the board has been "rotated" so we are playing
    upward."""
    piece = board[pos]
    i, j = pos
    assert piece.lower() == "p"

        

def is_white(p):
    return p.is_lower()

def other_side(s):
    if s == "White": return "Black"
    if s == "Black": return "White"

piece_successors = {
    "p": pawn_successors,
    # "s": springer_successors,
    # "b": bishop_successors,
    # "r": rook_successors,
    # "q": queen_successors,
    # "k": king_successors
    }
    

print_board(initial)
print()
print()
print_board(rotate(initial))

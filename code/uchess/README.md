uchess
======

I was looking at Tiny Chess [http://js1k.com/2010-first/demo/699], an
amazing 1018b of Javascript which plays a pretty respectable game. I
realised that a chess implementation in Python ought to be within my
reach. I guessed that Tiny Chess probably used some variation of an
expanding search algorithm, perhaps similar to that presented by Peter
Norvig in Udacity CS212. So I decided I'd have a go.

I'm going to reuse Norvig's very neat code for the search
algorithm. That means I need to write a function which, given the
state of the chess board, figures out the possible moves. Without the
1024b restriction I'll be able to add in castling and en-passant. 

I also need to do some evaluation of how good a board is, and I'm
hoping I can steal that from Tiny Chess.

Then I need to modify the search algorithm to take account of the
opposition's moves (some variant of minimax) -- I think one of
Norvig's earlier examples does this. I also need to set it up to
return the best-expected move, when a mate is not possible. Another
possibility: Monte Carlo Tree Search, ie carry out many random moves
after each possible move, and choose the best.


---
title: "Chess as a Microcosm of Intelligence and AI"
author: James McDermott
date: 2024/03/02
---


When Deep Blue beat Kasparov in 1997, I think a lot of people thought that chess became less interesting. No longer a pinnacle of human intelligence. 

But over the past few years, I started to realise that chess remains super interesting. Thinking about humans playing chess helps me think about human intelligence. And thinking about AIs playing chess helps me think about how more general and powerful AIs could be constructed to act in the real world.


# Logical abstractions versus the real world

From one point of view, there are three different "levels" of problem humans might be faced with.

1. The real world provides us with raw, sensory data. This is far too large and open-ended, and goals too far removed in time, for us to use any type of logic, like a game tree search. We deal with it either by acting on instinct, or by transforming problems as in 2:
2. Some types of real-world problems, when decomposed and abstracted at the right level, become tractable. I have tasks such as *buy bread*, *pick my wallet up from the table*, *walk to the shop*, *put on my shoes* - what order can I do these in?
3. A nice, constrained, discrete space with easily-specified goals - but the tree is still much too large to try all of it.

We invented chess as an example of (3), because it tickles the part of the brain that enjoys solving problems like 2, but substantially harder.

Game tree algorithms used to seem far too abstract to ever be generalisable to AIs which have to act in real life. But now, we're starting to see that a clear path towards general AI could be to use language models to help formalise situations into games, and then  use exploration of the game tree.

Chess demonstrates the grey areas between computation, pattern recognition, planning, and insight / intelligence. The oldest chess algorithms used simple heuristics for evaluating the board and didn't prune the tree search: they just evaluated up to a certain, low, depth. Later algorithms used better heuristics for both. Modern chess engines use pattern recognition, trained by deep learning, for sophisticated evaluation, and this is already a strong engine by itself: just evaluate each possible move to depth one and choose the maximum evaluation. The intelligence has moved from the purely logical tree search, to heuristic tree search and evaluation, to pattern recognition (learned, inscrutable, basically "thinking with your eyes").


# Abilities needed for chess and for life

A basic tree-search requires a few main abilities:

1. Produce candidate moves - let's say, moves which are not obviously bad.
2. For each candidate move, mentally make that move.
3. Evaluate the resulting position to say which side is winning and by how much. If it's not clear, go to 1.


## Seeing separable sub-problems

But from another point of view, there are a myriad of abilities. One starts to see the board as presenting a series of individual sub-problems to be solved and opportunities to be seized. For example, my pawn is weak, how can I defend it? My knight is on a bad square. His king is on the long diagonal where I could try to attack it. All of them are linked in two ways:

1. Obviously, any move on the board intended to have an effect on one sub-problem can affect the situation elsewhere.
2. Spending a move on one sub-problem costs the opportunity to address some other.

In this view, we don't just evaluate the board holistically as before. The candidate moves that come to mind aren't selected from a global pool, but rather appear while thinking about a specific sub-problem. 

And human intelligence is like this too. It helps a lot to focus on a specific sub-problem at a time, if we can plausibly see the entire problem space presented by the world as being cut up into somewhat separable sub-problems. 

Making a general-purpose AI which sees how to cut up a large, open-ended problem space into separable sub-problems is something good old-fashioned AI totally failed at. But perhaps LLMs' ability to confidently suggest a focus and a plan in a given context, mostly by imitating similar examples in training data, is the closest we've ever come to this.

## Prioritisation

A central ability in chess and in life is prioritisation, mentioned in (2) above. When exploring the tree, the chess master is constantly deciding whether a particular position which could be reached is clear. That is, when one side or the other has a large, clear-cut, stable advantage in a position, there is no need to explore it further. The game tree can be pruned - that doesn't mean deleting nodes which we previously formed, rather it means we don't need to create any further descendents of that position.

Prioritisation is also involved in another situation. When the player has explored a certain branch to some depth, they might decide it's time to explore another branch, so they back-track. They need good recall to store the fruits of exploring one branch, so that they can later explore it more, either if they decide it's still worth it during the same move, or during a later move if the same branch is still reachable.

The human also transfers knowledge from exploration of one subtree to exploration of another. The basic case is when two different lines converge further down the tree by transposition. But even if there is not an exact transposition, some knowledge transfer is often still possible.


# Introspection and types of thinking

Humans are highly introspective. Chess teachers are always thinking about thinking, and encouraging their pupils to do it. And chess *commentators* sometimes give us a good sense of the outcome of this. Just look at the vocabulary they use for different types of thinking:


* There is *blitzing out* moves, that is playing almost instantly, in order to save time for later. This happens especially when playing from preparation in the opening.
* There is *blitzing out* for a different reason, because you are under time constraints. This is based mostly on pattern recognition, sometimes in a quite reactive mode, but with a background "thread" of longer-term thinking.
* There is the mechanical *checks, captures and threats* type of checklist.
* There is *calculating a line*, where the player attempts to follow a sequence and all reasonable variations as far as is needed. How far is needed? Which variations count as reasonable?
* There is *going into the tank*, which means making a commitment to evaluating many different lines, which could include transpositions into the same position, and includes long-term considerations. Going into the tank means a 10-minute think or more for one move. It happens when a move is very commital. 

So, it suggests a tantalising idea: *introspective AI*. What would it mean? How could we make it happen?


# Communication

Something that is really interesting to watch is the new Team Chess Battle, and previous doubles formats like Mind and Hand. What's cool here is that in order to function as a team, the players have to verbalise their thoughts, which can be slow compared to the flashes of imagery which are happening inside their brains. This is another great microcosm which gives an insight into human intelligence, and maybe into possible AI. If AIs use a kind of "language of thought", that is they use something like natural language for self-talk and for thinking and planning internally - and I think they will, but I'll write more about it another time - then serialising for communication to peers might not slow them down so much compared to that. But if they also have specialist modules, like constraint programming solvers, or minimisers, for solving specific problems which have been formalised - which I think they will - then that's the part which would be extremely fast internally, and would be massively slowed down by serialisation. 

We sometimes hear speculation that AIs could communicate by direct transfer of encoded vectors. After all, digital stuff can be copied perfectly and quickly, and seems to have a huge advantage over serialisation in natural language as used by humans. But I'm not so sure. Obviously data as such can be transferred by direct copy. And if (for example) one chess-playing AI explored a tree, they could communicate a *summary* of their results as data. The problem comes when trying to communicate something more sophisticated, like opinions on how "dark forest"-esque, or how double-edged, or how drawish, a certain line might be. A direct copy of part one AI's state vector or weight vector just might not be readable by another. (Two identical AIs, with identical state vectors, would not be useful, so they would definitely be different.) The neurons that read such vectors are inherently fragile (eg, two identical algorithms could be implemented in the same architecture with *permuted*, incompatible weights). Natural language is robust. I think there's a possibility AIs could end up using some form of natural language as a robust communication medium.


# Us against the AI, in the real world

One last interesting angle: in Chess 960, where the starting position is different from standard, we see very interesting and different behaviours from normal chess. Some players are much weaker than in normal chess and that's quite revealing. 

But my favourite observation is this. In Chess 960, players spend a lot more time on the first few moves, because it's possible to lose very suddenly with one wrong move in an opening position you don't understand. Something we should bear in mind if we ever consider trying to outwit a very powerful AI.
---
layout: post
title: An interesting equivalence between two state-of-the-art symbolic regression systems
---

An interesting equivalence between two state-of-the-art symbolic regression systems
========

I was lucky enough to be present at the presentation of two
state-of-the-art genetic programming symbolic regression systems --
Trent McConaghy's Fast Function Extraction at GPTP 2011 and Leonardo
Vanneschi and colleagues' implementation of Alberto Moraglio and
colleagues' semantic geometric GP at EuroGP 2013. When I first
understood FFX and SGGP I was very impressed -- it felt like we were
taking real steps forward with symbolic regression.

After thinking quite hard about them both, and playing a bit with
code, I came to a realisation that the two methods are very similar,
if you look at them the right way. 

Fast Function Extraction (FFX)
------------------------------

McConaghy starts with a question: what would it take for SR to become
a *technology*? An example of a technology, in his sense, is *linear*
regression: it's fast, reliable, and deterministic. It achieves this
at the cost of being inflexible. GPSR is not a technology in this
sense: it is slow, non-deterministic, and it can fail. Sometimes it
fails once in every 10 runs on an easy problem; sometimes it fails 10
times on what we expected to be a solvable problem. Even when multiple
runs achieve equally good results, the models produced are almost
never exactly the same. This can be both a strength of GPSR (a route
towards ensemble methods) and a weakness (it is harder to explain to a
client that none of the resulting models is "the" model).

FFX addresses this by doing away with the GP aspect of SR. I will
describe a "caricature" version of FFX. It starts with a set of
independent variables, say X0 and X1. Then it expands this set to
include some simple transformations of the independent variables, such
as X2 = sqrt(X0) and X3 = abs(X1). Then it expands further to include
more recombinations such as X4 = X2 * X1. This process generates a set
of a few thousand variables (7100 in one example), which are then put
into a linear regression, y = b0X0 + b1X1 + ... + b7100X7100. Linear
regression finds good values for the coefficients bi very fast. In
fact, it is not vanilla linear regression, but an elastic net, which
tends (tunably) to push a large number of the coefficients bi to zero.
The result is a model which is highly readable.


Semantic Geometric Genetic Programming (SGGP)
---------------------------------------------

Moraglio has always pushed the idea that we must understand EC
operators as *geometric*: mutation should produce results within a
ball surrounding the original; crossover offspring should lie on a
line segment between their parents (interpretation of these statements
in a non-Euclidean space, like that of GP tree genotypes, requires the
definition of a distance metric for the space). But the big insight of
Moraglio et al is that after all this time, the relationship between
genotype and semantics in tree-based GP turns out to be easy to
understand. Or at least, easy enough to allow the definition of
geometric mutation and crossover operators which have the above
properties when viewed in the semantic space, ie the space of vectors
of outputs. Since fitness is equivalent to Euclidean distance in
semantic space, this transforms the fitness landscape into a unimodal
one, which is easily solved. Although both Moraglio and colleagues and
then Vanneschi and colleagues tried out both crossover and mutation,
there is a consensus, backed up by results from both, that a
mutation-only hill-climber is sufficient for a unimodal space.

That is the version I will describe. The mutation operator is simple.
Starting with a tree t, mutation produces a new tree tm = t + ms *
(tr1 - tr2). Here tr1 and tr2 are randomly-generated trees, so the
output of (tr1 - tr2) when run on the vector of fitness cases is a
vector with expected value (0, 0, ..., 0). ms is the mutation step, a
constant which defines the radius of the mutation ball. The output of
tm is a vector drawn from the ball around the output of t.

I did a few quick runs using a hill-climber with SGGP mutation. In my
implementation the initial point in the hill-climber, and the random
trees tr1 and tr2, are generated using the grow operator with maximum
depth 2 (counting a single-node tree root as depth 0). That might not
be optimal but it's ok for now. A typical result after just 10 steps
(7 of which were accepted by the hill-climber) is a tree like this (ms
= 0.01):

    ['+', ['+', ['+', ['+', ['+', ['+', ['+', ['-', ['/', 'x221', 'x44'],
        ['+', 'x189', 'x233']],
        ['*', 0.01, ['-', ['+', 'x191', ['/', 'x3', 'x211']],
        ['-', ['/', 'x141', 'x153'], ['*', 'x79', 'x5']]]]],
        ['*', 0.01, ['-', 'x8', ['-', ['-', 'x148', 'x187'], 'x218']]]],
        ['*', 0.01, ['-', ['/', ['/', 'x80', 'x225'],
        ['*', 'x74', 'x134']], ['*', 'x34', ['-', 'x41', 'x119']]]]],
        ['*', 0.01, ['-', 'x118', 'x57']]],
        ['*', 0.01, ['-', 'x124', ['-', ['/', 'x103', 'x138'],
        ['+', 'x21', 'x81']]]]],
        ['*', 0.01, ['-', ['*', ['-', 'x104', 'x141'],
        ['-', 'x223', 'x56']], ['-', 'x11', ['+', 'x183', 'x60']]]]],
        ['*', 0.01, ['-', ['+', 0.5, ['*', 'x18', 'x23']],
        ['-', 'x167', 'x47']]]]

There are several things to notice, which are possibly obvious by
looking at the mutation operator. The tree is already very large: in
fact it grows at each step by 4 nodes plus the size of tr1 and tr2.
The tree starts with lots of + operators, so it is a sum of subtrees.
Each such subtree is ms * (tr1 - tr2) = ms * tr1 - ms * tr2. Thus the
tree is a linear combination of tr1s and tr2s.



Shared strengths and limitations of FFX and SGGP
------------------------------------------------

This is the similarity between FFX and SGGP. Each produces a model
which is a linear combination of small subtrees. These small subtrees
in FFX are the basis functions; in SGGP the small subtrees are the tr1
and tr2 subtrees. The coefficients in the linear combination are the
bi values in FFX; the ms values in SGGP. Both FFX and SGGP work by
exploiting the fact that linear combinations are well-behaved and
well-understood.

Neither method, then, is a universal approximator, ie cannot represent
every possible arithmetic function, unless the subtrees are allowed to
become arbitrarily large. Of course, in practice standard GP is not a
universal approximator either, because of practical limits on tree
size and depth; however in principle and in practice, standard GP can
produce far more flexible models than the linear combinations of small
subtrees characteristic of FFX and SGGP.

Results with these methods suggest that the problems tackled so far do
not require universal approximators. However this suggests a possible
route to constructing a problem which is hard for FFX or SGGP: it
should be deeply non-linear, ie should feature non-linearities from
root to leaf, and larger than the allowed size of the method's
subtrees. Such a function would not be in the search space for either
method.

Note that re-introducing the SGGP crossover operator would change the
situation somewhat: it again produces a sum of subtrees, but now each
subtree multiplies a parent tree by a random tree tr. However, there
is still a strong limitation on the type of model which can be output
by the method.

A main difference between FFX and SGGP is that FFX uses a (relatively
small) fixed set of subtrees, and chooses among them optimally and
deterministically, whereas SGGP does not have a predefined set of
subtrees, but generates them randomly from among a possibly larger
space.


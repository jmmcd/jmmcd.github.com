---
layout: post
title: An alternative convex combination for semantic GP
tags: evolutionary_computation
---

An alternative convex combination for semantic GP
===

(This is only semi-frivolous.)

Getting crossover to behave well was a big question in genetic
programming for a long time. "Behave well" means "produce children
which are semantically between their parents". Most GP crossovers
don't achieve this very well.

But Moraglio and friends (PPSN 2012) pointed out that it's actually
really simple. If you have two trees *t1* and *t2*, you can get an
offspring *tn* which is on the (Euclidean) line segment between them
in this retrospectively obvious way: *tn = (1-r) t1 + r t2*, where *r*
is a random constant in *[0, 1]*. This is the geometric semantic
crossover.

The *(1-r) t1 + r t2* pattern is, if you like, a linear interpolation
from *t1* to *t2*. For every fitness case, as *r* increases, you move
from the value of *t1* to that of *t2*.

There is a variation: in the original Moraglio et al paper, instead of
a random constant *r*, you can have a random tree *r(X)* (where *X* is
the independent variables). If *r(X)* is in *[0, 1]* then for each
fitness case the value of *tn* is between the values of *t1* and *t2*.
In this case, the values for all fitness cases don't all move linearly
and in lock-step from *t1* to *t2*. So *tn* is in the Manhattan line
segment between *t1* and *t2* (instead of the Euclidean one, as
above).

Also another slight variation: in the Vanneschi et al paper (EuroGP
2013), *r(X)* is a random tree, but is not restricted to *[0, 1]*, so
*tn* is in the same hyperplane as the parents, but is not necessarily
between them.

All of these have in common the same basic pattern: you take two
numbers which sum to 1 (eg *r* and *(1-r)*), and use them as
coefficients in a weighted sum of the parents. Are there any other
options?

What about a trigonometric formula, like *cos^2(u) + sin^2(u) = 1*?
Then we can define a crossover as *tn = cos^2(r) t1 + sin^2(r) t2*.
Here, *r* could be any independent variable, or it could be a random
tree *r(X)*.

Or, if we see the original geometric semantic crossover as a weighted
mean of the parents, what about other types of means? The geometric
mean of *a* and *b* is *sqrt(ab)*, and you could define a crossover
*tn = sqrt(t1 t2)*. But that would be bad for the same reason it would
be bad to always use the (unweighted) mean *tn = (t1 + t2)/2*. But
there is a weighted geometric mean, which for just two values *a* and
*b* is just *exp(r ln(a) + (1-r) ln(b))*. So we could define a
crossover as *tn = exp(r ln(t1) + (1-r) ln (t2))*, and again *r* is
either a constant or a random tree *r(X)*.

There is also the harmonic mean, but that assumes the input values are
positive.

Another option: one could use the Vanneschi et al crossover where
*r(X)* is a random tree, but stay in *[0, 1]* using a sigmoidal map.
So the crossover would be defined as *tn = sigmoid((1-r(X)) t1 + r(X)
t2)*.

A final option: why is *r(X)* a *random* tree? Why not call any of
these a three-parent crossover, where *r(X)* is selected from the
previous population just like *t1* and *t2*? Vanneschi et al
anticipate this idea with their "slight abuse of terminology", calling
*r* an "ancestor" of later individuals.

Both the trigonometric crossover and the geometric mean crossover
(uh-oh, "geometric" is being used in two senses now) are geometric
when using a random constant *r*. When using a random tree *r(X)*,
they are still "weakly" geometric, ie geometric in Vanneschi's sense.
The sigmoid crossover is geometric for *r(X)*, and wouldn't really
make any sense for constant *r*.

All have the possible advantage that they allow for more complex tree
structures to come about -- not just weighted sums of trees. If we
just wanted weighted sums,
[we'd use linear regression](http://jmmcd.net/2013/05/03/symbolic-regression-state-of-the-art.html)!
Maybe we could use several types of crossover in a single run, in
order to accumulate complex tree structures?

First question: are there other options?

Empirical question: would it work?

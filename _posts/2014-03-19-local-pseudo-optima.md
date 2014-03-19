---
layout: post
title: Local pseudo-optima
tags: evolutionary_computation
---

Local Pseudo-Optima
========

Local optima are, basically, the reason search and optimisation exists
as a field of research, rather than a single algorithm that works
every time. The story we tell to the younglings is that if you don't
have local optima, then you use a hill-climber, and you find the
global optimum.

What is a local optimum? Well, if crossover is in the picture, then
it's complicated. Let's forget about crossover for the moment, and
consider mutation only. An individual is a local optimum if no other
individual, reachable by a single mutation, has a better fitness.

Now there are obvious counter-examples to the story we tell the
younglings:

* The genetic programming subtree mutation operator gives a landscape
  with no local optima. I'm talking about the version where mutation
  is allowed at any node, including the root. Since you can mutate at
  the root, any individual can mutate to any other individual in a
  single step. Therefore, there are no local optima. But if you use a
  hill-climber, you might do quite well (e.g. O'Reilly and Oppacher,
  *Program Search with a Hierarchical Variable Length Representation:
  Genetic Programming, Simulated Annealing and Hill Climbing*). But
  you can't expect to just hill-climb to the global optimum.

* You can construct a mutation operator which gives no local optima.
  Start with any existing mutation operator *m*. With some low
  probability, return a new random individual. Otherwise, return
  *m(x)*, where *x* is the current individual. Again, this gives a
  landscape with no local optima, but if you now run a hill-climber,
  it's equivalent to a hill-climber using *m* with random restarts.
  Getting rid of the local optima hasn't really helped.

So what is really going on? I think that we need the concept of local
*pseudo*-optima. A local pseudo-optimum is an individual with a
vanishingly low probability of mutation to any better individual in a
single step. Consider a GP individual which can only mutate to a
better individual by mutating at the root and generating one of some
small set of large trees. That is a mutation of very low probability.

This isn't an all-or-nothing definition anymore. How small is
"vanishingly small"? Anyway it would probably be a mistake to set an
arbitrary threshold. But maybe we can measure the "strength" of every
local pseudo-optimum as something like one minus the probability of a
one-step transition to any better or equally-good individual. With
this way of thinking, every individual is a local pseudo-optimum of
differing strength. One aspect of the difficulty of a landscape can be
measured by measuring the strength of the local pseudo-optima, or
perhaps the number of strong ones (where an arbitrary threshold is
used to define "strong").

The probability of transitioning to a better individual via a single
mutation will relate directly to how long the hill-climber gets stuck
on the individual in question. And that can lead us back to crossover.
The typical local optimum behaviour in a full EC algorithm is that the
evolution gets stuck at a single point for a long time, and then the
run ends. Whether this corresponds to a true local optimum in the
presence of crossover is, again, complicated, so again, let's ignore
that question. But we can estimate (as distinct from "measure") the
strength of a local pseudo-optimum in the presence of crossover by
estimating how many children of the individual in question have to be
tried before an individual of equal or better fitness is found. That
can be crudely estimated from the EC parameters (e.g. population size
and tournament selection size) and the number of generations during
which the evolution is stuck at a particular fitness. We don't need
new experiments: we can read old papers to get this data.

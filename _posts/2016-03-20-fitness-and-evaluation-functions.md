---
layout: post
title: Decoupling fitness and evaluation in benchmarks
tags: gp_benchmarks
---

Decoupling fitness and evaluation in benchmarks
========


I recently reviewed a paper where the authors suggested an existing
problem that they claimed would be a suitable benchmark for genetic
programming. And indeed it was: it was an interesting and difficult
problem, with several good properties. They tightened up some
definitions and added some insight that would help it become even more
useful.

However, there was one place I thought the authors went wrong. They
proposed a novel fitness function for this problem. It effectively
amounted to giving some partial credit to some types of partial
solutions. I can see the advantages of this -- partial credit means a
smoother landscape. So the fitness function itself was well-motivated,
and (I guess) would lead to improved performance on the problem.

However, if you specify the fitness function, then future researchers
won't be "allowed" to try variations of the fitness function. That
seems to defeat the purpose of a benchmark! Maybe the right approach
is to decouple the the *fitness function* and the post-run *evaluation
function*. The fitness function should be unspecified (and open for
experiment), but the post-run evaluation function should be rigidly
defined, so that all researchers can directly compare their results.

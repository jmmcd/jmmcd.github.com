---
layout: post
title: Train-test splits don't cut it
tags: evolutionary_computation gpbenchmarks
---

Train-test splits don't cut it
========

Probably we've all occasionally reviewed papers in genetic programming
classification and regression which report *training* performance
only. Now it's easy to write an algorithm that achieves very good
performance on the training set: just memorise the training set! So we
reject these naive papers, unless the authors make a good argument why
the result is interesting.

(Aside: memorising the training set doesn't necessarily get *perfect*
performance, because of the Bayes error rate or its regression
equivalent: the training data might include two identical x-values
with distinct y-values.)

But luckily these naive papers are rare. Most papers I review use a
respectable train/test split methodology, e.g. a random 70/30
split. They may report the performance on training data, but the focus
is rightly on test data. However, for a lot of problems this still
isn't enough.  As shown by
[Nicolau et al. in "Guidelines for defining benchmark problems in Genetic Programming"](http://ieeexplore.ieee.org/xpl/login.jsp?tp=&arnumber=7257019),
there can be *enormous* variance in the samples drawn from common GP
benchmark functions, therefore enormous variance in the "difficulty"
of some fitness cases versus others, and therefore enormous variance
in the performance of the same algorithm on different train-test
splits. 

This means that two authors' results on the same function cannot be
fairly compared, because they may not have drawn the same train-test
splits. Even worse, it means that results from a single paper may not
be comparable against each other, unless it is clearly stated that the
same train-test split was used for all experiments. Wishful authors
can deceive themselves by re-running the experiment multiple times
until they get a lucky split (and can persuade themselves that a
random tweak of parameters has had a beneficial effect). Dishonest
authors can deceive reviewers and readers.

The problem is not limited to regression or to datasets created by
drawing from defined functions (as opposed to real-world data). I
recently reviewed a paper where classification results on real-world
data with a standard method varied from far *below* to far *above* the
claimed performance of the proposed new method, just by varying the
split.

A natural solution is to use several random splits, or a full
cross-validation methodology. For some datasets this is appropriate,
but Nicolau et al.'s results show that on some common GP symbolic
regression problems even a cross-validation won't be enough, because
the different folds can be so different from each other. The issue
here is that standard cross-validation is still non-deterministic, or
(the same thing in practice) deterministic, but controlled by a seed
which is not published.

That could be addressed using the extreme case of leave-one-out
cross-validation, which amounts to a deterministic experiment. However
that is usually infeasible in GP because of long training times.

The solution proposed by Nicolau et al. is to carry out a single split
(or a single draw, if drawing from a function), to and publish the
training and test data files. In effect, the problem becomes defined
by these two files, rather than by the original data file or
function. Results (within-paper or between-paper) become directly
comparable only if using the same data files. 

This solution seems appropriate when defining a benchmark problem. The
problem remains that if that single original split (or draw) is
"lucky" or "unlucky", the problem will appear misleadingly easy, or
difficult. For real-world datasets, we don't want to be deceived in
this way. For many real-world datasets, we can at least check
performance on many train-test splits, *before* choosing just one,
which is not misleadingly easy or difficult, to publish as our
"official" split.

In conclusion, *train-test splits just don't cut it*.

---
layout: post
title: GP Needs Better Baselines
tags: code python evolutionary_computation
---

Genetic programming needs better baselines
========

Introduction
------------

We've been talking about deficiencies in genetic programming
experimental practice, benchmarking, and so on
[for a while](http://gpbenchmarks.org/). Our first paper on this topic
was
[Genetic programming needs better benchmarks](http://gpbenchmarks.org/wp-content/uploads/2013/05/paper1.pdf).
Now I want to focus on a more specific issue in experimental practice,
which is the use of appropriate *baselines* in experiments.


Gratuitous metaphor
-------------------

Imagine we're managing a football team, and we're trying to decide who
will take penalty kicks for us. We already have a guy who takes them.
He's a bit old, and maybe the goalkeeper stops his shots too often,
but at least he always hits the target.

But we've spent a huge amount of money on three new players, all have
great reputations, and we're confident that they'll be much better. We
test the new guys out:

* Player A tries to eat the football
* Player B picks up the ball and runs around the city for several hours
* Player C punches the referee in the face.

How should we respond?

* "Well, Player A did very well, got the ball closer to the goal than
  Player C, and was more efficient than Player B."
* "No matter what their reputation, none of these guys is even close
  to the performance of our existing penalty taker."

I propose that if we spend our time discussing which of the new
players was the best, then the opposing team are probably going to
laugh at us.

That is the situation we could find ourselves in when we spend a lot
of time developing new and exciting methods for genetic programming
symbolic regression, if we are not careful. The opposing team --
remember, they are laughing at us -- are people who use
non-evolutionary methods for regression. They know when their methods
are failing to beat the old, reliable, *linear regression*.


Details
-------

I've seen some papers which fail this test recently. One example is
Vanneschi et al, *A new implementation of geometric semantic GP and
its application to problems in pharmacokinetics*, available
[here](http://link.springer.com/chapter/10.1007/978-3-642-37207-0_18)
(best paper award EuroGP 2013). Another is Spector and Helmuth,
*Uniform linear transformation with repair and alternation in genetic
programming* (GPTP 2013). I can't find it available online yet.

* On the
  [bioavailability](http://kdbio.inesc-id.pt/~sara/gptp2013/bioavailability.txt)
  data set, both papers report the median  RMSE using novel GP
  methods (a geometric semantic method in Vanneschi et al, and a novel
  mutation in the PushGP framework in Spector and Helmuth) as about
  32-33. Standard GP does far worse. But they don't say that
  predicting a constant (about 66) can do better (RMSE < 30), and
  linear regression about the same. These figures are all on unseen
  data, using a 50/50 split and randomisation.
* On
  [protein plasma binding](http://kdbio.inesc-id.pt/~sara/gptp2013/ppb.txt),
  the Vanneschi et al paper reports a median test RMSE (again using a
  geometric semantic GP method) of about 37. Predicting a constant can
  do better, and linear regression about the same.

To reproduce my results,
[download this script](https://gist.github.com/jmmcd/7790588) as well
as the data linked above. The script requires Python, Numpy and
Scikit-learn. It reads a single data file, taking the last column as
the dependent variable, and it has parameters for shuffling the data
and setting the train/test split. (Shuffling the data makes a small
but noticeable difference to the result, even though both linear
regression and prediction of a constant are deterministic.)

I think it would be interesting to try the same test -- predicting a
constant or using linear regression -- on a large selection of
published symbolic regression papers which don't state baseline
results. I suspect we'd find a few more which fail to beat linear
regression. If someone has the time, please go ahead!

Now, the interpretation of these facts is not obvious. I am *not*
saying that failing to beat linear regression makes a symbolic
regression paper worthless, or anything like that. A new technique
might be very useful on some problems, even if it performs worse than
standard GP or linear regression. Even if it's not better on any
problem, a well-motivated study is still worth publishing. We should
not be playing
[the "up-the-wall" game](http://www.cs.stir.ac.uk/~goc/papers/GECCO09Decwk1005-ochoaATS.pdf).
But in order to say "our result may be negative, but it is still worth
publishing", we have to first *know* and *state* that the result
actually is negative.

I also think that the bioavailability problem, and the protein plasma
binding one, and the toxicity one often associated with them, are not
necessarily damaged as benchmarks by this result. We want our
benchmark problems to be difficult, and these clearly are. Previously
our benchmark *result* on these problems was as stated by previous
work using standard GP and variations. Now we know that the benchmark
result -- the one we should be aiming to beat -- is actually set by
linear regression or even by predicting a constant. So, have at it!


Conclusion
----------

I have focussed here on symbolic regression, but similar comments
apply to any GP problem. In symbolic regression an obvious choice of
baseline is linear regression, or prediction of a constant. In other
cases it might be an ARIMA-style time-series prediction, or a
1-nearest neighbours classification, or something else. It depends on
the problem. I think the best approach is to identify an appropriate
baseline for the task, and carry it out *before* doing a single GP
run.

One obvious lesson for symbolic regression researchers is that
standard GP symbolic regression sometimes does really, really badly --
not only worse than linear regression, but far far worse on test data.

The authors of the papers I point to above are senior researchers, big
names in the field, with excellent reputations for doing excellent
work. I am not trying to attack them or single them out. I know they
are interested in improving GP experimental standards. And I am not
pointing fingers: it is a lesson I have only really learned recently,
and I might well have written papers which have similar flaws. I think
we all benefit from discussion of higher standards in experiments and
benchmarking.

Authors, reviewers and editors all have a responsibility in this:

* Authors: make your data available, and choose and report appropriate
  baselines.

* Reviewers: get into the habit of thinking more carefully about
  results, and not just the comparison the author chooses to show you.
  If you have Python with Numpy and Scikit-learn and you want to run a
  linear regression or constant-fitting very quickly (with a single
  data file, a parameter for train/test data split, and optional
  shuffling of data), then
  [download this script](https://gist.github.com/jmmcd/7790588).

* Editors: give prizes, special mentions, money, beer, chocolate or
  something to reviewers who do the work to improve experimental
  standards.

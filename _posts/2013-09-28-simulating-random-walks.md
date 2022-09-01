---
layout: post
title: Simulating random walks
tags: code python evolutionary_computation
---

Simulating random walks
=======================

This is about estimating the *mean first passage time* (MFPT) using
random walks.

I've been using random walks to model behaviour of evolutionary
algorithms. Each individual is a state, and the probability of
mutating from individual `u` to individual `v` is the transition
probability `p(v|u)`. Given a particular evolutionary operator, say
subtree mutation, transition probabilities can be calculated exactly
and collected in a transition matrix for all `u` and `v`. 

One of the properties of most interest to me is the mean first passage
time, also known as the hitting time, from `u` to `v`. It's the mean
number of steps you expect to have to wait, if you start at `u` and
random-walk until you hit `v`. It's interesting because it's a natural
way of quantifying the distance, in the fitness landscape, between
evolutionary individuals.

It's kind of amazing that, given a transition matrix, you can
calculate the mean first passage time matrix efficiently in closed
form. Kemeny and Snell gave a method in *Finite Markov Chains*, 1976.
A Python implementation (not written by me) is
[here](https://github.com/jmmcd/GPDistance/blob/master/python/RandomWalks/ergodic.py). 

However, that can only work where the number of states `n < 4000` or
so -- depending on your available RAM -- simply because you need to
store the `n x n` transition matrix in memory, together with a few
other matrices, and finally the MFPT matrix of the same size. In my
current work, I'm looking at spaces with many billions of elements, so
that is completely out. We might not even know the names of all the
states, or how many there are. Maybe the space could even be infinite?
But don't hold me to that, because maybe MFPT is undefined then.
Anyway, there is a subset of states in which we're interested, and for
all pairs `(u, v)` in that subset, I want to be able to estimate the
MFPT.

So, the natural thing to do is to simulate some random walks and see
what happens. This is possible because instead of storing a transition
matrix, we just have to have a transition function -- given a state,
it will transition to a new state. In an evolutionary algorithm, the
transition function is just mutation. In many interesting algorithms,
such as tree-based genetic programming, mutation is non-uniform -- we
are more likely to mutate to certain individuals than others. We
iterate this function, counting the number of steps: if we start at
`u` and stop when we hit `v`, the number of steps taken is a sample of
`MFPT(u, v)`. We can then repeat the whole thing to get another
sample. Writing this algorithm is very easy.

However, running it might take a long time. Each walk might take
billions of time-steps, and we'll need to collect quite a few samples
of the length in order for our estimate to be reliable. Remember we
are interested in multiple pairs `(u, v)`. If we only think about two
states at a time, we can't collect information on all those other
states of interest even though we might be going through them. So this
way of running the random walk is very inefficient.

We can do a lot better if use a single long walk and some book-keeping
to collect samples for many pairs at the same time. We start walking,
and every time we hit one of those states of interest, we record how
long it took to get here from the previous sighting of the other
states of interest. It's like running multiple interleaved walks at
once. This is much more efficient, and it sounds pretty simple: just
record the time-step of the last occurrence of each state of interest,
and when you hit a state of interest, subtract the last occurrence..?

Actually, it's not that simple. There are a couple of tricky issues
which could cause bad estimates, and that's why I want to document my
algorithm here.

First, consider this situation. We start out, hit `u` at time-step 100,
then walk for a while, hitting `u` again at time-step 200, and so on.

`others -> u (100) -> others -> u (200) -> others -> v (300) -> others -> v (400)`

What happens when we hit the `v` at time-step 300? Should we record a
sample for `MFPT(u, v)` of 100? 200? Or both? The answer is 200, only.
We started at `u` at time-step 100, and even though we arrive there
again at time-step 200, for the purposes of sampling `MFPT(u, v)` that
is not the start of a new walk. So instead of recording the last
sighting of `u`, we need to record when the walk from `u` to `v`
started. In other words, we need a variable `rw_started(u, v)`, which
records the time-step at which the current walk from `u` to `v`
started. If -1, that means we are not currently in a walk from `u` to
`v`. When we hit `v`, we regard it as the end of a walk from `u` to
`v` (and thus save a sample) only if `rw_started(u, v)` is not -1. We
then update `rw_started(u, v)` to -1, and `rw_started(v, u)` to the
current time-step, to say that a new walk from `v` to `u` is now
starting.

Similarly, what should we do when we hit `v` at time-step 400? Save a
sample 200? 300? Both? This time the answer is to save *neither*. At
time-step 400, we are in the middle of a walk from `v` to `u`. We're
not in a walk from `u` to `v`.

However, at time-step 400 we *do* save a sample of 100 for `MFPT(v,
v)`, ie the random walk from `v` to itself.

So here is what should happen at each step:

Time step 100: set `rw_started(u, v) = 100`, set `rw_started(u, u) = 100`

Time step 200: save a sample `MFPT(u, u) = 100`, set `rw_started(u, u) = 200`

Time step 300: save a sample `MFPT(u, v) = 200`, set
`rw_started(v, u) = 300`, set `rw_started(u, v) = -1`, set
`rw_started(v, v) = 300`

Time step 400: save a sample `MFPT(v, v) = 100`, set `rw_started(v, v) = 400`

One more issue. After running for a while, hopefully we'll have saved
some samples. Can we trust them? There is a danger of a systematic
under-estimation. Why? Suppose our walk is of length, say, 1 billion
steps, and there are, say, 10 billion states. Then there must be some
pairs whose true MFPT is longer than the length of our walk. For those
pairs, the only samples we *can* collect are those which are
underestimates of the MFPT. If we get lucky and collect some of those
samples, they can only be underestimates. So to be safe, it's best to
use the results only for pairs where there are quite a few samples. We
then hope that this happened because these are pairs whose true MFPT
is less than the length of the walk.

The code below carries out this algorithm. Given about 50 steps, it's
already getting pretty good estimates for MFPT between all pairs.

Code
----

Download this Python code [here](http://jmmcd.github.com/code/rw.py).
A Java version, somewhat coupled to the surrounding code, is available
[here](https://github.com/jmmcd/GPDistance/blob/master/java/GP/Sample.java).

{% highlight python %}
#!/usr/bin/env python

import numpy as np
import scipy.stats
import random

def roulette_wheel(a):
    """Randomly sample an index, weighted by the given sequence of
    probabilities."""
    s = np.sum(a)
    assert s > 0
    r = random.random() * s
    cumsum = 0.0
    for i, v in enumerate(a):
        cumsum += v
        if r < cumsum:
            return i
    raise ValueError("Unexpected: failed to find a slot in roulette wheel")

def simulate_random_walk(f, nsteps, selected, nsaves):
    """f is the transition function. nsteps is the number of steps.
    selected is the set of states (can be a list of integers) in which
    we're interested. nsaves is the max number of samples to save for
    each pair. Return an array of samples for MFPT for each pair (i,
    j) from selected."""

    n = len(selected)
    # samples is all nans to start
    samples = np.nan + np.zeros((n, n, nsaves))
    # in the rw_started matrix, the (i,j)th entry is the time-step at
    # which a walk from i to j began. -1 means we are not currently in
    # a walk from i to j. can't be in a walk from i to j and from j to
    # i simultaneously.
    rw_started = -1 * np.ones((n, n), dtype='int64')
    # for each transition there are nsaves spaces to save samples --
    # this says where to save
    saveidx = np.zeros((n, n), dtype='int')

    def print_state(v, rw_started, samples, t):
        print("%d: %d" % (t, v))

    # su and sv are states (may be integers). u and v are the indices
    # into selected of su and sv
    sv = selected[0]
    for t in range(nsteps):
        print_state(sv, rw_started, samples, t)
        
        # when we see a state sv which is of interest
        if sv in selected:
            v = selected.index(sv)
            
            for u, su in enumerate(selected):

                if rw_started[u,v] == rw_started[v,u] == -1:
                    rw_started[v,u] = t

                elif rw_started[u,v] > -1:
                    # we are currently in a walk from u to v, and we
                    # have just reached v, so save a sample (now -
                    # start of walk), if there is space
                    if saveidx[u,v] < nsaves:
                        samples[u,v,saveidx[u,v]] = (t - rw_started[u,v])
                        # update the space left
                        saveidx[u,v] += 1
                    # now we start a walk from v to u. because of the
                    # order of these two assignments, this does the
                    # right thing if v == u.
                    rw_started[u,v] = -1
                    rw_started[v,u] = t

                elif rw_started[v,u] > -1:
                    # we are in a walk from v to u, and have
                    # re-encountered v. ignore.
                    pass

                else:
                    raise InternalError
                    
        # transition to a new state
        sv = f(sv)
    return samples
    
def main():
    """The Land of Oz example from Kemeny & Snell 1976. The states are
    rain, nice weather, and snow. The transition probabilities (tp)
    are given. The mean first passage time (mfpt) can be calculated
    exactly using their method. We will simulate to estimate mean
    first passage time (mfpte)."""
    tp = np.array([[.5,  .25, .25],
                   [.5,  .0,  .5 ],
                   [.25, .25, .5 ]])
    mfpt = np.array([[ 2.5,        4., 3.33333333],
                     [ 2.66666667, 5., 2.66666667],
                     [ 3.33333333, 4., 2.5       ]])
    samples = simulate_random_walk(
        lambda i: roulette_wheel(tp[i]), # transition according to tp
        200, [0, 1, 2], 10)
    mfpte = scipy.stats.nanmean(samples, axis=2)
    mfpte_std = scipy.stats.nanstd(samples, axis=2)

    print("Samples")
    print(samples)
    print("MFPT")
    print(mfpt)
    print("MFPTE")
    print(mfpte)
    print("MFPTE_STD")
    print(mfpte_std)
    
if __name__ == "__main__":
    main()
{% endhighlight %}


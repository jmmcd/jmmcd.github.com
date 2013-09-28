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

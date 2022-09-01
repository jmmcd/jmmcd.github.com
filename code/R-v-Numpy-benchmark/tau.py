#!/usr/bin/env python2.7

import scipy.stats
import numpy as np
import time
import random
import sys

n = int(sys.argv[1])
reps = 1
elapsed = 0.0
for i in range(reps):
    start = time.time()
    x, y = [np.random.random((n, n)) for i in range(2)]
    scipy.stats.mstats.kendalltau(x, y)
    end = time.time()
    elapsed += end - start
print("Elapsed time (s): " + str(elapsed / reps))
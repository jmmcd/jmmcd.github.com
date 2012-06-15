---
layout: post
title: R versus Numpy benchmark
tags: code python R
published: false
---

R versus Numpy benchmark
========================

In an experiment I'm doing, I need to do correlations between very
large matrices. I was surprised to see that a single correlation
calculation could take many hours. I decided it was worthwhile to
benchmark my two main statistics options, R and Numpy, to see which
would do it faster.

Here's code I used to do the Python:

{% highlight numpy %}
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
{% endhighlight %}

Here's the code I used to do the R (it's not exactly the same, because
R doesn't give the option to run a correlation on a matrix directly,
so I'm just using a lineary array).

{% highlight rout %}
cmd_args = commandArgs();
n = as.real(cmd_args[4]) # use like this: R --vanilla --silent < tau.r 10 [10 is then arg 4]
x <- runif(n*n, 0.0, 1.0)
y <- runif(n*n, 0.0, 1.0)
system.time(cor.test(x, y, method="kendall"))
{% endhighlight %}


And here's the enclosing shell script which runs each of the above for
different sizes:

{% highlight bash %}
for i in 10 50 250 1250; do
	echo $i; R --vanilla --silent < tau.r $i; ./tau.py $i;
done
{% endhighlight %}

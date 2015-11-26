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
fairly compared, because they may not have drawn the same train and
test sets. Even worse, it means that results from a single paper may
not be comparable against each other, unless it is clearly stated that
the same train and test sets were used for all experiments. Wishful
authors can deceive themselves by re-running the experiment multiple
times until they get a lucky test set (and can persuade themselves
that a random tweak of parameters has had a beneficial
effect). Dishonest authors can deceive reviewers and readers.

The problem is not limited to regression or to datasets created by
drawing from defined functions (as opposed to real-world data). I
recently reviewed a paper where classification results on real-world
data with a standard method varied from far *below* to slightly
*above* the claimed performance of the proposed new method, just by
varying the train-test split. *Train-test splits just don't cut it*.

A natural solution is to use several random draws (or splits), or a
full cross-validation methodology. For some problems this is
appropriate, but Nicolau et al.'s results show that on some common GP
symbolic regression problems even a cross-validation won't be enough,
because the different folds can be so different from each other. The
issue here is that standard cross-validation is still
non-deterministic, or (the same thing in practice) deterministic, but
controlled by a seed which is not published.

That could be addressed using the extreme case of leave-one-out
cross-validation, which amounts to a deterministic experiment. However
that is usually infeasible in GP because of long training times.

The issues raised here obviously arise outside GP. Why isn't the idea
of fixed train/test datasets common in the bigger world of machine
learning? For one thing, some machine learning methods are fast enough
to use leave-one-out cross-validation. For another, many common
datasets are large enough and/or homogeneous enough that different CV
folds end up being closely equivalent in difficulty. It's a particular
feature of common GP problems, as shown by Nicolau et al., that this
is not the case.

The solution proposed by Nicolau et al. is to carry out a single split
(or a single draw, if drawing from a function), and to publish the
training and test data files. In effect, the problem becomes defined
by these two files, rather than by the original data file or
function. Results (within-paper or between-paper) become directly
comparable only if using the same data files. 

This solution seems appropriate when defining a benchmark problem. The
problem remains that if that single original split (or draw) is
"lucky" or "unlucky", the problem will appear misleadingly easy, or
difficult. For real-world datasets, we don't want to be deceived in
this way (we might wrongly conclude that GP was very good at
regressing data from a particular medical domain, for example). For
many real-world datasets, we can at least check performance on many
train-test splits, *before* choosing just one which is not
misleadingly easy or difficult, and publish that as our "official"
split.

There are a couple of obstacles. First, we've seen examples in the
past where distinct versions of what should be a fixed dataset are
actually in use
(e.g. [Bezdek et al.](http://pages.bangor.ac.uk/~mas00a/papers/jbjkrklknptfs99.pdf)
show this for the Iris dataset). Publishing the URL for training and
test datasets doesn't solve this problem, because it's easy for an
author to run experiments, publish the URLs, and later on upload new
versions to the same URLs. To counter this, perhaps an MD5 checksum
could be run on the datasets by the authors who first use them, and
(say) the last 4 characters of each could be published *in the paper*
as part of the same table which lists the datasets' names and
dimensions. This gives a permanent, verifiable link between results
and original data
[(see Principle 4 here)](http://guerrilla-analytics.net/the-principles/).

Another practical obstacle to good practice is double-blind reviewing.
Many authors will be happy to publish their datasets, but when they're
submitting a paper to a double-blind venue they naturally omit the
URLs if they easily identify the authors (e.g. pointing to a
university webpage). Later on, if the paper is accepted, they may or
may not remember to add them. Either way, the reviewer isn't able to
download the data and run
[simple baselines](http://jmmcd.net/2013/12/19/gp-needs-better-baselines.html)
to check out the results.

This is similar to a problem faced by EvoMUSART (the International
Conference on Evolutionary and Biologically Inspired Music, Sound, Art
and Design): music and other media which don't fit well in papers can
be put online for review, but authors remove the URLs for double-blind
review, and reviewers aren't able to judge the work. When Penousal
Machado and I were chairs in 2013 we added a line to the call for
papers: authors should use a URL-shortening service like Tinyurl to
add an anonymous-looking link. The URL should point to a download,
rather than to a html page, to avoid showing the true URL after
redirection. It's not perfect, because a determined reviewer can still
find the original URL. If an author is worried about anonymity, they
could instead upload to an anonymous file-sharing site. This should
preferably be a permament location like a
[Github gist](https://gist.github.com), and not one of the ones where
you wait 30 seconds and then click Download, only to discover that the
*real* download link was hidden at the bottom of the page and instead
you've opened up a video chat with a group of sexy singles living in
your area.

One more small issue: if the original author creates the dataset in an
Excel file, and calculates the checksum on this, but the next author
downloads and exports to csv in order to suit a different platform,
then clearly the checksums won't match. That's good: it warns
subsequent authors that something has happened. As long as the
original file is available, with its original checksum mentioned in
paper, subsequent authors can go and get it and verify the checksum,
and do the conversion to their preferred format by themselves.



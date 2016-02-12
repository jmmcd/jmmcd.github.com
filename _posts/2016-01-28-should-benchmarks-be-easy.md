---
layout: post
title: Should Benchmarks be Easy?
tags: evolutionary_computation gpbenchmarks
---

Should Benchmarks be Easy?
========

Quite a while back I wrote about the importance of using [sensible baselines in our GP research](http://jmmcd.net/2013/12/19/gp-needs-better-baselines.html) in order to avoid misleading ourselves about GP performance. At GECCO 2015, Grant Dick and colleagues presented a really excellent paper which follows up on that point: ["A Re-Examination of the Use of Genetic Programming on the Oral Bioavailability Problem"](http://dl.acm.org/citation.cfm?id=2754771). I'll call it the "Re-Examination" paper. It examines one dataset in particular, the *Bioavailability* one which has presented an interesting challenge to GP researchers since [Archetti et al., GECCO 2006](http://dl.acm.org/citation.cfm?id=1144042), and the same one I discussed in my post.

Their Re-Examination analysis goes much further than mine. It's excellent:

-demonstration that the problem is "hard", due to many cases where a small change in the feature space results in a large change in the response space;
-measurement of variability of problem difficulty depending on train-test split;
-discovery of zero-information features, ie features which are literally constants, and discovery that GP often uses them in best-of-run models (this was my favourite part: we can't trust GP to carry out variable selection);
-performance of non-GP models, including null models (predicting a constant).

The main conclusion is that this dataset should not be used as a benchmark. Despite agreeing with almost everything else in the paper, I think I don't agree with the assumptions that underlie this conclusion, so I want to examine them. I'll quote the conclusion section in full:

    GP needs better benchmarks. Increasingly, the bioavailability data set is being used in an attempt to address this need. However, this data set has not received the necessary attention to provide the context and understanding to make it a truly useful benchmark. The goal of this paper was to take the initial steps into increasing the GP community’s understanding of this data set. In the process, it was found that the data set contains a large amount of redundant features, inconsistencies within the relationship between input features and response values, and does not respond well to the application of feature selection. The problem also presents challenges in selecting training and testing samples: this paper demonstrates that the natural deviation within the response values in the data set can plausibly explain the differences in performance exhibited in previous work. This means that many results in previous work cannot be ruled out as consequences of chance events. Additionally, when models are built from this data set, they will often resort to developing a null model that does not use information from the feature space and instead resorts to building models around the mean of the training data. Based upon this, the conclusions of this paper are that we cannot recommend the use of the bioavailability data set for benchmarking until these characteristics are properly understood and resolved.
	
	
I disagree: I think this dataset has already been clearly demonstrated to be useful, not least by Grant himself and colleagues! Their paper finds that the performance of a null model is comparable to that of some GP methods, and that random forests can out-perform GP. But that is itself a benchmarking result! We are learning something useful from experiments on this dataset! We are learning about failures in GP fitting, generalisation, and feature selection! All of this is exactly what I want from a benchmark. 

It's true that there are large differences in problem hardness, depending on train-test splits. However, what Grant and colleagues haven't said is that is not atypical of either real-world or synthetic datasets, and it doesn't prevent the problem from being used to draw reliable conclusions, [as long as experimental practice is good enough](http://jmmcd.net/2015/11/25/train-test-splits-dont-cut-it.html). Unfortunately there are no shortcuts: we need good experimental practice regardless of dataset choice. The problem is real, and not confined to this dataset, and we have to deal with this somehow. One approach is to use a fixed train/test split, as argued in my last post. Another way would be a full cross-validation methodology, as used in other branches of machine learning research. The latter would be slow with GP, but that excuse doesn't deter researchers working on image recognition with neural networks. But the problem of misleading results only arises if people say "we're working on the bioavailability problem" but they're actually working on a relatively easy version of it caused by a lucky train-test split. The solution is *don't do that*. 

It's true that this dataset looks pretty hard, eg in Fig 1 of the Re-Examination paper. Great! Easy problems don't need new research. [Have at it.](http://jmmcd.net/2013/12/19/gp-needs-better-baselines.html) Maybe the problem is actually impossible, though -- meaning null models are the best we can do? No, because Random Forests are already out-performing null models.

In other words, I think that the assumptions underlying this Re-Examination paper are a bit different from mine. We have different *desiderata* in mind for benchmarks. I think the Re-Examination paper assumes that benchmark datasets should be "tamed" before use, should be relatively easy, and should already have been demonstrated to be amenable to *existing* GP methods out-performing non-GP methods. I don't agree with those assumptions.
	
If we stick to tamed datasets where GP methods are already doing quite well, we might never learn about flaws in novel methods. For example, how will we learn whether a novel GP method is susceptible to using zero-information features, if we hand-delete them in advance?

I think the following quote demonstrates very well the difference in thinking: "the data set [...] does not respond well to the application of feature selection." I would instead say "the data set [...] does not respond well to the application of *current methods of* feature selection". (Bear in mind GP is often used, including in the literature on this dataset, as an integrated feature-selection + modelling method.) A benchmark is not something that plays nicely with existing methods. That is for undergraduate textbooks. A benchmark is intended to spur new developments and reward good ones. (And good ones are rewarded by this dataset: compare the generalisation performance of linear regression with a modern regularised variant, like the elastic net.)

Bioavailability is still (potentially) a good choice of benchmark. If we have sometimes drawn false conclusions from it, that is due to a lack of good baselines and train-test procedures. It's not because the dataset is flawed in some way. No-one is disputing whether the data is real. The data is what it is, and it's up to us develop methods to learn about it. If our existing methods are all failing, that is exactly the type of challenge we need. 

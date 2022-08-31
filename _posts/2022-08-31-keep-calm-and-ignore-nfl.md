---
layout: post
title: Keep Calm and Ignore No Free Lunch
tags: evolutionary_computation
---

<img src="../../../images/nfl.png" alt="Keep Calm and Ignore No Free Lunch" width="400" align="center">

Over many years, I've encountered a lot of arguments on the internet, usually bad, concerning the famous No Free Lunch theorem(s). 

There are quite a few NFL theorems, also in various fields, but usually when people say *The* NFL, they're referring to the NFL theorem for search and optimisation, due to Wolpert and Macready. It says that averaged over all possible fitness functions on a fixed search space, any black-box search algorithm has the same search performance. That includes pure random search, so according to this, the most sophisticated modern metaheuristic is no better than random search.

The theorem itself isn't in doubt, but misinterpretations are common. Some people come away with the feeling that well-known algorithms like Genetic Algorithms are useless, due to NFL. That's totally wrong, but that particular error doesn't occur in the academic literature, only among people who have studied a little metaheuristics as part of a mandatory AI course. There are many other misinterpretations also, and some are also in the academic literature.

After a while, I decided to collect some of these misinterpretations. I wanted to collect them and counter them in one place, so that I'd have a resource I could point to. And I wanted to put this in an academic paper. The result is in *Springer-Nature Computer Science* [Volume 1](https://link.springer.com/article/10.1007/s42979-020-0063-3), with arXiv version [here](https://arxiv.org/abs/1906.03280).

To summarise it very quickly:

My position is that the majority of the people who feel that a particular algorithm's performance will be constrained in practice by NFL are wrong, and they should just *ignore NFL*. 

Some common misunderstandings include: 

* Most people don't have a good intuition for how large and weird the set of "all possible objective functions" is (or the sharpened variant, "all objective functions closed under permutation"). 
* Many researchers think that the real impact of NFL is in showing that the algorithm has to be tailored to the problem -- this is the position of the original authors. But as I argue in the paper, our *generic* algorithms (like Genetic Algorithms, or Simulated Annealing) are *already* tailored to the problem. 
* Another common position (in a way, equivalent to the above) is that algorithms must use some "domain knowledge". But as I argue, the term "domain knowledge" is usually undefined, and when we realise what it has to mean in the context of NFL, we realise that the intuition it creates is totally misleading.

Instead, I claim via an anthropics argument that the true meaning of NFL is different. NFL shows that a search algorithm can't do better than random, without some extra assumptions about the problem (ie, domain knowledge). Similarly, (cf Hume), NFL ideas show that science cannot work, without some extra assumptions. Similarly, another NFL theorem shows that supervised machine learning cannot work, and indeed everyday human learning cannot work. But they do work! If they didn't work, it would be because the Universe was not well rule-bound. In that case intelligent life wouldn't exist. The extra assumption that we need is provided by the anthropic principle.

Thus the true meaning of NFL: everyday learning works, science works, supervised learning works, and metaheuristic search works, *because we are here*.
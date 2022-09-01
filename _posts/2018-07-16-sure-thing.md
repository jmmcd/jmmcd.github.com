---
layout: post
title: The Book of Why and the sure-thing principle
tags: analytics
---

The Book of Why and the sure-thing principle
========

*The Book of Why* by Judea Pearl and Dana Mackenzie is really, really good! It's about *causality*: how the principle "correlation is not causation" came to be so central in statistics that discussion of causation came to be almost off-limits not only in statistics but in medicine and social science, and how in the last couple of decades statisticians, led by Pearl, have made enough progress to allow discussion of causality after all. 

Causality is important because often the questions we want to answer with statistics are indeed causal ones: not whether there is an association between jogging and health, but whether if someone decides to start jogging, they will become healthier. The former might be written *p(health \| jogging)*, but the latter as *p(health \| do(jogging))*, where the *do()*-operator indicates an *intervention*, i.e. *choosing* to start jogging. The *do()*-operator and the manipulations which can be done to formulas containing it are central contributions of Pearl's programme. Crucially, they allow researchers to ask and answer causal questions even when they only have observational data, not randomised controlled trial (RCT) data. [Pearl has said](https://twitter.com/yudapearl/status/1012512462770298880) that one of the biggest effects of his programme will be to erode the "hegemony" of RCTs.

According to the book, statistics has been crippled by being unable to discuss these questions without RCT data. The enjoyable narrative is that of a few causality-speaking renegades in the early days of statistics being side-lined by the founding fathers, until the "causal revolution" of recent decades, led by Pearl. It's a "popular science" book, but a relatively detailed one. I don't think it will be accused of over-simplifying as many pop science books are. Maybe there are places where statisticians will say that they aren't really as crippled in their methods as the book suggests, but on the other hand we are still hearing [reports from researchers](https://twitter.com/yudapearl/status/1018564041373933568) that they have to pretend not to talk about causation at all in order to placate reviewers for statistical journals.

A big contribution of the book and the "causal revolution", for me, is that it is *unifying*. By the way, I am not a statistician, so the following is an outsider's impression. Just as Bayesianism seems to be a single, consistent framework (in contrast to the framework of frequentist null-hypothesis testing, which seems like a collection of recipes for particular situations), so Pearl's causal methods seem to give a unified approach to situations involving confounding and similar issues (in contrast to the current, disunified collection of approaches and methods).

One of the goals of the book is to explain why artificial intelligence needs causality. We humans operate just fine, distinguishing correctly between causation and correlation: we don't prevent the sale of ice-cream in order to prevent forest fires, even if [there's a correlation between them](https://www.goodreads.com/quotes/693894-most-of-you-will-have-heard-the-maxim-correlation-does). But how can we teach this type of intuition to our AIs? The *do()-calculus* is one part of the answer, but it still requires as an input, constructed by a human, a causal diagram representing possible causal effects. After all, ["no causes in, no causes out"](https://twitter.com/yudapearl/status/1015343363468357633). Perhaps this step is being automated at the cutting edge of research right now?

There's a lot more to enjoy in the book. I've already said [elsewhere](https://twitter.com/bleepbeepbzzz/status/1017871404216266752) that Pearl is a rare combination of (1) unimpressed by current deep learning and "scruffy" approaches to AI, and (2) open about the fact that he himself is working towards AI/AGI. So in the debate between those who over-hype deep learning approaches, and those who try to look cool by downplaying the possibility of AGI, he effectively says that both sides are wrong. And he's too important to be dismissed. I love that, because I hate debates where there are sides.



Simpson's paradox
-----------------

Anyway, the main reason I started typing this post, which turned into a mini-review and recommendation, is a small pedagogical point I picked up on while reading the section on Simpson's paradox and the sure-thing principle. First, an introduction. [Simpson's paradox](https://en.wikipedia.org/wiki/Simpson%27s_paradox) is well-known. I like one of the examples given in the book, which concerns the effect of a drug on heart attacks. Here's the (fictitious) data from the book (Table 6.4):

|     | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Does not take drug |                     | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Does take drug   |                     |
| --- |:------------------:|:-------------------:|:----------------:|:-------------------:|
|     | **Heart attack**   | **No heart attack** | **Heart attack** | **No heart attack** |
| Female        | 1   | 19 | 3  | 37 |
| Male          | 12  | 28 | 8  | 12 |
| Total         | 13  | 47 | 11 | 49 |

It seems that the drug is bad for females (1 heart attack out of 20 patients without the drug, versus 3 out of 40 with, that is **1/20 versus 3/40**), bad for males (**12/40 versus 8/20**), but good for people overall (**13/60 versus 11/60**). How can that be?

The underlying explanation is that females had a higher propensity to take the drug, and males had a higher propensity to heart attacks. So, sex is a confounder here, and we need causal thinking to get the right interpretation. We can't just *add raw numbers*. We adjust for the confounder by *averaging proportions*.

We calculate the *rate* of heart attacks in no-drug females as 1/20 = 2/40, and it's 3/40 for yes-drug females. And similarly it's 12/40 for no-drug males and 8/20 = 16/40 for yes-drug males. We now average these: it's mean(2/40, 12/40) = 14/80 overall for no-drug people and mean(3/40, 16/40) = 19/80 overall for yes-drug people. So the drug is  **bad** for females, for males, and overall.

(In fairness, Simpson's paradox was understood and resolved by mainstream statistical methods before the "causal revolution".)



The sure-thing principle
------------------------

Why did the example violate our intuition in the first place? Because if a drug is bad for females and bad for males, it can't be good for people overall! The *sure-thing* principle, named by Savage in 1954, is the principle that makes this thinking work. The patient has to be male or female, so if the same conclusion holds for either, then it holds if we "don't know" the sex of the patient. That's the "sure thing". The sure-thing principle works as long as there are no confounding effects, like the effect of sex in the drug/heart attack story. If there are, we have to identify the confounders and control for them to make sure we get the right result.

Now, another story. Suppose a businessman can buy property A or property B, and thinks that the outcome of the upcoming presidential election could affect the probability of financial gain. He uses some very detailed simulation models, I guess, to arrive at the numbers below for the probabilities that he'll achieve a financial payoff for the properties, under a Democrat-wins scenario and under a Republican-wins one.

|     | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Buy property A      |                      | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Buy property B     |                     |
| --- |:-------------------:|:--------------------:|:------------------:|:-------------------:|
|     | **$1 payoff**       | **No payoff**        | **$1 payoff**      | **No payoff** |
| Democrat wins             | 5%  | 95% | 7.5% | 92.5% |
| Republican wins           | 30% | 70% | 40%  | 60%   |

These numbers are exactly the same as in the drug/heart-attack story! As before, it is a "sure thing": a Democrat or a Republican has to win, and it looks like property B is better no matter which, so the right decision, assuming no confounders, is to buy property B. 

However, as before we need to check for a confounder. A confounder could indeed arise if the businessman's decision could affect the election outcome! If so, and if buying property A could materially help the Republican, then maybe the businessman should do so after all, because that would get him 30% instead of the 5% or 7.5% he would get if the Democrat wins. (I say "maybe" because it depends on *how strongly* his decision could affect the election outcome. We don't have numbers for this, corresponding to the fact that we don't have a final "total" row in the table this time.) This example illustrates, using the same numbers as in the previous story, that the sure-thing principle is an ingredient in this type of problem, and that it only works as advertised if there are no confounders.

... or at least, that's what I expected the book to say. Now, finally, I'm reaching the small point I wanted to raise about the pedagogy here. What the book *actually* says is that if the businessman's decision could affect the outcome, then perhaps he should consider all *other* effects of one president over another, i.e. effects other than the probability of financial payoff. Now, that's not false at all, in the real world. The businessman's *vote* is affected by his principles, and his vision for society, and the implications for his tax bill, and his view of which candidate has the best hairstyle; and if his buying decisions can affect the election outcome, maybe he should allow those things to affect his buying decisions too! 

But in my view this is no longer a good illustration of the sure-thing principle. If we are talking about outcomes other than the financial payoff, then the whole scenario is destroyed. Maybe he should buy property A, regardless of financial payoff, because his aunt lives next door and he'd like to visit her more. Similarly, maybe the patients should choose not to take the drug because it tastes bad, or they want to annoy the scientist carrying out the trial. If we change the objective function we're trying to optimise, everything else goes out the window. 

Instead I think it would be pedagogically better, in an Occam's razor way, to keep the two scenarios (businessman and heart-attack drug) exactly parallel. That is, focussing only on the payoff as originally defined, but introducing the extra causal dependency (property choice -> election outcome). This is how I have written it above. Somehow I feel that having *the same numbers* for both stories presented a perfect opportunity to make the point in a clean way. Introducing a new causal dependency *and* changing the objective to include non-payoff considerations obscures the point; the correct point could have been made by introducing the causal dependency and keeping the same objective. I'm not just going against Pearl and Mackenzie here, because they are following "The sure thing principle" (Jeffrey, 1982). Jeffrey changed the scenario to a local election (not presidential) to make it more realistic, and changed the objective to include non-payoff effects.


Conclusion
----------

I've written a lot here about a small point where I wanted the book to say something differently. This small point stood out, for me, because my impression is that otherwise the pedagogy is *excellent* throughout. Both Pearl and Mackenzie deserve credit for making it so accessible. I've written far less than I could have (if I had time) about the many ways in which I loved this book. I'd like to pick up on the book's discussions of artificial intelligence and its implications for decision theory, and to make a link between the book's treatment of counter-factuals and that of Douglas Hofstadter, but that will have to wait for future posts. So don't get me wrong: this book is great and everyone should read it. 

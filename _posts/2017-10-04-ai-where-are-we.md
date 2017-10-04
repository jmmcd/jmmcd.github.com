---
layout: post
title: AI: Where are we?
tags: artificial_intelligence
---

AI: Where are we?
========

We are not close to general AI, but there seems to a clear trend towards increasing generality in machine learning methods over the past 10 years. Generality means that the same algorithms can be applied to many different problems. This short blog post (with many citations omitted) describes my position, that we are making real progress towards general AI, that is agents with a high level of intelligence (perhaps superhuman, perhaps not, but still high) across many tasks and situations.

Narrow machine learning
-----------------------

Machine learning was always about creating algorithms, such as decision trees, into which could be plugged "any" data set -- they were generic in that sense. But there were always several important respects in which they were not generic.

* An algorithm for supervised learning (e.g., support vector machines) could not carry out unsupervised learning, or vice versa; and neither could carry out "action-oriented" tasks such as reinforcement learning;
* For supervised and unsupervised learning algorithms, the input was required to be a structured data set, that is consisting of rows and columns of numerical (perhaps binary or categorical) data, with a numerical or categorical label for supervised learning.


What has changed?
-----------------

It is now more common to use the same algorithm for multiple tasks, e.g. gradient boosted trees are near the state of the art for both regression and classification. This unifies these tasks. Image, audio, and other sensor-type data can now be processed using convolutional networks which implicitly learn representations suitable as input to the same types of regression and classification algorithms already mentioned. These supervised learning algorithms can in fact be placed "on top of" the convolutional network and trained end-to-end, that is using a single architecture and a single training algorithm. This unifies image, audio, and other sensor data with structured data. Natural language can be treated using recurrent networks and embedding methods, which again make the data suitable for input to a standard algorithm. They do not retain all aspects of the original language, but examples including modern neural network-based translation show that they can learn sufficient aspects of language structure and semantics to be useful. Again, such models can now be trained end-to-end. This unifies language data with the other types. Although unsupervised learning algorithms have existed for a long time, modern algorithms can use unlabelled data to learn representations suitable for supervised tasks. This unifies supervised and unsupervised learning.

Finally, reinforcement learning (RL) research now takes advantage of the representations mentioned above, including convolutional networks, recurrent networks, and embeddings, to represent environment data. In principle, it is now possible to create an RL agent with a single architecture including these components, which learns using unlabelled data and solves regression and classification problems implicitly as part of its overall sense-act-reward loop. The RL paradigm is defined by an agent in an unknown environment, with sensors, actuators, and a reward signal -- a setting sufficiently general for artificial general intelligence to live in. In other words, a sufficiently good RL agent would be an AGI. Therefore, this "grand unification" of reinforcement learning with supervised and unsupervised paradigms, and of regression and classification tasks, and of many different types of data representation, will represent an important step towards true AGI. It is not far away.

All of the ingredients mentioned above were made to work only in the last 10 years or so.

Missing ingredients in true intelligence
----------------------------------------

But perhaps there is a missing ingredient for true intelligence -- such as consciousness. Some argue that consciousness is not required for intelligent behaviour, or that consciousness emerges in any sufficiently complex system, or any sufficiently complex system acting with goals in the world. There seems no way to answer this question for now. However, some research relevant to a functional implementation of consciousness has been done, as follows.

As a first step, consciousness requires the ability to *introspect*. RL agents would require the ability to sense their own internal state. This is not the same as saying that the state is readable as part of the agent's computation, which it trivially is. (Similarly, a neural network, which carries out a million internal additions and multiplications at every iteration, would need to be trained to map a pair of inputs to their sum, and will do so imperfectly.) Instead, the point is that the agent's state can be sensed and processed using the same machinery which is already used to sense and process external state, hence taking advantage of pattern recognition and other machinery learned there. Pattern recognition on internal states is actually a pretty good functional definition of consciousness. Progress in this has already been achieved. Whether this would lead to "true" consciousness, with qualia and all -- [if such a thing exists](https://en.wikipedia.org/wiki/Consciousness_Explained) -- may be moot.

Another seemingly-important aspect of human conscious thought is *attention*. Our multiple senses, including our introspective sensing of our own mind, are not always given equal prominence in [every decision we make and action we take](https://en.wikipedia.org/wiki/The_Police). Attention is a mechanism for focussing on the right data. Again, recent progress has been made in taking advantage of attention mechanisms in machine learning.

Hardware
--------

Some commenters argue that increasing computing power will inevitably lead to AI, for example [Kurzweil](https://en.wikipedia.org/wiki/The_Age_of_Spiritual_Machines) takes advantage of exponential trends in computing (Moore's law, and similar) as a cornerstone of his argument. Many AI researchers dismiss arguments based purely on computing power, arguing instead that progress in "software" -- in models, representations, learning algorithms, datasets, task specifications, and so on -- is what is required. (Others argue that exponential trends cannot continue, either for *a priori* reasons or because of physical limits.) I think the focus on software improvements is correct, and I have argued that such improvements are happening, though certainly more are required. However, a separate line of argument supports the claim that improvements in raw compute power are relevant. It relates to [AIXI](http://www.hutter1.net/ai/aixigentle.htm), a general RL agent. In principle, AIXI is already a super-human AI -- it's just not computable. There are approximations to AIXI, including [AIXItl](http://www.hutter1.net/ai/aixigentle.htm) and [Monte Carlo Tree Search AIXI](https://arxiv.org/abs/0909.0801), but they're not good enough yet. However, computing power will make these approximations better, and no new improvements in software are required for this. This alone suggests that increasing computing power is relevant to whether and when AGI is possible.

AI safety
---------

I will finish with a short and subjective statement on AI safety. by stating that I regard self-improving AI agents as being possible in principle, and in particular if agents are at human level in many other respects then their self-improvement seems plausible. I agree with Bostrom and others that [AI motivations will not be inherently positive](https://www.fhi.ox.ac.uk/wp-content/uploads/Orthogonality_Analysis_and_Metaethics-1.pdf) for humanity. I agree with [MIRI and others](https://intelligence.org/files/Interruptibility.pdf) that kill switches, AI boxes, and other obvious AI safety measures are fallible. I suppose that the risk of catastrophic outcomes of self-improving AI with goals uncontrolled by humans may be small, but it is not zero. Therefore, I think that research into AI safety is needed.

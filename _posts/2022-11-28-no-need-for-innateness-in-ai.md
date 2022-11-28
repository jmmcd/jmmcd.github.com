---
title: No need for innateness in AI
layout: post
tags: artificial_intelligence, evolutionary_computation
---


The current debate in AI about *innateness* goes back far beyond the origins of AI itself. It's a continuation of the debate about innateness  in the human mind. No-one nowadays argues that the human mind is really a blank slate, other than some people for whom idealogy requires it. 

But in AI, there are two lively and well-founded schools of thought. Some argue we need to create AI systems with strong innate properties, such as a human-designed decomposition of the system into modules, and / or symbol-processing methods. Others argue that innateness isn't really needed, as end-to-end training can create implicit modules and symbols as needed. (Even the latter are still in favour of priors such as convolution or transformer architectures -- something I'll come back to below.)

Some of those in favour of innateness in AI point at the human brain as evidence. The human brain has a lot of innate structures and priors. It seems to learn a lot of things that should not be learnable based on the data that is available in the first few years of life. 

### Everything innate is actually learned

However, this can't be taken as evidence that we have to program AI systems with innate structure, because everything innate in the brain was itself learned -- by evolution. Evolution used feedback from the environment to create implicit modules and priors in the brain. 

Some people argue that evolutionary learning of this type is not learning. This is a clear-cut case of [disputing definitions](https://www.lesswrong.com/posts/7X2j8HAkWdmMoS8PE/disputing-definitions). Tom Mitchell would say this *is* learning: "A computer program is said to learn from experience E with respect to some class of tasks T and performance measure P, if its performance at tasks in T, as measured by P, improves with experience E." Here, T consists of the tasks of *lifetime* learning, while E is the experience of many organisms' success or otherwise.

But I don't care whether we call evolution "learning" or not! The point is that if wanted to, we could design an AI system in the same way. Everything that pro-innateness people want to build in, we could instead learn.

Maybe that would work well, maybe not -- I'll talk more about that below. Maybe there are other reasons to argue in favour of innateness. But **the human brain provides no evidence in favour of innateness in AI systems**.




### Priors for learning

But there are two snags to deal with.

First, doesn't a No Free Lunch argument prove that we have to have priors in order to learn anything? In fact, how did evolution manage to do anything, if it doesn't have priors?

Second, aren't those in favour of NO innateness in AI still in favour of a *little* innateness? Successful neural network architectures already embody some priors: a prior in favour of local information processing (Convolutional nets) and a prior in favour of permutation invariance (Transformers). Nobody seems to be against those.

The same argument answers both of these points, and I will try to set it out. 

We live in a nice universe. It has locality properties in space and time, [without which evolution wouldn't work at all](http://www.jmmcd.net/2022/08/31/keep-calm-and-ignore-nfl.html), because every adaptation to the environment in one generation would become useless in the next.

And it so happens that the types of information-processing available to evolution also have these locality properties. In the physical world, information-processing is inherently local in space and in time, e.g.:

1. It's easier for a neuron to connect to a neighbouring neuron than to a distant neuron;
2. It's easier for two neighbouring retina cells to connect to two neighbouring neurons, than to two widely-separated neurons;
3. Because of entropy, it's easier to remember something for a short time than for a long time.

Look again at these properties: (1) gives us a prior in favour of modular structure; (2) gives us a convolution-like prior; (3) gives us a prior not too dissimilar from a Transformer with a limited attention window.

These priors are inherently useful for learning in our rule-bound universe; and the neuronal system that evolution hit on for information processing has these priors, simply because they match physical properties of the universe. This was a very nice free lunch for evolution!

However, it is not a free lunch for AI! Because information-processing in our machines does not have these inherent properties. It was the invention of RAM -- **random access** memory -- which created the possibility of information processing without any locality prior in space or time. RAM is great for algorithms, because any part of the algorithm can refer to any other, and if some very old information is needed, we can rely on it being present. But RAM doesn't have that inherent match with the locality properties of the universe. In principle, our algorithms could learn them. Instead, we gradually understood them and wrote them in by hand. 

But the lesson of deep learning versus feature engineering is that there is always room for a learning process to improve on hand-engineered designs. Maybe we'll eventually settle on priors a bit like those of modules, convolution and transformers, but learned -- by evolution or otherwise.
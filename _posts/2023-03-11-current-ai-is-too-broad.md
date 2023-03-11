---
title: Current AI is too broad, not too narrow, but actually it's fine
author: James McDermott
---

Here are two common objections to AI:

1. AI systems need ridiculous amounts of training data, compared to humans, eg 1M games of chess or 1B images or 1T words. 

2. AI systems are only good at narrow tasks, not at general tasks, as humans are.

Actually, objection 2 is false (in a specific sense which I will explain). Our current systems are *too general* because they learn things human cannot learn, and that causes objection 1. But I'll argue that this ability to learn things we cannot learn turns out to be useful after all.

---

A ConvNet can learn visual patterns that humans cannot: it is broader, in this sense, than we are. That is one of the reasons we want to use ConvNets for tasks like medical diagnosis. That is also the source of adversarial examples. How did humans come to be narrower in this sense? Most of the vision system is hard-coded. Evolution "knows" what universe the new human will live in, and has pre-designed a lot of hardware for it. The new human has relatively little to learn. So fewer than 1B images are needed. (Also, every time we see something, we also see many augmentations of it, which both gives us a larger training set than we initially think, and gives us robustness to adversarial examples -- but let's leave that aside for now.) If we really do want a ConvNet that can itself learn from fewer images as humans do, we could create a *narrower* prior than a ConvNet has -- either by hand, or by learning the prior as evolution did, using many more than 1B images.

In ["Priorless Recurrent Networks Learn Curiously"](https://www.semanticscholar.org/paper/Priorless-Recurrent-Networks-Learn-Curiously-Mitchell-Bowers/6d0cc01e4bdf18b86bb74d1c6d9a41b5a4890c58), Mitchell and Bowers (cited recently by [Chomsky et al](https://www.nytimes.com/2023/03/08/opinion/noam-chomsky-chatgpt-ai.html)) show that LLMs can learn languages that would never arise as human languages. An example is that "colorless green ideas sleep furiously" is grammatical, but the reversal "furiously sleep ideas green colorless" is not. But LLMs can learn a language where that is legal. This is another case of the AI being too broad, not too narrow. 

For Chomsky this is a shortcoming of the LLM, because it shows that an LLM doesn't conform to a theoretical model of human language, universal grammar (UG). That's true, but not important for most purposes. It's obvious that this will happen because the networks we use -- LSTMs, Transformers, whatever -- don't enforce a UG structure. And there are lots of formal languages and pseudo-languages in the training data, and even lots of reversed sentences, so the LLM has to learn to predict tokens in them. It still seems to do a good job of writing grammatically in English.

But what is important is that **the theory of universal grammar refers to sentence structure only, and an LLM is not only learning sentence structure**. It has to learn other, more abstract structures as well. 

For example, the LLM has to learn the sequential structure of an argument: "Premise 1, therefore Lemma 2, therefore Lemma 3, therefore Conclusion 4". And a high-quality LLM needs to be able to reverse such an argument, just as any human could: "Conclusion 4 is true, because Lemma 3, because Lemma 2, because Premise 1." This reversal at the level of abstract argument structure is perfectly legal and definitely useful to learn. Whereas, as we saw, a reversal at the level of sentence structure is not grammatical in any language. (Some individual sentences can be reversed, in some languages, but it is never a general rule, whereas the reversal of the argument above is.)

The reversal of a sequential argument is just one example. More generally, I think that there are no structures in our abstract arguments which are ruled out on UG-like grounds. If there were, it would be a hole in our thinking -- analogous to being less than Turing-complete. I don't mean that such a hole is impossible in principle, but rather that if such a hole existed, we would fill it.

This has an important consequence for the design of LLMs! If we try to build in a narrower prior to push LLMs to conform to UG, this could work against their ability to use abstract argument structures which don't have to conform to universal grammar at all. Remember that early layers, eg in a Transformer, deal with words, and later layers deal with something more abstract, and all are implemented with the same mechanism!

So: current AI systems are actually broader than humans, not narrower -- but being broad is a good thing after all.
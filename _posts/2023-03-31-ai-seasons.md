---
title: AI Seasons
layout: post
tags: artificial_intelligence
author: James McDermott
---

AI is having a moment in the sun right now.

> *[tell them, the winters grow](https://www.lightspeedmagazine.com/fiction/love-is-the-plan-the-plan-is-death/)*

Everyone knows the AI Winter. Could it happen this time? I think there's too much value on the table already, and too much potential value. But we might destroy all life on earth, which is quite a wintery thought.

Many people now advocate a pause or a ban on further development of large-scale AI. Eliezer Yudkowsky quotes [@gwillen](https://twitter.com/gwillen/) who framed it very well: let's have [AI Summer](https://twitter.com/ESYudkowsky/status/1636315864596385792) instead, that is let's have the season when we relax and enjoy the fruits of our work. I might call that AI Harvest, but ok. Funny enough, Autumn is the season [Led Zeppelin didn't mention](https://genius.com/Led-zeppelin-the-rain-song-lyrics).

It's true that there's a lot we could do now, without making bigger and more dangerous models. Advocating a pause on bigger models is not advocating for a pause on research! People who want to publish papers (ie, everyone *except* the big AI labs, who [only publish ads](https://cdn.openai.com/papers/gpt-4.pdf) for their products now) will be better off, because the cutting edge of research won't necessarily require a giant GPU cluster. People who want to make money will be better off, because they won't have to worry that the next GPT will under-cut everything they develop. 


### So what should we do this summer?

1. We could make smaller models! Alpaca and GPT4ALL is one direction for this. These are about broadening access, with some cost in performance, so maybe the pure AI companies may not have a good incentive to push in this direction. But consumer-oriented companies might want to put a good LM-vision model on a cheap phone: then they have a motivation to make a smaller model. Maybe there's more value in this end of the market. Open-sourced code and weights wouldn't change the value proposition here.

2. We could make smaller models in a different sense! To simplify a bit: a current LM uses its parameter budget and its training budget to achieve four things:

    1. Language use (syntax and semantics)
    2. General facts about the world (cats chase mice, not the other way around)
    3. Specific facts about the world (Lima is the capital of Peru)
    4. Reasoning.

    A huge amount of the parameter / training budget must be spent on category (c). And just like in humans, it seems natural that (c) is the category that could be most easily out-sourced. Not completely, because there are shades of grey among all categories, and it helps to have facts available to reason with, but partly. A lot of obscure knowledge would be better represented either as knowledge base lookups (like in the OpenAI Wolfram Alpha plugin) or as pre-existing external text (Wikipedia, scientific articles, or just web pages), to be read in using a search mechanism (like in Bing Chat). The return value from the lookup is read in the background and becomes part of the LM's ticker tape, but it's not echoed to the user - the LM just continues talking after reading the ticker tape. In these mechanisms, the LM has to decide when it needs to out-source. I think this is probably pretty easy, but an interesting research question is how to train it to learn as few specific facts about the world as possible! 

3. We could make existing systems much more sample-efficient! This is partly accomplished by the previous point, ie out-sourcing the reading of some specific information to run-time reading instead of training. But there's a lot more that could be done!

4. We could see how to improve LM reasoning! Currently they do seem to reason, to some extent. I'm not sure whether this is just at the level of learning useful templates for sentences and paragraphs, or how much deeper it is. But we could go beyond the simplest autoregressive model. Currently, every token gets the same fixed amount of computation. That's why the "let's think step by step" hack works: it allows more computation to achieve an answer to the same problem. One idea is that we should allow the system to keep generating tokens all the time, building up potentially useful thoughts in the context window; and only sometimes choose to connect those to the output. This would be good for GPU utilisation stats too! As it stands, the GPU is idle while the human is typing!

5. We could work on both Ethics and Safety! Let's figure out some solutions which would help the next generation of models to be much better from both points of view. For a long time we didn't have AI systems which were really worth studying from the Safety point of view, but now we definitely do. 


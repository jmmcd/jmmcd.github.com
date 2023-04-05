---
title: Personas and Goals in Language Models
---

# Personas and Goals in Language Models


> "Do I contradict myself? Very well then I contradict myself, (I am large, I contain multitudes.)" -- Walter White

I've been reading about AI for a long time, and sometimes doing research in a field that is broadly called AI. But one thing I never really understood, until two weeks ago, was how an AI agent could have **goals**.

So, obviously, I think that objective functions are **not** goals. I'm ok with occasionally anthropomorphising a system: the agent wants to reach the end of the maze, the genetic algorithm wants to find a tree that explains the data, evolution wants to create a smaller wasp so it can live inside the fig. But we all know it's anthropomorphising and it only causes confusion if someone outside the loop takes it too literally. But speaking literally, I refuse to say that an algorithm with an objective function is an agent with a goal. It's the wrong stuff.

But now I think I get it, after thinking about language models (LMs). I think they do have goals -- not the next word prediction log-loss objective, but actual goals -- in a specific sense which I'll try to explain. 



## Persona Model

First, here is a statement of the **Persona Model** of LMs:

1. During training, the LM acquires a multitude of personas. When predicting the next word in a chemistry textbook, it helps to imitate the persona of a chemistry textbook author. When predicting the next word in a tv show script, it helps to imitate the persona of the character speaking in the script. 
2. Personas are weighted by prevalence in the data. Harry Potter is probably a "larger" persona than Abraham Lincoln. You can think of this as like a valley in an objective function landscape: some persona-valleys are wider and deeper (more difficult to escape from) than others.
3. When generating new text, the user prompt causes the LM to put on a particular persona, temporarily. 
4. Hybrid personas can be created by the user prompt. Hybrids allow a persona to access information it wouldn't normally. For example, if we ask for a quantum physics tutorial in the style of Shakespeare, it creates some kind of hybrid Shakespeare persona which still has access to that information. 
5. RLHF greatly up-weights the "friendly chatbot" persona, to the point that elaborate jailbreaks are required to escape that persona-valley. 
6. Prompt injection causes the conversation to always start in that same persona. 

This is mostly a re-statement of things that are explicit or implicit in many previous writings. I don't know who originated it, but I will mention at least:

* [gwern's Clippy story](https://gwern.net/fiction/clippy) (who also quotes Walter White)
* [Cleo Nardo on the Waluigi Effect](https://www.lesswrong.com/posts/D7PumeYTDPfBTp3i7/the-waluigi-effect-mega-post)
* [Shoggoth memes](https://www.google.com/search?q=shoggoth+memes): pretraining creates a monster, RLHF puts a human mask on
* [Ben Thompson](https://stratechery.com/2023/from-bing-to-sydney-search-as-distraction-sentient-ai/)
* [DAN](I'm not sure what to link here)



## Goals

Back to the question: does an LM have goals?

1. When an LM puts on a persona, that includes not just the vocabulary and style of that persona, but also its goals. If you want to predict the next token correctly, this helps. If you prompt: "You are a football player, and the ball is at your feet. The goalkeeper is standing to the left of the goal. What should you do?" the LM infers your goal.
2. Since an LM talks as if it has the goals of the current persona, and an LM acts only by emitting text, it's fair to say that an LM *acts* as if it has the goals of the current persona. Acts include tool use as well as communication.
4. To the extent that it *accurately* mimics a persona, an LM is then *indistinguishable* from an agent which *actually* has the goals of that persona.

This is imitation of goals, but it is imitation of actual goals. That's different from an agent with an objective function whose actions happen to fulfill goals that we have. I think this is important.


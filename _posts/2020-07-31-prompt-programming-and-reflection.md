---
title: Prompt Programming and Reflection
author: James McDermott
---

TLDR Could we use GPT-3 in a reflective paradigm both to improve its performance in writing long text, and also to add an aspect of intelligence that it lacks? Idea: rewrite the prompt with exponential compression of previous input.



To start we need three observations:

1. If we ask GPT-3 to write some longer text, it does so. Often these longer texts are coherent. But sometimes [they wander and contradict themselves](http://dailynous.com/2020/07/30/philosophers-gpt-3/). This is partly because GPT-3 has a limited attention window ("short-term memory"). It lives in the now, generating one word at a time. It doesn't settle on a position for the essay it's about to write and then hold that in mind as the goal throughout. 

2. Our own intelligence is different in this respect, at least when we're concentrating and engaging System 2. We store what's happened so far, and refer back to it when deciding what to say or do next. When it becomes too much to store it all, we summarise and compress, and refer back to the summarised version. We are *reflective*: we think about our own thinking, and this is crucial to our next action. We often have a sense of multiple sub-agents (Minsky, Hofstadter) in a dialogue. In a sense we command ourselves.

3. Using GPT-3 effectively via *prompt programming* is [a new paradigm](https://twitter.com/ch402/status/1273765062633639936) in AI. It's like being a horse whisperer, or talking to [a superintelligent cat](https://www.gwern.net/GPT-3#prompts-as-programming).

To explain the idea, I'm going to stick to the setting where GPT-3 is required to write an essay. Typically we provide a prompt such as a title and opening sentence. In the current approach, we just keep pressing enter, so that at each step GPT-3 takes the text so far as its prompt. It is easy to see how this could wander and eventually [contradict itself](https://twitter.com/raphamilliere/status/1287047986233708546/photo/2).

So, the proposal is that we need an extra agent sitting on top of GPT-3, continually rewriting prompts. At each step, we take GPT-3's output and append it to a buffer, and that buffer eventually becomes the essay. But then, we write a new prompt before requesting more output. In the new prompt we include the original prompt (the essay title and opening sentence), a short summary (e.g. the first sentence) of each paragraph, and then the current paragraph. This forces GPT-3 to retain the entire context and argument in its attention window. Hopefully it prevents self-contradiction.

In a longer text, we might need to go much further. To write a book, we continually rewrite the prompt to include the title and a summary of the introduction, then a short summary of each chapter, then a short summary of each paragraph in the current chapter, then the complete current paragraph. In other words, we continually rewrite the prompt as an exponentially-decreasing compression of what we have so far.

Doing this in a simple way might be good enough to achieve some improvements. But doing it in a more intelligent way might be the key to achieving a more reflective type of intelligence. GPT-3 is already able to compress text. So, let's run a second copy of GPT-3 to compress each paragraph and then each chapter after it's written.

To me, this proposal is a nice mirror of what happens in our own minds. We use the same kinds of mechanisms -- based on compression -- to understand our current sensory input and to understand and reorganise our memories for future use. When planning we seem to engage in a kind of internal dialogue, with one part of the mind posing questions and problems, and another responding to them. So it makes sense to use multiple copies of GPT-3, both using the same mechanisms, to create this kind of prompt-response dialogue.

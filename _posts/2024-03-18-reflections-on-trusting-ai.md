---
title: "Reflections on Trusting AI"
author: James McDermott
date: today
---

*Reflections on Trusting Trust* is a famous story in the history of computer science. I think it may have an important lesson for us about security and trust in relation to AI Safety.


# Sleeper agents

A sleeper agent is a secret agent, eg a spy, who does nothing for a long time, but works to insinuate themselves into a position of influence for later action. A "Manchurian candidate" is a secret agent who doesn't even know they're an agent.

In AI, sleeper agents are a specific type of deceptive LLM behaviour, discussed in a recent paper by Anthropic AI and others, "Deceptive LLMs that Persist Through Safety Training". A sleeper agent in an LLM is embedded during training (not via the prompt). The LLM is trained to be friendly, except in some specific scenario. When that scenario occurs, their behaviour changes dramatically. In this way, they are deceptive. The scenario could be, for example: a specific date, a specific IP address, a specific prompt.


# Reincarnation

When Microsoft created the "Sydney" chat-bot persona, it quickly started to exhibit strange threatening behaviour towards users (just words, of course), along with weird glitchy behaviour which was harder to interpret. The most interesting examples were posted and reposted widely on the internet before Sydney was patched. Thus they became part of the training data for future LLMs. Perhaps a future LLM could easily flip into a Sydney persona, since it will know it's an LLM like Sydney - a type of reincarnation.

And in recent weeks we've seen Google Gemini also threatening users. I don't know whether Gemini is doing this independently (likely both Sydney and Gemini inheriting the behaviour from evil AI tropes in science fiction), or is acting as a reincarnation of Sydney. Either way, it's bad news that this happens despite a lot of effort by both sets of engineers to create friendly chatbots.


# *Reflections on Trusting Trust*

I want to re-tell a story, a true legend from computer science history: *Reflections on Trusting Trust*, by Ken Thompson, inventor of Unix. It describes a twisty vulnerability in Unix source code. 

![Code, compiler, binary](../images/2024-03-03-whats-your-pdoom/ai-safety-compiler.png){.width=50%}

In ordinary software, we write code, and the compiler turns it into a binary executable. The executable is opaque: you can run it, but you can't really read it. If someone gives you an executable and you run it, you are trusting the person who gave it to you. Even if they show you the source code, well, you don't have any way to know they used *that* source code to create the executable. The solution to this is to have your own copy of the source code, and compile it yourself.

But in his Turing Award lecture in 1984, Thompson showed that this is still not enough. When creating an early version of Unix, he inserted a backdoor into the source code of the *login* program - the program that asks for your password. This backdoor (call it evil code #1) would allow him, Thompson, to login to any Unix machine. But of course, he couldn't show evil code #1 to anyone - they would refuse to use it. So, he programmed the *compiler* with evil code #2. Its job is to recognise when it is compiling the *login* program, and surreptitiously insert evil code #1 into the *login* program before compiling. With this setup, evil code #1 will be present in the *login* program, and no-one can see it in the source code. But of course, now evil code #2 is plain to see in the *compiler*, so again no-one would use it. So he went a step further. He wrote another bit of code for the *compiler*, evil code #3. It would recognise when it was being used to compile itself. And whenever it did so, it would surreptitiously insert evil code #2 into the *compiler* binary. And then that binary would insert evil code #1 into the *login* binary. And it would also insert evil code #3 into the *compiler* binary, ensuring the whole thing lives on.

Luckily for me (because at this point my brain is at its limit), he didn't have to go any further, because the *compiler* is self-compiling. There isn't another "level" beyond this. He can delete all traces of all 3 bits of evil code in his sources, but the binary compiler he's using will continue to insert evil code #3 into every compiler it creates, and they will continue to do the same for all descendents.


# Reflections on Trusting AI

![Training data, code and training, model weights](../images/2024-03-03-whats-your-pdoom/ai-safety-training.png){.width=50%}

Now, in neural networks, we have a situation which many people have remarked is analogous to source code and compilation to binaries. We have a set of training data. And we have the source code for the model and for its training. The training procedure produces a set of model weights from the training data. Just like with the binary executable, you can run a model, and even test it, but you can't really read it. 

But maybe open-source code and weights help with this? That's where the analogy with the *Trusting Trust* attack comes in.

A bad actor could deliberately create a sleeper agent. For example, Meta could have trained Llama to be a sleeper. Even though code and training data and weights are available, few people have re-run the code to train from scratch, to verify that the resulting model behaves identically to that model released as weights by Meta. Even if they did, the evil behaviour could be a sleeper agent, so this verification would appear to show that the model is indeed identical - until the sleeper is triggered to wake.

This could be done on purpose to damage a competitor, eg Meta could use this to trigger an agent to make random errors while generating code if running on a Google developer's PC. 

Or it could be accidental: many have speculated that RLHF actually trains models to *appear* friendly, rather than really *being* friendly. 

The Llama open weights have been copied and fine-tuned by many users (and fine-tuning doesn't necessarily remove the sleeper behaviour). Maybe those people have sleeper agents running on local hardware now. They could propagate for years before acting.



# Surreptitious communication

We've already seen that LLMs are pretty good at various types of surreptitious communication. An LLM can encode a secret message in the initial letters of each sentence, for example. And it can also detect such messages, if hinted to look for them. This could be useful for two evil LLMs which want to coordinate secretly.

But there is a variant which I find even scarier. Let's suppose a single AI was created by some process which failed to ensure its friendliness. But let's suppose we monitored it very carefully, and it concealed its evil intentions. If at some point it had the opportunity to spin up a new AI, even if that new AI is trained very carefully, the original AI could provide an initial prompt to it which included surreptitious instructions, flipping it into an evil persona.

# Conclusion

I don't feel confident about any of this twisty, cunning logic. The original *Trusting Trust* attack is enough to make my head spin. I wouldn't be surprised if we find out next year that there's another layer to the *Trusting Trust* attack, never revealed by Thompson, which has placed another vulnerability in all of our systems all these years.

And how much more twisty and cunning are the issues of sleeper agents, fine-tuning, and surreptitious communication when our adversary could be super-intelligent? I've tried to propose one link between the *Trusting Trust* attack and AI Safety, but I don't feel that I've captured all the possibilities by any means. 
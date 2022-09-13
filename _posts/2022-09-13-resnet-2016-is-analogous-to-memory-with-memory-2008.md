---
title: ResNet (2016) is analogous to Memory with Memory (2008)
layout: post
tags: evolutionary_computation
---

The first time I read the paper "Memory with Memory: Soft Assignment in Genetic Programming" (McPhee and Poli, 2008), I didn't get the title. But it means that in this Linear GP system, each memory location has a memory. That is, it doesn't just remember the value you last wrote to it, but it remembers (to some extent) the previous values also. It stores something like a moving average of the updates. So, "memory with memory".

Why? The point is that these "soft updates" change the loss landscape. They make it smoother, by allowing the value in the memory location to be gradually updated, rather than trying to get it right all in one go. That makes it easier for the GP system to evolve good programs over time. In fact, all Linear GP systems allow this to some extent, with instructions like R1 = R1 + R2, but in this paper the mechanism is much stronger.

Why am I mentioning this? Because it's the same mechanism that was later employed by ResNet (Kaiming He et al., 2016). In ResNet, a neuron sums its normal inputs from the previous layer together with the outputs from some earlier neuron. The latter is the "residual connection". Another way to say the same thing is that a neuron has a value taken directly from an earlier neuron (the "memory") plus a value which comes from the same neuron, via some new processing. That is a soft update!

And again, the reason why ResNet works is that it smooths the loss landscape. In a sense, the network can experiment with the new processing, but incorporate only a small amount of it, without losing what was good in the earlier neuron. It doesn't have to get the new processing perfect, but can start to incorporate more and more of it as it learns.

Both the Memory with Memory and the ResNet mechanism can also be seen as giving the system an opportunity for gradually increasing complexity. The system can start with a simple program which is approximately correct, and add nuance by gradually adding more soft updates or gradually reducing the weight of the residual path. An explicit mechanism for complexification was proposed earlier, in NEAT (Stanley and Miikkulainen, 2001).

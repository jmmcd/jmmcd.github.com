---
title: Let's Automate Existing Inequalities
author: James McDermott
---

[ITAG Skillnet](https://www.itag.ie/) hosted a nice [AI Summit event](https://www.itag.ie/events/ai-summit/) today, including a very nice talk from [Ivana Bartoletti](https://www.linkedin.com/in/ivana-bartoletti-77b2b29/) on ethics/etc. of AI. One of Ivana's slides (not one of her main points) mentioned that one of the ways AI can be dangerous is by *automating existing inequalities*. 

Automating existing inequalities means there are inequalities in our society, which existed before AI; and now our AI systems pick up on the effects of these in the training data and perpetuate them. This definitely happens and is definitely a problem. For example, if a recruitment AI notices that most successful computer scientists have been male, maybe it will preferentially recommend males for computer science jobs.

However. People who know about process control always tell us there are benefits to getting tacit process knowledge *out* of our heads and putting it down on paper, or in code, or into a database. [Consolidate team knowledge on disk](https://guerrilla-analytics.net/). If you know there's a bug in the team's code, then your first job is to *create an issue* on the bug-tracker. Now it's explicit, and available to everyone, and it can be tracked until fixed. If you carry out some manual process on a regular basis, eg allocating weekly tasks to members of a team, your first step is to *document* that process. Now it's explicit, and it can be shared, achieving transparency and reducing the [bus factor](https://legacy.python.org/search/hypermail/python-1994q2/1040.html). If it seems possible, you might move on to improving the process, or automating it.

Moving process knowledge from inside heads and onto disks is a *prerequisite* for making improvements. Once knowledge is on-disk, improvements can *accumulate*.

Also, dark things can lurk inside heads. That brings us to the automation of existing inequalities. Pre-AI inequalities exist, often, for pretty dark reasons. Often inequalities continue not because people proudly proclaim their support for inequalities, but because biases hide inside people's heads, either known or unknown. A HR worker in computer science can favour hiring males over females, either deliberately or unconsciously. An institution, or even a society, with implicit, undocumented processes can do the same. To fix these problems, we have to keep educating individuals, and raising awareness, and reforming institutions (to try to deal with non-deliberate inequalities) and that's saying nothing about how to deal with the deliberate cases. All this has to be done over and over again, eg each time a new HR worker joins the team. I hope it won't be a shock if I reveal that this isn't working. There's no shortage of new people with the same old biases. Improvements don't accumulate.

So, it would be better to automate. Even if the process is biased, it's better to have an automated biased process than a manual biased process. In an automated process, there's no room for intervention by those who are deliberately biased. Once a process is automated, we can track it, and start measuring inequality, and testing counterfactuals, and auditing the training data. We can start applying all the new tools for understanding AI systems' decisions, which are already better than the tools we have for understanding human decisions. And if we make an improvement *it stays made*. 
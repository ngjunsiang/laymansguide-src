Title: Issue 178: Model thinking and reasoning
Date: 2026-07-27 08:00
Tags: 
Category: Season 14
Slug: issue178
Author: J S Ng
Summary: Thinking/reasoning models are those that have been trained on examples of how to think about different problems in different domains, or plan and execute complex tasks. They often use tools to aid them in goal tracking and updating. The full thinking trace from the model may be removed or hidden to present a more legible response to the user. 

[**Previously:**](https://buttondown.email/laymansguide/archive/) Multimodal models represent text, image, and audio tokens alongside each other in their embedding space. The model uses the input tokens, regardless of type, to calculate the next output token. Multimodal models typically only output text tokens in their response, delegating to more specialized models for image and audio generation if necessary.

In this issue we fill in the last piece of the puzzle needed to "unlock untold economic value", if the AI labs are to be believed. Let's talk about how models "think".

## Making thinking happen

You're in a lesson. The teacher asks a question, something innocuous really: "\<Name\>, what's the value of X?" All eyes are on you. You reply with the first answer off the top of your head. Wrongly, it turns out.

Your teacher could mock you at this point, but if they decide to get you to think harder instead, what do they say?

As it happens, this trick works on LLMs too. The ways we try to get people to think harder appear to be well-represented in books, on the internet, and in other media that the models are trained on.

What this means is: you add any of the following:
- "think step by step."
- "think carefully."
- "check your assumptions before you answer."

And it influences the model's next token. It begins to output phrases like:
- "Let's break this down."
- "First, let's identify what's being asked."
- "One way to approach this is..."
- "Before answering, let's consider..."
- "Let's work through the problem systematically."

It begins to imitate the patterns of careful thinking that it picked up during training. Surprisingly (or perhaps unsurprisingly), this improves the model's answer in many cases! It generates a much longer answer, taking more time and using more compute in the process—this is what AI folks call "spending compute for intelligence". If you don't have a large LLM, you can have a smaller LLM "think harder" and come up with a better answer.

## Where thinking breaks down: insufficient examples

When this trick was first discovered, early adopters experimented with different prompt patterns, trying to get models to generate longer responses that led to better answers. But thinking doesn't always succeed. We've all had the experience of trying to think through some difficult math problem, writing lots of working that ultimately led nowhere.

GPT-3 may have been trained on a really large dataset, but most webpages and books are not showcases of how to solve difficult problems through clear thinking.

So it's back to supervised learning again. Look for examples of how to solve difficult problems. Recruit experts and have them write down their chain of thought for different kinds of problems. Then train the model on this labelled data, so that it doesn't require users to be clever with prompts to extract this thinking. Train the model to differentiate between requests for a quick answer, and requests requiring deeper thinking.

## Thinking vs. planning

A model that is able to think longer and in a more disciplined way to produce a better answer is able to tackle harder questions. These are the models that were solving olympiad questions that humans struggled to solve.

But this isn't enough for another kind of challenge: long-horizon tasks that involve multiple tool calls, putting together information and feedback from multiple sources, maintaining task coherence and a consistent goal orientation throughout the process, and finally producing output in the correct format. For example, filing tax returns involves digging through a large number of financial documents, remaining aware of legal requirements for filing, extracting relevant information, and putting it together following those requirements. Along the way, detours and failed tool calls threaten to derail the model; it can get stuck researching an edge case rule, debugging a failing tool call, or get distracted by other things.

This requires the model to *plan*. It has to take an end-goal, break it down into phases and steps, think about immediate steps, execute them and observe the result, decide next steps, repeat, .... Along the way, it has to keep track of goals and sub-goals (usually aided by task management tools), be able to tell when they are met and check them off the list.

Again, books and websites seldom contain detailed worked examples of how to do this, so the model has to be trained with labelled data (again!), given examples of planning steps through supervised learning until it is able to reproduce them reliably.

## Hidden vs visible thinking

Frontier labs found that showing the full thinking process to users isn't always beneficial. For example, the full thinking trace—tokens that constitute the analysis and are not part of the final answer—could be really lengthy. Users tend not to like that; they want to see the key steps for a quick check, and then the final answer.

This could be because the full thinking trace includes mistakes the model made and corrected later, erroneous tool calls that it subsequently fixed, search tool calls which the user does not need to see the full contents of, etc. In other cases, frontier labs may have found ways for the model to output a more efficient form of thinking with tokens that is not human-readable.

Either way, this means one more step in the runtime: detecting and processing thinking tokens. If the model is trained to demarcate thinking tokens with a special start and end sequence, e.g. `<thinking>...</thinking>`, the runtime may look for it.

Once detected, this hidden thinking may be removed, summarized (with a different model), or collapsed to take up less space in the user interface.

**Issue summary:** Thinking/reasoning models are those that have been trained on examples of how to think about different problems in different domains, or plan and execute complex tasks. They often use tools to aid them in goal tracking and updating. The full thinking trace from the model may be removed or hidden to present a more legible response to the user.

---

This really is the primary concept behind thinking/reasoning models: more supervised training to output a sequence of tokens that lead the model to a useful answer.

If this sounds simple, that's because most of the magic is in the model training: crafting and labelling training examples, and then training the model on them, is a much more complicated process than it sounds, and I'm excluding it from this issue because it is very technical and not suited for a newsletter named Layman's Guide.

Now you know what a model is doing when you activate a feature named "Extended Thinking", or switch to a model that is described as a thinking/reasoning model.

## What I’ll be covering next

**Next issue:** [Issue 179: Agents]({filename}/season14/issue179/issue179.md)

Finally we can talk about this term, "agents", and what differentiates them from a model. If you've heard this term before and wondered what goes into one, subscribe to be notified when I lay it bare ;)

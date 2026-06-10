Title: Issue 179: Agents
Date: 2026-08-10 08:00
Tags: 
Category: Season 14
Slug: issue179
Author: J S Ng
Summary: Agents are software applications that comprise a harness, a runtime, and a model (typically accessed through an API instead of directly executed on the computer). They enable a user to type in a request or send it by other means and thus instruct the agent to carry out a task on the computer until completion. The capabilities of agents are limited by the tools available to them. 

[**Previously:**](https://buttondown.email/laymansguide/archive/) Thinking/reasoning models are those that have been trained on examples of how to think about different problems in different domains, or plan and execute complex tasks. They often use tools to aid them in goal tracking and updating. The full thinking trace from the model may be removed or hidden to present a more legible response to the user.

Let's review the ingredients we have so far:

1. A large language model ([Issue 170]({filename}/season14/issue170/issue170.md)) or multimodal model ([Issue 177]({filename}/season14/issue177/issue177.md)): a next-token predictor that takes input tokens and keeps generating output tokens which feed back to the input
2. Training data, which the model is trained on to pick up general patterns through unsupervised learning ([Issue 171]({filename}/season14/issue171/issue171.md)), and then steered to avoid harmful output and generate useful output through the use of labelled training data through supervised learning ([Issue 174]({filename}/season14/issue174/issue174.md))
3. A runtime ([Issue 175]({filename}/season14/issue175/issue175.md)), which handles multiple responsibilities:
   - parsing the model output to block it if found to be harmful
   - formatting the text for display to the user
   - separating and executing tool calls (typically in an isolated container), and injecting the results back into the input ([Issue 175]({filename}/season14/issue175/issue175.md))
   - processing thinking tokens, removing or hiding them ([Issue 178]({filename}/season14/issue178/issue178.md))
4. Other optional runtime extensions, such as those that add retrieval-augmented generation (RAG) capabilities ([Issue 176]({filename}/season14/issue176/issue176.md)), or add information that the model remembered about the signed-in user

What does an agent do?

## AI Agents

> agent(n.)
> late 15c., "one who acts," from Latin *agentem* (nominative *agens*) "effective, powerful," present participle of *agere* "to set in motion, drive forward; to do, perform; keep in movement" (from PIE root **\*ag-** "to drive, draw out or forth, move").

The term "agent" means "one who acts". So agents are software applications, comprising a trained model and a runtime. We can broadly think of the model as the "brains" of the partnership, and the runtime as the "body".

Because agents need a computer (physical or virtual) to "act", these software applications are typically installed on a computer, although they may also include a web interface to allow users to control them remotely.

The model has remained conceptually similar as I went from Issue 170 to here, but the runtime is picking up more and more responsibilities. So as not to muddy the terms, I'll keep the runtime focused on the model: processing the output, executing tool calls and injecting results, re-invoking the model if it has not reached a stop token, and any RAG if implemented. Everything else that we are adding today, that makes the agent an effective partner, I'll explain under the label **harness**.

## The model

Some harnesses make it easy to swap out the underlying model, allowing the model to run the agent harness with different models. Many model providers have standardized on OpenAI's API so as to make their models easily accessible to programmers.

While state-of-the-art models are typically capable enough to not require a more specialized version for agentic use, the agent harness usually provides a special system prompt for this purpose. This special prompt includes information on the use context, on the tools available to the model, and other pertinent information to guide the model and keep it on task.

## The runtime

A runtime used within a harness needs to include additional features: the ability to pause or stop the model, to understand access control configuration (which tool calls require user approval) and route matching tool calls to the user for permission grants, and introspectability: allowing the harness program to check the state of the runtime and model.

## The harness

When a user uses agentic software, the harness is what they see. That means the harness handles typical software responsibilities:

- it handles installation and initial setup, allowing the user to select a directory that the agent will begin working from
- it handles extensions/plugins that the user may wish to install, making the tools/MCPs ([Issue 175]({filename}/season14/issue175/issue175.md)) available to the runtime
- it handles file uploads, request customisation (e.g. enabling extended thinking), other request-related settings
- it handles the model output through the runtime, displaying to the user tool calls and their results, any visible thinking traces, and any permission requests which come from the runtime (remember that the model remains unaware of these). If the API supports it, the harness streams these to the user, allowing them to see tokens as the model outputs them, without having to wait for the model to finish the entire response
- it provides an interrupt mechanism for the user to halt the runtime if the model is going off-track, or to queue up more messages for the runtime to inject into the request at an appropriate juncture
- some harnesses may support agent memory features, giving the agent tools to write information to its internal memory, and retrieve the information when required
- harnesses for continuously running agents may include features for setting the wake-up interval of the agent, e.g. invoking the agent every 30 seconds with standard intructions to check for outstanding tasks and complete them
- harnesses that integrate with external services will include features for receiving requests via email, WhatsApp, Telegram, or other channels, passing them to the agent and returning the response when it is ready.

## What an agent does

... I don't know what to say here. By itself, a model can do nothing besides generate text. When embedded in a harness+runtime, what it can do is limited by the tools it has available—remember that the model relies on the runtime executing its tool calls to have any effect on the world.

With simple toolsets (primarily a commandline tool), the agent can plausibly:
- read, edit, and delete files on the computer
- search through files on the computer
- check the computer's stats, such as memory usage, free space on disk, CPU usage
- troubleshoot or diagnose computer issues
- perform a web search or retrieve a web page

If given the appropriate tools and permissions from the user, the agent can also:
- install or uninstall software on the computer (through the commandline)
- download source code, compile it, install it, and run it
- run a server on the computer, handle web requests, return responses
- read, write, and test code
- push code to a code repository
- add bug reports or issues to a task board, or read existing ones from it
- send requests to an API (if authenticated by the user), and thus execute any supported action through the APIs of Google Drive, Dropbox, Notion, and other services ([Issue 6]({filename}season01/issue006/issue006.md))

With more advanced tools or MCP servers that handle the complex details, an agent can even:
- be registered as a plugin in Adobe or Microsoft Office software, reading and editing documents
- work with PDF files
- fix bugs

When provided with detailed explanations of how to perform complex tasks (typically through a skill file that the agent can read), the agent can plausibly:
- analyze large datasets
- follow company workflows
- scan software or APIs for vulnerabilities

## ... Why haven't they taken over the world yet?

Because most people aren't using them!

... Just kidding, there are other reasons too. For example:

- Most complex tasks aren't described in skill files that are agent-readable, or are not well described
- Many of the advanced tools or MCP servers that are needed don't exist, e.g. those for editing PDF files reliably. If they exist they aren't always reliable
- The really effective tools might be hyper-customized for the tool author and not as useful for others
- Most users are used to doing things themselves, and don't have enough experience with an agent harness to be accustomed to instructing one
- Users might not know that it is possible to do something, and have not considered asking an agent to do it
- Agent models still have limited context windows (even a context window of 1 million tokens can fill up quickly with a sufficiently complex task), and ways to enable a model to keep relevant task details in context while removing irrelevant details are still being studied
- The model might not have been trained on a particular task, and its general reasoning capabilities might not be sufficient to carry out the task effectively
- Agent harnesses tend to run in the commandline, or be designed primarily for programmer use, thus scaring layfolks away
- ...

Agent capabilities tend to be emergent. That means researchers and frontier labs can train a model to carry out tasks A, B, and C, and a user giving the agent a different kind of task *discovers* that it is also effective at task D but not task E.

Generally, a question can "can an agent do F?" can't be answered definitively prior to actually asking the model to do F. And even if one person fails to get the agent to execute the task successfully, another person might succeed, because they asked differently, because they are familiar with the terminology required to instruct the agent, or for some other reason.

All of this is still ongoing research work: agents only really took off in 2025, when Anthropic's Claude Code became the first generally capable agent, and every day users are discovering new things that it can do. The things that it can't, Anthropic and other frontier labs are still training it to be able to do them.

**Issue summary:** Agents are software applications that comprise a harness, a runtime, and a model (typically accessed through an API instead of directly executed on the computer). They enable a user to type in a request or send it by other means and thus instruct the agent to carry out a task on the computer until completion. The capabilities of agents are limited by the tools available to them.

---

You now have a pretty good idea of all the pieces involved in getting an AI agent to do things. The part I can't authoritatively tell you about is what they can or can't do, because that is still changing every week as frontier labs continue to train more capable models and agent harnesses continue to add more tools and features.

If you're curious, consider trying them out. You could search for an online guide, or let ChatGPT/Claude help get you started.

## What I’ll be covering next

In ten issues, I've walked you through the key concepts that help you understand what AI agents do. With three issues left to go, what else should I cover?

Some questions I'm anticipating, or have fielded some variant of:

1. Can I run my own AI model?
2. Why can't the AI do \<thing\>?

Question 2 has a boring answer and an interesting one. The boring answer is "because it hasn't been trained yet". The interesting answer is ... not really suitable for a newletter titled Layman's Guide to *Computing*, because it'll be rooted in philosophy and cognitive science. In a different publication perhaps.

So let's tackle question 1, which will draw on computing concepts I've covered in earlier issues and give you an idea of the kind of compute and memory capacity needed to run a model.

**Next issue:** [Issue 180: Running a model]({filename}/season14/issue180/issue180.md)

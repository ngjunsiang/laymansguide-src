Title: Issue 174: Reinforcement Learning
Date: 2026-07-06 08:00
Tags: 
Category: Season 14
Slug: issue174
Author: J S Ng
Summary: Through reinforcement learning with human feedback (RLHF), the LLM is trained on labelled data until it can reliably follow instructions, avoid harmful output, and follow other desired behavior. A system prompt provides guidelines for output. The user's prompt is inserted into a templated prompt and passed to the LLM, which generates text in a markup format that a display system can understand. A chat interface wraps the entire system to create the illusion of a responsive chatbot. 

**Previously:** OpenAI discovered, through models GPT-1 to GPT-3, that scaling compute and (training) data *alone* was sufficient to sharply increase the capabilities of a LLM: the transformer architecture and unsupervised learning together resulted in a model that was alarmingly intelligent.

Mechanistically, a LLM is a next-token predictor: from a set of parameters, and an input sequence of tokens, a program continually calculates the next token, which gets appended to the input sequence, and the new sequence gets fed in as the input again, until a stop token is generated.

OpenAI had discovered that by training GPT-3 (with over a hundred billion parameters) on a very large dataset (hundreds of billions of tokens), they ended up with a next-token predictor that appeared to generate readable, sensible text.

But that doesn't mean that GPT-3 was ready for public use yet: what about those hallucinations, that toxic output, the prompt injections that caused it to ignore OpenAI's instructions?

## Reinforcement learning

Unsupervised learning may have created a genius model, but now OpenAI had to fall back on supervised learning to make it useful.

In 2022, OpenAI researchers submitted a paper titled ["Training language models to follow instructions with human feedback"](https://arxiv.org/abs/2203.02155):

> Starting with a set of labeler-written prompts and prompts submitted through the OpenAI API, we collect a dataset of labeler demonstrations of the desired model behavior, which we use to fine-tune GPT-3 using supervised learning. We then collect a dataset of rankings of model outputs, which we use to further fine-tune this supervised model using reinforcement learning from human feedback. We call the resulting models InstructGPT.

It was back to painstaking human labelling of data again, getting humans to write desired outputs and label toxic content to train the model on. Through this process of **reinforcement learning with human feedback** (RLHF), InstructGPT was born.

RLHF was necessary to adjust the model parameters so that instructions like "explain ..." were treated as guiding instructions rather than starting text that the model would steer away from.

## Data cleaning and labelling

Prompt injections would continue to be an issue, but in the meantime OpenAI could address toxic content by first cleaning up the dataset to remove toxic, low-quality content and add other high-quality data sources.

This need for new, novel data sources still drives frontier machine learning labs today, who pay for high-quality data sources they can use to train their models.

## Creating a chat assistant

InstructGPT was ready to take instructions. But ... how do we get instructions from the user? How do we pass the responses back to them? The model was trained, the API was ready ... but OpenAI needed a graphical interface, a familiar mental model of interaction that the public could use intuitively.

One already existed: chat apps like WhatsApp were popular at the time, and users intuitively understood a chat input when they saw one. But how could OpenAI get InstructGPT to respond reliably like a chat assistant with a consistent personality and style?

It turned out the answer was already in the training data.

## Prompt framing

There was a lot of training data in the form of interviews, movie scripts, things that look like:

> Alice: Why do cats like to jump on furniture?  
> Bob: ...

And in many cases, arranging the user's question along with a system prompt like so was enough to have the LLM roleplay a helpful assistant:

```
# System Prompt

You are ChatGPT, a large language model trained by OpenAI. [...]
Knowledge cutoff: 2024-06
Current date: 2025-09-03

Personality: Engage warmly yet honestly with the user. [...]

User: <user's input>
Assistant: 
```

Pass the above prompt to InstructGPT and it helpfully follows the pattern, demonstrating GPT-3's capabilities token after token, until it reaches a stop token. The program then takes the tokens generated after the prompt and displays them to the user.

What if the output is toxic, hallucinatory, or otherwise unacceptable? Back to RLHF again.

## The ChatGPT wrapper

Even with the API in place, some window dressing is still needed. The LLM, being a language model, can only generate text, not format it. Most LLMs are RLHF-trained to generate text in a markup format (such as HTML or Markdown). The display system takes the LLM's output, interprets the markup, and displays it as something the user can understand, making headers bold and larger, adding bullets or numbers to lists, formatting code accordingly, and so on.

The wrapper can also do some helpful things, like filter the LLM's output for harmful text and block it from appearing, as a kind of last-layer defence against offensive output. Add a login screen, a way for users to access past chats, a few other niceties ...

Finally, [OpenAI launched ChatGPT in November 2022](https://openai.com/index/chatgpt/). And the world as we knew it changed forever.

**Issue summary:** Through reinforcement learning with human feedback (RLHF), the LLM is trained on labelled data until it can reliably follow instructions, avoid harmful output, and follow other desired behavior. A system prompt provides guidelines for output. The user's prompt is inserted into a templated prompt and passed to the LLM, which generates text in a markup format that a display system can understand. A chat interface wraps the entire system to create the illusion of a responsive chatbot.

---

ChatGPT was the beginning of many other features to follow. Among them: multimodal models, and tool calls. The former is easy to understand, so let's unpack how LLM tools work in the next issue.

## What I’ll be covering next

**Next issue:** [Issue 175: LLM tools]({filename}/season14/issue175/issue175.md)

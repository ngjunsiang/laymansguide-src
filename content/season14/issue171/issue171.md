Title: Issue 171: The first Generative Pre-Training model, GPT-1
Date: 2026-06-15 08:00
Tags: 
Category: Season 14
Slug: issue171
Author: J S Ng
Summary: The Transformer architecture, unlike previous machine learning model architectures, could generate its next item while processing all previous items at the same time. The technique of unsupervised learning trained models on unlabelled data, letting the model pick up patterns in underlying data instead of having it learn correct answers only, and was much faster than supervised learning. OpenAI applied both these ideas at scale, producing GPT-1, a model that beat best-performing models while requiring relatively little human supervision during training.
Modified: 2026-06-08 16:00

[**Previously:**](https://buttondown.email/laymansguide/archive/) Models simplify and represent a relationship between input values and output values. The more complex the relationship, the more parameters the model needs to learn. Models are simplifications of reality, and their performance depends on how well they capture underlying patterns in the data, as well as the quality and quantity of the dataset.

We are going to set aside image and audio models for today, and narrow down to focus on **language models** in particular, because that's what sparked off the AI craze.

## The pre-2018 machine learning paradigm

I am not a machine learning researcher and can't tell you what the prevailing *research* paradigm at that point was. But in open-source and consumer applications, it seemed machine learning models were *bespoke*:

1. You started with something specific you needed, like image classification, optical character recognition (OCR), speech recognition, translation, ...
2. You collected a *huuuuuge* dataset of input-output pairs for that specific task: images and their labels, scanned documents and their text, audio, etc. And by huuuuuge I mean tens of thousands to millions of examples.
3. After collecting the data you often have to clean it up (remove duplicates, remove outliers, etc.) and label it (e.g. label images with their correct labels).
4. You then trained a model on part of the dataset, tweaking parameters and trying different architectures (ways of arranging parameters).
5. You tested the model on the other part of the dataset, passing each input through the model and comparing the output to the expected output, and measuring how well it performed.
6. You repeated steps 4 and 5 until you were satisfied with the model's performance, and then you deployed it for use.

This technique of using labelled data to train the model is called **supervised learning**, because of the need to tweak the model's parameters (under human supervision) to match the expected output.

There were (and still are) many machine learning models trained this way and used. For example, tesseract is an open-source OCR engine that was first released in 2005. It was trained on a dataset of scanned documents and their corresponding text, and has been used in various applications for OCR tasks. Another example is the ResNet architecture for image classification, which was introduced in 2015 and has been widely used for image recognition tasks.

## The Transformer architecture

Before Google's 2017 paper on the attention mechanism, the prevailing machine learning models had two problematic limitations:

- they "looked" at input data one item at a time to produce the output, resulting in slow output generation
- because of the above, data that was processed earlier seldom made it through to the end of the model, resulting in a recency bias: the model tended to focus on the most recent input data and ignore earlier input data

The attention mechanism introduced in Google's 2017 paper allowed models to "look" at all input data at once, speeding up output generation. The same mechanism also computed which parts of the input data were most relevant for producing the output.

Attention was not a new mechanism in machine learning: prior models had used them, but in separate stages, and alongside other mechanisms. Google's paper was the first to ask: "what if we *only used attention everywhere*?" The resulting architecture, which they called the "Transformer", was a breakthrough in speed and simplicity.

## Unsupervised learning

Besides the Transformer architecture, another breakthrough was already making its rounds: instead of task-specific datasets, researchers wondered why they needed so many task-specific datasets. Since the data represented different subsets of reality (from different tasks), what if they just trained a single model on a really, really large dataset of text to produce a **base model**? Then they could fine-tune it on smaller task-specific datasets to produce task-specific models.

This technique, called **unsupervised learning**, did not require data to be labelled—the model "learns" patterns in the underlying data without human correction, simply trying to predict the next word in the training data given the previous words.

## Generative Pre-trained Transformer (GPT)

A few researchers at OpenAI then had the idea to try this pre-training approach on the Transformer architecture. OpenAI built the first **Generative Pre-trained Transformer** (GPT) model, which they released in 2018. **Generative** means the model generates output based on input, producing one output item at a time (but processing all inputs simultaneously). **Pre-trained** means the model was largely trained through unsupervised learning. **Transformer** refers to the underlying architecture.

They went *big* on scale: GPT-1 trained on a dataset of 7,000 self-published books comprising 985 million words, representing this data using 117 million parameters—an unheard-of scale at the time (but now considered paltry). It attracted attention from the research community not only by improving on best-performing models on various language tasks, but by improving on *all of them*, with *minimal task-specific training*.

Due to the unprecedented number of parameters used, GPT-1 was considered a **large language model** (LLM), to distinguish it from smaller models that came before. However, this was a research idea, with code that was far from release-ready, and nobody except research-minded folks knew how to get GPT-1 running. And thus, this went unnoticed by the public.

Still, this was a breakthrough: no research lab before OpenAI had the kind of resources that enabled them to try this idea. It did require resources that most labs didn't have at the time: 8 GPUs, when most labs ran their training on a single GPU.

**Issue summary:** The Transformer architecture, unlike previous machine learning model architectures, could generate its next item while processing all previous items at the same time. The technique of unsupervised learning trained models on unlabelled data, letting the model pick up patterns in underlying data instead of having it learn correct answers only, and was much faster than supervised learning. OpenAI applied both these ideas at scale, producing GPT-1, a model that beat best-performing models while requiring relatively little human supervision during training.

---

We're almost at the meaty part! I kinda snuck in 2 ideas today: the Transformer architecture (a minor part of this series actually) and unsupervised learning. I don't think you would have wanted to wait a week in between before hearing how OpenAI combined the two, haha ... so there you go.

## What I’ll be covering next

**Next issue:** [Issue 172: Tokens, the currency of LLMs]({filename}/season14/issue172/issue172.md)

Wait—what exactly does a large language model (LLM) work with? Individual letters? Entire words? Find out next issue!

Title: Issue 181: Quantization
Date: 2026-08-10 08:00
Tags: 
Category: Season 14
Slug: issue181
Author: J S Ng
Summary: Quantization trades parameter precision for a smaller memory footprint and faster inference, making many models feasible for running on user devices. Model capabilities depend on their parameter count and training data. Models with higher parameter counts can represent more patterns, while model capabilities are added by training them on well-labeled data.
Modified: 

[**Previously:**](https://buttondown.email/laymansguide/archive/) Proprietary models do not have their weights published publicly, while open-weight models do. Various runtimes are available for download, and can run models that have a compatible file format. But models are extremely compute- and memory-intensive, requiring extremely high-end hardware and capacious memory to run.

Great, so a 12B model takes up 24GB of disk space, uses 24GB of RAM, and another 96GB for the KV cache (model's calculated representation of input tokens). That's out of reach for most consumers without AI-grade GPUs, which currently cost thousands per unit.

Enter quantization.

## Parameter representation

Models are typically trained with full precision, allowing them to store each parameter using 16 bits (2 bytes). This is necessary because the training process results in multiple adjustments to the weights. If the intermediate values are not stored with full precision, subsequent adjustments to those values are not accurately represented, and may result in inaccurate training results.

However, once the model is trained and its weights released, they are effectively "frozen": the weights do not change as the model is used for inference (Issue 173).

## Quantizing parameters

Can we reduce the model size and memory footprint by reducing the precision? Yes. Experiments have shown that models lose some accuracy as their parameters are quantized: represented using 8 bits (twofold reduction), or even 4 bits (fourfold reduction!). Below that range, running the model at 2 bits often results in unacceptable performance.

This inaccuracy shows up in models not following instructions as well, potentially making mistakes more noticeably, especially on complex tasks, or being less accurate with tool call syntax. However, compared to the alternative of not running the model at all, this is usually an acceptable tradeoff for users running the model on their own computers.

## Running a quantized `gemma-4-12B-it`

Okay, let's run those numbers on a quantized Gemma 4 12B model. We don't even need to do the quantization ourselves usually: other enthusiasts have already done it, [providing the models on HuggingFace as well](https://huggingface.co/Brunobkr/OFFELLIA_Q4_0_gemma-4-12B-it.gguf) (they can be identified through the `Q4` in the model naming scheme; 8-bit quantized models are labelled `Q8`).

We already see immediate benefits: the 4-bit quantized model weights are only 7GB, a stark contrast to the 24GB of full-precision weights.

The KV cache requirement now drops to ~6GB for 32K tokens, and ~50GB for 256K tokens. *Very* uncomfortable for a Macbook, which means we would have to limit ourselves to a 128K or even 64K token context length. Annoying, but not show-stopping.

The inference speed now increases to ~60 tokens/sec, about as responsive as ChatGPT or other chatbots!

## What do we gain from larger models?

Unlike programs or data files, which store data as-is (perhaps compressing them for a smaller filesize), models **represent** information: the training process produces a highly compressed set of numbers that are able to approximately reproduce the training contents (not 100% accurately, but quite close), and more importantly generate tokens following the same pattern for inputs that it was not trained on.

What if we try to break the laws of physics, taking GPT or Claude's training corpus, and training it into a 1B model? What happens?

1B parameters means the model only has 1 billion numbers to try to represent everything. If the training data is repetitive and largely similar, 1B might even be sufficient since there just isn't that much variation in the data.

But if the data is highly varied, the model might not be able to adjust the weights to represent everything. It will end up storing one additional data point at the expense of worse representation for other data points. This might show up as a plateau in benchmark scores: the model can't improve further. Or it might show up as the model not "remembering" data that shows up less frequently.

What do frontier models, often with parameter counts running into trillions, gain? With so many parameters, they can represent more patterns: more thinking scaffolds and reasoning frameworks, more sentence/paragraph patterns from more books and articles, etc. And not just more patterns, but higher-order patterns: writing styles, writing intents, idea development, longform writing structure, etc.

Google's Gemma 4 12B model will end up not being able to represent everything. Our running model might give less nuanced answers, consider fewer perspectives in its answer, and otherwise give worse answers.

But hey, it runs! Give it a spin, see what you can do with 12B parameters.

## Model capabilities

Even frontier models with poor training data will disappoint. 1 trillion parameters won't necessarily make a model much smarter if the training data is poor.

Most new capabilities are added through additional training, usually supervised learning. If we can't train the underlying model, we might be able to create skill files explaining how to do something, let the harness read it and add it into the input context, and lean on the model's pattern-following capabilities to tackle the task.

Either way, if you have the hardware to support it and manage to get a local agent running, try it with different questions and tasks to get a feel for what it can and cannot handle. That beats any amount of reading on what these models are supposed to be able to do.

**Issue summary:** Quantization trades parameter precision for a smaller memory footprint and faster inference, making many models feasible for running on user devices. Model capabilities depend on their parameter count and training data. Models with higher parameter counts can represent more patterns, while model capabilities are added by training them on well-labeled data.

---

12 issues in, that's a wrap! At this point I think what I've written is what's unlikely to change in the next couple of years, and still useful for layfolks to know about the ongoing AI development. Anything newer is still in active development.

## What I’ll be covering next

**Next issue:** [LMG S14] Issue 182: Running a model, part 2

In the last issue, I'll explore other options for running a model on your device (called **local deployment** in parlance): running smaller models, and other feasible hardware options

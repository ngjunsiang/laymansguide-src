Title: Issue 170: Machine learning models
Date: 2026-06-08 11:30
Tags: 
Category: Season 14
Slug: issue170
Author: J S Ng
Summary: Models simplify and represent a relationship between input values and output values. The more complex the relationship, the more parameters the model needs to learn. Models are simplifications of reality, and their performance depends on how well they capture underlying patterns in the data, as well as the quality and quantity of the dataset.
Modified: 2026-06-08 11:30

**Previously:** By better understanding how search bots categorise pages, a website owner can use keywords and other techniques to optimise the ranking of their page for specific search terms.

**[Editor's Note]** Layman's Guide to Computing went on hiatus after its 13th season, because my promise when I began was to write only things widespread enough that I thought layfolks should have an accessible-yet-useful introduction to.

As I wrapped up Season 13 in 2022, the trend at that time was cloud computing. I tackled emulation and virtualization in Season 12, then the internet and online services in Season 13. ChatGPT launched in November 2022 that year. In 2024, I was first asked if I would continue Layman's Guide again to write about AI. I said no; less than half my colleagues were using ChatGPT or had heard of it, and I didn't think there would be enough common knowledge for me to usefully write about AI yet.

But now, in 2026, even my employers are actively promoting genAI, my students are using ChatGPT, and by the end of this year it would likely be difficult to find someone who hasn't heard of Claude Code or Gemini Pro or Codex. I suppose it's time to add one more season.

There are many explainers out there; I've read a large number of them, many very good! But this is Layman's Guide to Computing, and something I noticed talking to laypeople is confusion: where did this AI come from? Why hadn't it been invented earlier? How does it work? What can it do? What can't it do?

So let's rewind time: I started writing Layman's Guide to Computing in 2018. A year before that, eight machine learning engineers at Google had published "_Attention is All You Need_," the paper that introduced the transformer architecture that underpins most of today's genAI. In mid-2018, before I started writing, OpenAI was still a non-profit research lab founded by Elon Musk and Sam Altman, and had just released the first version of GPT, a language model that was not yet large enough to generate coherent text. Following Google's whitepaper on the attention mechanism, they had just released a paper, "_Improving Language Understanding by Generative Pre-Training_", that described the architecture and training process for GPT, their first large language model.

It's a little hard to mentally reconstruct the tech culture and public awareness of the field of artificial intelligence and machine learning at that point in time. So let's start by understanding: what is a model? How were they used then?

## Models

You may not know it, but you were already using models in your daily life in 2017. When the iPhone launched, it had intelligent autocorrect and touch auto-adjustment features. For these features to work, Apple had to train machine learning models on large datasets of text and touch interactions. These models were then deployed on the iPhone to provide the autocorrect and touch adjustment functionality.

What are these models? You would likely have used them in a stats course, perhaps even in high school. If you were ever asked to sketch a best-fit line, a trendline, or a linear regression, you were already drawing a model. To do that, you:

1. Hypothesized a linear relationship between an input variable `x` and an output variable `y`.
2. Collected data points (`x`, `y`) through an experiment.
3. Represented the relationship between `x` and `y` using a mathematical formula (`y = mx + b`).
4. Determined the parameters `m` and `b` that best fit the data points.

You *compressed* the data—multiple sets of points (which we call a **dataset**)—into two **parameters**, `m` and `b`, a simpler representation that captures the underlying relationship. This representation is a **model**. (We sometimes call it a mental model when we don't have it formally represented as a mathematical relationship, just a conceptual description.)

Apple's machine learning models do something similar. An autocorrect model takes a dataset of incorrect words/phrases and their actual words/phrases, and compresses it into a text correction model. A touch auto-adjustment model takes a dataset of touch interactions and their intended targets, and compresses it into a model that can predict the intended touch target based on the touch input.

**tl;dr** A model takes in input values and produces output values based on patterns it has learned from training data.

## More complex models

Of course, more complex models do not use a linear equation or a simple mathematical formula anymore. Machine learning researchers first represent more complex relationships using more complex formulas, such as polynomials or decision trees, which use more parameters.

But for other purposes the input may not be a single variable and the output may not be a single variable either. For example, in image recognition, the input is an image (which can be represented as a grid of pixel values), and the output is a label (e.g., "cat", "dog", "car"). An image classifier may have 64 input values (one for each pixel in an 8×8 image) and 10 output values (one for each possible label). The model would learn to map the input pixel values to the correct label based on patterns in the training data. That's 640 parameters (64 input values x 10 output values) that the model would learn to adjust during training.

This direct mapping of input to output can only take us so far. Perhaps output 1 doesn't just depend on inputs 1 to 10, but on some intermediate value calculated from them. Now we have to add intermediate **layers** between input and output, which researchers call "hidden layers". These layers allow the model to learn and represent more complex relationships between input and output. Each layer can have its own parameters, and the model learns to adjust these parameters during training to improve its performance.

**tl;dr** More complex models use more parameters to represent the relationship between input values, intermediate values, and output values. Each parameter represents a relationship between two values. The more parameters, the more complex the relationships the model can learn.

## Limitations of models

Models sound like mathematical dark magic, and often feel like it too. But like the mathematical models we learned in school, they have limitations.

If you've seen how far some of your data points deviate from your best-fit line or trendline, you already know that the model cannot accurately represent all the data points—it is only a simplification. Likewise, all machine learning models are simplifications of reality.

Their performance depends on how well they capture underlying patterns in the data: pick an inappropriate representation for the feature, e.g. a linear formula instead of a polynomial, and the model will perform poorly.

It is also possible to go to the other extreme, adding a complex model with many parameters that fits the training data perfectly, but does not predict other data points well—an overfitted model. You can have a computer come up with a sine-decay formula that fits your first 6 data points perfectly, but wildly overshoot a 7th data point.

Also, their performance depends on the quality and quantity of the dataset. If your data does not represent the underlying reality well enough, missing important patterns or exceptions, or not covering a sufficient variety of cases, the model can pick out the wrong features and learn the wrong patterns. In the early days of machine learning, some researchers found that when training image classifiers on images of dogs and cats, the model began identifying any brown creature sitting on grass as a dog, because the training dataset had many images of dogs sitting on grass, but few images of cats sitting on grass. The model had learned to associate grass with dogs, which was not the intended pattern.

**Issue summary:** Models simplify and represent a relationship between input values and output values. The more complex the relationship, the more parameters the model needs to learn. Models are simplifications of reality, and their performance depends on how well they capture underlying patterns in the data, as well as the quality and quantity of the dataset.

---

After experiencing the magic of ChatGPT and other genAI tools, it's easy to forget, or perhaps not even realise, that fundamentally they are powered by the same underlying principles that we apply in simpler experiments.

But between `y = mx + b` and ChatGPT, there is still ... such a huge gulf of complexity. We still have quite a way to go.

## What I’ll be covering next

**Next issue:** [Issue 171: The first Generative Pre-Training model, GPT-1]({filename}/season14/issue171/issue171.md)

What was the fundamental insight that made GPT and other LLMs possible? Find out next season ;)

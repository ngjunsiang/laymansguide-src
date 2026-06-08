Title: Issue 173: Training, Inference, and Scaling
Date: 2026-06-29 08:00
Tags: 
Category: Season 14
Slug: issue173
Author: J S Ng
Summary: OpenAI discovered, through models GPT-1 to GPT-3, that scaling compute and (training) data *alone* was sufficient to sharply increase the capabilities of a LLM: the transformer architecture and unsupervised learning together resulted in a model that was alarmingly intelligent.
Modified: 

[**Previously:**](https://buttondown.email/laymansguide/archive/) A model does not see letters or words, only tokens. These tokens are typically generated from user input through a pre-tokenizer program. Tokens are represented in the model as embeddings, a sequence of numbers representing the token's position in the embedding matrix. The model uses each token's embedding, and its surrounding tokens, to infer its meaning in context.

## Model Training

In issue 171, I explained a little about how model training happens:
1. we pass tokens generated from text to the input
2. we pass the expected output (in supervised training), or the subsequent tokens (in unsupervised training)
3. the model generates output from input
4. we compare the model's output to the expected output
5. we adjust model parameters
6. we repeat from step 3, attempting to adjust parameters to have the model generate output that is closer to the expected output

Notice that there's a "forward" step: step 3, where the input "feeds forward" to each hidden layer. Here, the computer calculates the values for the next layer based on the values of the previous layer and on the model's parameters between the two layers. This is repeated for each layer until we get to the output.

Notice also that there's a "backward" step: step 5, where we could adjust model parameters randomly—inefficient! Instead, the mathematical technique of gradient descent gives us a more optimized way to adjust the last hidden layer based on how it would affect the output. The second-to-last hidden layer is then adjusted with the same technique, based on how it would affect the last hidden layer. And this is repeated all the way to the first hidden layer. This "backward trickling" is called **backpropagation**, or "backprop" more informally.

The above steps are repeated *for each input:output data pair* (supervised training) or *for each token sequence run* (unsupervised training). That's **a lot** of repeated steps; researchers often have some shortcuts they take to speed up the process. Even then, it is still too many for a typical CPU to complete in a reasonable time; the big labs use specialized GPUs instead (Issue 123), resulting in training runs that take weeks to months to complete on multiple GPUs for today's state-of-the-art LLMs.

This is not a cheap hobby.

## Inference

Fortunately, using a model is a different affair, involving only steps 1 and 3 of the above. No backpropagation, no repeated runs, just pass the input in, run one forward step per output token, repeat until done. This process is called **inference**, and is what happens when we users send a request to ChatGPT or Claude.

(Hang on, how does a model "know" when it is "done generating text"? In model training, a special token, e.g. `<EOS>` for end-of-sequence, is inserted at the end of text. When this token is detected in the program, it stops invoking the model.)

Needless to say, inference is much cheaper than training, which is why we are able to enjoy many of these models for free.

## Scaling up to GPT-2

GPT-1 had 117 million parameters, was trained on ~7,000 books (about 5GB), took a few days to complete training on 8 GPUs, costing $0.5 mil or less.

In 2019, OpenAI released GPT-2, which was the first large language model to capture public attention. GPT-2 had 1.5 billion parameters (1.5B), was trained on ~40GB of text from the web, and took a few weeks to train on hundreds of GPUs, costing OpenAI $1 mil to $5 mil to train.

GPT-2 was the same architecture that GPT-1 used, only with a larger model (tenfold) and with more training data (eightfold). What they got was a model that:
- could perform tasks it was never explicitly trained on (zero-shot learning): answer questions, understand text, summarize, translate (rudimentarily)
- could generalize from examples given in user input (one-shot/few-shot learning) without needing supervised learning
- showed emerging ability on non-language tasks: counting, basic arithmetic, even some attempts at simple proofs

These are capabilities we take for granted today, but in early 2019 this was cutting-edge performance never demonstrated by any other machine learning model, and certainly not with so little human supervision. This discovery was scary enough that it took OpenAI nine months to fully release GPT-2's weights, fearing how its capabilities might be misused.

## The bitter lesson, and GPT-3

These findings prompted Rich Sutton, an influential machine learning researcher to write [a blog post published on 13 March 2019](http://www.incompleteideas.net/IncIdeas/BitterLesson.html), where he summed up this finding in a single sentence: "The bitter lesson is that general methods that leverage computation are ultimately the most effective, and by a large margin. [...] Seeking an improvement that makes a difference in the shorter term, researchers seek to leverage their human knowledge of the domain, but the only thing that matters in the long run is the leveraging of computation."

A tenfold increase in model parameters and training data led to a surprising leap in capability. OpenAI and other researchers wondered: What if we pushed this to its logical conclusion, and threw more compute and more data into machine learning training?

In 2020, OpenAI released GPT-3. GPT-3 had 175 billion parameters (175B, a hundredfold increase in model size), was trained on a mix of books and websites totalling 300 billion tokens, took weeks to train on hundreds of GPUs, and cost OpenAI up to $12 mil to train.

GPT-3 could:
- take instructions given in natural language
- *reliably* tackle many tasks zero-shot (with no examples)
- *reliably* adapt examples given in the user input, and generalize from patterns

It had reached a level of capability that took the focus away from *training data* and placed it on the user input, called the **prompt**: without further training, the model could give you a response, the quality of which depended on the quality of your prompt.

## Alarming behavior

LLMs had finally reached a point where they were easy enough to use by the general public. But before it could actually launch for public use, there were some concerns to be addressed.

For one, GPT-3 was extremely prone to hallucinations—making up things that never happened, papers that were never written, academic journals that never existed. It also readily reproduced toxic outputs from its data source—the internet (especially reddit and 4chan). It was extremely steerable through the prompt—a little too steerable for OpenAI's liking, when some users got GPT-3 to leak its system prompt—the instructions that OpenAI prepended to every request guiding GPT-3's response style and guardrails.

It would be some time before ChatGPT could even launch without dragging OpenAI down with it.

**Issue summary:** OpenAI discovered, through models GPT-1 to GPT-3, that scaling compute and (training) data *alone* was sufficient to sharply increase the capabilities of a LLM: the transformer architecture and unsupervised learning together resulted in a model that was alarmingly intelligent.

---

We are getting closer to the LLMs we know and love/hate today. 
This issue covered the miracle story of GPTs 1 to 3. If GPT-3 was a child genius, ChatGPT is GPT-3 dressed up for work. Let's talk about what OpenAI had to do to it for public release—next issue.

## What I’ll be covering next

**Next issue:** [LMG S14] Issue 174: Reinforcement Learning

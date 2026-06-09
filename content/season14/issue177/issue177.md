Title: Issue 177: Multimodal models
Date: 2026-07-27 08:00
Tags: 
Category: Season 14
Slug: issue177
Author: J S Ng
Summary: Multimodal models represent text, image, and audio tokens alongside each other in their embedding space. The model uses the input tokens, regardless of type, to calculate the next output token. Multimodal models typically only output text tokens in their response, delegating to more specialized models for image and audio generation if necessary.
Modified: 

[**Previously:**](https://buttondown.email/laymansguide/archive/) In retrieval-augmented generation (RAG), the runtime performs a search with the user's request to retrieve relevant chunks from a set of documents from a knowledge base. The chunks may be further re-ranked by the runtime before finally being included in the LLM's input. One alternative to RAG, where information lookup happens outside of LLM generation, is to provide the LLM with search tools instead, and rely on its judgement to use them well.

Multimodal models. Try saying that three times quickly. It's quite a mouthful, but if you've managed to keep up so far, it's really not complicated, so I don't expect this to be a long issue.

## Multimodal models

While a large language model works only with text tokens, a **multimodal model** can work with other types of tokens as well. We've previously covered what text tokens are and how LLMs use them (Issue 172), so let's focus on image and audio tokens.

The approach is similar, really: text gets broken up into common repeating patterns. Image and audio likewise gets broken up into common repeating patterns. Each common repeating pattern is represented by a number, or set of numbers, and located in an embedding space (Issue 172).

## Image tokens

There are a variety of approaches for tokenizing images. A common way to do this is to break it up into 16×16-pixel patches. Each pixel has three values representing red+green+blue (Issues 43 & 44), so each patch is a sequence of 16×16×3 = 768 values.

Each unique combination of 768 values constitutes an image token. During training, these image tokens appear alongside other tokens (text, image, audio), and the model adjusts its embedding parameters to locate semantically similar tokens in close proximity.

During inference (Issue 173), hidden layers represent more abstract patterns that the model identifies: lower layers may encode information about edges, while higher layers capture information about shapes, textures, and even objects.

## Audio tokens

While intuitively it seems natural to chunk audio into 1-second or even sub-second samples, in reality 1 second of audio contains 44,100 samples (Issue 45) which is still far too large.

Instead, audio is usually converted from waveform representation (amplitude vs time) into spectrum representation (frequency vs amplitude at a snapshot in time). The spectrogram gets split into shorter windows of a few milliseconds each (a few thousand samples per window). The values of each frequency in that window then naturally form an audio token, which appear alongside other tokens in training and get represented in embedding space the same way as other tokens.

## Multimodal models need supervised training

Supervised learning plays a big part here. Images, audio, and text seldom appear together in unlabelled training data (except in video), so associating images and audio with text relies heavily on manual labelling. This is why multimodal models took so long to emerge.

During inference, all tokens regardless of type are represented as embeddings, and the model uses the input tokens to calculate the output token.

## Multimodal models vs image/audio generation models

An app like ChatGPT can take user-uploaded image files, reference them in their response to the user, and then generate an image, or even convert the response from text to audio. But this seamlessness is an illusion; at the backend, these do not use the same model.

Multimodal models can take input tokens of multiple types, but typically only generate text in response; users do not expect image patches or audio snippets in the response, and would not know how to interpret them.

Instead, image and audio generation use different kinds of (non-Transformer) models, which might be worth exploring briefly in a future issue, but not this one.

**Issue summary:** Multimodal models represent text, image, and audio tokens alongside each other in their embedding space. The model uses the input tokens, regardless of type, to calculate the next output token. Multimodal models typically only output text tokens in their response, delegating to more specialized models for image and audio generation if necessary.

---

There you go. Multimodal models demystified: once you figure out how to tokenize something alongside text, and give the model lots of labelled data to associate it with text tokens during training, you can create another modality for your model. This sentence hides months of complexity that AI labs tackle, because that's what you're reading Layman's Guide for, isn't it?

## What I’ll be covering next

**Next issue:** [LMG S14] Issue 178: Model thinking and reasoning

We've covered retrieval-augmented generation (RAG), and now we've covered multimodal models. Text, images, audio: Check check checked. Tools? You bet.

We've got almost all the ingredients to assemble an AI to scare the economic labor pool, but we are still lacking one final piece of the puzzle: how do LLMs "think"?

Title: Issue 182: Running a model, part 2
Date: 2026-08-31 08:00
Tags: 
Category: Season 14
Slug: issue182
Author: J S Ng
Summary: Open-weight models range in size from sub-1B to 100+B. A range of device options below SGD6,000 are already capable of running these models, ranging from the humble Raspberry Pi for running harness support to the Mac Studio M3 for running 70B models. 

[**Previously:**](https://buttondown.email/laymansguide/archive/) Quantization trades parameter precision for a smaller memory footprint and faster inference, making many models feasible for running on user devices. Model capabilities depend on their parameter count and training data. Models with higher parameter counts can represent more patterns, while model capabilities are added by training them on well-labeled data.

Last issue, we discovered that there are quantized models that can actually run on laptops. (You can also run GPT-1 and GPT-2 on a laptop, but you would likely be disappointed in their performance today given the leaps-and-bounds improvement in AI capability that have happened since 2022.)

Besides `gemma-4-12b`, what else can we run?

## Open-weight model options

Open-weight enthusiasts have a number of well-known options available to them (sizes are unquantized):

- Google's Gemma 3 series, available in sizes 1B to 27B
- Google's Gemma 4 series, available in sizes 5B to 31B
- Microsoft's Phi series, available in sizes 2.7B to 14B
- Meta's Llama series, available in sizes 8B to 405B
- Alibaba's Qwen series, available in sizes 0.5B to 72B
- Deepseek's titular Deepseek series, available in sizes 16B to 72B
- Mistral's Mistral series, available in sizes 7B to 176B

There are also many lesser-known models, whose capabilities are still increasing every few months.

I won't give you a comprehensive low-down on what each model is good for, because:
- the models can be fine-tuned by those who know how, and may have variants that are better at specific task categories,
- the models are updated every few months, and see new capabilities added through post-training (supervised learning),
- the agent harness and runtime do play a part: some models are useful "out-of-the-box", some work best within a particular harness or with a particular set of tools

## Model capabilities

In [Issue 181]({filename}/season14/issue181/issue181.md) I mentioned that **more parameters** lets the model represent more patterns in its weights, while **better training data** determines the model's capabilities. Useful to know as a general pattern, but difficult to apply when deciding on a specific model to run. Should we just run the largest model that our device is capable of running?

As of June 2026,
- **0.5B–3B** models can handle classification, extraction, summarization tasks and are generally good for single request-response purposes.
- **7B–9B** models are useful assistants (in a harness) that can hold short conversations, handle basic Q&A, do simple coding or tool calls, and otherwise generally match GPT-3's capabilities.
- **12B–15B** models can follow instructions consistently, generate code that mostly works (and do some debugging if necessary), generate tool calls more reliably, making them capable tool-using agents.
- **27B–35B** models can handle most tasks, even across longer contexts: analyze documents and write reports, generate and debug code, execute requests involving multiple steps. With a well-designed harness and accurate task documentation, these become capable general-purpose agents.
- **70B** models can handle what previous tiers can do, but better: fewer hallucinations and mistakes, better answers, better general understanding, more consistent planning, and over longer context windows—smaller models sometimes see a sharp performance drop when the context window extends past a certain length.
- **100B+ Frontier models**—GPT-5, Claude Opus, Kimi K2.5, et al—can do all of the above, with state-of-the-art reasoning and thinking, knowledge, error recovery, ambiguity handling, and more

Specialized non-LLM models include:
- **OpenAI Whisper (0.4B–1.5B)** for speech-to-text transcription, text-to-speech generation
- **Stable Diffusion (0.9B–8B)** for text-to-image generation
- **FLUX.1 (12B)** also for text-to-image generation
- **CLIP (0.4B)** for image-to-text understanding
- **Stable Audio 3 (0.6B–2B)** for text-to-audio generation

Models are still improving through post-training (supervised learning) and distillation—training small models on output from larger, more capable models. A 9B model today already exhibits capabilities that GPT-3 (175B) was capable of in 2022. So you should expect a different set of capability tiers this time next year.

## Hardware options

The sweet spot for "value-for-money" sits around **12B–35B** for now. Smaller models are faster and use less memory. Speed decreases and memory use increases as model size increases.

With this in mind, these are some popular options for running models on-device (local deployment) as of June 2026 (prices are Singapore retail):
- **Raspberry Pi** (8–16GB RAM): popular for tiny models (2B or smaller), used to generate document embeddings for search, OCR documents and clean up the OCRed text, etc. These form the support system for the agent harness, and usually are not used directly for the agent models.
- **Mini-PCs** with a sufficiently capable CPU, no dedicated GPU are a decent budget option
  - **AMD Ryzen AI 300-class CPUs, 12 CPU cores, 8–12 GPU compute units & 64GB RAM**: this can run 7B–13B models capably (if slowly), and 34B quantized models at a crawl. [~SGD2,000]
  - **AMD Ryzen AI MAX+ (Strix Halo) CPUs, 16 CPU cores, 40–48 GPU compute units & 256GB RAM**: this bundles a much more capable integrated GPU ([Issue 123]({filename}season10/issue123/issue123.md)) and can run 34B models capably, 70B models at a crawl. [~SGD4,800]
  - **Mac Mini M4, 12 CPU cores, 10 GPU compute units & 24GB RAM**: despite initial appearances, the Mac Mini is a much more capable little beast than the Ryzen AI 300-class series above, thanks to its unified memory architecture that has much better memory bandwidth (800GB/sec) compared to the Ryzen's DDR4 (256GB/sec). Expect double the Ryzen's performance, although the memory capacity means it runs quantized 34B models at a crawl. [SGD1,299]
  - **Mac Mini M4 Pro, 14 CPU cores, 20 GPU compute units & 48GB RAM**: The same deal as the M4, but with more GPU compute units and more memory, this can run 34B models quite capably. [SGD2,659]
  - **Mac Studio M3 Ultra, 28 CPU cores, 60 GPU compute units & 96GB RAM**: This can run everything mentioned above, and run 70B models decently well. That's what most folks would be buying this for. A higher-end 32 CPU core, 80 GPU compute unit configuration exists if you add SGD2,025—doesn't add new capabilities, makes everything a little faster. [SGD5,199]
- **Full PCs** with a capable CPU & dedicated GPU
  - Many options exist here, none below SGD6,000, most above SGD10,000. Dedicated GPUs capable of running AI models already have prices in the thousands.

If you already have an existing laptop/PC and want to know how it will manage different model sizes, you can ask ChatGPT or Claude; they are pretty up-to-date with hardware capabilities and can give you an estimate. Alternatively, try to download and run the models and see for yourself—ground truth doesn't care about your estimates.

## Cloud options

Wow that's a lot of zeros. Besides, owning hardware comes with its own maintenance needs and headaches. Enter the cloud, i.e. pay-per-use.

If you don't want to have to manage the hardware that runs these models, don't plan to be running a model long-term, or want to run a model larger than what your hardware can handle, these are the current most user-friendly options:

- [HuggingFace](https://huggingface.co/models?inference_provider=hf-inference) not only catalogues model weights, it also automates inference hosting (provided by AWS or Google Cloud underneath). Caveat: not all models are supported; you need a model that lists "HF Inference API" as an Inference Provider. The HuggingFace link in this bullet point links you to models that do. On the model card page, click **Deploy > HF Inference Endpoints**
- [Replicate](https://replicate.com/explore) provides an even simpler interface, but for a smaller catalogue of models. Try the models out directly on the model card, or create an account for deployment options.
- [Fireworks AI](https://fireworks.ai/models) is where you go once you've decided on a (supported) model and want reliable hosting. Browse their model list and click **Try In Playground** or **Deploy On Demand** (requires registration).

There are other options that require more technical expertise to use, but if you reach that point you shouldn't be relying on a layman's guide anymore :\)

**Issue summary:** Open-weight models range in size from sub-1B to 100+B. A range of device options below SGD6,000 are already capable of running these models, ranging from the humble Raspberry Pi for running harness support to the Mac Studio M3 for running 70B models. For larger models, or short-term workloads, cloud options for deploying and running open-weight models also exist.

---

This is the most tentative issue for this season, and probably for the entire newsletter so far. I try not to write issues that I will have to retroactively edit as the frontier shifts, but I'll make this an exception: I think expounding on available open-weight models illustrates how the ecosystem is similar to open-source software, that allows the (sufficiently educated) public to experiment and provide feedback, how advances in AI over the past 3–4 years have made them feasible to run on consumer-class devices, and how cloud infrastructure has made larger models accessible to those who don't own sufficiently powerful hardware.

## The Layman's Guide to Computing archive

Buttondown still does not have a very browseable archive, so I've made the newsletter content available on a static site. You can browse past seasons more easily at https://ngjunsiang.github.io/laymansguide/categories.

I may add more seasons in future, as computing technology stabilizes enough for me to write about them in a static newsletter. If you'd like to receive future issues, do subscribe below:



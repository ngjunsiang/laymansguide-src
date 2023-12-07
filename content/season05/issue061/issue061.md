Title: Issue 61: Mapping the cache
Date: 2020-02-22 08:00
Tags: 
Category: Season 5
Slug: issue061
Author: J S Ng
Summary: 
Modified: 2020-02-22 08:00

**Previously:** Speculative execution is a feature that lets the CPU speed up execution if it correctly predicts a decision point. The CPU carries out the operations along the predicted decision branch and loads the results if it predicts correctly.

Meltdown and Spectre need 2 pieces of the puzzle to leak data, and we have covered the first piece already: How to load the forbidden information into the cache, where it will not be immediately wiped by the OS when we are “found out”.

If we were trying to pull off a Meltdown or Spectre, we would try to:

1. Set up the request to have the info loaded into the cache
2. Attempt to read the cache ... how?

The second piece of the puzzle, naturally, is how to get the info out of the cache before the CPU eventually evicts old data from it.

## Failure from the start

At this point, we would have failed. We have gotten the secret into the cache, but we have no idea where it is in the cache, and we have no way to access the cache directly—remember that the cache is managed by the CPU and there is no instruction we can issue to the CPU to give us cache data directly.

We’ve come so far … and it doesn’t even matter.

We’ll need to modify our approach slightly. We can’t store the leaked data directly in the cache naïvely like that. We’ve got to be a little cleverer.

## The cache “mirrors” a part of virtual memory

A quick refresher on how the cache works ([Issue 57]({filename}/season05/issue057/issue057.md))):

1. When the CPU needs data from a memory address, it looks in the cache first.
2. If the data is not there (a **cache miss**), it will load the data from the memory address, and store a copy in the cache for faster reference in future. [**SLOW**]
3. If there is a cache hit, the data from the cache will be returned. [**FAST**]

Hmm … there’s something here. A cache miss is slow, and a cache hit is fast. Could we exploit this in some way, possibly? If we are creative, yes!

Many secret ways of transmitting information involves a shared cipher, a secret way of converting what is sent to what is meant. Leaking cache information will require a cipher of some sort.

It’s like a WWII spy story. Two spies arrange 3 different dropoff locations. Dropoff location 1 means their country is going to attack. Dropoff location 2 means their country is not going to attack. And dropoff location 3 means the information is compromised and they should avoid contact. Even if they are caught by the secret police, there is no way of figuring out what the two spies had communicated to each other indirectly.

All right, I’m writing a newsletter here, not a workshop. And the rest of the story will need more technical detail, so let’s call it a week. Next issue, all will be revealed ;)

**Issue summary:** A cache miss is slow, and a cache hit is fast. This difference in cache reading speed can be used to transmit secrets out from the cache, which cannot be read directly by programs.

I know, I know, what a cliffhanger! Before you started reading this newsletter, you never thought you’d be waiting with bated breath to hear some technical explanation of how to read data from a CPU cache, huh? Or that you never thought you might (in the next issue) find newfound appreciation of an ingenious CPU vulnerability exploit, and just how difficult it would be to fully resolve it.

We are getting close to the big reveal. Same time next week.

## What I’ll be covering next

**Next issue:** [LMG S5] Issue 62: Snooping the cache

I was about to write both the mapping and the snooping in one issue, then I momentarily lost my train of thought and was trying to trace it again. And I realised that if I could lose the train of logic like that, I probably should split it up into two issues. One idea per issue, and I will still try to stick to it. I haven’t been able to write short issues that communicate a single idea, and it feels good to achieve it again.

**Sometime in the future:** What is:

- booting up? [Issue 15]
- a cookie? [Issue 8]
- XSS? [Issue 8]
- a CDN? [Issue 8]
- a good reason developers write code and give it away for free online? [Issue 21]
- firmware? [Issue 34]
- OpenType? And what are fonts anyway? [Issue 42]
- What is involved in installing a piece of software? [Issue 48]
- How do apps know where a file starts and ends? [Issue 49]

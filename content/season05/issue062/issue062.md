Title: Issue 62: Cache snooping
Date: 2020-03-03 17:00
Tags: 
Category: Season 5
Slug: issue062
Author: J S Ng
Summary: 
Modified: 

[**Previously:**](https://buttondown.email/laymansguide/archive/) A cache miss is slow, and a cache hit is fast. This difference in cache reading speed can be used to transmit secrets out from the cache, which cannot be read directly by programs.

Okay, okay, we managed to leak data from memory to the cache, now how do we leak it from the cache to our program?

## Cache snooping: tapping on tiles

Here in Singapore, before moving in to a newly built apartment, we have a “ritual” of tapping each ceramic floor tile to check if they have been properly fastened to the ground.

Most people don’t actually know what a fastened or unfastened floor tile sounds like. What we do know is that they sound *different*.

So we go *tok*, *tok*, *tok*, *tok*, *tok*, … *tik*! Aha, there’s a loosened floor tile!

That’s kind of what we are going to do to the cache. We are going to load information located in memory cells addressed 1 through 256, and see how long each request takes.

Address 1: 135 ns  
Address 2: 134 ns  
Address 3: 136 ns  
Address 4: 134 ns  
…  
Address 136: 130 ns  
Address 137: 66 ns  
Address 138: 137 ns  
…  
Address 256: 135 ns

Can you tell what the secret number is? It’s the one with an *obviously lower* request latency. In this case, the other addresses didn’t have a copy of their data already in the cache, so they result in a cache miss ([Issue 57]({filename}/season5/issue057/issue057.md)))—the CPU has to go to main memory to read the data again, and that’s slow. Address 137 already had its data loaded before, and a copy of it was already in the cache, so loading it again results in a cache hit and is fast.

## Treating memory addresses as data

One key thing to remember here is that each memory address points to a memory “cell”, which only stores one byte (8 bits), with a value that can run from 0 to 255 to give us 256 (i.e. 2^8) different values.

Meltdown or Spectre have gotten the secret number (137), but in that small window of opportunity before it gets terminated, it would not have time to even store it into a text file that we can open later. How could we get that secret number without Meltdown or Spectre storing it?

We can write a snooping program to do the following:

1) Empty the cache cells for memory addresses 1 to 256, so that loading information from them would result in a cache miss.

Then instead of storing the value 137 somewhere, we would get Meltdown/Spectre to **load** information from memory address 137. A load operation is much faster than a store operation, and Meltdown/Spectre would be able to pull this off within the window of opportunity. This would cause a copy of the information in memory address 137 to be stored in the cache; the next time any program tries to load information from address 137 again, it will be a cache hit (fast).

The snooping program would then:

2) Make requests for information from each of these 256 memory addresses (“tapping on tiles”) and see which request has an *obviously lower* latency.

3) Determine that memory address 137 has obviously lower request latency, and store the “transmitted” secret: “137”

It’s a lot of work to get a single byte (256 possible values), but computers are good at doing lots of tedious work in a short amount of time. Using sample working code that exploits out-of-order execution ([Issue 58]({filename}/season5/issue058/issue058.md))) and speculative processing ([Issue 60]({filename}/season5/issue060/issue060.md))), coupled with a snooping program like the one we described above, the Meltdown and Spectre authors are able to leak data at a rate of about 580 KB/s, which seems slow. But there are 86,400 seconds in a day, so that’s roughly 43 GB/day at full exploit speed! (There are 4 videos of demonstration exploits near the bottom of the [Meltdown page](https://meltdownattack.com/).) Malicious actors would probably do it at a slower rate to keep it covert, but in the weeks or months it would take to notice something was amiss with the memory access operations, that’s a lot of data they can siphon off … .

We’ve covered quite a bit of technical ground, so I’ll summarise.

**Issue summary:**
To prep the cache, our program empties addresses 1 to 256, so that they are guaranteed to have a cache miss if their information is loaded.

To cache snoop (after Meltdown/Spectre have “delivered the payload”), we load information from memory addresses 1 to 256 and look for the one with an obviously lower request latency (a cache hit). The memory address itself is the value to keep.

Okay, that’s it. Secret is leaked, cat is out of the bag, and now you know how Meltdown and Spectre work, without all the technical detail (like how addresses 1 to 256 need to be in separate pages which are 4 KiB each because the CPU will speculatively load adjacent data from memory, *yaddah yaddah*).

So what can we do about it? Why hasn’t Intel fixed it after a year? I’m no computer engineer, but I’ll offer some thoughts in the next issue.

## What I’ll be covering next

**Next issue:** [LMG S5] Issue 63: Limitations of Meltdown and Spectre

This isn’t even a fraction of 1% of what happens inside a CPU. It’s hard to convey just how complex CPU design is; no single person can explain in full detail how every part of the CPU works. Much of the design and validation work is already being done by software, but it still takes a human to write the code that does the checking.

Does it surprise you that a little hack like this can get past so many pairs of eyes? It really shouldn’t.

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

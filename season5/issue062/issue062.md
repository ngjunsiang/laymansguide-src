**Previously:** A cache miss is slow, and a cache hit is fast. This difference in cache reading speed can be used to transmit secrets out from the cache, which cannot be read directly by programs.

Okay, okay, we managed to leak data from memory to the cache, now how do we leak it from the cache to our program?

## Exploiting memory addresses

One key thing to remember here is that each memory address points to a memory “cell”, which only stores one byte (8 bits), with a value that can run from 0 to 255 to give us 256 (i.e. 2^8) different values.

If we can only request virtual memory addresses ... then we just need to map each possible value of the memory cell to a virtual memory address.

What we can do, then, is to decide beforehand on 256 different memory addresses to use for transmitting secrets. For convenience, I will just refer to them as address 1, address 2, … there is really no reason to use numbers 1 to 256, since we have 16 billion different addresses that we can use. But they should be addresses that our program can legally use without raising an exception.

Then we need to prep the cache. We first request address 1 to 256 once each. Their contents are now cached (in the CPU cache), and if we request the same data again, they will load quickly. In fact, they will load with very consistent latency.

Now, we flush the cache. Attempting to load any address from 1 to 256 now results in a slow load.

And then we perform a Meltdown or Spectre attack to obtain a leaked secret (one byte). Suppose this byte value is 137. Then during the small window of opportunity, instead of storing the value 137 to memory, I **request a load of address 137 instead**. This is a cache miss, and it is slow, but still quick enough to happen before the program gets caught.

To the OS, nothing is amiss; a malicious program attempted to access a memory address it wasn't supposed to, an exception was raised, it was caught, and previous data flushed. But our cache has still changed!

How are we going to get that data out from the cache though?

## Cache snooping: tapping on tiles

Here in Singapore, before moving in to a newly built apartment, we have a “ritual” of tapping each ceramic floor tile to check if they have been properly fastened to the ground.

Most people don’t actually know what a fastened or unfastened floor tile sounds like. What we do know is that they sound *different*.

So we go *tok*, *tok*, *tok*, *tok*, *tok*, … *tik*! Aha, there’s a loosened floor tile!

That’s kind of what we are going to do to the cache. We are going to request a load for address 1 through 256, and see how long each request takes.

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

Can you tell what the secret number is? Its the one with an *obviously lower* request latency. The other addresses had been flushed, so they result in a cache miss—the CPU has to go to main memory to read the data again, and that’s slow. Address 137 was already requested by the malicious program, so loading it again results in a cache hit and is fast.

It’s a lot of work to get a single byte, but computers are good at doing lots of tedious work in a short amount of time. the Meltdown and Spectre authors have working code that is able to leak data at a rate of about 580 KB/s, which seems slow, but there are 86,400 seconds in a day. So that’s roughly 43 GB/day at full exploit speed! Malicious actors would probably do it at a slower rate to keep it covert, but in the weeks or months it would take to notice something was amiss with the memory access operations, that’s a lot of data they can siphon off …

We’ve covered quite a bit of technical ground, so I’ll summarise.

**Issue summary:**
To prep the cache, we load addresses 1 to 256 (but we don’t actually care what data is there.)

To cache snoop, we:

1. Flush the cache for all 256 addresses
2. Load the secret value into its corresponding address using Meltdown or Spectre attacks (the secret is only one byte, and cannot be greater than 256)
3. Request each address and look for the one with a lower request latency

Okay, that’s it. Secret is leaked, cat is out of the bag, and you now know how Meltdown and Spectre work, without all the technical detail (like how addresses 1 to 256 need to be in separate pages which are 4KB each because the CPU will speculatively load adjacent data from memory, yaddah yaddah).

So what can we do about it? Why hasn’t Intel fixed it after a year? I’m no computer engineer, but I’ll offer some thoughts in the next issue

## What I’ll be covering next

**Next issue:** [LMG S5] Issue 63: Fixing Meltdown and Spectre

This isn’t even a fraction of 1% of what happens inside a CPU. It’s hard to convey just how complex CPU design is; it has gotten beyond the point that a single person can explain in full detail how every part of the CPU works. Much of the design and validation work is already being done by software, but it still takes a human to write the code that does the checking.

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

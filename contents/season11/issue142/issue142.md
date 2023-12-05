Title: Issue 142: Implications (Part 1) - Software
Date: 2021-10-16 08:00
Tags: 
Category: Season 11
Slug: lmg-s11-issue-142-implications-part-1-software
Author: J S Ng
Summary: 

[**Previously:**](https://buttondown.email/laymansguide/archive/) The Apple A14 and Apple M1 are essentially the same chip architecture: they use almost the same building blocks, just with different numbers of them. On top of that, the Apple M1 implements unified memory, allowing the CPU and GPU (and other SoC components) to share the same system memory, greatly facilitating intra-chip communication.

So, before 2020: smartphones are smartphones, laptops are laptops. They use different types of CPUs with different architectures ([Issue 141]({filename}/season11/issue141/issue141.md)) and even different instruction sets ([Issue 53]({filename}/season5/issue053/issue053.md)). Never the twain shall meet.

After 2020: It turns out that smartphone chips can be upgraded and used in laptops, while remaining essentially the same architecture? Its power consumption dial can be turned down to almost zero but also turned all the way up?

That opens up the possibility that smartphones and laptops can run on the same hardware, and there’s nothing technically stopping apps compiled ([Issue 54]({filename}/season5/issue054/issue054.md)) for that instruction set to run on both![^1]

[^1]: Nothing, that is, besides all the software workarounds that will need to be written ...

Hmm, where has something like this happened before?

## The big console alignment

Sometime in mid-2013, Microsoft announced the Xbox One (henceforth XB1), the successor to the Xbox 360. The 360 ran on a PowerPC CPU made by IBM—different from smartphone chips that used the ARM instruction set, and also different from laptops that use the x86 instruction set.[^2]

[^2]: In an interesting narrative twist, PowerPC was the architecture that Macbooks used before Apple switched them to Intel processors. And now Xbox did the same thing.

The Xbox One, on the other hand, uses a CPU+GPU made by AMD[^3], following the x86 instruction set.

[^3]: AMD calls it an Accelerated Processing Unit (APU). Doesn’t matter for us.

The Xbox One essentially uses a custom laptop chip!

This *was* interesting news because earlier that year, in Feb 2013, Sony had announced the PlayStation 4 (PS4), which was ... also running on an AMD CPU+GPU! The previous iteration, the PlayStation 3 (PS3), was running on an interesting custom architecture that used PowerPC cores and a completely original GPU.

At this point it would be oh-so-tempting, for a tech nerd, to descend into point-by-point comparisons of the hardware specifications of both consoles. We will fortunately not be doing that.

What’s more important is what this meant for the video games.

## Alignment in game development

If you wanted to write a game for the Xbox 360, you had to learn its API: which functions to call to make it do what you want, how to store data into its storage, and so on. It’s a lot of time and effort to look at your options and figure out the limitations, and how to work around them to achieve what you want in your game.

And if you wanted to make the same game for the PS3, you now had to learn a completely different API, running on hardware with completely different limitations, and figuring out completely different approaches to achieve the same end. While the game might feel the same, the time and effort is almost as much as what it would take for a new game!

The XB1 and PS4, on the other hand, are much more similar. They both use AMD CPU+GPUs with similar architecture. While Microsoft and Sony may add their own features on top of the chips and the software, the API is ultimately guided by hardware decisions. If you made a game for XB1 and wanted to port it to PS4, the effort of learning a new API is greatly lessened.

## The gulf between smartphones and laptops

Back to smartphones vs laptops. Running on two different types of chips, using different architectures and instruction sets.

We have seen some forays from one into the other: Intel’s doomed Medfield chip was an attempt to bring the x86 architecture to smartphones, while Google has been trying to get ARM chips into Chromebooks, with limited but increasing success.

But now that we have an iPhone 12 using the A14 chip, a Macbook using the M1 chip, and we know that the A14 and M1 are essentially the same architecture and the same instruction set … it does suggest that the challenges of making software for both devices now primarily exist on the software side. The gulf of hardware incompatibility has been closed.

## Feature alignment

The M1 chip is capable of power standby (i.e. screen off with the CPU in a low-power state), in a way that most laptop chips aren’t. This is a key feature for smartphone software and operating systems, and the M1 paves the way for laptop chip-makers to introduce this feature into their processors as well.

And the M1, being living proof that unified memory is possible, would also likely push existing companies to speed up development towards that goal.

**Issue summary:** Using the same hardware for both smartphones and laptops would make it much easier to write apps for both platforms. The closer they are in features, hardware, and software support, the easier things will be for developers.

I was looking for a way to sneak in the XB1-and-PS4 story, and I think I found just the right place for it. It really does excite me to think that one day a developer could write software for a smartphone, and it would work on laptops with minimal modification, and vice-versa. And perhaps a decade from now, we’d be scratching our heads why we even had to choose between the two!

## What I’ll be covering next

**Next issue:** [LMG S10] Issue 143: Implications (Part 2) – Future Goals

So what’s next? Is unified memory the holy grail for hardware, and is there any further room for improvement? I’ll share some thoughts in the next issue.

**Sometime in the future:** What is:

- XSS? [Issue 8]
- a good reason developers write code and give it away for free online? [Issue 21]
- OpenType? And what are fonts anyway? [Issue 42]

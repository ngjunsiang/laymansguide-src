**Previously:** Computers compress image and audio data through a process similar to summarising: it analyses the data using algorithms that use brightness and colour instead of RGB values for images, and different frequencies of sound rather than samples at different points in time for audio. These algorithms then discard parts of the information that human senses do not perceive easily, and reduce the resolution of other parts that human senses are not as sensitive to.

I went into quite a bit of technical detail in the last issue, and am loathe to do so again this issue. Let’s see how much math I can avoid explaining this issue.

Lossless compression is necessary in cases where the information must be stored verbatim. For example, if you are sending a 26MB Powerpoint file to a friend, but GMail’s attachment limit is only 25MB, one thing you might try to do is put it into a compressed ZIP file to see if you can bring the size below 25MB. However, you would not want any information to be lost when it reaches your friend; they must be able to decode the ZIP file to  retrieve the original Powerpoint file.

While lossy compression depends very much on how our senses (particularly sight and hearing) work and on their deficiencies, lossless compression only depends on the characteristics of the information. Accordingly, a wide variety of lossless compression techniques have been developed, each suited for a particular domain. I will attempt to give a very brief overview of some common techniques before I explain some common things people try to do in compression.

## Lossless audio compression

Your brain works in interesting ways. If it sees two images that are near-identical (like a game of Spot The Difference), it won’t remember it as two separate images, but as one image, and the difference between the two images. So when people try to recall the two images you hear things like “this photo had a cat and a dog staring each other down and it also had [blahblah], the other photo is exactly the same except the cat’s ears were furled back and the dog was drolling”. Certainly a lot faster than describing the second image exactly the same way, with the additional detail!

Lossless audio compressors work in a similar way. They sample the audio in short segments, and try to see how lazy they can get in describing the next sample. This is known as **predictive coding**, because is a little similar to the process of trying to “predict” the next sample. For example, based on the past 10 samples, a predictive algorithm might say “the next sample will have 0.09% of sample 1, 1.02% of sample 2, 5.63% of sample 3, …”. Storing those percentages will use a lot less space than storing the entire sample; when decompressing, the algorithm can then multiply the percentages with the respective samples to reconstruct the original sample.

In lossless compression, the predictive algorithm already knows what the next sample is, so most of the work is in calculating exactly what those percentages are. It does so by making an initial guess, then refining that guess in successive stages of calculation, each stage bringing it closer to the original waveform. This requires a lot of computation time. If such a setting is available, the algorithm can shorten the process, leading to a poorer guess. It then calculates the difference between the best guess and the original sample, and stores the difference between the two. This part is what makes it lossless rather than lossy.

# Lossless image compression

The most common image formats that use compression are GIF (yes, really) and PNG. Some kinds of images, such as screenshots, have patterns that are repeated. The algorithm used in GIF and PNG, LZ77, attempts to spot these patterns, and reduce them to 1) the repeating portion, and 2) the number of repetitions. This is known as **run-length encoding**. The nature of images makes the process easier, as each pixel only has 256 possible values rather than 65536.

Those patterns are stored in a table, and *references* to them are used instead. So instead of saying “Pattern 0101011101110110”, the algorithm will store a list of these patterns, and refer to them as Pattern 0, Pattern 1, Pattern 10, Pattern 11, … (these are 1, 2, 3, and 4 respectively, in binary format ()[Issue 40](https://buttondown.email/laymansguide/archive/lmg-s4-issue-40-bits-and-bytes/)).

This is known as **entropy coding**. By linking the longest pattern with the smallest reference number (i.e. Pattern 0), the next-longest pattern with the next-smallest reference number (Pattern 1, 10, 11, 100, 101, 110, …) you can reduce quite significantly the number of bits needed to represent the image.

# Text compression

Text lends itself very well to compression, since there are so many repeated words and phrases. In general, text compression algorithms will use a combination of entropy coding and run-length encoding to reduce a document of text into repeating patterns, and using shorter references to those patterns rather than the full pattern itself.

# What is the maximum possible compression?

Excellent question. Shannon’s source coding theorem[^1] defines a compression limit for each block of information, called Shannon entropy (unbolded, don’t worry!). The source coding theorem says it is impossible to compress data beyond its Shannon entropy.

[^1]: Yes, that’s the same Shannon from Nyquist-Shannon sampling theorem. Claude Shannon is lauded as “the father of information theory” with good reason.

So what is the Shannon entropy of the data? That depends on its predictability. A block of text that only consists of the letter ‘e’ would be highly predictable, and therefore a low Shannon entropy (I will stop using this term and use **predictability** instead). A block of text that is just completely random characters would be unpredictable and would therefore have a high Shannon entropy.

*tl;dr* higher predictability  = higher (lossless) compression, lower predictability = lower (lossless) compression



And now it is myth-busting time! Well, not really, since most observant folks would have noticed this by now.

# When I put a zip file in another zip file, why is the second zip file no smaller in size that the first?

When the first zip file compressed its contents, the predictability of the resulting data decreased (ever tried compressing shorthand?). You won’t get very far trying to compress unpredictable data.

If you want greater compression, use a higher compression setting on the original file instead.

<span style="text-align:center">
![7zip archive settings, showing options for compression level, compression method, and dictionary size](https://github.com/ngjunsiang/laymansguide/blob/master/season4/issue047/issue047_01.png?raw=true)<br />
7zip archive settings for zip files.<br />
Image from [Wikimedia Commons](https://en.wikipedia.org/wiki/File:Colorcomp.jpg).
</span>

A higher *compression level* generally causes the algorithm to try more combinations and iterations of compression, a larger *dictionary size* enables the algorithm to use more pattern references. Play with these two settings to find the best tradeoff between compression time and compression ratio (the ratio of final filesize to original filesize).

# Why do Powerpoint files sometimes compress very well and sometimes not at all?

Powerpoint is already a compressed file format, so the only filesize gains you will get are from compressing embedded media, such as videos or images. If you used any uncompressed images, you might be able to achieve some filesize gains. But it is better to have Powerpoint handle the compression instead; it offers a [Compress Pictures](https://highspark.co/how-to-compress-powerpoint/) option.

# You talk about your highfalutin Shannon entropy, but I can find so many tiny video and image files online! How do they achieve that?

Shannon’s source coding theorem does not claim that you cannot compress data beyond its Shannon entropy. It only claims that you cannot do so losslessly. Which means you can compress data beyond its Shannon entropy, *lossily*.

You are getting video and image files from those sources with lots of information thrown away. If you can’t tell the difference, good for you.

**Issue summary:** Data cannot be compressed beyond its predictability limit (Shannon entropy) in a lossless fashion. Lossless compression does not discard any information. It generally tries to spot patterns in the data, and represent those patterns with fewer bits, through a combination of predictive coding, run-length encoding, and entropy coding.

**Predictive coding:** express samples as a combination of past samples  
**Run-length encoding:** spot repetitions of patterns in the data  
**Entropy coding:** Store the list of patterns, using a shorter symbol as reference to the pattern

<hr/>

If the lossy compression articles are hard to read, the lossless compression articles are even worse, because so much of it is math theory. I got the gist of it as best as I can.

I don’t like the way most layman explanations in the media completely skip over the details; before I understood lossless compression, these explanations were often no help to me. I think at least knowing what kind of patterns can be found in the data would help with imagining the process, hence the crash-course introductions to predictive coding, run-length encoding, and entropy coding.

## What I’ll be covering next

**Next issue:** Of containers and codecs

Why have we been talking so much about images and audio and compression? Because I want to get to the meat, which is: video formats! This is probably the single biggest source of confusion for most people who come to look for me regarding file types: “What kind of video file is this? How do I open it? Why can’t it open?” Next issue: a simple way to understand video formats and what they need.

**Sometime in the future:** What is:

- booting up? [Issue 15]
- a cookie? [Issue 8]
- XSS? [Issue 8]
- a CDN? [Issue 8]
- a good reason developers write code and give it away for free online? [Issue 21]
- compiling code into an application [Issue 26]?
- firmware? [Issue 34]
- HTML? [Issue 38]
- OpenType? And what are fonts anyway? [Issue 42]

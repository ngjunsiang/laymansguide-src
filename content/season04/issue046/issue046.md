Title: Issue 46: Lossy compression
Date: 2019-11-09 08:00
Tags: compression
Category: Season 04
Slug: issue046
Author: J S Ng
Summary: 
Modified: 2019-11-09 08:00

**Previously:** Humans can distinguish 120 dB of loudness, which means the loudest perceivable sound is a million times louder than the softest perceivable sound. CD audio provides 16 bits of information per sample, sufficient to provide 96 dB. Humans have a hearing range from 20 Hz to 20 kHz. CD audio is sampled at 44.1 kHz. Uncompressed audio thus requires 705,600 bits per second, or 86 kB/s.

Lots of numbers in the last issue, and you don’t need to memorise any of them, but those numbers were necessary to demonstrate some fundamental facts about data and information: We need a heck lot of data to produce images and audio that doesn’t sound distorted! And this is closely related to the limits of our eyes and ears.

## Why are the images and audio files on the internet so much smaller?

Because they are compressed, that’s why.

We all have that one friend (or maybe more) who can just drone on and on about their day, or about something that happened, giving a detailed account with every little thing that happened, and all the things that it reminds them of, and finally in their entire speech there’s that piece of information you are looking for!

Or maybe you’ve been in an hour-long meeting and your colleague missed it and asked you what they missed. Would it take you an hour to recount the key points? Probably not. You’d give a summary, highlighting only the key bits that would make a difference.

Computers do something similar using **compression algorithms** that analyse the data and figure out which parts can be safely discarded without affecting the gist of what’s being transferred. Because information is being discarded, this is known as **lossy compression**—you can never get back *all of* the original information once it has been lossily compressed.

If you’re thinking “this part is going to be incredibly math-ey”, you are right, but I have only an hour for this issue so I’ll see how I can further summarise the theory for you readers :)

## Lossy image compression: luma and chroma

In [Issue 44]({filename}/season04/issue044/issue044.md)), I mentioned that the human eye has 3 types of cones that sense red, green, and blue light. What I didn’t mention then is that partly due to the way these cones are distributed, the human eye is more sensitive to differences in brightness (or “**luma**”) than differences in colour (“**chroma**”).

A black-and-white image has only luma information (brightness), while a colour image has both luma and chroma information—you can mathematically separate the data of a colour image into the brightness component (which looks just like a black-and-white photo), and a colour component, which looks like nothing you have ever seen. The closest thing to chroma information would be analog colour photo negatives, if you were born early enough to get to see those.

So that’s another way of representing image information: you can either represent it as RGB (red-green-blue) colour values, or YUV (1 luma value, Y, and 2 chroma values, U & V). In RGB, all 3 colour components are equally important and you can’t treat them differently, but in YUV you _can_ process them differently to achieve lossy compression.

## Lossy image compression: chroma

Since the human eye is less sensitive to chroma (colour) information, in the JPEG image format, the chroma components are compressed by averaging each 2×2 group of pixels into 1 value for U and V each. (This process is known as subsampling.) Theoretically that halves the amount of data required for the same image! (4/4 Y + 1/4 U + 1/4 V = 6/12 of the original information)

![4 images with different chroma subsampling]({attach}/season04/issue046/issue046_01.jpg)  
*Compare the image without chroma compression (4:4:4) to the image with chroma compression (4:2:0).<br />Without scrutiny, the human eye is not very sensitive to lower resolution in chroma.<br />Image from [Wikimedia Commons](https://en.wikipedia.org/wiki/File:Colorcomp.jpg)*    

## Lossy image compression: luma

Furthermore, even within the luma channel (i.e. looking at luma information only), the human eye is more sensitive to sharp changes in brightness across adjacent pixels than gradual changes in brightness across adjacent pixels. Through a Discrete Cosine Transform (DCT) algorithm, a computer can separate the luma information and differentiate parts with sharper changes, and parts with gradual changes.

As the compression level increases (this is the quality setting you often play with in Photoshop and other image-editing software), the computer increasingly discards more and more information, starting from the gradual-change information. For photograph images, you will generally hit diminishing returns below 85%: each 1% decrease in quality brings you less and less savings on filesize.

And that, in a nutshell, is how most lossy image compression works, and how the JPEG format works (well, okay, I’ve explained the main 30% of it maybe).

## Lossy audio compression: discarding what we can’t hear

What about audio?

If you are all about the bass, or like tweaking with sound settings, or have worked with audio systems before e.g. for a performance or for your school’s events, you would have used an equaliser at some point. An equaliser is a device (or software application) that lets you adjust how much bass (low pitch), medium (middle pitch), and treble (high pitch) you want from the sound. How is the system able to do that?

Through transforms! DCT, mentioned earlier, is one such transform; audio formats often use another one, known as the Fast Fourier Transform (FFT). (Aren’t you glad this is a newsletter about computing and not about math?) Anyway, a transform lets us transform information organised by position (e.g. in images) or by time (e.g. in audio) into information organised by other properties, such as frequency.

The FFT algorithm organises audio information (for a certain time length) by frequency. Depending on your equaliser settings, it increases or decreases the weightage of different frequencies to produce the sound you want, be it bass-heavy rock or medium-light jazz.

But the FFT algorithm can do much more! It is known that most sounds we hear are typically in the 40 Hz to 19 kHz range, so it is usually a safe bet to discard frequency information below 40 Hz and above 19 kHz. If we lower the frequency ceiling for discarding, down to 16 kHz, we can reduce the amount of audio information even more.

## Lossy audio compression: masking

It is also known that the human ear, when it hears a very loud sound around one frequency, will not process much softer sounds in other frequencies. This is known as masking. With the help of the FFT algorithm, it’s easy to identify which frequencies will be masked for each range of time samples, and therefore can be discarded.

Furthermore, because of the way the cochlea works, right after hearing a very loud sound, the ear will not be able to hear softer sounds for a fraction of a second (maybe the fluid in the cochlea of the ear needs some time to settle? I don’t know). So softer sounds occurring right after a loud sound are **masked**. We can discard that audio information too.

Lastly, long periods of silence (a couple seconds for example) are not worth all that information they take up as well, and can be further compressed.

## Lossy audio compression: lowering dynamic range

We don’t always need to record audio with the full dynamic range of human hearing. For an orchestra concert, maybe that is important, but if you are just recording an interview, you don’t need to hear every tiny detail of how that person speaks (unless maybe you’re a doctor who can pick up telltale signs of cancer from the way a person speaks? That would be amazing.).

Human voice frequency typically ranges from 85 to 255 Hz, and only covers a range of up to 65 dB. That’s a full 30 dB lower than the 96 dB of CD audio, which means we don’t need 16-bit audio to store that; about 11 or 12 bits would be sufficient. And you won’t need a 44.1 kHz sampling rate for that; 11.025 kHz is sufficient.

That, in a nutshell, is how we get such small images and audio files on the internet. If you’re particularly sensitive you can often make out the difference caused by this lost information. But most of the time, we’re not listening or looking closely, and it’s easy to overlook such minor differences.

**Issue summary:** Computers compress image and audio data through a process similar to summarising: it analyses the data using algorithms that use brightness and colour instead of RGB values for images, and different frequencies of sound rather than samples at different points in time for audio. These algorithms then discard parts of the information that human senses do not perceive easily, and reduce the resolution of other parts that human senses are not as sensitive to.

-----

It took me a long while to understand the lossy compression algorithms well enough to explain them simply, and even longer to summarise them still further without using terms like RLE, high- and low-frequency components, and subsampling. If you found the previous two issues overly technical, I hope this issue makes up for that by helping you understand compression in less time than detailed technical articles elsewhere, yet in more depth than your mainstream internet sources.

## What I’ll be covering next

**Next issue:** Lossless compression: like repacking but for data

If you’ve bought anything online before, you know how much of the space is taken up by packing peanuts or styrofoam or recycled cardboard or crumpled brown paper or those airbag things. You might also know about how some third-party shipping services help you cut down on shipping costs by repacking your items together before shipping so as to reduce the volumetric weight that you have to pay for. In all cases, you’re still getting the same thing, just in a smaller package that is smaller in size.

Computers can also do something similar: give you the exact same information but in a smaller filesize. This is lossless compression, in contrast with what you learnt this issue on lossy compression (which keeps the gist of things but does not give the exact same information). How do computers do this? And when will you want to use lossless vs lossy compression?

I didn’t manage to get into what happens when you save, edit, and re-save a JPEG image repeatedly in this issue, so I’ll see how I can work it into the next issue :)

**Sometime in the future:** What is:

- booting up? [Issue 15]
- a cookie? [Issue 8]
- XSS? [Issue 8]
- a CDN? [Issue 8]
- a good reason developers write code and give it away for free online? [Issue 21]
- compiling code into an application [Issue 26]?
- firmware? [Issue 34]
- What is HTML? [Issue 38]
- What is OpenType? And what are fonts anyway? [Issue 42]
- ~~What is compression? [Issue 43]~~
- ~~Why are music files so large when a voice call over internet uses so little data? [Issue 45]~~

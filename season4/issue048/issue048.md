**Previously:** Data cannot be compressed beyond its predictability limit in a lossless fashion. Lossless compression does not discard any information. It spots patterns in the data and represent them with fewer bits, through a combination of predictive coding, run-length encoding, and entropy coding.

In past issues this season, I went into some detail about how images and sound are represented as data in computers. I also went into a little detail about lossy compression, in which imperceptible information is discarded, and lossless compression, in which the original information can be reconstructed.

That progression finally brings me to this issue, where I introduce the first complex data representation: the video file.

A video file, as we like to think about it, actually is not a simple form of data. It can have one or more of the following:

- video data
- audio data
- subtitles
- annotations (e.g. on Youtube videos)
- chapters (which let you jump to certain points in the video, like a bookmark)
- miscellaneous files (e.g. embedded copyright information)

These various types of information, if they are time-sensitive (video, audio, and subtitles), have to be presented in synchrony. It’s not like you can just throw them into a simple zip file or folder and the computer knows what to do with them! How does a computer know how to put them together into an engaging movie?

# The video container

What we usually understand as a video file is actually a **video container** format. The common ones we encounter online today are MP4 (.mp4) and Quicktime (.mov). In a more recent past, you would have commonly encountered AVI (.avi), 3GPP (.3gp), and Flash Video (.flv). And if you’re a video techie who dives into DVDs and Bluray discs, you would also see Video Objects (.vob) and MPEG Transport Streams (.ts).

The audio, image, and text data in the video container are referred to as **streams**. At the binary level, it’s all 1s and 0s; how does the computer know which part of the file contains audio, image, or text data? This information is in the video container metadata, along with more details on how to load the correct part of the video, audio, or text at the right time.

If you have come across poorly formed video where the image and audio data is not in sync, or the subtitles come too early/late, you know how critical it is to get this right: the human eye and ear can be pretty sensitive to even slight discrepancies in timing.

# From still image to video

I’ve talked about pixels are perceived in still image data, now I’ll introduce one more aspect of psychovisuals: how the human eye perceives *motion*.

The eye interacts with the brain in strange ways. Over millions of years of evolution, the brain has evolved [a ‘high-power’ and a ‘low-power’ way](https://www.eurekalert.org/pub_releases/2006-07/uops-prc072606.php) to receive information from the eye. Under everyday conditions, the brain is able to connect separate frames of image data into a coherent picture and interpretation without being confused by the differences between each frame.

Decades of experimentation have set the gold standard for motion pictures at 60 frames per second (fps) for a seamless experience. That’s a lot of images per second, and a lot of corresponding video data!

For everyday purposes, such as online streaming, it is more common to encounter 30fps, or even 25fps for older videos. In certain types of video entertainment, such as hand-drawn animation, the human eye can make do with 15fps and still piece together an enjoyable performance!

# Data streams

How about the data streams? How are they stored?

To start with the obvious, they obviously are not stored uncompressed; we saw that a single image of 1920×1080 pixels (that’s 1080p video standard, with 1080 pixels vertically) already requires 6MB ([Issue 43](https://buttondown.email/laymansguide/archive/lmg-s4-issue-43-images-a-mosaic-of-3-colours/)), while one second of audio requires 86kB ([Issue 45](https://buttondown.email/laymansguide/archive/lmg-s4-issue-45-audio-a-sampling-of-values/)).

Various video stream formats exist for the purpose of compressing video data lossily. In addition to the lossy compression techniques I covered in [Issue 46](https://buttondown.email/laymansguide/archive/lmg-s4-issue-46-lossy-compression/), software that creates these streams can also compare video frames at different points in time and throw away identical parts (if there’s no scene change, or if the camera is panning slowly, for instance).

h264 is still the most common video stream format in use today. h265 (a.k.a. HEVC) is slated to replace it and is set to become more and more popular, while Google’s VP9 is attempting to compete with it (with companies such as Netflix already on board). FLV (as a video stream format, not a container; I know it’s confusing) are becoming less and less common.

What about audio? We used to encounter mp3 pretty often, but today most audio stream data is stored as AAC (Advanced Audio Coding, the standard that’s meant to replace MP3), Dolby (often on DVDs and Blurays), and sometimes Vorbis (.ogg).

Confused yet? Just remember that the video file you have is the container, and it contains one or more streams.

# Encoding and decoding

To use these streams, you need a piece of software on your computer. This piece of software en**co**des or **dec**odes the data stream, so it is called a **codec**. If you don’t have the required codecs, you will get an error when you attempt to open a video container file that has one or more streams in that format.

The operating system you use comes bundled with support for the most common formats, although for free-and-open-source OSes this may be hampered by copyright restrictions.

About a decade ago, when video formats proliferated like a tropical ecosystem, codec packs containing just about every codec you need were a common sight online. Today, with most video moved to online streaming platforms, you no longer need them.

# MediaInfo: a program to decipher containers and streams

You can use a program like [MediaInfo](https://mediaarea.net/en/MediaInfo) to help you read the metadata and figure out the container and stream formats. Here’s an example of the information it shows about the only video file on my laptop at the moment:

![MediaInfo screenshot showing container, video stream, and audio stream information](https://github.com/ngjunsiang/laymansguide/blob/master/season4/issue048/issue048_01.png?raw=true)<br />
<small>Mediainfo screenshot showing metadata for an MP4 file containing an h264 (a.k.a. AVC) video stream and an AAC audio stream.</small>

**Issue summary:** A video container can hold one or more audio, video, or text data streams. To encode or decode a data stream, you need to have the necessary codec installed[^1]. Most video runs at 25 or 30 fps, with high-quality video going up to 60 fps. You can use a program like MediaInfo to help you decipher the streams inside a video container file.

[^1]: Come to think of it, that’s a good topic for a future issue: what goes on when a piece of software is installed on your computer?

<hr/>

The key part of this issue I really wanted to get to was about codecs. “Why can’t I open this video file?” was a much more popular question in the recent past, but it has gradually faded as more and more video gets moved to Youtube. Today, I suppose the only people who still run into this problem are teachers who come across archives of old videos while hunting for teaching resources.

But still, I anticipate that I need a gentle introduction to data encapsulation. That’s a complex way of talking about data being nested in a series of shells, like a Matryoshka doll. We’ve seen some examples from the previous season on networking: data stored in an HTTP request, which is encapsulated in a TCP packet, which is encapsulated in an IP packet before it is sent over the Internet.

Today, I can have video stream information stored in an MP4 container, placed in a folder in a losslessly-compressed ZIP file (for whatever strange reason), and sent over the Internet to somebody else. Data surrounded by shells and more shells. It’s like opening a delivery box: your tiny item inside, surrounded by cardboard packaging, surrounded by bubble wrap, surrounded by a cardboard box, which was probably placed on a pallet and shipped in a shipping container.

The next few issues will continue to be about encapsulated data, but I’ll start with something simple first: what is a file?

## What I’ll be covering next

**Next issue:** What is a file?

Sometimes, the hardest questions are deceptively simple. We all have an intuitive idea of what a file is. But what actually goes on under the hood?

See you again next week, next issue.

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
- What is involved in installing a piece of software? [Issue 48]

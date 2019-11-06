**Previously:** An image’s resolution describes its dimensions. Its pixel resolution gives an indication of its physical size (if printed or displayed on a screen), and thus its sharpness. A display with imperceptibly small pixels is often referred to as a Retina display (Apple’s branding) or as a high-PPI display; this requires at least 220 PPI (pixels per inch) nominally. For an image to be printed sharply, it needs at least 300 DPI (dots per inch) on paper.

I uncovered some of the complexity of image display last issue, and I hope it has helped you to see that computers and humans influence each other very closely. The design of computers and the way they store information is inextricably linked to the way humans store and display information too. Colours are stored as RGB (red-green-blue) values because that is how humans perceive colour as well. And the monitors we buy have a pixel density that is just high enough for us to not perceive individual pixels easily.

This issue, we will explore the limits of human sensory perception again, and how it influences the way computers store information. This issue, we talk about audio. And let’s start with a question that I’ve pondered a few years back:

## Why are music files so large (a few MB) when a voice call over internet uses so little data?

This is not a question I can answer within one issue; you will have to wait until next issue for a complete answer :) But let’s start here.

We’ll answer the first part, why audio files are so large, by looking at just how much information we need to provide an undistracting audio experience.

## The human ear

Humans detect sound through vibrations of the eardrum which are transmitted through the cochlea of the inner ear. These vibrations are caused by variations of air pressure in the ear, which in turn are caused by vibrations in the air.

These vibrations can be produced by computers through speakers. The cones of a speaker, which are the movable rubber parts, are connected to electromagnets which control the movement of the cone. The computer sends a signal that causes the cones to move in a particular pattern that produces ... sound, or sometimes music!

## Converting sound to data

If we plot the vibrations of air on a graph known as a waveform, they look something like this:


![Audio waveform](https://github.com/ngjunsiang/laymansguide/blob/master/season4/issue045/issue045_01.png?raw=true)
<small>An audio waveform<br />
Image by [Gordon Johnson](https://pixabay.com/users/GDJ-1086657/?utm_source=link-attribution&utm_medium=referral&utm_campaign=image&utm_content=1781570) from [Pixabay](https://pixabay.com/?utm_source=link-attribution&utm_medium=referral&utm_campaign=image&utm_content=1781570).</small>


This waveform is converted into numeric values through a process called **Pulse Code Modulation** (PCM). If you see the acronym PCM or LPCM in any audio-related file, this is likely what it is referring to.


![Audio waveform](https://github.com/ngjunsiang/laymansguide/blob/master/season4/issue045/issue045_02.png?raw=true)
<small>Pulse code modulation to convert a waveform into numeric values<br />
Image from [Wikimedia Commons](https://en.wikipedia.org/wiki/File:Pcm.svg).</small>


These numeric values can then be stored digitally as bits ([Issue 40](https://buttondown.email/laymansguide/archive/lmg-s4-issue-40-bits-and-bytes/)).

## How high do these values go? Of decibels and dB

Well … how many different values would we need? That depends on how loud we need the sound to be … or does it?

The maximum loudness actually depends on your speaker, not on the signal. The number of levels we can represent in the sound should depend on the range between the loudest and softest sound, shouldn’t it? If we have sixteen levels, we can represent a range of sound where the softest sound is no softer than 16 times below the loudest sound. Any sounds softer than that can’t be represented on the waveform.

So just how many levels can the ear make out? Welcome to the field of psychoacoustics, the study of how sound is processed in the ear and perceived in the brain.

Loudness is measured in **decibels** (dB). The softest sound the human ear can hear corresponds to 20 microPa (microPascals) of pressure; this is taken to be 0 dB, a reference point. A sound 10 times louder (200 microPa) is 20 dB, so every increase of 20 dB represents a tenfold increase in loudness. A jet liner taking off (120 dB) is 10^6 times louder, or a million times louder! That is generally the limit of human hearing: from 0 to 120 dB, or a range of 120 dB.

CD-Audio quality audio uses 16 bits to store a single sample of sound; that provides 65,536 (2^16) different levels, which corresponds to a 96 dB range of loudness. I doubt we will find speakers that can produce close to jet engine levels of sound, and if we do, they probably won’t be using CD Audio as a sound format, so this is pretty much sufficient for most quality audio you’ll find on the internet.

Today, 16-bit audio is pretty much standard on all computers. Audiophiles will tout the benefits of 24-bit audio, but we won’t go into detail on that in a layman’s guide to computing.

So each point produced from pulse code modulation (PCM, above) of sound contains 16 bits (2 bytes) of information. How many samples do we need?

## Sampling and frequency

You probably can’t make out the individual waves in the waveform much earlier in this issue; that’s because the waveform is visually squeezed horizontally. But if we expanded it, you would be able to make out individual waves.

A sound with higher pitch has higher frequency; it has more waves per second. A sound with lower pitch has lower frequency; it has fewer waves per second. It is the upper limit we need to worry about: we must have enough samples per second to be able to represent so many waves. To be able to see a complete wave, we need at least two points: one for the peak, and one for the valley.

This agrees with what signal engineers learn from the [Nyquist-Shannon sampling theorem](https://en.wikipedia.org/wiki/Nyquist–Shannon_sampling_theorem): to store a 1 Hz sound (1 wave per second), you need at least 2 samples per second (to distinguish the peak and valley of the wave).

The human range of hearing ranges from 20 Hz to 20 kHz (that’s 20,000 Hz).  To store a 20 kHz sound, you need at least 40,000 samples per second. CD-quality audio is sampled at 44,100 samples per second (enough for up to 22.05 kHz), which is sufficient to cover the human hearing range of frequencies.

So for 1 second of audio, uncompressed, we will need 16 bits × 44,100 samples = 705,600 bits, or 86 KiB. 1 minute of uncompressed audio would be 5.05 MiB!

**Issue summary:** Humans can distinguish 120 dB of loudness, which means the loudest perceivable sound is a million times louder than the softest perceivable sound. CD audio provides 16 bits of information per sample, sufficient to provide 96 dB. Humans have a hearing range from 20 Hz to 20 kHz. CD audio is sampled at 44.1 kHz. Uncompressed audio thus requires 705,600 bits per second, or 86 KiB/s.

-----

This issue and the past 2 issues set the stage for the next issue, which is the first milestone for this season when I can finally introduce compression! And then we will finally get to answering the question: Why are music files so large (a few MB) when a voice call over internet uses so little data?

## What I’ll be covering next

**Next issue:** Lossy compression: a computer’s attempt to summarise

We’ve all done this before. “What were you talking about with X?” “Oh, we were just talking about Y. I said _blah_ and X said _blah_ and that was about all that was important.” It’s called summarising, and if we didn’t do it, 75% of our lives would just be talking.

How do computers summarise and attempt to convey only the important parts of all the information we store and transmit? This and more in the next issue on lossy compression!

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
- What is compression? [Issue 43]
- Why are music files so large when a voice call over internet uses so little data? [Issue 45]

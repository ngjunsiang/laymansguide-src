**Previously:** Unicode is an encoding format which is meant to support every language, ever. Most websites, apps, and interfaces support it today.

In the last two issues, I explained how text is stored as numbers through the use of lookup tables, whether ASCII or Unicode. The more total characters we want to store in the lookup table, the more bits we need for each character.

This is going to be a recurring theme: If we want to be able to differentiate more shades of colour, or more degrees of loudness in sound, we will need more and more bits for each **sample**, and that means our file—whether text, image, or sound—is going to have a larger filesize.

How many bits is good enough? In the case of text, that is determined largely by the upper limit on the number of symbols we might possibly need to communicate. But how do we decide that for colour? The number of different shades of colours is possibly infinite, and yet we can’t possibly differentiate between really fine shades, nor can our screens possibly produce all of them …

In this issue, I’ll be summarising and oversimplifying decades of colour theory and colour vision research. Buckle up!

## The human eye

Any effective colour system must take into account how the human eye is structured, and how vision occurs. Today, we understand that humans are trichromatic: there are 3 types of cone cells in the eye (and also 1 type of rod cell, which I won’t be explaining here), and each one recognises a different shade of colour: red, green, blue. Each type of cone cell can differentiate roughly 100 different shades, which theoretically enables us to distinguish 1 million shades of colour (100^3).

So it makes good sense that our colour systems in computers evolved similarly, to store single dots of colour as a combination of red, green, and blue. To be able to store 100 different shades, we will need at least 7 bits (2^7 = 128), but [computer systems like things in 8s](https://buttondown.email/laymansguide/archive/lmg-s4-issue-40-bits-and-bytes/). For this and other historical reasons, 1 byte (8 bits) are used for each shade, giving us 256 shades of red, green, and blue each. That’s over 16 million (256^3) shades of colour!

## Colour encoding

Since one byte stores one colour value, three bytes are needed for a single spot of colour combining red, green, and blue—a combination commonly called **RGB**. In a computer, each byte represents the level of that colour; 0 means minimum level (i.e. black) while 255 means maximum level (complete saturation of that colour). So any of those 16 million colours can be stored as a number triplet, representing the red, green, and blue values respectively.

(0,0,0) is black
(255,255,255) is white

So now you know what to do with colour pickers in applications: just find the combination of red, green, and blue that is closest to the colour you want!

![The Microsoft Paint colour picker](https://raw.githubusercontent.com/ngjunsiang/laymansguide/release/season4/issue043/issue043_01.png)<br />
<small>A colour picker, common in graphics applications. This one is from Microsoft Paint.</small>

You can play with a simple colour wheel on [colorspire.com](https://www.colorspire.com/rgb-color-wheel/), or if you’re feeling more adventurous, try the more technical one on [rapidtables.com](https://www.rapidtables.com/web/color/RGB_Color.html).

## Colour production

On a screen, colours are produced by millions of liquid crystals (in LCDs) or light-emitting diodes (in LED displays). These are arranged in a rectangular grid pattern, and each one is known as a **pixel** (shortened from _picture element_). Each pixel is capable of producing 256 shades of red, green, or blue.

It is extremely difficult to manufacture pixels that can produce any colour; this would require that the crystal or diode can emit light of different frequencies. Instead, the display industry has settled on combining 3 sub-pixels into a pixel. Each sub-pixel produces—you guessed it—either red, green, or blue light.

![Close-up of LCD/LED pixels from various displays](https://raw.githubusercontent.com/ngjunsiang/laymansguide/release/season4/issue043/issue043_02.png)<br />
<small>Extreme close-up shots of pixels.<br />
Taken from [lcdtech.info](http://lcdtech.info/en/tests/lcd.pixels.structure.htm).</small>

When colour information is sent from the computer to the display (through the video cable) and decoded in the display, it also uses RGB values. In this sense there is remarkable consistency in computer systems in how colour is stored, sent, and displayed. That minimises the amount of time spent by computers converting from one format to another.

## Colour storage

In a computer, combinations of **image pixels** are stored as image files, but you already know that. I’m on the verge of exceeding my one-idea-per-week promise, so I’ll end this issue with a short comparison of common image formats. Each image format is labelled below by its file extension, the part of the filename that comes at the end.

**BMP**  
BMP is short for “bitmap”. The bitmap format commonly encountered in computer systems, stores pixels uncompressed. This means that each pixel requires 3 bytes of space, so a full-screen image on a typical modern laptop (1920 pixels horizontally, 1080 pixels vertically) would require about 6 MB (1920×1080×3)!

**GIF**  
GIF (Graphics Interchange Format) is one of the earliest image formats, and is rather more restricted in its capabilities as a result. Each GIF pixel is only 8 bits, so a GIF image is limited to using only use 256 colours. One of those colours can be “transparent”, allowing GIF to produce images with transparent parts.

**JPEG**  
JPEG stands for Joint Photographers Expert Group, so it wouldn’t surprise you to learn that it was designed to display photographs with as small a filesize as possible. Today, it is in use for a variety of image types. JPEG can display pixels in 24 bits (i.e. 8 bits for RGB each), but does not store them uncompressed like BMP. Instead, it applies compression to reduce the filesize by “discarding information” from the image in a way that does not affect the final image visibly.

**PNG**  
PNG (Portable Network Graphics) was designed as a replacement for GIF. It supports 24-bit image pixels, with an additional 8 bits per pixel for transparency information. That means PNG pixels have 256 different levels of transparency, allowing for blending effects where one image overlaps another. PNG files support image compression, allowing them to be stored with smaller filesizes than BMP.

**Issue summary:** Colour is stored as a combination of red, green, and blue. In a computer system, each
colour is stored as one byte (8 bits), allowing for 256 different levels. An image is made up of many such pixels of colour.

-----

I get carried away easily explaining colour, and it took incredible discipline to rein that exploratory instinct in and stick to the most essential parts. There’s so much to go into, even for laypeople! But, I know, one idea a week, and I’ve sort of worked out where the other ideas should go, so we’ll have a nice and gradual introduction to colour over the course of several seasons.

## What I’ll be covering next

**Next issue:** Image resolution

![Meme: One does not simply resize an image](https://github.com/ngjunsiang/laymansguide/blob/release/season4/issue043/issue043_03.jpg?raw=true)

After examining a single pixel, I’ll look at a whole image: what does it take to trick our brains into seeing an image instead of a collection of pixels?

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
- What is compression? [Issue 43]

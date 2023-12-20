Title: Issue 44: Image resolution
Date: 2019-10-26 08:00
Tags: 
Category: Season 04
Slug: issue044
Author: J S Ng
Summary: 
Modified: 2019-10-26 08:00

**Previously:** Colour is stored as a combination of red, green, and blue. In a computer system, each
colour is stored as one byte (8 bits), allowing for 256 different levels. An image is made up of many such pixels of colour.

An image is two-dimensional and certainly much larger than a single pixel. How do we talk about its size?

## Image resolution

It is common to hear people refer to an image’s size as its pixel size. When we say that an image has a resolution of 1000×3000 pixels, that means it is 1000 pixels wide by 3000 pixels high. In other words, the image is made up of 3 million pixels of colour, arranged in a grid 1000 pixels wide by 3000 pixels tall.

But how large is this image _physically_? Well, that’s a harder question to answer …

## Resizing

You see, on a computer, you can resize an image as you like. I’m sure you have done it many times, preparing for a presentation or just creating a document. So you can make that image 1cm×3cm, or 10cm×30cm. But how large is an image originally meant to be?

## Image resolution: a ratio between dots and inches

In more finicky circles, the term “resolution” is used in another way: to refer to the ratio of pixels to a physical dimension, usually in inches (this is a legacy thing, I can’t explain why it’s imperial and not metric).

For example, if that 1000×3000 image was meant to be displayed as a 10cm×30cm image on screen (approx. 4 inches by 12 inches), it would have a resolution of 250 pixels per inch (**PPI**)— 1000 pixels ÷ 4 inches. If you could see pixels, and you took out a ruler to count the number of dots in a 1-inch line across or down the image, there would be 250 pixels.

If it was displayed as a 100cm×300cm image instead, that printed image would have a resolution of 25 pixels per inch (1000 pixels ÷ 40 inches). And it would look 10 times blurrier; each image pixel would be about 1mm wide!

So image resolution, as pixels per inch, also gives a measure of sharpness of the image.

For printed images, the same idea applies: a 1000×3000 image printed as a 10cm×30cm image has a resolution of 250 dots per inch (**DPI**) — 1000 ÷ 4 inches. It’s dots instead of pixels because a printer lays down dots of colour rather than displaying pixels (I’ll go into more detail in a future season on computer accessories and peripherals).

## Monitor resolution

When you buy or browse computer monitors, you would have heard the monitor’s pixel dimensions (number of pixels across and down) referred to as its resolution. Its measure of sharpness is usually listed under a label like DPI or PPI, if not pixel density. If not, you can calculate the PPI of a monitor yourself: Just take the horizontal pixel dimension (number of pixels in the screen horizontally) and divide it by the display width, or take the vertical pixel dimension and divide by the height.

Your OS might have a setting for fixing blurry apps, or making small text appear larger. These are typical problems faced on a high-PPI screen. But how high does the PPI need to be for us to get a reasonably sharp image?

## Retina: a brand name for high pixel density displays

In 2010, the late Steve Jobs first used the term Retina referring to the iPhone 4. I suppose he meant to describe a class of devices with a display so sharp that the pixels were practically imperceptible; it wasn’t that long ago that if you squinted a little, you could make out the pixels on your monitor or laptop. High pixel density displays are a lot more common today, so you would probably have to visit the budget section of the computer monitor department in a store to see the low-pixel-density effect again.

So what’s the minimum PPI required to have a Retina display? Apple doesn’t specifically designate a number, but it appears that [the minimum PPI of their Retina devices is 218](https://en.wikipedia.org/wiki/Retina_display). Devices that will be further to your eye can get away with about 220 PPI, while those that will be closer to your eyes will need a higher PPI (up to 400 on the iPhone 6).

But all of that is useless if you scale up an image and still view it at a low _image PPI_!

## Why do my printed images come out blurry?

Here’s a problem I think some of you might have encountered: You are editing a picture on your laptop or computer monitor, and it looks just fine. You send it to the printer and it comes out really blurry. What happened?

What happened is that the image was presented in two different ways. On a screen, it appears as a grid of pixels. a 14" laptop with a 1920×1080 screen resolution actually only has a screen PPI of 157. An image at 100% zoom (1 image pixel displayed as 1 screen pixel) on such a screen would appear fine, because it would be displayed alongside other screen elements (such as the application window) that appear sharp.

But once it is printed, it appears as a collection of ink dots on paper. These dots are a lot finer than the pixels on a screen, so any blurriness is immediately apparent. Your computer or laptop screen is a poor device for assessing print sharpness! To get a better sense of print sharpness, you will want to view the image on a high-PPI display (such as an iPad) and adjust the zoom such that the image on screen has the same size when printed.

For printing images, you will want to make sure your image has a resolution of at least 300 DPI; at least 600 DPI is ideal. You can also calculate this by taking the horizontal pixel dimension of the image, and dividing by the horizontal size you intend to print it at.

**Issue summary:** An image’s resolution describes its dimensions. Its pixel resolution gives an indication of its physical size (if printed or displayed on a screen), and thus its sharpness. A display with imperceptibly small pixels is often referred to as a Retina display (Apple’s branding) or as a high-PPI display; this requires at least 220 PPI nominally. For an image to be printed sharply, it needs at least 300 DPI.

-----

It took a lot of discipline this time to not burrow down rabbit holes (like image-to-screen pixel grid alignment); that would have taken a lot longer than an hour to write.

Pixels and dots are an abstraction that anyone working with computers have to think in terms of, and the relationship between them to physical size can be really tricky to articulate clearly. I hope in this issue I have at least introduced you, my dear readers, to PPI and DPI. And if you work with printers, I think knowing what is going on is a big relief, and takes away the stress from guesswork. Many times I have saved myself the stress of trying to get a sharp banner printed by doing the DPI calculations and realising that there is no way that is possible; I would need too large an image!

Okay, I think we’re done with basic colour and pixel theory! Next up, basic sound theory, and then we can move on the compression :)

## What I’ll be covering next

**Next issue:** Audio, a sampling of values

Sound is so easily taken for granted, but how exactly is it represented in the computer, and how much information is required to store sound? Stay tuned.

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

[**Previously:**](https://buttondown.email/laymansguide/archive/) The VGA video format originated in the time of cathode-ray televisions (CRTs). It was superseded by HDMI, a video format standardised by consumer electronics companies. DisplayPort, on the other hand, is a video format standardised by computer display companies.

The bulk of the story has been written in [Issue 123](https://buttondown.email/laymansguide/archive/lmg-s10-issue-123-graphics-cards-the-pixel-factory/), so this issue will be short.

## Why two digital formats? HDMI vs DisplayPort

HDMI is a consumer electronics standard, and is thus heavily focused on broadcast and home video needs. HDMI primarily supports video and audio data. It also carries some control signals through CEC (for Consumer Electronics Control) capability, enabling a video game console or set-top box to send remote-control commands to a television set via the HDMI connection.

DisplayPort is a computer display standard, focused on computing needs. DisplayPort supports video data, optionally audio data, and additional data (such as USB). Since 2014, compatible devices can also transmit DisplayPort signal format over USB-C, provided both the transmitting and receiving devices support it.

## Analog vs digital formats

Digital formats differ from analog formats, because they do not carry the raw signal for the device. Instead, they carry information about the image, encoding the image data ([Issue 43](https://buttondown.email/laymansguide/archive/lmg-s4-issue-43-images-a-mosaic-of-3-colours/)) into video form; after all, video is just a series of moving images! The device takes on the responsibility of figuring out how to make the images appear on-screen, which is why digital TVs require significantly more electronics than CRT TVs.

## Analog to digital conversion

An analog signal does not easily convert to a digital signal! Analog-to-digital converters, such as the VGA-HDMI adapters that seem to be needed universally, have to figure out how to process a wave-like signal, and convert it into the bits that constitute an image. These adapters need a digital-analog conversion (DAC) chip to carry out that conversion.

In contrast with analog signals, digital signals usually carry uncompressed video data. Digital-to-digital converters thus do not need to carry out any conversion—it’s the same image! Most of these converters merely need pins to be mapped to each other, which makes them cheaper (e.g. DisplayPort-HDMI converters).

A chip that is able to handle multiple formats and produce a robust output is costly, and it is expected that a good adapter will cost quite a bit. That is no guarantee, however, that a costly adapter will always be a good adapter.

## Annddddd ... back to graphics cards

The graphics card is in charge of converting the final rasterised signal ([Issue 122](https://buttondown.email/laymansguide/archive/lmg-s10-issue-122-the-great-flattening/)) to a video signal, depending on the video format that is required. Naturally, this requires additional chips. Most integrated graphics chips support VGA and HDMI, while DisplayPort support is usually reserved for higher-end devices.

Higher-end graphics cards offer support for more video formats. Furthermore, they also have the capability to rasterise and output video streams for multiple screens, enabling multi-screen support for those who need it. If you find that you need more than two screens for work or play, you are likely going to need a dedicated video card that supports three or more simultaneous video output ports.

**Issue summary:** Analog formats such as VGA mostly contain the control signals that the CRT needs to operate, while digital formats such as HDMI and DisplayPort contain image data that the device must convert to control signals. Analog signals need a digital-analog-conversion (DAC) chip to be converted to digital signals, hence VGA-HDMI adapters tend to be more costly than DisplayPort-HDMI adapters. Dedicated graphics cards generally support more simultaneous output video streams than integrated graphics cards.

I hope this sufficiently explains a question I hear so often: why do VGA-HDMI adapters cost so much? I’m also glad this issue ended up much shorter than I expected.

In general, if your adapter/cable needs a chip to carry out signal conversion, it’s going to cost more than a plain cable.

## What I’ll be covering next

**Next issue:** [LMG S10] Issue 126: USB Type-C

Next issue, let’s zap some common questions about the latest USB standard! This is going to stretch over two issues. First up: USB-C for data.

**Sometime in the future:** What is:

- XSS? [Issue 8]
- a good reason developers write code and give it away for free online? [Issue 21]
- OpenType? And what are fonts anyway? [Issue 42]

Title: Issue 124: Video formats
Date: 2021-06-12 08:00
Tags: 
Category: Season 10
Slug: issue124
Author: J S Ng
Summary: 
Modified: 2021-06-12 08:00

[**Previously:**](https://buttondown.email/laymansguide/archive/) Graphics cards contain lots of tiny cores that are much better at performing the same calculation for lots of decimal numbers. These cores are organised into compute units; a graphics card with more compute units can perform more calculations every second. Graphics cards have their own onboard memory, separate from the CPU. GPU memory is different from computer memory; it is configured for much higher data throughput. Integrated graphics are GPUs that are integrated into a CPU chip; these do not have their own onboard memory, and share memory with the CPU.

Ah, the esoteric, tricky, complicated art of shooting electromagnetic radiation into the eyes of humans … entire tomes have been written about this. And I will attempt to summarise the pertinent parts into a single newsletter issue. The hubris!

It’s really something when you suddenly remember that television has been around since the 1930s, while computers in some recognisable form were a 1970s invention. The first part of the computer to be invented was the screen![^1]

[^1]: To be pedantic, the first part of the computer to be invented was actually the keyboard, but they were non-electronic and were called typewriters then.

How did screens work if computers weren't invented? A crash course:

## Cathode-ray tube (CRT) televisions

Early colour television screens had primary-colour (red, blue, and green) phosphor dots embedded in the user-facing portion of the screen. These dots emit coloured light when struck by electrons. At the back of the television, cathodes made of barium oxide are heated, causing them to emit electrons.

These electrons, when emitted, fly in all directions, but they are shaped into a beam by an electric field (hence the name “cathode *ray* tube”, which you might have seen in the form of the acronym **CRT**).

![Cutaway of a CRT, showing the phosphor dot screen]({attach}/season10/issue124/issue124_01.png)<br />
<small>1: Barium oxide cathode, which is heated to emit electrons (labelled “2”), which are shaped into a a beam by an electric field (labelled “3”)<br />
4: Deflecting coils, discussed in the next paragraph<br />
8: Coloured phosphor dots, arranged on a flat screen (labelled “7”).<br />
Image via [Wikipedia](https://en.wikipedia.org/wiki/Cathode-ray_tube)</small>

This electron beam could be aimed at any of the phosphor dots by a set of electromagnetic deflecting coils mounted along the sides of the TV, on the inside surface. One set, oriented vertically (mounted left-right), controlled the horizontal deflection of the electron beam, while another set, oriented horizontally (mounted top-bottom), controlled the vertical deflection.

![Graphic showing an electron beam deflected upwards by deflecting coils in a CRT]({attach}/season10/issue124/issue124_02.png)<br />
<small>The electron beam produced by the cathode is deflected by (electromagnetic) deflecting coils.<br />
Image via [Wikipedia](https://en.wikipedia.org/wiki/Cathode-ray_tube)</small>

To produce an image, the electron beam is manipulated to scan across the screen, one line at a time. Each pass across the screen causes it to strike phosphor dots, emitting light in a line. A variety of techniques (microdeflections, masks, and filters) are used to ensure the correct dots are struck.

Each line of the screen is laboriously scanned with this technique, about 60 times a second. This means that the screen “updates” with a refresh rate of 60 Hz.

To make this happen, a varying voltage is applied across the two sets of deflecting coils. The required pattern for the deflecting coils has to come from the television signal source; the television signal from the broadcasting station, therefore, closely resembles the pattern required by the deflecting coils. The television itself applies almost no processing to this signal! (Remember that the chips used to do this kind of processing had not been invented yet.)

These are what we call **analog** signals. Phonographs and early telephones also used analog signals.

## Video Graphics Array (VGA)

So when the computer was first invented, and these screens were widely available, there was no need to reinvent the screen. Graphics cards ([Issue 123]({filename}/season10/issue123/issue123.md))) simply had to figure out how to emit analog signals that would work with CRT screens.

The graphics standard for doing so is called **VGA** (Video Graphics Array), and was first released by IBM in 1986. An organisation, the Video Electronics Standards Association (**VESA**), was quickly formed in 1989, spearheaded by Nippon Electric Company (NEC), to extend this standard and allow it to support higher resolutions (up to 1080p!).

## LCDs replaced CRTs

As CRTs grow larger, they ran into a few problems. CRTs were big, bulky, and heavy. The larger you made them, the longer you had to make the cathode ray tube, which made them immensely heavy!

By this point, LCD technology had been developed. Instead of using a scanning electron beam, it consisted of a backlight[^2] behind a liquid crystal layer (hence the term liquid crystal display, **LCD**).

[^2]: Older LCDs used cold-cathode fluorescent lamps (CCFLs) for backlights, but today LEDs are used instead.

The liquid crystal layer consisted of pixels of each primary colour. Each pixel had an adjustable transparency, which depended on the voltage applied across it (high voltage = transparent, low voltage = opaque); a cluster of red, green, and blue pixels formed a single image pixel on screen. By applying different voltages across each primary-colour pixel, we can put an image together.

## Digital signals

CRTs controlled the voltage plates directly to deflect an electron beam, through an analog signal. But LCDs use an internal processor to determine what voltage to apply across each liquid crystal pixel. As the technology improved, lower voltages could be used to reduce power usage. So LCDs need a different kind of signal: a **digital** one, consisting of the *raw image data* ([Issue 43]({filename}/season04/issue043/issue043.md))).

## The exodus to digital formats

As digital television became more feasible due to decreasing microprocessor and LCD screen costs, digital formats sprung up to replace VGA.

An early competitor, Digital Visual Interface (**DVI**), was launched by a working group convened by some computer makers (Intel, Silicon Image, Compaq, Fujitsu, HP, IBM, NEC). It was very quickly superceded by High-Definition Multimedia Interface (**HDMI**), an interface which implemented standards set by consumer electronics companies (Hitachi, Sanyo, Silicon Image, Sony, Technicolor, Toshiba).

![HDMI and mini-HDMI connectors displayed top-to-bottom]({attach}/season10/issue124/issue124_03.jpg)  
*HDMI and mini-HDMI connectors displayed from top to bottom. Both support the HDMI video standard<br />Image via [DataPro](https://www.datapro.net/techinfo/hdmi_info.html)*    

This was followed by the DisplayPort (**DP**) standard, developed by PC and chip manufacturers and standardised by VESA, and released in in 2006.

![DisplayPort, mini-DisplayPort, and Thunderbolt Type-C connectors displayed side-by-side]({attach}/season10/issue124/issue124_04.jpg)  
*DisplayPort, mini-DisplayPort, and Thunderbolt Type-C connectors displayed from left to right. All three support the DisplayPort video standard<br />Image via [DataPro](https://www.datapro.net/techinfo/displayport_info.html)*    

**Issue summary:** The VGA video format originated in the time of cathode-ray televisions (CRTs). It was superseded by HDMI, a video format standardised by consumer electronics companies. DisplayPort, on the other hand, is a video format standardised by computer display companies.

Phew. This issue is much longer than I would like; there is so much history to these things! The HDMI-vs-DisplayPort question/complaint I keep hearing is one that only made sense for me in the context of the respective industries they sprung from, and this is something I think most layfolks could definitely understand.

## What I’ll be covering next

**Next issue:** [LMG S10] Issue 125: Analog and digital conversion

Now that I’ve laid out the key differences between VGA, HDMI, and DisplayPort, we can talk about ... video adapters.

**Sometime in the future:** What is:

- XSS? [Issue 8]
- a good reason developers write code and give it away for free online? [Issue 21]
- OpenType? And what are fonts anyway? [Issue 42]

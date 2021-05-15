[**Previously:**](https://buttondown.email/laymansguide/archive/) Graphics cards contain lots of tiny cores that are much better at performing the same calculation for lots of decimal numbers. These cores are organised into compute units; a graphics card with more compute units can perform more calculations every second. Graphics cards have their own onboard memory, separate from the CPU. GPU memory is different from computer memory; it is configured for much higher data throughput. Integrated graphics are GPUs that are integrated into a CPU chip; these do not have their own onboard memory, and share memory with the CPU.

Ah, the esoteric, tricky, complicated art of shooting electromagnetic radiation into the eyes of humans … entire tomes have been written about this. And I will attempt to summarise the pertinent parts into a single newsletter issue. The hubris!

It’s really something when you suddenly remember that television has been around since the 1930s, while computers in some recognisable form were a 1970s invention. The first part of the computer to be invented was the screen![^1]

[^1]: To be pedantic, the first to be invented was actually the keyboard, but they were non-electronic and were called typewriters then.

How did screens work if computers weren't invented? A crash course:

## Cathode-ray tube (CRT) televisions

Early colour television screens had primary-colour (red, blue, and green) phosphor dots embedded in the user-facing portion of the screen. These dots emit coloured light when struck by electrons. At the back of the television, cathodes made of barium oxide are heated, causing them to emit electrons which are shaped into a beam by an electric field (hence the name “cathode ray tube”, which you might have seen in the form of the acronym **CRT**).

![Cutaway of a CRT, showing the phosphor dot screen](https://raw.githubusercontent.com/ngjunsiang/laymansguide/release/season10/issue124/issue124_01.png)<br />
<small>The coloured phosphor dots, labelled as “8” here, are arranged on a flat screen.<br />Image via [Wikipedia](https://en.wikipedia.org/wiki/Cathode-ray_tube)</small>

This electron beam could be aimed at any of the phosphor dots by a set of electromagnetic deflecting coils mounted along the sides of the TV, on the inside surface. One set, oriented vertically (mounted left-right), controlled the horizontal deflection of the electron beam, while another set, oriented horizontally (mounted top-bottom), controlled the vertical deflection.

![Graphic showing an electron beam deflected upwards by deflecting coils in a CRT](https://raw.githubusercontent.com/ngjunsiang/laymansguide/release/season10/issue124/issue124_02.png)<br />
<small>The electron beam produced by the cathode is deflected by (electromagnetic) deflecting coils.<br />Image via [Wikipedia](https://en.wikipedia.org/wiki/Cathode-ray_tube)</small>

To produce an image, the electron beam is manipulated to scan across the screen, one line at a time. Each pass across the screen causes it to strike phosphor dots, emitting light in a line. A variety of techniques (microdeflections, masks, and filters) are used to ensure the correct dots are struck. Each line of the screen is laboriously scanned with this technique, about 60 times a second. This means that the screen “updates” with a refresh rate of 60 Hz.

To make this happen, a varying voltage is applied across the two sets of deflecting coils. The required pattern for the deflecting coils has to come from the television signal source; the television signal from the broadcasting station, therefore, closely resembles the pattern required by the deflecting coils. The television itself applies little to no processing to this signal! (Remember that the chips used to do this kind of processing had not been invented yet.)

These are what we call **analog** signals. Phonographs, and the early telephone also used analog signals.

## Video Graphics Array (VGA)

So when the computer was first invented, and these screens were widely available, there was no need to reinvent the screen. Graphics cards ([Issue 123]()) simply had to figure out how to emit analog signals that would work with CRT screens.

The graphics standard for doing so is called **VGA** (Video Graphics Array), and was first released by IBM in 1986. An organisation, the Video Electronics Standards Association (**VESA**), was quickly formed in 1989, spearheaded by NEC, to extend this standard and allow it to support higher resolutions (up to 1080p!).

## Digital signals

While an analog signal contains a voltage pattern to control deflecting coils, a **digital** signal does not presume to know how the image is being produced. It merely sends the image data ([Issue 43](https://buttondown.email/laymansguide/archive/lmg-s4-issue-43-images-a-mosaic-of-3-colours/)) in digital format to be displayed, and lets the display device figure out how to convert that information to lit pixels.

## The exodus to digital formats

As digital television became more feasible due to decreasing microprocessor and LCD screen costs, digital formats sprung up to replace VGA.

An early competitor, Digital Visual Interface (DVI), was launched by a working group convened by some computer makers (Intel, Silicon Image, Compaq, Fujitsu, HP, IBM, NEC). It was very quickly superceded by High-Definition Multimedia Interface (HDMI), an interface which implemented standards set by consumer electronics companies (Hitachi, Sanyo, Silicon Image, Sony, Technicolor, Toshiba).

![HDMI and mini-HDMI connectors displayed top-to-bottom](https://raw.githubusercontent.com/ngjunsiang/laymansguide/release/season10/issue124/issue124_03.jpg)<br />
<small>HDMI and mini-HDMI connectors displayed from top to bottom. Both support the HDMI video standard<br />Image via [DataPro](https://www.datapro.net/techinfo/hdmi_info.html)</small>

This was followed by the Displayport standard, developed by PC and chip manufacturers and standardised by VESA, and released in in 2006.

![Displayport, mini-Displayport, and Thunderbolt Type-C connectors displayed side-by-side](https://raw.githubusercontent.com/ngjunsiang/laymansguide/release/season10/issue124/issue124_04.jpg)<br />
<small>Displayport, mini-Displayport, and Thunderbolt Type-C connectors displayed from left to right. All three support the Displayport video standard<br />Image via [DataPro](https://www.datapro.net/techinfo/displayport_info.html)</small>

**Issue summary:** The VGA video format originated in the time of cathode-ray televisions (CRTs). It was superseded by HDMI, a video format standardised by consumer electronics companies. Displayport, on the other hand, is a video format standardised by computer display companies.

Phew. This issue is much longer than I would like; there is so much history to these things! The HDMI-vs-Displayport question/complaint I keep hearing is one that only made sense for me in the context of the respective industries they sprung from, and this is something I think most layfolks could definitely understand.

## What I’ll be covering next

**Next issue:** [LMG S10] Issue 125: Analog and digital conversion

Now that I’ve laid out the key differences between VGA, HDMI, and Displayport, we can talk about ... video adapters.

**Sometime in the future:** What is:

- XSS? [Issue 8]
- a good reason developers write code and give it away for free online? [Issue 21]
- OpenType? And what are fonts anyway? [Issue 42]

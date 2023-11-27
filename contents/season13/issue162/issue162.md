[**Previously:**](https://buttondown.email/laymansguide/archive/) Cross-site scripting attacks occur when a webpage loads malicious code from a third-party, usually carried out by a script in the page. Today, websites are protected from loading unauthorised scripts through cross-origin resource sharing (CORS) policy implemented in browsers, which only allows a website to load scripts from authorised domains.

This is the issue that doesn’t really fit anywhere, but this season is about lots of things we take for granted and fonts are one of them.

I could probably fill at least half a season talking about fonts and typesetting, but let’s stick to the basics here.

## What is a font?

I’m going with [Source Sans](https://fonts.adobe.com/fonts/source-sans), an open-source **typeface** designed in-house by Adobe. Let’s open one up one of its **font**s[^1], Source Sans Pro Regular, in a font editor[^2] and see:

[^1]: A font is a single style in a typeface family. The full family will usually have regular/bold/italic styles. More advanced typefaces may have small caps, display, and caption fonts.

[^2]: The one I use is called [Fontforge](https://fontforge.org), and it is open-source.

![Fontforge with Source Sans Pro Regular open, showing glyphs](https://raw.githubusercontent.com/ngjunsiang/laymansguide/release/season13/issue162/issue162_01.png)  
<small>Source Sans Pro Regular, in Fontforge.</small>

You might already be aware that fonts contain **glyphs**, which are the shapes of each separate character. What makes up those glyphs?

![Uppercase Q from Source Sans Pro Regular](https://raw.githubusercontent.com/ngjunsiang/laymansguide/release/season13/issue162/issue162_02.png)  
<small>Uppercase Q from Source Sans Pro Regular.</small>

These glyphs are mathematical shapes. They are stored as a series of points, joined by curves[^3] or straight lines[^4], which are stored as numbers. The diagrams we draw in Microsoft Word are much the same!

[^3]: For the curious, the specific type of curve used in fonts are [Bézier curves](https://jdhao.github.io/2018/11/27/font_shape_mathematics_bezier_curves/).

[^4]: Don’t be alarmed if the mathematicians among us casually remark that a straight line is a trivial example of a curve.

## Font variants

When you bold or italicise text, the operating system swaps in the appropriate glyphs from the bold or italic fonts from the same typeface family. A lot of careful work goes into ensuring that these fonts are recognised as belonging to the same typeface, or this feature would not work.

This means that when you install fonts, remember to grab the bold and italic fonts as well!

Many applications, if they are unable to find the bold/italic fonts, will artificially “bold” or “italicise” the regular font by thickening the glyph, or slanting it. Any graphic designer worth their salt will notice this immediately; even without scrutinising the font, it will feel “off” in some vaguely inscrutable way until you take a closer look and notice the proportions are wrong.

## Font display

For an application to be able to support text formatting, it must have a program called a text rendering engine. This program takes a single long string of text and determines the appropriate places to chop it up with line breaks. To do that, it first needs to convert the glyph shapes from mathematical formulas into actual real lit pixels or real inky droplets (in a process called **rasterisation**, [Issue 122](https://buttondown.email/laymansguide/archive/lmg-s10-issue-122-the-great-flattening/)).

Then their dimensions have to be considered in the line of text, to know where the line breaks should be placed. Because glyphs are not actually rectangular boxes and they protrude in different ways, optically they need some horizontal adjustment (called **kerning**) to look evenly spaced optically, so that needs to be done too[^5].

[^5]: The kerning information is created by the font designer and embedded in the font file. Applications usually pass this information to the text rendering engine, although some might not actually use it.

![Kerning for some common glyph pairs in Source Sans Pro Regular](https://raw.githubusercontent.com/ngjunsiang/laymansguide/release/season13/issue162/issue162_03.png)  
<small>Kerning for some common glyph pairs in Source Sans Pro Regular.<br />  
A kern value of 0 or blank means no kerning is required. A negative value means the letters need to be brought closer, and a positive value means they need to be spaced further (quite rare).</small>

Advanced renderers might even do other things, like avoiding too many terminal hyphens on consecutive lines (looks ugly), or making microadjustments to letter spacing. But, oops! This changes the line length, so the engine needs to go back to re-check the line breaks. This is an iterative process.

Text rendering engines are an art in themselves, and we are not going to go in depth here.

## Font formats

The classic file extension is `.ttf`, which stands for Truetype font, a font format created by Apple in the late 1980s and subsequently adopted by other systems.

These days, you might also see `.otf`, which stands for Opentype font. This is a more modern font format, co-developed in the mid-90s by Microsoft and Adobe. This adds much more functionality and new features, which after some deliberation I have decided not to write about—it is simply not a layperson topic!

If you do web development, you might also see `.woff`, the Web Open Font Format, co-developed by Mozilla and other type organisations. It shares some features in common with TTF and OTF, but adds other features for licensing information, which is usually more important for the web, where these font files need to be downloaded to the users’ computers.

**Issue summary:** Typeface families consist of multiple fonts for each style in the typeface. Each font consists of glyphs, which are mathematical shapes described by curves joining points. These shapes need to be rasterised for display on a computer screen, or for printing on paper. Font files usually come in `.ttf`, `.otf`, or `.woff` formats.

This difference in representation vs display, fonts-as-mathematical-shapes vs fonts-as-pixels-or-dots, has been and continues to be the cause of much weeping and gnashing of teeth. But I’ve decided it’s not worth delving into that for a layman’s guide to computing—perhaps in a separate publication!

## What I’ll be covering next

**Next issue:** [LMG S13] Issue 163: System & software ecosystems

With this diversion over, let’s return to talking about distribution. Content distribution, code distribution, and next issue I’ll move on to software distribution!

With this I have also cleared my backlog of questions, and will be closing the below section as well.

**Sometime in the future:** What is:

- ~~OpenType? And what are fonts anyway? [Issue 42]~~

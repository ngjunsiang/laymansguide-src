**Previously:** 8 bits comprise 1 byte. Humans count bytes in multiples of thousands, while computers count bytes in multiples of 1,024.

It’s still difficult to wrap our minds around how computers do everything with exactly two symbols: 0 and 1. Let’s start simple: How do computers represent text?

The simple answer is that text can be represented as numbers. In the simplest scheme we know of, A=1, B=2, C=3, and so on. A computer does something more complicated, it keeps a table of characters and the numbers that represent them, in an **encoding table**. One encoding that is commonly used for plain text is known as the American Standard Code for Information Interchange, or ASCII table.

## Some ASCII background and history

To put things in some context, keep in mind that ASCII actually predates the internet! (We had computers way longer than we had the Internet, after all.) This was the 1960s, Morse code was the standard in telegraph transmission until the 1900s, when the [Murray code](https://en.wikipedia.org/wiki/Baudot_code#Murray_code) was used instead (itself derived from the earlier Baudot code). The Murray code employed a keyboard much like a typewriter’s. This was an improvement over Morse code, because instead of tapping a single control key (like you see in classic movies), you can now use **all five fingers** of the hand to type.

In the 1920s, the Murray code was developed into the International Telegraph Alphabet No. 2 code (ITA2 code). Behold:

![ITA2 table](https://github.com/ngjunsiang/laymansguide/blob/master/season4/issue041/issue041_01.jpg?raw=true)<br />
<small>Image from [Wikimedia Commons](https://en.wikipedia.org/wiki/File:International_Telegraph_Alphabet_2.jpg)</small>

But the Murray code actually used more bits to transmit the same information! In Morse code, every letter is represented with between 1 to 5 symbols. Each symbol is either a dash or a dot:

![Morse Code table](https://github.com/ngjunsiang/laymansguide/blob/master/season4/issue041/issue041_02.png?raw=true)<br />
<small>Image from [Wikimedia Commons](https://en.wikipedia.org/wiki/File:International_Morse_Code.svg)</small>

What do we gain from using more symbols to transmit each number or letter? If you compare the two, you see that ITA2 has some things that are missing in Morse code:

- Spaces
- Carriage return
- Line feed
- Symbols

Symbols and spaces are easy enough to understand, and very welcome; if you’ve ever tried reading early telegrams (or using Morse code) you’ll appreciate their addition. But what is carriage return and line feed?

## The typewriter

With the advent of the typewriter, people had access to nicely formatted text. You could type text on multiple rows instead of one long row! But you had to remember to do the actions when using a typewriter for it to be formatted properly.

![A typewriter on a table](https://github.com/ngjunsiang/laymansguide/blob/master/season4/issue041/issue041_03.jpg?raw=true)<br />
<small>The Underwood Five typewriter<br />
Image from [Wikimedia Commons](https://en.wikipedia.org/wiki/File:Underwoodfive.jpg)</small>

There were two separate actions involved as you pulled the leftmost lever to the right: (1) The carriage, which holds the paper and moves a bit to the right after each letter is typed, now resets its position so you can start typing from the left again, and (2) the paper is moved up so you can begin typing on the next line.

(1) is called a carriage return, (2) is called a line feed.

ITA2 could not only send letters and symbols, it could send formatting commands!

## ASCII proper

The ASCII code chart expands the capabilities of ITA2, while requiring 7 bits for each character. Each character is situated in a specific row and column, out of 8 columns and 16 rows which are numbered starting from 0. (Note that 8 is 2^3 and requires 3 bits, 16 is 2^4 and requires 4 bits.)

![ASCII code chart](https://github.com/ngjunsiang/laymansguide/blob/master/season4/issue041/issue041_04.png?raw=true)<br />
<small>(An early version of) The US ASCII code chart. Each row number is represented by 4 bits, while each column number is represented by 3 bits.<br />
Image from [Wikimedia Commons](https://en.wikipedia.org/wiki/File:USASCII_code_chart.png)</small>

Technical details aside, look at what ASCII has:

- Symbols and numbers (mainly columns 2 and 3, but also scattered elsewhere)
- Upper _and_ lowercase letters (columns 4 to 7)
- Lots and lots of control codes! (columns 0 and 1)

What do these control codes mean?

- `NUL` stands for null, a placeholder code for when the machine wasn’t transmitting.
- `SOH`: start of header, to indicate the portion of the transmission that contained information about the message.
- `STX` and `ETX`: start of text and end of text, to indicate the message portion.
- `EOT`: end of transmission.
- `DEL`: to delete the previous character (hello, backspace).
- `CR` and `LF`: we just met them, carriage return and line feed.

I won’t explain the rest in this supposedly-short newsletter, but if you’re interested the full list is [on Wikipedia](https://en.wikipedia.org/wiki/ASCII#Control_characters).

## ASCII today

In a basic text file, text is still stored using ASCII (although it has seen some modifications since). Some of the control codes are obsolete, while some are still in use today. Remember this image from Issue 12?

![An HTTP request captured in Wireshark showing my developer API key](https://github.com/ngjunsiang/laymansguide/blob/master/season1/issue012/issue012_01.png?raw=true)<br />
<small>An HTTP request captured in Wireshark.</small>

The `\r` and `\n` you see there are control codes. They stand for 'return' and 'newline', the modern equivalent of 'carriage return' and 'line feed'.

Formatting codes are well and alive today, and they are more prosperous than ever! Without formatting codes, all our files would be stored only in the same boring format, represented only as letters and numbers and punctuation marks.

And there you have it.

**Issue summary:** In computers that can encode and decode ASCII, text is stored as a 7-bit sequence. Text consists of letters, numbers, symbols, and control codes.

-----

A rather long issue, but that’s what it takes to explain carriage return and line feed, which don’t make sense to folks who have never seen or used a typewriter before (why can’t you just have a single control code that moves to the start of the line _and_ moves to the next line? Well, sit down and let me tell you a story …)

Much of the idiosyncracies of computers and technology are this way: accumulated from decades of historical developments, forming legacy baggage in some cases, and interesting bits of history in others.

## What I’ll be covering next

**Next issue:** Unicode, computers go international

These days, most of the text you encounter is not encoded in ASCII. It is rather limited, after all, and we need a lot more than just letters, numbers, and symbols today. Next issue, we’ll go into modern-day text encoding, using Unicode.

**Sometime in the future:** What is:

- booting up? [Issue 15]
- a cookie? [Issue 8]
- XSS? [Issue 8]
- a CDN? [Issue 8]
- Unicode? And what does it have to do with emoji? [Issue 8]
- ~~those '\r\n’s in the HTTP request packet [Issue 12,17]?~~
- a good reason developers write code and give it away for free online? [Issue 21]
- ~~ASCII? [Issue 23]~~
- compiling code into an application [Issue 26]?
- firmware? [Issue 34]
- What is HTML [Issue 38]

Title: Issue 40: Bits and bytes
Date: 2019-09-28 08:00
Tags: 
Category: Season 4
Slug: lmg-s4-issue-40-bits-and-bytes
Author: J S Ng
Summary: 

**Previously:** Networks enable data packets to get from one computer in the network to another through gateways that forward the data packets according to fixed rules. These rules are encoded in the various protocols followed by network systems, and all computers on the network agree to follow the same protocol.

But what kind of data gets transmitted over the network? And why do strange file-related things happen on my computer? I’ll unpack some of these gradually over the course of this 13-issue season.

Let’s start Season 4 slow, with a simple question: when I buy a 1TB hard drive, why does my computer say it has only 930GiB available?

## A bit: the littlest bit of data

You know the game Animal, Plant or Mineral, where you ask yes/no questions to guess what the other person has chosen (from the Animal, Plant, or Mineral category)? Each yes/no question narrows down the range of options until you are finally reasonably certain you know what they have in mind.

It seems everybody knows that all the way down, computers work with 0s and 1s. They work kind of like Yes and No, too, with each digit acting like the answer to a Yes/No question, to narrow down the available information. Quick example:

**Animal**

1. Does it have more than two legs? → Yes (1)
2. Does it have four legs? → No (0)
3. Does it crawl on the ground? → No (0)
4. Can it jump? → Yes (1)

With this question sequence, a grasshopper would be represented as YNNY, or `1001`. A millipede would be represented as `1010`. A dog would be represented as `1101`, but so would a cat. 4 digits can help us categorise different animals, but not all. The more questions we can ask, the better we can categorise them.

The answer to each question has 2 possible outcomes, and gives us a little _bit_ more information. Claude Shannon, the father of modern Information Theory, thus named it the **bit**. What is a bit? It’s a unit of measure for information. Just as we measure weight in units of kilograms, height in units of centimetres, or time in units of seconds, we measure information in bits.

1 bit of information is enough information to reduce the uncertainty by 50%. Each question you ask in Animal, Plant, or Mineral should reduce the possibilities by half, until the remaining possibilities are small enough to guess.

So in a computer, a single digit—0 or 1—is a bit.

## A byte: a convenient cluster of 8 bits

In the 1970s, 8-bit microprocessors were all the rage. These were processors that processed everything in clusters of 8 bits. It became convenient to refer to 8 bits as a **byte**, and the term has stuck since. The term didn’t die off because so many things still use clusters of 8 bits to represent information.

8 bits can store 256 (2^8) unique values, and that turns out to be enough for many purposes. I won’t list examples here, since those examples will come in subsequent issues. If you need greater precision, you can always use 2 bytes.

## It’s all Greek (prefixes): kilo, mega, giga, tera

The metric system gave us nice prefixes to count in thousands (kilo-), millions (mega-), billions (giga-), or trillions (tera-), neatly represented by the letters _k_, _M_, _G_, and _T_ respectively (case-sensitive).

So a kilobyte is 1,000 bytes, a megabyte is 1,000,000 bytes, a gigabyte is 1,000,000,000 bytes, and a terabyte is 1,000,000,000,000 bytes.

## Uh oh …

Here we run into a little bit of a problem. Computers like to count in powers of two, because increasing the number of bits by one gives us double the number of possible values.

8 bits gives us a byte. 9 bits gives us two bytes, since the additional bit can be 0 or 1. 10 bits gives us four bytes, since the additional 2 bits can be 00, 01, 10, or 11.

11 bits: 8 bytes (000, 001, 010, 011, 100, 101, 110, 111)  
12 bits: 16 bytes (I won’t list them from this point onwards; I think you can see the pattern)  
13 bits: 32 bytes  
14 bits: 64 bytes  
15 bits: 128 bytes  
16 bits: 256 bytes  
17 bits: 512 bytes  
18 bits: 1024 bytes  

1024 bytes is the closest we can come to 1000 bytes.

## Can’t be unseen

If you’re on a Windows computer, go to My Computer. If you’re on another OS, go to whichever app shows you available disk space. Look carefully at the units for free space.

Disk space is not reported in MB, GB, or TB. It’s reported in MiB (mebibytes), GiB (gibibytes), or TiB (tebibytes)! Those units are not the decimal notations we are used to. We count bits differently from computers.

**Humans:** Since 10^3 is 1000, a kilobyte is 1000 bytes, a megabyte is 1000 kilobytes, a gigabyte is 1000 megabytes, and a terabyte is 1000 gigabytes.  
**Computers:** Since 2^10 is 1024, a kibibyte (kiB, or kilo binary byte) is 1024 bytes, a mebibyte (MiB, or mega binary byte) is 1024 kibibytes, a gibibyte (GiB, or giga binary byte) is 1024 mebibytes, and a tebibyte (TiB, or tera binary byte) is 1024 gibibytes.  

When you buy a 1TB hard drive, you are buying a 1,000,000,000,000-byte drive.

1,000,000,000,000 bytes ÷ 1,024 = 976,562,500 kibibytes (kiB)  
976,562,500 kibibytes ÷ 1,024 = 953,674 mebibytes (MiB)  
953,674 mebibytes ÷ 1,024 = 931 gibibytes (GiB)  

So your computer isn’t lying, it’s just using different units of counting.

**Issue summary:** A bit is a unit of measurement for information. 1 bit of information is enough to reduce the uncertainty by 50%. 8 bits comprise 1 byte. Humans count bytes in multiples of thousands, while computers count bytes in multiples of 1,024.

-----

There are much shorter versions of this explanation on the Internet, but I found none of them satisfying, because they try to paper over the mathematical detail. While this newsletter is intended for layfellas, the math is something that can be worked out with a calculator, and I found that showing the detail makes it easier to understand.

There may be a social-construct argument to be made here for units of measurement, but I won’t go into that here. I wanted Issue 40 to start with an example of how things work differently between a human mind and a computer’s “computational mind”, and I hope I’ve achieved that.

## What I’ll be covering next

**Next issue:** ASCII, the typewriter digitised

We started with a (figurative) bit of bean-counting, let’s get right into how computers work with text in Issue 41 so that I can finally answer one of the sometime-in-the-future questions below: What is ASCII? And I’ll answer another one in Issue 42: What is Unicode?

**Sometime in the future:** What is:

- booting up? [Issue 15]
- a cookie? [Issue 8]
- XSS? [Issue 8]
- a CDN? [Issue 8]
- Unicode? And what does it have to do with emoji? [Issue 8]
- those '\r\n’s in the HTTP request packet [Issue 12,17]?
- a good reason developers write code and give it away for free online? [Issue 21]
- ASCII? [Issue 23]
- compiling code into an application [Issue 26]?
- firmware? [Issue 34]
- What is HTML [Issue 38]

Title: Issue 122: The great flattening
Date: 2021-05-29 08:00
Tags: 
Category: Season 10
Slug: lmg-s10-issue-122-the-great-flattening
Author: J S Ng
Summary: 

[**Previously:**](https://buttondown.email/laymansguide/archive/) 3D models are represented with vertices (points), edges (line segments between points), and faces in a computer. Images known as textures can be mapped to faces to give the impression of detail.

Having a model represented in a computer as a large set of numbers is cool, but nobody does 3D modelling like that. We need something to look at! We need a way to convert our model into a flat picture, ideally displayed on our monitors. And this conversion process needs to be fast enough that as we rotate or change the view of our model, the computer can keep up, displaying the changes in real-time.

This process is called **rendering**.

## A pipeline for rendering pictures

During rendering, data from the modelling program is processed in a series of steps; these steps together are known as the **graphics pipeline**. If you’ve done perspective drawing or tried to figure out how to create clever camera tricks, you already have a sense of what the computer needs to do here.

The 3D cube on screen looks different depending on where our eye is, and which direction it is looking. Our distance to the cube affects how much distortion the view undergoes. Lighting also affects how the cube appears, by making shaded areas appear darker, and lit areas appear brighter.

Finally, this 3D model needs to be “distorted” into a 2D view so it can be displayed on a screen. (We don’t have 3D holo-projectors yet … 😢)

Lastly, since our screens display images as a grid of pixels, we need to figure out the best way to convert the distorted 2D view into a pixel grid. This part of the pipeline is known as **rasterisation**. Here, the computer figures out what colour each pixel should be, based on which part of the model actually gets projected here. Hidden parts do not need to be rasterised, and neither do parts of the model which are outside the screen.

All these steps take place in the graphics pipeline.

## The hardware

The pipeline used to be carried out by the CPU ([Issue 53]({filename}/season5/issue053/issue053.md)), but that isn’t ideal. The CPU’s hardware is optimised for *general-purpose processing*: keeping track of integers (i.e. natural numbers like 1, 2, 3, …), adding or subtracting them, and resetting them. It has many more computational units that carry out this calculation.

Graphics processing, on the other hand, requires a different kind of calculation. The position of vertices do not fit nicely into integers; we have to carry this out using decimal numbers (1.46776, 2.58704, –3.57514, …). The CPU does not encounter these often, and therefore does not have many of these computational units.

For graphics, we need a different kind of processor, one that is jam-packed with decimal computational units. We need a **graphics card**.

**Issue summary:** Computers are general-purpose machines that usually process integer calculations. The graphics pipeline requires more specialised hardware that can process decimal number calculations. This is why high-performance graphics usually requires a graphics card.

## What I’ll be covering next

**Next issue:** [LMG S10] Issue 123: Graphics cards: The Pixel Factory

So what does a graphics card do, just pop out pixels like nobody’s business?

Yep! Next week, a quick intro to graphics cards, and why they are so amazing. And, because this is recent news, some coverage on how the M1 differs from most laptops in the way it manages the CPU and GPU (graphics processing unit).

**Sometime in the future:** What is:

- XSS? [Issue 8]
- a good reason developers write code and give it away for free online? [Issue 21]
- OpenType? And what are fonts anyway? [Issue 42]
- a video card? [Issue 113]

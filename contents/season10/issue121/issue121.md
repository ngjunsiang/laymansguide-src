[**Previously:**](https://buttondown.email/laymansguide/archive/) Driver files provide information about the driver, and instructions on how to receive information from the device, and encode information to be passed to the device. The operating system may come with generic driver files for the device, but custom driver files might provide better performance or additional features.

This issue, let’s start from scratch with graphics: how does a machine that only processes 1s and 0s work with graphics? For starters, let’s think: what can we represent about graphics if we only have numbers?

## Representing graphics using numbers

Numbers can be used to represent points (a **vertex**, in graphics-speak). In 3D space, a point can be represented with 3 numbers, usually written in math as `(x, y, z)`.

A line (**edge**, in graphics-speak) can be represented as a segment between two points. So we can represent straight-line segments using two points. Curved-line segments are trickier, but for now a lazy way to represent them is just ... using a series of points 😛 like connect-the-dots puzzles!

Surfaces are ... a bit trickier. What is the minimum number of points we need to represent a flat surface? Turns out the answer is 3 points: if we pick any 3 points that are not along the same line, we can join them along their edges and they form a triangle, which is a flat surface!

In graphics-speak, we call these surfaces **faces**. Four points which form a flat four-pointed face are called quads, and we can do the same for polygons with more points too. But most graphics hardware just deals with triangles and quads, because everything else can be represented using triangles and quads anyway.

## Making 3D models

3D modelling software (also referred to as computer-aided design software, or CAD software) helps us with the process of creating vertices (plural for vertex), edges, and faces. Any object we model digitally is just a collection of vertices, edges, and faces: we call such collections a **mesh**.

## Textures

With just meshes, we quickly run into the limits of what can be represented. For simplicity of calculation, each face can only have one colour. To make really detailed and realistic models, we need very finely detailed meshes. These are problematic because a lot of calculation is needed to make these models appear on screen; the more faces it has, the more calculation is needed!

One way to reduce the number of faces in the mesh while still creating a decent model is to *use images on the face*. (I explained how images are represented in computers in [Issue 43](https://buttondown.email/laymansguide/archive/lmg-s4-issue-43-images-a-mosaic-of-3-colours/)) We will need additional information to describe the scale and rotation of the image on the face, but at least we can use the same image across multiple faces if necessary. Instead of having to model a hundred thousand blades of grass, I could just model a few stalks, and use a grassy texture to complete the impression.

## Scene modelling

Just having models is pretty boring. We will usually be putting multiple models in a scene. Besides models, a scene needs to have lighting, a way to model the sky as the background, and other niceties.

We can use numbers to describe the position, luminosity (i.e. **brightness**), hue (i.e. **colour**), and other properties of lighting in our scene.

**Issue summary:** 3D models are represented with vertices (points), edges (line segments between points), and faces in a computer. Images known as textures can be mapped to faces to give the impression of detail.

Great, we have a way to use numbers to describe a 3D model; that’s nice progress. But how do we turn those numbers into a picture on screen?

## What I’ll be covering next

**Next issue:** [LMG S10] Issue 122: The great flattening

Numbers, numbers, and more numbers … isn’t the CPU great at numbers? Why do gamers and 3D modellers have the hots for graphics cards instead? Stay tuned next week!

**Sometime in the future:** What is:

- XSS? [Issue 8]
- a good reason developers write code and give it away for free online? [Issue 21]
- OpenType? And what are fonts anyway? [Issue 42]
- a video card? [Issue 113]

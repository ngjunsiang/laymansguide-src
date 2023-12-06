[**Previously:**](https://buttondown.email/laymansguide/archive/) Time is synchronised from higher-precision sources through a protocol called Network Time Protocol (NTP). A public pool of time servers is available for synchronisation at pool.ntp.org.

Ah, GPS. The only topic that actually has almost nothing to do with computing ... and yet the mobile computers in our pocket rely on it so much.

## A short history

The Global Positioning System (GPS) was born of the space age, in 1973, before computers even went mainstream. It was originally used for military applications, particularly for navigation. It was first widely used in a political conflict in the Gulf War (1990–1991). The public finally had access to it in 1996, after US President Bill Clinton issued a policy directive for it to be dual-use (used for both military and civilian purposes).

## Principles

The principle of triangulation far predates GPS. Triangles have been used to estimate distance since antiquity; there is evidence of such techniques being used from sources as far back as 6th century BC.

In essence, if you know the location of two reference points, then with those two reference points and your own location as the third point, you can draw a triangle and solve a little geometry puzzle to figure out your own location.

If you were hiking or just taking a walk, you need to have at least two landmarks with locations marked on a map. As long as you stop somewhere with good visibility, you can get your bearings to those landmarks on the map, draw a line backward from each landmark following your bearing, and the intersection of the lines from each landmark will show your location.

But digital compasses are not ubiquitous in all devices yet; typically they are only included in high-end phones. A simpler way for devices to get their location is to estimate their distance to the two landmarks. This they can do using radio waves, which travel at (close to) the speed of light: 300 million metres per second. Provided the landmarks contain devices that can receive this signal and send it back, the time delay can be used to calculate the distance between the device and landmark.

## The GPS network

For this to work globally, you are going to need such landmarks positioned all over the world, within receiving range of any device. These landmarks need to be:

1. electrically powered, so they can broadcast signals
2. tall, very tall, since radio waves do not follow Earth’s curvature. A short tower would not be able to receive signals for devices that are too far away: the signal would be blocked by the Earths curved surface!
3. aware of their own position, and synchronised at regular intervals

Let’s solve problem 2 first: instead of building millions of towers worldwide (and how would we do that on the oceans?), we can just launch satellites into space to serve as landmarks for triangulating position. GPS satellites orbit at an altitude of 20,200 km, almost twice of Earth’s diameter, allowing any of them to be reached from almost half of the Earth’s surface.

Solving problem 3: if we launch enough satellites, they can continually synchronise their clocks with each other, and triangulate their own position relative to other satellites.

Solving problem 1: satellites all face this common problem of needing electrical power. They have largely resolved it with the use of solar panels.

## Getting your location using GPS

When your smartphone tries to triangulate its location using GPS, it gets its distance from four overhead satellites, along with their location (remember that there is an altitude component!). It then determines its position from this information using triangulation.

The triangulation calculation here is rather more complicated, given that the satellites are in constant motion and not geostationary (above the same spot on earth all the time). At an orbit altitude of 20,200 km, even radio waves, travelling at lightspeed, still take about 0.07 seconds to reach your phone from a GPS satellite. But it is possible, and your phone does it each time you get your location from GPS—to a precision of about 10m!

**Issue summary:** To get your location using GPS, your phone receives information from four overhead GPS satellites: their location, and the distance between them and your phone. With this information, your phone can calculate its location.

## What I’ll be covering next

**Next issue:** [LMG S13] Issue 159: Wifi & cell tower location tracking

Receiving radio signals all the time requires the receiving unit to be on all the time; if you use GPS heavily you will find your battery draining quickly!

The reason our smartphones can maintain such good battery life is that they *don’t* use GPS most of the time. After all, it is not possible to get GPS in a lot of places: in basements, tunnels, anywhere you can’t get a solid signal from four overhead satellites. There are less energy-costly ways to get your location these days, especially if high precision isn’t necessary.

Next issue, let’s look at how wifi and cell towers come in!

**Sometime in the future:** What is:

- XSS? [Issue 8]
- OpenType? And what are fonts anyway? [Issue 42]

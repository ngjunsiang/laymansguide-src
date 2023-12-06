Title: Issue 129: Cooling
Date: 2021-07-17 08:00
Tags: 
Category: Season 10
Slug: lmg-s10-issue-129-cooling
Author: J S Ng
Summary: 

[**Previously:**](https://buttondown.email/laymansguide/archive/) Upgradable parts need a slot or socket to be inserted into; these slots/sockets need to be made robust enough, causing them to take up more space than a soldered part. Devices which were designed to be small and portable generally eliminate these as far as possible, opting to have parts directly soldered to the board instead.

Why do computers need power?

Other home appliances I can understand. They need to heat up air/water, move air/water around, or extract heat from air/water to move it elsewhere. These things all need energy. But a computer … all it does is move electrons around! All the information in a computer that changes is just electrons moving; that should not need so much power, should it?

As it turns out, energy-information equivalence theories posit that manipulating information does increase entropy which does involve energy—but this is the Layman’s Guide to Computing, not a physics newsletter. Let’s just say that managing information, in its abstract sense, needs very little energy.

## Energy usage in computers

What happens to all the energy that a computer uses, then? Some miniscule amount of it goes to manipulating information. A tiny amount goes to lighting up LEDs (these devices somehow always have LEDs), and maybe running the cooling fans. The rest of it is wasted as **heat**.

The history of computing is also a history of less and less wasted heat. The Cray 2 supercomputer, in 1985, needed 195 kW to produce 1.9 gigaflops (1.9 billion **fl**oating-point **o**perations **p**er **s**econd; more context in [Issue 123]({filename}/season10/issue123/issue123.md))) of computational performance. The iPhone XS, in 2016, needed less than 1 W to produce 1 gigaflop.

No, I’m not going into the environmental concerns and carbon footprint of computing. We have more tangible and immediate concerns here.

Because heat is bad for computers. When microprocessor chips heat up, the semiconductor material they are made of no longer behaves as it should; it gets “leaky”, allowing electrons to go where they shouldn’t. The data it handles starts to get corrupted, and it eventually crashes.

## Thermal throttling

In the past, microprocessors were simpler, and had no thermal controls whatsoever; if you allowed them to run as-is, without any cooling assistance, they would just run until they began smoking and sometimes even catch fire (enjoy this [2005 video of a CPU doing just that](https://www.youtube.com/watch?v=Xf0VuRG7MN4&t=99s)).

Today, CPUs are somewhat more sophisticated. Once they start heating up to their thermal limit, onboard thermal control circuitry will attempt to **throttle** the CPU’s performance to keep it at a safe temperature. So you will have a laggy and unresponsive CPU, but at least it’s not on fire!

Still, most CPUs are going to need some sort of heatsink that helps to draw heat away from it, and dissipate the heat into the surroundings.

## Getting rid of heat

There are two things you need to know about heat loss to the surroundings:

1. The larger the surface area, the faster an object loses heat.
2. The larger the temperature difference between object and surroundings, the faster the object loses heat.

CPUs are kind of at a disadvantage here.

1. They are really small; the part that is in contact with the heatsink is usually about 400 sq mm (approx. 2 cm by 2 cm, or 0.64 sq in)[^1]
2. The thermal limit for most CPUs is only about 100 °C (212 F), compared to most metals which have theirs in the hundreds or even over a thousand °C

[^1]: Multiple CPUs are produced from a single semiconductor wafer. Keeping CPUs small maximises the yield from manufacturing, and reduces the chance of a manufacturing error on any single CPU. This is going to take a whole ’nother season to explain …

## Heatsinks

In practice, this means that a bare chip can only run about 4 W before it starts to run into its thermal limits (we call this **overheating**). Anything more powerful than a basic home router or smart device (such as the Amazon Echo or Google Home Assistant) will need some sort of heatsink to avoid overheating.

The simplest way to cool a chip is to slap a piece of metal on it to increase the surface area (factor 2). This is known as **passive cooling**. A paste called **thermal paste** is applied between the heatsink and chip to improve the transfer of heat. To pack as much surface area as possible into a tiny space, this piece of metal usually has long, thin fins, giving the characteristic look of heatsinks:

![A passive heatsink on a chip]({attach}/season10/issue129/issue129_01.jpg)<br />
<small>A passive heatsink on the northbridge chip of a computer mainboard<br />Source: found on [Superuser](https://superuser.com/questions/1043094/difference-between-active-and-passive-heatsink)</small>

The effectiveness of passive heatsinks depends on the ambient airflow around it. Some creative setups that manage to get *the metal case itself* in contact with the CPU can readily cool up to 45 W, with zero fan noise!

For mobile phones, tablets, and laptops, such heatsinks would add too much to the device thickness. Instead, the CPUs are usually in direct contact with a larger metal surface, sometimes even the metal back of the device; this is why they feel warm to you in the first place. This allows tablets to use up to approx. 8 W of power.

![Logic board cover in an iPad]({attach}/season10/issue129/issue129_02.jpg)<br />
<small>The logic board cover in an iPad Pro 11 has copper inside; it helps to spread heat to the rest of the device instead of concentrating it all in one spot<br />Source: [iFixit](https://www.ifixit.com/Teardown/iPad+Pro+11-Inch+Teardown/115457)</small>

Where there isn’t this luxury of space, another option is to use a slim heatsink, and increase its cooling ability by forcing air through it. This form of cooling is called **active cooling**, and usually done with a fan of some sort, a popular option for thicker laptops. This allows laptops to run between 25–45 W, and desktop computers to run 65 W and hotter (with larger heatsinks, of course)

![An active heatsink on a chip]({attach}/season10/issue129/issue129_03.jpg)<br />
<small>An active heatsink on the CPU of a computer mainboard<br />Source: found on [Superuser](https://superuser.com/questions/1043094/difference-between-active-and-passive-heatsink)</small>

These numbers are for stereotypical mobile devices, laptops, and desktops; stranger or hybrid designs may have different cooling capacities (e.g. a tiny cube desktop might only have 25–35 W of cooling capacity).

**Issue summary:** The larger the surface area, the faster an object loses heat. The larger the temperature difference between object and surroundings, the faster the object loses heat. Heat is bad for computers, and CPUs will need cooling to be able to process computations quickly. A mobile phone thus typically uses no more than 4 W of power, a laptop can use 25–45 W, and a desktop can usually use 65 W and more. Two popular ways of increasing the cooling capacity of a device is to attach a larger piece of metal to the chip (passive cooling), or use a fan to force air over the heatsink (active cooling).

If you walk away with only one thing from this issue, it’s that heat dissipation constrains the max performance for any device, and heat dissipation is usually constrained by the surface area available for cooling.

## What I’ll be covering next

**Next issue:** [LMG S10] Issue 130: Power limits

Computers turn electrical power to heat, drawing a miniscule amount off for computation. But where does that power come from? In the last issue of Season 10, I’ll touch on a highly underrated hardware component: the power supply.

This and more, next issue!

**Sometime in the future:** What is:

- XSS? [Issue 8]
- a good reason developers write code and give it away for free online? [Issue 21]
- OpenType? And what are fonts anyway? [Issue 42]

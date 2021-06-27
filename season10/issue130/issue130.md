[**Previously:**](https://buttondown.email/laymansguide/archive/) The larger the surface area, the faster an object loses heat. The larger the temperature difference between object and surroundings, the faster the object loses heat. Heat is bad for computers, and CPUs will need cooling to be able to process computations quickly. A mobile phone thus typically uses no more than 4 W of power, a laptop can use 25–45 W, and a desktop can usually use 65 W and more. Two popular ways of increasing the cooling capacity of a device is to attach a larger piece of metal to the chip (passive cooling), or use a fan to force air over the heatsink (active cooling).

**Point 1:** A powerful device produces lots of heat.  
**Point 2:** A device that produces lots of heat needs a large surface area (directly in contact with the heat source) to stay (relatively) cool.

These are two of the primary factors determining how tiny a computer can be. Can something the size of an iPhone be as powerful as something the size of a Macbook? It depends on how much cooling is available to it!

One more factor to add in this issue: power. Without power, none of your devices would work ... and that is one more source of heat to be dissipated, incidentally.

## Batteries and DC power

Some devices need to carry their own stored energy (in the form of batteries); the devices are powered by direct current (DC) from batteries. In this form of power transmission, electric current only flows one way—this is why it is important to put batteries in the right way! Electric current comes out from one end, and re-enters from the other end, marked with + and – symbols.

Batteries seldom provide power at the voltage required by devices and CPUs. For example, smartphone batteries usually have a voltage of about 3.7 V, even though the CPU usually requires about 1 V to operate. This allows the batteries to power the device with a low current[^1], so as to minimise the heating effect of current in the wires.

[^1]: Power = Voltage × Current, so to provide the same power with a lower current, you have to provide it at a higher voltage

That means some power conversion has to take place on the smartphone’s mainboard. Fortunately, DC-to-DC conversion is highly efficient (though not 100%), so it doesn’t contribute much heat in the device.

## Wall sockets and AC power

On the other hand, alternating current (AC) from wall sockets has electric current flowing both ways—the current switches directions 50 or 60 times a second (see [this PDF of Worldwide AC Voltages & Frequencies](https://www.oaktreeproducts.com/img/product/description/List%20of%20Worldwide%20AC%20Voltages.pdf)). Connecting this directly to a device that needs DC is looking for trouble! This AC power source has to be converted to DC through an **AC-DC converter** (a.k.a. “power brick”, “power supply”, “AC adapter”, …), and that process currently only goes up to 90% peak efficiency[^2].

[^2]: AC-DC converters typically have a range of input power they can convert (e.g. 0–65 W for laptop adapters, 0–500 W for desktops). The efficiency is highest at about 50% of that load, and efficiency drops as the load increases or decreases from that point.

That means if you have a desktop running at 100W (maybe while gaming or encoding video files), the *AC-DC converter alone* draws 111W at the wall socket, **wastes 11W** (in the form of heat), and provides 100W of power to the desktop.

And heat is the enemy of CPUs.

## External vs internal power supplies

Ughh, power bricks … so many different types, with different connectors, and we never quite know if we can use one laptop’s power brick on another laptop (at least, until USB Type-C power for laptops came along; more in [Issue 127](https://buttondown.email/laymansguide/archive/lmg-s10-issue-127-usb-type-c-power-delivery/))

In a laptop, you really do not want the power supply dumping this heat *into the laptop*! The laptop already has enough work to do getting heat from the CPU out of that cramped space into the surroundings. You don’t want to give it more heat to remove, and risk throttling the CPU’s performance ([Issue 129](https://buttondown.email/laymansguide/archive/lmg-s10-issue-129-cooling)). It’s better that the AC converter/power brick remains external to the laptop, dumping that heat into the surroundings directly without heating up the laptop’s internal space.

![An Apple power adapter, with the cover removed](https://raw.githubusercontent.com/ngjunsiang/laymansguide/release/season10/issue130/issue130_01.jpg)<br />
<small>The internals of the Apple AC converter (i.e. power adapter)<br />Source: [Ken Shiriff](http://www.righto.com/2015/11/macbook-charger-teardown-surprising.html)</small>

In larger devices—the Mac Mini, game consoles (e.g. PS4 or Xbox One), and larger desktops, there’s plenty of space in the device’s internals, and they have sufficiently powerful cooling systems that can remove this heat. In desktops especially, the power supply may be large enough that it has its own cooling fan!

![A desktop power supply, with the cover removed](https://raw.githubusercontent.com/ngjunsiang/laymansguide/release/season10/issue130/issue130_02.jpg)<br />
<small>The internals of a desktop power supply.<br />Notice the cooling fan mounted on the back with 4 silver screws, and the two silver heatsinks mounted vertically<br />Source: [Wikipedia](https://en.wikipedia.org/wiki/Power_supply_unit_(computer))</small>

So for large devices, it makes sense to hide the power supply within the device for a sleeker look.

In fact, for high-power devices, a power adapter is a poor option. Since power adapters don’t have their own cooling fans, they have limited cooling ability, and are liable to overheat easily if they have to provide >100 W to a device (remember that this means they release at least 11 W of heat, while passive cooling can typically up to 8 W).

## Device categories

Putting together the information from [Issue 129](https://buttondown.email/laymansguide/archive/lmg-s10-issue-129-cooling) and this issue, we can deduce that devices seem to sort themselves into form-factor categories depending on how much power they draw, and how much heat they put out:

**Devices drawing >100W at peak, and putting out >80 W of heat:**

Generally large, directly powered from the wall (by AC), with power supply within the device.

In rare cases they do use external AC adapters (such as high-power gaming laptops).

**Devices drawing 12–65W at peak, putting out 25–45W of heat:**

These devices cannot be passively cooled, and thus require active cooling (i.e. a cooling fan and heatsink).

To avoid adding heat to the device from the AC-DC conversion process, they usually use external AC adapters.

Even in devices as small as the Nintendo Switch, you can usually spot the cooling vents where the cooling fan blows warm air from the device into the surroundings.

These may be safely powered by USB Type-C.

**Devices drawing <12W at peak, putting out <10W of heat:**

These devices can be passively cooled.

Large devices, such as tablets, have a larger surface area to dissipate heat and can afford to draw as much as 8–10W, while smaller devices such as smartphones typically have to remain under 5W.

These are usually powered by USB (at a voltage of 5V), though some may draw power at 9V.

The M1 Macbook Air is passively cooled and thus in this category because its M1 processor is configured to limit its maximum heat output to approx. 10W or less; the M1 Macbook Pro has a cooling fan and a higher max heat output configuration, which allows it to perform at greater capacity.

<hr />

If you spot a device in the wild that claims to have performance much greater than its form factor—its shape, size, footprint—suggests, you would be wise to suspect over-optimism or a scam! At least until it is clear how they plan to provide that power and get rid of that heat …

**Issue summary:** AC power from the wall uses electric current that alternates directions, while DC power from batteries uses electric current that flows in one direction only. All electronics are DC-only, and require an AC-DC adapter to be powered from the wall. The AC-DC conversion produces a significant amount of heat; AC-DC adapters are usually external unless the device has sufficient space or cooling capacity for it.

I’m noticing a pattern: issues where I explain concepts tend to be shorter than issues where I explain limits due to engineering and the physics of reality. I hope I can shorten the latter without sacrificing practical knowledge. Let me know how you’re finding these issues :)

## What I’ll be covering next

**Next issue:** [LMG S11] Issue 131: What do early CPUs and startup founders have in common?

This season was focused on firmware and computer components; it is part 1 of a set of concepts I need to explain why the Apple M1 processor is a game-changer for personal computers. I explained what a graphics card is and what it does, I explained why some laptops are upgradeable and why some are not, I explained why some devices need cooling fans and others don’t, and I summarised the relationship between device form factors and their power limits.

Part 2 will extend this exploration inside the computer. I noticed that layfolks’ mental concept of a computer typically includes the idea that there is a CPU, memory, a hard disk/solid state disk, and maybe a graphics card inside a computer. That’s plenty good enough for everyday life; it’s like understanding that all the employees of a company are in a particular building. But it is not sufficient to understand *why the M1 is so much faster*; you’re going to need to know where the employees are situated, and what their workflow is like!

It’s a tempting but misleading story to imagine that Apple simply has much better engineers; I would say that their engineers were instead under the influence of incentives that allowed them to imagine a more coherent architecture. Let’s get into it starting next issue, again beginning from first principles: how exactly does the CPU, memory, and storage disk work together?

**Sometime in the future:** What is:

- XSS? [Issue 8]
- a good reason developers write code and give it away for free online? [Issue 21]
- OpenType? And what are fonts anyway? [Issue 42]

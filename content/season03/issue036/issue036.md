Title: Issue 36: Latency
Date: 2019-08-31 08:00
Tags: 
Category: Season 03
Slug: issue036
Author: J S Ng
Summary: 
Modified: 2019-08-31 08:00

Previously: VPNs link devices that are not within the same network using an encrypted tunnel that prevents gateways from snooping on the data packet as it passes en-route.

In the past two issues, I looked at the basics of web filtering: how data packets are detected (by snoopers or gateways), and how they are protected (by encryption).

In the next few issues, I’ll look at speed: what causes internet speed to be slow or fast. This issue, we look at latency.

## Latency

In business, the idea of “turnover time” refers to the amount of time taken to complete a process or fulfill a request. With so many businesses relying on the Internet these days, latency is a big part of this turnover time. Simply put, latency is the time duration between a device sending out a request and the same device receiving a response.

You can see how a long latency will result in long waiting time in an app; if the app has to complete many requests to obtain all the data it needs, it can take a long while before the app is able to even start processing the data, let alone displaying it.

## Internet latency: an illustration

> **ping (n.)**

> 1835, imitative of the sound of a bullet striking something sharply. Meaning “short, high-pitched electronic pulse” is attested from 1943. As a verb from 1855; in computer sense is from at least 1981. Related: _Pinged; pinging._

In WWII, a ping is a sound pulse emitted by submarines to detect other submarines and undersea objects. The sound pulse bounces off hard surfaces, such as the ocean floor, or other submarines, and returns to the submarine as an echo, giving it an audio report of what is around it. The longer the time gap between the ping and its echo, the further away the object is. It is called a ping because, well, it _sounds like a ping_.

An internet ping does not sound like a ping, but it serves a different function through a similar idea. By sending out a data packet to a target server, and measuring the time it takes to get a response, it can “gauge the distance” that the device is away from the target server.

On any laptop, you can measure the latency of any server using a commandline application ([Issue 15]({filename}/season02/issue015/issue015.md))) called `ping`. Here, I will show you the output from `ping` while it pings two different servers.

The commandline prompt in Linux usually starts with a `$`, so any text you see after a beginning `$` in the same line is the command I am using. Everything that follows is the output from the `ping` application. the `-c 20` option tells `ping` to measure the latency statistics from sending 20 packets of data to the specified server.

Compare this:

```
$ ping -c 20 google.com
PING google.com (74.125.24.100) 56(84) bytes of data.
64 bytes from 74.125.24.100 (74.125.24.100): icmp_seq=1 ttl=46 time=19.5 ms
64 bytes from 74.125.24.100 (74.125.24.100): icmp_seq=2 ttl=46 time=37.9 ms
64 bytes from 74.125.24.100 (74.125.24.100): icmp_seq=3 ttl=46 time=40.0 ms
[… TRUNCATED …]
--- google.com ping statistics ---
20 packets transmitted, 20 received, 0% packet loss, time 48ms
rtt min/avg/max/mdev = 19.484/33.354/50.181/7.413 ms
```

with this:

```
$ ping -c 20 baidu.com
PING baidu.com (39.156.69.79) 56(84) bytes of data.
64 bytes from 39.156.69.79 (39.156.69.79): icmp_seq=1 ttl=41 time=329 ms
64 bytes from 39.156.69.79 (39.156.69.79): icmp_seq=2 ttl=41 time=355 ms
64 bytes from 39.156.69.79 (39.156.69.79): icmp_seq=3 ttl=41 time=276 ms
[… TRUNCATED …]

--- baidu.com ping statistics ---
20 packets transmitted, 20 received, 0% packet loss, time 24ms
rtt min/avg/max/mdev = 275.903/340.161/391.440/30.893 ms
```

What we are interested in is the last line. Notice that the average time between a ping packet to google.com and its response packet is 50 milliseconds, while that for baidu.com is 391 milliseconds. That is almost an 8× difference!

What accounts for this difference? Stay tuned for the next issue of Layman’s Guide to Computing! ;)

**Issue summary:** Latency is the time duration between a ping packet being sent out and its response being received. It is an indication of how far away a target server is.

-----

I promised one idea a week, and I am sticking to that promise. Remember how the Internet works: packets being forwarded from gateway to gateway. You can probably guess what might account for the latency difference from this, but I am still saving the juicy details for next issue.

## What I’ll be covering next

**Next issue:** Traceroute – Google Maps for data packets

**Sometime in the future:** What is:

- booting up? [Issue 15]
- a cookie? [Issue 8]
- a cache? [Issue 8]
- XSS? [Issue 8]
- a CDN? [Issue 8]
- Unicode? And what does it have to do with emoji? [Issue 8]
- those '\r\n’s in the HTTP request packet [Issue 12,17]?
- a good reason developers write code and give it away for free online? [Issue 21]
- ASCII? [Issue 23]
- compiling code into an application [Issue 26]?
- firmware? [Issue 34]

Previously: Latency is the time duration between a ping packet being sent out and its response being received. It is an indication of how far away a target server is.

Last issue, we saw that the latency for google.com's servers was almost 8× shorter than that for baidu.com's servers. Let's see why.

## traceroute

I use the commandline application ([Issue 15](https://buttondown.email/laymansguide/archive/lmg-s2-issue-15-sysadmins-and-the-command-line/)) `traceroute` to display the entire route taken by the data packet. The commandline prompt in Linux usually starts with a `$`, so any text you see after a beginning `$` in the same line is the command I am using. Everything that follows is the output from the `traceroute` application. the `-T` option tells `traceroute` to use TCP packets to trace the path of our data packets.

```
$ traceroute -T google.com
traceroute to google.com (74.125.24.138), 30 hops max, 60 byte packets
 1  _gateway (192.168.1.1)  0.971 ms  0.959 ms  0.951 ms
 2  1.128.104.27.unknown.m1.com.sg (27.104.128.1)  4.577 ms  4.579 ms  4.572 ms
 3  43.245.104.65 (43.245.104.65)  3.868 ms  3.865 ms  3.854 ms
 4  5.246.65.202.unknown.m1.com.sg (202.65.246.5)  6.396 ms  3.829 ms  3.799 ms
 5  37.246.65.202.unknown.m1.com.sg (202.65.246.37)  18.766 ms  18.761 ms  5.129 ms
 6  134.246.65.202.unknown.m1.com.sg (202.65.246.134)  8.222 ms 221.246.65.202.unknown.m1.com.sg (202.65.246.221)  3.928 ms  3.901 ms
 7  72.14.222.102 (72.14.222.102)  3.882 ms  3.705 ms  3.661 ms
 8  209.85.243.27 (209.85.243.27)  3.621 ms 74.125.252.107 (74.125.252.107)  4.638 ms 72.14.238.42 (72.14.238.42)  4.621 ms
 9  108.170.254.227 (108.170.254.227)  4.180 ms 108.170.240.241 (108.170.240.241)  4.071 ms 108.170.240.242 (108.170.240.242)  4.059 ms
10  72.14.236.242 (72.14.236.242)  4.882 ms 216.239.57.50 (216.239.57.50)  4.771 ms 216.239.50.192 (216.239.50.192)  5.476 ms
11  72.14.233.43 (72.14.233.43)  9.760 ms 72.14.233.27 (72.14.233.27)  4.700 ms  4.665 ms
12  * * *
13  * * *
14  * * *
15  * * *
16  * * *
17  * * *
18  * * *
19  * 74.125.24.138 (74.125.24.138)  4.572 ms *
```

Wall of numbers and text! Whoa, scary! It’s all right, I’ll throw that output into Google Sheets and prettify it a bit:

<span style="text-align:center">
![prettified traceroute output for google.com](https://github.com/ngjunsiang/laymansguide/blob/master/season3/issue037/issue037_01.png?raw=true)<br />
The traceroute output for google.com, prettified
</span>

`traceroute` sends 3 TCP packets, tracing the path they take to the destination IP address. Each time the data packet gets forwarded to another gateway, it is considered a ‘hop’. `traceroute` helps to do a **reverse DNS lookup**; a DNS query is when you want to find out the IP address associated with a hostname, a **reverse DNS lookup** helps you find out which hostname is associated with an IP address. IP addresses with successful reverse DNS lookups have the hostname shown; those that didn’t will have only the IP address shown. Some servers are configured to block `traceroute` packets (done by the [firewall](https://buttondown.email/laymansguide/archive/lmg-s3-issue-34-firewalls/)), and thus return no information; these are represented by asterisks (`*`) in the output.

As the data packets are sent from my router (`_gateway` in the output) to the first ISP gateway (`27.104.128.1`), they don’t always take the same path. Some of the internet servers along the path are programmed with algorithms that will send the data packets to a group of servers. This group of servers are configured to work together to share the packet-routing load. Two data packets sent through the same internet server may end up getting routed to different places along the route.

Notice that each hop has a latency associated with it. This is the time taken for the server to decode the packet, figure out what is the next destination, and send it forward. This will often not happen immediately. The data packet joins a queue of other data packets waiting to be dispatched; when the server is under a heavy load, with many data packets waiting to be dispatched (perhaps a whole deluge of Google searches are happening), the waiting time can rise to hundreds of milliseconds or even a few seconds! (Simply unbearable …)

Let’s look the `traceroute` output for baidu.com:

<span style="text-align:center">
![prettified traceroute output for baidu.com](https://github.com/ngjunsiang/laymansguide/blob/master/season3/issue037/issue037_01.png?raw=true)<br />
The traceroute output for baidu.com, prettified
</span>

Notice that:

1. More of the servers along the way are `traceroute`-friendly
2. The data packets take fewer hops to reach baidu.com …
3. But they take longer, because some of the servers along the way have really high latency (almost 300 milliseconds; that’s slower than human reaction time)
4. My ISP is M1, but sometimes the packets can go through other ISP servers as well (hop 7)

And that, in two images, is why Baidu’s latency is so much higher: the latency for some of their servers is much higher.

**Issue summary:** The process of forwarding data packets from server to server takes time. Each hop a data packet takes adds to the latency. The more hops a packet must undergo, the longer the latency. The slower the servers along the route, the longer the latency as well.

<hr/>

I didn’t have much writing space (or readers’ mind space, I wager) to show what the entire route of a data packet looks like when I was describing how the Internet (and packet routing) works. I hope this big-picture post puts everything into clearer perspective now :)

We’ve looked at how data packets weave their way through the Internet, and next issue I want to shed some light on when/how data packets are sent.

## What I’ll be covering next

**Next issue:** Loading a web page

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

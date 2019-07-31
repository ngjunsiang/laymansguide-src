Previously: The devices on your home network share the single ISP-assigned IP address through your router. The router rewrites the source IP and port number on outgoing data packets, and rewrites the destination IP and port number on incoming data packets, acting as a middleman for your devices so that they can access the Internet.

In Issue 32, when I was explaining Network Address Traversal (NAT), I mentioned this:

> Another of those things is that TCP will give the request a port number. Yes, you might have heard this term when configuring routers. We won’t need to discuss port numbers yet, so let’s put that aside.

And then I went on the explain how the source and destination IP addresses are tagged on through the Internet Protocol (IP).

Well, now is the time to talk about what’s going on through the Transmission Control Protocol (TCP). Within a single device, you often have different software services running:

1. DNS querying ([Issue 29](https://buttondown.email/laymansguide/archive/lmg-s3-issue-29-how-to-resolve-a-hostname/))
2. Internet time synchronisation (over the Network Time Protocol)
3. Software updaters checking for updates online
4. Skype/Zoom/videoconferencing
5. Instant messaging
6. Web browsers
7. Others . . .

When a data packet comes in through the network chip and arrives at the operating system (OS), how does it know which software app to forward the data packet to?

## Port numbers

When a software app needs to send a request or some data through the Internet, it has to go through the OS. The OS decides which software gets to use the Internet, and which ones don’t (that is what your firewall is for). If a software app has permission to access the internet, it requests a **port number** from the OS. The OS assigns the app a port number, and stores information about which application is mapped to which port number.

When the software app sends data to the OS to be sent out via the network, the OS adds identifying information, including the source and destination port number, as part of TCP. Then the OS sends the resulting data packet to the network card to be forwarded to the gateway (via your LAN cable or wifi connection). The network card then adds the source and destination IP address information (and other identifying information) as part of IP, creating a larger data packet (which at this point is app data inside a TCP shell inside an IP shell ... like a Matryoshka doll).

```
Request #4676 to host
Source IP:        *27.104.229.65*
Source Port:      *45784*
Destination IP:   172.217.26.78
Destination Port: 80
```

When response data is returned, the OS checks the destination port number, looks up its list of assigned ports, and forwards the data to the correct app. Cycle complete!

```
Request #4676 from host
Source IP:        172.217.26.78
Source Port:      54674 (random port from host)
Destination IP:   27.104.229.65
Destination Port: 45784
```

Just like there is a source and destination IP address, there is also a source and destination port number. The source port number is the assigned port number from the OS. The destination port number, well ... how are we to know that?

## Reserved port numbers

With so many types of data being transferred over the Internet, how do things not get mixed up?

Reserved port numbers is how. The well-known internet traffic data types have standardised protocols: web traffic follows HyperText Transfer Protocol (HTTP - [Issue 7](https://buttondown.email/laymansguide/archive/lmg-issue-7-what-is-http/)), some types of file transfer occur in accordance with the File Transfer Protocol (FTP), DNS queries obey the DNS protocol, etc.

These well-known protocols are assigned standard port numbers by IANA, the same authority that manages known IP addresses. HTTP uses port 80. FTP uses port 20 (data transfer) and 21 (control). DNS uses port 53. You can find the [full list of well-known port numbers on Wikipedia](https://en.wikipedia.org/wiki/List_of_TCP_and_UDP_port_numbers). Port numbers 1 to 1023 are reserved for this purpose and may not be used publicly for other purposes.

If your app is trying to query a hostname to get the associated IP address, the destination port number is 53. The app simply uses the standard port number depending on what service it is trying to use, and which protocol it is following. If your app is trying to request data from a web server, the destination port number is 80; your web browser actually requests https://google.com:80 but it will leave out the port number if it is a standard port number. You can also try requesting https://google.com:8000 but you won't get any data in return since nothing is listening on that port number at Google's end.

Web servers will (by default) listen on port 80, FTP servers on port 21, DNS servers on port 53, and so on. Any traffic arriving with those port numbers will be directed to these (software) servers for processing.

## Registered port numbers

Port numbers 1024 to 49151 are available for organisations, corporations, and other corporate bodies to request if they are setting up widespread area services. Whatsapp uses ports 4244, 5222, 5223, 5228, 5242. Apple uses port 5223 for push notifications. Google Play uses port 5228 for messaging. This makes it possible for these services to work without knowing what the port numbers of the software apps on the receiving end are mapped to.

## Private port numbers

Port numbers 49152 to 65535 are available for anyone to use. Tinkerers, hackers, anyone who just needs a number to send data from.

... and that’s a wrap. Source and destination IP addresses get data to the right computers, source and destination port numbers get data to the right apps in those computers.

**Issue summary:** When an app makes a network request through the OS, the OS adds the source and destination port number to the query in accordance with TCP. When the OS receives the response, it forwards the data to the app which is mapped to the destination port number. Port numbers 1-1023 are registered to standard Internet services, port numbers 1024 to 49151 may be registered to other services, and port numbers 49152 to 65535 may be used by anyone.

<hr/>

Short and sweet! Issues 30-33 are my summary of how data packets find their way across the internet (via IP addresses) and to the right apps (via port numbers). It’s amazing that this is basically how almost all Internet traffic gets routed; the rules are simple and hence very scalable, you don’t need massive computation to get packets to the right places (but you do need massive hardware to process lots of packets quickly).

In the next few issues, I’ll go into some security and performance considerations for internet traffic: VPNs, traffic blocking, and internet speeds.

## What I’ll be covering next

**Next issue:** VPNs: Virtual Private Networks

**Sometime in the future:** What is:

- booting up? [Issue 15]
- a cookie? [Issue 8]
- a cache? [Issue 8]
- XSS? [Issue 8]
- a CDN? [Issue 8]
- Unicode? And what does it have to do with emoji? [Issue 8]
- those '\r\n's in the HTTP request packet [Issue 12,17]?
- a good reason developers write code and give it away for free online? [Issue 21]
- ASCII? [Issue 23]
- compiling code into an application [Issue 26]?

[LMG S3] Issue 35: Virtual Private Networks

Previously: Port numbers are assigned by the OS to apps that request one. Data packets sent by the OS through the network card have the port number appended in accordance with TCP. The port number allows the OS to identify data packets that should go back to the app. Port numbers 1-1023 are registered to standard Internet services, port numbers 1024 to 49151 may be registered to other services, and port numbers 49152 to 65535 may be used by anyone.

Thus far, our picture of networks divides them into public networks (consisting of devices with public IP addresses) and private networks (devices with private IP addresses). Data traffic between devices in the same private network goes through their common gateway without getting forwarded to the rest of the internet. This data traffic cannot be snooped by outsiders who are not in that network. Theoretically, data within this private network is secure; you can do network printing or share files with other computers within your private home network and know that nobody outside of that network will inadvertently receive a leaked data packet.

What if you’re out but desperately need to access a file on your home shared network? Or you’re out of the office but need to send a print job to the office printer? (I leave it to you to imagine more plausible scenarios; I’m just trying to explain when you might want a VPN :P)

You would want some way for your computer to be able to access that private home/office network, but you can’t do it through a public gateway: that would compromise data security, since packets travelling through the Internet from the private network to your computer can be intercepted by other devices along the way.

You need a . . .

## Virtual Private Network (VPN)

A Virtual Private Network (VPN) is a way for devices that are not in the same private network to **behave as though they are**. This network consists of a VPN server, and one or more VPN clients. The VPN server acts as a DHCP server for the clients, assigning them a private IP address for the VPN. This allows devices within the VPN to communicate with each other, regardless of location.

How is data prevented from leaking outside of the VPN then? By encryption (which we won’t go into the technical details of in this issue). Data travelling between VPN clients is encrypted before being sent out, and decrypted when it arrives. Anyone snooping on the packet contents as it travels gateway to gateway will just see encrypted jumble.

**Issue summary:** 

<hr/>



## What I’ll be covering next

**Next issue:** VPNs: 

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

Previously: Firewalls block data packets that match certain rules. They decrypt the data packet layer by layer, dropping those that match its programmed rules without allowing them to be forwarded to the next point in its journey. The type of filtering that can be applied depends on the processing power available to the router, since some information is hidden more deeply in the data packet than others. Such filtering is typically circumvented by the use of VPNs, or other means of encrypting the data that is required.

Thus far, our picture of networks divides them into public networks (consisting of devices with public IP addresses) and private networks (devices with private IP addresses). Data traffic between devices in the same private network goes through their common gateway without getting forwarded to the rest of the internet. This data traffic cannot be snooped by outsiders who are not in that network. Theoretically, data within this private network is secure; you can do network printing or share files with other computers within your private home network and know that nobody outside of that network will inadvertently receive a leaked data packet.

What if you’re out but desperately need to access a file on your home shared network? Or you’re out of the office but need to send a print job to the office printer? (I leave it to you to imagine more plausible scenarios; I’m just trying to explain when you might want a VPN :P)

You would want some way for your computer to be able to access that private home/office network, but you can’t do it through a public gateway: that would compromise data security, since packets travelling through the Internet from the private network to your computer can be intercepted by other devices along the way.

You need a …

## Virtual Private Network (VPN)

A Virtual Private Network (VPN) is a way for devices that are not in the same private network to **behave as though they are**. This network consists of a VPN server, and one or more VPN clients. The VPN server acts as a DHCP server for the clients, assigning them a private IP address for the VPN. This allows devices within the VPN to communicate with each other, regardless of location.

How is data prevented from leaking outside of the VPN then? By encryption (which we won’t go into the technical details of in this issue). Data travelling between VPN clients is encrypted before being sent out, and decrypted when it arrives. Anyone snooping on the packet contents as it travels gateway to gateway will just see encrypted jumble. That means firewalls won’t be able to identify the information it needs to block data packets, and the data packets thus usually get through unmolested.

**Issue summary:** VPNs link devices that are not within the same network, such that they can behave as though they are. By encrypting the packet data before it is sent between devices, the VPN software hides these packets from being snooped (i.e. spied upon), effectively forming an encrypted tunnel for information to travel between devices. This enables devices to circumvent firewalls and protect the privacy of information in the data packets.

<hr/>

Last issue was firewalls, this issue is VPNs. You’ll notice that the more advanced the technology, the shorter my posts. That’s because I have already laid out most of the framework for understanding the Internet infrastructure in the issues leading up to these two.

That’s part of the beauty of the Internet: understanding its basic pieces gives you a pretty good picture that helps you understand most of what’s happening in Internet-related news today. But that’s also the difficulty: finding all the information put together in a coherent, easy-to-read way that actually lays out the picture helpfully. I hope this newsletter has largely succeeded in doing that. If it has not, please let me know where it fell short, and how I might improve it :)

## What I’ll be covering next

**Next issue:** Latency

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

[**Previously:**](https://buttondown.email/laymansguide/archive/) Actually making a web application requires you to set up lots of supporting software and carry out lots of steps to create a suitable app environment.

Last issue, I described the whole host of things that need to be done just to make a web application work on another server, different from where you did your programming.

How do people deploy web services so quickly if there is so much tedium involved?

## Birth of the Cloud

You could set up the environment, containerise it, and deploy it through a container … that’s one way to solve for distribution.

But somebody smart realised that this is likely a common problem. 99%[^1] of applications are going to need the same building blocks: one or more databases ([Season 7]({filename}/season7/issue079/issue079.md

[^1]: Illustrative but not accurate estimation!

All these pieces must themselves run on a machine (physical or virtual). The hardware, the network resources, the type of database, the type of storage, … these are usually not key differentiators for the business. They do not derive their business value by managing it differently from other companies.

Amazon was the first to realise that whatever they were doing to scale Amazon’s business globally, their competitors and other businesses would eventually need as well.

## The Cloud is born

The Cloud is a collection of services that can be plugged in to an application, in lieu of writing your own code. Instead of implementing your own storage server, you could use Google Cloud Storage, or Amazon S3, or Microsoft Azure Storage, etc. You access these and other services typically through a web API ([Issue 4]({filename}/season1/issue004/issue004.md

![screenshot of Google Cloud Storage’s web interface]({attach}issue153_01.png)  
<small>Google Cloud Storage web interface</small>

Besides virtual machines ([Issue 147]({filename}/season12/issue147/issue147.md

![Google Cloud Storage’s main cloud offerings]({attach}issue153_02.png)  
<small>Google Cloud main offerings</small>

Here are Google’s mainstay offerings:

- Compute Engine: virtual machines
- App Engine: a pre-configured, setup-free virtual machine that runs code which you upload, through a web API or their web interface
- Kubernetes Engine: a hypervisor ([Issue 148]({filename}/season12/issue148/issue148.md
- Cloud Storage: a storage service for files (see earlier screenshot)
- Cloud SQL: a relational database service ([Issue 87]({filename}/season7/issue087/issue087.md
- Cloud Bigtable: a NoSQL database service ([Issue 90]({filename}/season7/issue090/issue090.md

Then there are variants for running big data queries, using machine learning nodes, and rebranded services for running the backends of mobile apps, … the key common factor here is that using these services is much simpler than rolling and maintaining your own version![^2] And it lets you speed up development by not having to reinvent the wheel that cloud services have implemented for you.

[^2]: Provided your use case is in the 99-percentile! If yours is an edge case, you might find that rolling your own version is better value for money in the long run.

## The Cloud grows

As web applications got larger and larger, beyond the capacity of even a single high-end server to manage, they had to be redesigned so that they could run on multiple servers while maintaining data synchronicity. As businesses standardise on ways to do that, cloud providers add these tools as part of their offerings.

For example, sending/receiving messages between servers is a key engineering problem. Data packets sometimes get dropped en-route, or when a server gets overloaded. Sometimes they get held up at a server, time out, and then they get resent by the client ([Issue 9]({filename}/season1/issue009/issue009.md

If you don’t want to write your own software for managing communication between servers, the cloud lets you write code for your machines to communicate easily, without having to crack your head thinking about how to make it happen.

**Issue summary:** The cloud offers standard digital business services, accessible through a web interface and API, which any developer (with a credit card) can use. Developers don’t have to reinvent the wheel, so long as they know how to use web APIs.

There is, of course, much more to developing an application than just gluing services together. For commercial applications, you still have compliance requirements, logging, monitoring, and other things to set up. But these are not new needs, and not really worth going into detail in a layman’s newsletter.

I hope the gist of what the cloud does is at least clearer!

## What I’ll be covering next

**Next issue:** [LMG S12] Issue 154: Emulation

I am done with virtualisation and the cloud at this point. You’ve learned about hardware virtualisation (through drivers), system virtualisation (through system VMs), process virtualisation (through process VMs), and service virtualisation (through APIs) so far this season.

I’m going to use the last three issues to talk about a related and current thing: instruction translation and emulation. Let’s start with a question: How is the Apple M1, an ARM chip, able to run MacOS programs compiled for the Intel x86-64 chips? Aren’t they two very different instruction sets ([Issue 53]({filename}/season5/issue053/issue053.md

Yes, yes they are. More next issue ;)

**Sometime in the future:** What is:

- XSS? [Issue 8]
- OpenType? And what are fonts anyway? [Issue 42]

Title: Issue 12: What is HTTPS? How is it different from HTTP?
Date: 2019-03-01 08:00
Tags: 
Category: Season 01
Slug: issue012
Author: J S Ng
Summary: 
Modified: 2019-03-01 08:00

Was the last issue too scary? I hope you haven’t completely lost faith in protecting your privacy on the internet! If you’re close to it, let this issue bring you some hope.

We are going to get a little technical here, because I want to give you a view of the internet that most layfolks won’t get a chance to see. I just want you to remember something: you don’t need to understand every single bit of it. The things I point out will help you come to useful realisations that help you make good decisions about what you do on the internet.

-----

## What did the laptop say to the access point?

[Insert screenshot of random letters and numbers here ... :D]

Nah, I won’t do that. It would be merely decorative and not at all illustrative. Instead let’s focus your attention on one particular packet:


![An HTTP request captured in Wireshark showing my developer API key]({attach}/season01/issue012/issue012_01.png)  
*An HTTP request captured in Wireshark. Notice the line `Authorization: Bearer [CENSORED]`. That’s my developer API key!*    


This screenshot comes from an app called Wireshark, used to “capture” packets received by my laptop. This includes packets that my laptop sends to and receives from the access point, but it also includes packets from surrounding devices, such as my robot vacuum, smartphone, home electricity monitor … let’s see what information is visible from these captured packets. (I say “capture” because I haven’t trapped the packet at all, and other devices connecting to the same access point can read the packet as well.)

It took some filtering and digging, but I’ve finally found the HTTP request data packet which my laptop sent to the server. It’s the right packet; the request is `GET /api/profile HTTP/1.1` like we saw in Issue 7. What are those \r\n’s? Not important for now, we’ll eventually get to those sometime.

Look what else is visible there: my developer API key! Look for the line that starts with `Authorization: Bearer [CENSORED]`. Even though the API key appears to be hidden in the request header, any device that receives the packet and decodes the header can actually receive my API key, and the user can use it to retrieve my profile data if they know how to :( Or worse, they can intercept the packet, modify the header, and send it to the Hypothes.is server, which will think it is coming from me!

## HTTPS to the rescue

Since wifi works by broadcasting the data packets, I can’t possibly stop other devices receiving my data. How do I protect my identity and prevent other people stealing my API key then?

The same way we prevent people who can overhear us from understanding what we are saying: by speaking in code.

How will the server know what I am saying then? The server and my laptop will need to coordinate a way of speaking in code so that any information that is intercepted will make no sense to the interceptor, and if the data is modified by them, my laptop or the server would know when trying to decode the data. These are called cryptography methods, and we will not go into more detail than that for this issue.

That means we need a slightly different set of rules, that enable us to coordinate such cryptography. This is where HTTPS comes in.

## What is HTTPS?

HTTPS stands for **HTTP Secure**. Why is it secure? I think a screenshot will make it clear. This is a screenshot from Wireshark again, but this time capturing an HTTPS request packet:


![An HTTPS packet in Wireshark, with the packet data encrypted]({attach}/season01/issue012/issue012_02.png)  
*An HTTPS request captured in Wireshark. Notice that the packet header data is now encrypted, and an app would need to know the prearranged encryption code to be able to decode the data.*    


The `Authorization: Bearer` line is no longer visible; in fact, all the information we saw in the HTTP packet is no longer visible. It has all been encrypted! Any third party intercepting this packet will not be able to decode or modify it without knowing the encryption code that was prearranged between my laptop and the Hypothes.is server.

-----

## HTTP considered harmful

In a more innocent time, it was perfectly all right for passwords to just be sent unencrypted, and for anything and everything to use HTTP. Online shopping wasn’t even a thing then, and there was no financial value to anything that happened on the internet. Hard to believe, I know.

It is now the year 2018. That is no longer the case. We transmit all kinds of valuable data over the internet: financial transactions and credit card details, home addresses and email addresses and passwords, even pictures. If you are using HTTP, any data you send or receive is being broadcast unencrypted. If you are just browsing and not transmitting critical data, that is fine. But you are really much, much safer using HTTPS.

Issue summary: HTTPS encrypts the request or response header and body, ensuring that anyone trying to intercept it will not be able to decode the data without knowing the encryption code. It is much safer to use HTTPS in general to protect your personal data from being snooped.

## What I’ll be covering next

**Next issue:** How do I use HTTPS?

**Sometime in the future:** What is:

- a specification? [Issue 6,8]
- a cookie? [Issue 8]
- a cache? [Issue 8]
- XSS? [Issue 8]
- a CDN? [Issue 8]
- Unicode? And what does it have to do with emoji? [Issue 8]
- What are those ‘\r\n’s in the HTTP request packet [Issue 12]?

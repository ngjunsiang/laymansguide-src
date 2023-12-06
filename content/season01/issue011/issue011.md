Title: Issue 11: How does wifi work?
Date: 2019-02-23 08:00
Tags: 
Category: Season 1
Slug: issue011
Author: J S Ng
Summary: 
Modified: 

In the last issue, I showed you how I create HTTP requests with custom headers. I put my developer API key in the request header and Hypothes.is gave me a response containing my profile data.

Let’s do a perspective change. Zoom out, out of the computer. Where does my request go? Obviously it has to get out of my computer and get to the server. My laptop’s wifi chip turns the request from an electrical signal into electromagnetic waves, which are broadcasted to the nearest wifi access point, which converts it back to an electrical signal and sends it on its way to the rest of the internet.

Pause that picture for a while. How does my laptop know which access point to send the request to? How does the access point know, from among a bunch of laptops in the vicinity, which laptop to return the response to? (This is becoming quite a disturbing pattern of questioning isn’t it.)

**Short answer:** my laptop doesn’t know! Neither does the access point!

**Long answer:** When you tune in to the radio and get an FM signal, do you ever wonder how the radio broadcast station knows which radios to send the signal to?

Silly question isn’t it? It doesn’t send the signal, it **broadcasts** the signal. That means the signal is simply sent out in all directions from the wifi antenna, like someone shouting aloud or like a lighthouse spreading light all around.

That is how wifi works too. More shocking news: unlike radio, wifi works on the same two frequencies: 2.4GHz and 5GHz. That means that everything you are sending via wifi can actually be picked up by other wireless devices in the vicinity.

Your signals not only can be picked up, they **are** picked up by other devices. Remember: those other devices have no way of telling beforehand which signals are from you, and which ones are from the access point! They would have to receive the signal, decode the request (or response), look at the metadata information that is provided about the data packet, and then determine if it is actually for them. Think of it as a shared data mailbox where everyone can see everyone else’s data packets.

-----

Okay, take a deep breath, control your breathing first … feeling better? Good. So you heard the bad news: all your data is being broadcasted in the open, for anybody with a wifi antenna to receive. Now for some good news.

Wifi was introduced in 1998 and has been around for 20 years. In those 20 years, someone must have thought about this, realised “oh man, this is actually a really bad idea”, and did something about it, right?

Yep! The answer to this problem is HTTPS.

-----

Issue summary: wifi broadcasts your data in the open. Any device with a wifi antenna receives your data packets, but normally does not decode it unless it is meant for them. This may seem to be a security risk, but measures have been developed and implemented to keep your critical information secure. HTTPS is one such measure.

## What I’ll be covering next

**Next few issues:** What’s the difference between HTTP and HTTPS?

**Sometime in the future:** What is:

- a specification? [Issue 6,8]
- a cookie? [Issue 8]
- a cache? [Issue 8]
- XSS? [Issue 8]
- a CDN? [Issue 8]
- Unicode? And what does it have to do with emoji? [Issue 8]

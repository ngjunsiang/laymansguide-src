Title: Issue 10: How do websites actually know if you are really you?
Date: 2019-02-16 08:00
Tags: 
Category: Season 1
Slug: lmg-issue-10-how-do-websites-actually-know-if-you
Author: J S Ng
Summary: 

**Short answer:** They actually don’t. This is not a snarky answer; it is true! Think about it. When the server receives a request, it has no idea if it’s coming from real-you, or someone pretending to be you. All it knows is your IP address, your user agent, and your request. And all three can actually be spoofed (but we won’t go into detail here).

**Long answer:** We have a long and complicated system of verifying that the person making the request really owns the account and it is called … the login.

Logins depend on what is known in cryptography as a **shared secret**. A shared secret is a piece information that only you and the server know, and no one else is supposed to know it. If you are able to provide that shared secret, it is probably safe to assume that you are … really you (hopefully?).

When I first access the Hypothes.is API, the Hypothes.is server has no way to know that I am the user whose username is “kureshii”. Even if I declare that I am kureshii, the server has no way to know I really am kureshii—anybody could say that! So when I request a profile, it returns me the default public profile:

```
https://hypothes.is/api/profile (without custom header)
{
  "userid": null,
  "groups": [
    {
      "public": true,
      "name": "Public",
      "id": "__world__"
    }
  ],
  "authority": "hypothes.is",
}
```

I need to submit a shared secret in my request to let the server know, “hey, I really am kureshii! Look, this is the shared secret which you gave to me when I set up my account”.


![Screenshot of the Hypothes.is developer page providing a developer API key]({attach}/season1/issue010/issue010_01.png)
<small>The shared secret I share with the Hypothes.is server: my developer API key</small>


How do I put that shared secret in the header? I could write a few lines of code in Python, a programming language … but I found an online API tester, which makes my life a bit easier. I just need to fill in the appropriate text fields:


![Screenshot of the API tester]({attach}/season1/issue010/issue010_02.png)
<small>The API tester makes it really easy for me to create and send HTTP requests with customised headers</small>


When the server receives the header with my developer API key, it can verify that the key is correct, and hence give me my profile data.

```
https://hypothes.is/api/profile (with custom header)
{
  "user_info": {
    "display_name": "JS Ng"
		},
	"preferences": {},
	"groups": [
	  {
		  "public": true,
			"name": "Public",
			"id": "__world__"
		}
	],
	"userid": "acct:kureshii@hypothes.is",
	"authority": "hypothes.is"
}
```

That’s pretty cool, right? Only people who know my developer API key and provide it in the header are able to access my profile data. And thankfully I’m not some kind of bigshot whose shared secrets are coveted by many … but does that mean this shared secret is safe? As my web browser, the client, sends this request, it passes through many digital hands. The first step is making it out of my laptop to the nearest wifi access point.

In the next issue, I’ll tell you some things about how wifi works which I hope will make you pause and think about this more carefully.

## What I’ll be covering next

**Next few issues:** How does wifi work? What’s the difference between HTTP and HTTPS?

**Sometime in the future:** What is:

- a specification? [Issue 6,8]
- a cookie? [Issue 8]
- a cache? [Issue 8]
- XSS? [Issue 8]
- a CDN? [Issue 8]
- Unicode? And what does it have to do with emoji? [Issue 8]

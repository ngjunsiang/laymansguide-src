[**Previously:**](https://buttondown.email/laymansguide/archive/) By not enforcing strict cookie policies on their own sites, publishers allowed advertisers to sneakily set cookies on their site audience. This allowed advertisers to reach the same audience via their advertising slots on other websites, which could be bought more cheaply. The publishers were cut out of the value chain and were not longer “gatekeepers” to their own site readers. They could not sell their advertising slots at a premium.

## First-party cookies

Almost every site that needs to “remember” who you are will set cookies on your browser. The reasons for doing so can range from simply remembering that you are not new to the site and don’t need to be reminded to subscribe to their promotional newsletter, to giving you a login cookie so that the site knows you are logged in. (This cookie gets removed when you log out, which is why clearing cookies automatically logs you out of most sites.)

The site publisher sets these cookies via scripts that are often hosted on the same URL. Since cookies are tagged by URL domain, these cookies will have the same domain as the site. These are **first-party cookies**. Blocking these will result in internet-wide breakage, particularly the large majority of login mechanisms.

## Third-party cookies

On the other hand, if the site uses a script from another domain, and this other-domain script sets a cookie, that cookie will have a domain tag that is not the same as the site URL domain (e.g. huffpost.com using a script from an advertiser that sets an advertising cookie, which will not have huffpost.com as its domain). These cookies are known as **third-party cookies**.

These cookies enable advertisers and data-mining companies to track you across websites. Any website you visit which is running their script can retrieve these cookies and send the cookie information back to their servers. This is known as **cross-site tracking**.

A simple way to block pretty much all cross-site tracking is to block third-party cookies. But this also causes other problems, as I will explain below.

## Software-as-a-Service needs third-party scripts

There was once a time when sites took it upon themselves to run all the services they needed. Login, authentication, database management … everything was handled on the server, by scripts that originated on the same server. first-party everything.

As sites grew more complex, Software-as-a-Service (SaaS) companies grew to provide more specialised services involved in the running of such sites. Companies cropped up offering off-site databases, login servers, and all manner of services. That means that when users visit your site, the browser downloads the SaaS company’s script, which carries out the task for you.

For example, Google’s reCAPTCHA service lets you add a CAPTCHA to your site. A CAPTCHA is a test that humans are supposed to pass and bots (automated scripts) are supposed to fail: usually some image recognition-based task such as “identify all buses” or “identify all traffic lights” or “type the letters you see”. The code involved in carrying this out is not simple, and most sites are not capable of running the full backend required to make it work. So they embed a reCAPTCHA script from Google on their site, let the script verify that the user is a human, and then carry on as usual.

However, the Google reCAPTCHA script sets and retrieves cookies. (I am guessing it probably sends your Google cookie to its servers to look up your online history and determine if you are malicious or not.) Since the script originates from Google and not from the website itself, the browser considers it a third-party cookie. Disabling third-party cookies will also cause reCAPTCHA to fail, resulting in a non-functional login for the site.

## Cookie categories

For this reason, cookie policies often differentiate between cookie categories:

1. Session cookies  
   Cookies that are set **for that browsing session only**. These cookies are removed when the browser window is closed. These cookies may be used to remember your progress in a multi-step transaction, e.g. doing a multi-page survey.

2. Persistent cookies  
   These cookies last beyond the current browsing session, and normally terminate after a pre-defined period of time (I often see “1 year” as a default value of sorts, although it can even be set to 30 years!)  Such cookies are used to remember the state you left a service in (e.g. what you have in your shopping cart, even if you didn’t log in or create an account).

3. Strictly necessary cookies  
   (Subjectively) necessary cookies for legal compliance or other reasons, for example implementing parental controls, or internal analytics (tracking most-visited pages, or visit frequency).

4. Functional cookies  
   Cookies set for the intent of enabling site functionality, e.g. remembering preferences and settings.

5. Performance cookies  
   Cookies that enhance the website’s performance, not always what you think that means. For example, if the website is trying out a new feature, they may do A/B testing, giving one cohort of users the “A” interface and another cohort the “B” interface. Which cohort you are in is decided at random, and remembered with a performance cookie.

6. Advertising cookies  
   Just explained in Issues 73 and 74.

## Caveats

I think it is only responsible for me to point out here that the above categorisation is not exactly enforced by law, and nothing stops a company from miscategorising their cookies so as to mislead a user into enabling them. For instance, some sites may categorise a cookie for tracking identity as a functional cookie, justifying it by claiming it as part of their security measures, and thereby require the user to enable third-party functional cookies before they are able to use the site.

## Objections to internet-wide disabling of third-party cookies

It would come as no surprise that ad companies object to such measures, claiming it will “hurt the user experience”, “sabotage the economic model for the Internet”, and “disrupt the valuable digital advertising ecosystem that funds much of today’s digital content and services”. (The quoted parts come from an [open letter from the Digital Advertising Community to Apple Inc.](https://www.patentlyapple.com/patently-apple/2017/09/ad-groups-send-an-open-letter-to-apple-objecting-to-the-new-intelligent-tracking-prevention-setting-in-safari.html))

Other websites have chimed in with the above concerns about disrupted provision of third-party services (X-as-a-Service providers e.g. Software-as-a-Service especially). Right now the shakeout is happening, with the browsers working out an alternative to third-party cookies, software service providers working out alternatives to cookies for providing services, and ad companies finding more subtle ways to track users. It remains to be seen what the Internet will be using in the next 5 years.

**Issue summary:** Cookies with the same domain as the site are first-party cookies, while cookies with domains different from the site are third-party cookies. Cookies are used for all kinds of purposes, from remembering browsing sessions, to logging users in, to tracking their identity across websites. Blocking all third-party cookies indiscriminately can result in most of not all of these functions breaking.

## What I’ll be covering next

**Next issue:** [LMG S6] Issue 77: Wearing clothes on the Internet

Today we wear clothes for all kinds of reasons: to look cool, to cover ourselves up, to feel comfy … but I suppose in more prehistoric times, the primary purpose of clothing were more basic: to protect one from the elements, and to hide information.

What kind of information? Wounds, vulnerabilities, illnesses, recognisable features (e.g. tattoos), sometimes even sex … all of these are information that people sought to hide from each other in popular fiction, and presumably in real life as well.

Whether you believe in sharing about yourself openly or only sharing what is necessary, nobody today goes around naked (with the exception of nudist communities). Yet, as recently as ten years ago, we were doing the equivalent on the Internet: any information that websites requested about us was given freely, with few restrictions if any.

Today, with advertisers and other data-mining companies tracking you everywhere you go, with malicious hackers, phishers, and scammers waiting to snare unsuspecting users, and with more at stake being tied to your personal digital identity, we have to do better.

We have to wear clothes on the Internet.

**Sometime in the future:** What is:

- booting up? [Issue 15]
- XSS? [Issue 8]
- a good reason developers write code and give it away for free online? [Issue 21]
- firmware? [Issue 34]
- OpenType? And what are fonts anyway? [Issue 42]
- What is involved in installing a piece of software? [Issue 48]
- How do apps know where a file starts and ends? [Issue 49]
- What is a password hash? [Issue 63]

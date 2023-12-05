Title: Issue 59: Meltdown
Date: 2020-02-08 08:00
Tags: 
Category: Season 5
Slug: lmg-s5-issue-59-meltdown
Author: J S Ng
Summary: 

**Previously:** The CPU comprises different types of execution units. All the execution units can run at the same time, but they may execute instructions over different numbers of clock cycles. To minimise wait time, CPU instructions are carried out in an order that keeps the execution units busy as often as possible.

## Last issue: optimising the old-school robot bank teller

Last issue, I modelled a simple CPU bank teller consisting of two units, an ALU (arithmetic logic unit), and a LSU (load-store unit). The ALU does the calculations, while the LSU loads from or stores data to memory. For the CPU to hum along optimally, the ALU should not be kept waiting for data, and the LSU should not be left twiddling its thumbs while the ALU is working.

By reordering the instructions that come in, we can optimise CPU usage by making sure the LSU is loading data for the next few instructions while the ALU is still working; this is known as **out-of-order execution**.

For the CPU to give a customer his bank account balance, the following steps need to happen:

1. **GET** ID from customer
2. **LOAD** bank account owner from memory (using ID number)
3. Check that customer is the bank account owner (verifying other details) *[SLOW]*
4. *IF* verified, **LOAD** bank account balance
5. **SEND** bank account balance to customer

Where I last stopped, we were optimising the robot bank teller by carrying out the two **LOAD** steps together. This helps to optimise CPU use, because while the ALUs are busy carrying out operations to verify that the customer is the owner of the bank account, the LSU is loading the bank account details, ready to be used once the ALU is done.

Where do the bank account details go while the LSU is waiting for the ALU? In the case of the bank teller, they’re written on a piece of paper (yes, old-school, because analogy). In a real CPU, every piece of data requested by the CPU first goes through the CPU cache. This means the cache has a copy of all data ever requested, and it evicts the oldest data to make way for new data. The bank teller’s piece of paper is an analogy for the CPU cache.

## Meltdown: the exploit

Suppose I’m an ill-intentioned customer who wants to snoop on a neighbour’s bank transactions. I go up to the bank teller and ask it to retrieve the last 5 transactions of account ID 23983698576 (that’s my neighbour’s account ID, unknown to the robot tellers).

The bank tellers need to execute the following instructions. There is an implicit step after step 4 to ensure security:

1. **GET** ID[23983698576] from customer
2. **LOAD** bank account owner of [23983698576] from memory (written back to cache)
3. Check if I am the bank account owner *[SLOW]*
4. *IF* verified, **LOAD** bank account balance of [23983698576]
5. *IF* **not verified**, dump data and start over with the next customer
6. **SEND** bank account balance to me
7. **LOAD** last 5 transactions of [23983698576] from memory (written back to cache)
8. **SEND** last 5 transactions to me

However, after reordering for efficiency, the steps now look like this:

[1.] **GET** ID[23983698576] from customer  
[2.] **LOAD** bank account owner of [23983698576] from memory (written back to cache)  
[3.] Check if I am the bank account owner *[SLOW]*  
[4.] *IF* verified, **LOAD** bank account balance of [23983698576]  
[7.] **LOAD** last 5 transactions of [23983698576] from memory (written back to cache)  
[5.] *IF* **not verified**, dump data and start over with the next customer  
[6.] **SEND** bank account balance to me  
[8.] **SEND** last 5 transactions to me

While the ALU is carrying out authenticity checks in step 3, the LSU is simultaneously carrying out steps 4 and 7, the LOAD steps, to avoid sitting idle.

This also leaves a copy of the data in the cache; the LSU teller has written down the bank balance and last 5 transactions on a piece of paper while waiting for the ALU.

When the ALU reaches step 5 and figures out I’m not the owner of that account, then they start over with the next customer and I get evicted from the queue (this is called retiring an instruction, in a real CPU). But meanwhile, the papers on the desk don’t get cleared!

## Cache snooping: the oldest trick in the book

If this sounds horrifying to you, remember that the *real* CPU is just a bunch of transistors and it really isn’t all that smart. And remember that programs cannot access the cache directly; it is a hardware implementation detail (like the backroom of any business), and so this is considered normal practice.

But still, that leaves a small window of opportunity for me to crane my neck and try to snoop the paper. And that’s all the time I need to see my neighbour’s transactions, and even his bank balance!

**Issue summary:** A set of instructions can trick a CPU into reordering load instructions so that the data is temporarily loaded into the cache before the instructions are retired. The cache can then be snooped to retrieve the data.

Okay, I’ve left out the meaty details of cache snooping here, because there are a whole bunch of tricks to doing it, written up into white papers by cybersecurity researchers. Also this is a one-idea-a-week newsletter, and cache snooping is a whole ’nother idea. Also, I’ll get round to it later.

But first I want to talk about Spectre, which is another way of getting the desired data into the cache. But Spectre exploits another feature, known as speculative execution. It is also an intuitive concept, not difficult for normal folks to understand, and I’ll go straight into it next issue.

## What I’ll be covering next

**Next issue:** [LMG S5] Issue 60: CPU Optimisation Part 2 – Speculative Execution and Spectre

Cache snooping is interesting to me, because things like this actually happen all the time IRL! What’s really going on here is that any business operation needs to have a place to put things, move things, work on things, in a way that is invisible to customers and outsiders. But making sure that these inner workings are truly invisible to other people is helluva difficult.

Consider, for instance, [this article from The Atlantic](https://www.theatlantic.com/magazine/archive/2019/05/stock-value-satellite-images-investing/586009/). It describes how some rich investors try to make more accurate predictions of their investments’ performance by buying satellite imagery of their factory or operations sites. By seeing visual data that is not readily available to other investors, they can better predict how those companies are really performing.

Cache snooping is another instance of hardware snooping, but at a different scale and scope. Just how hidden are our hardware implementations? It is difficult to think about ways people can obtain such dearly desired info if we are not those people; human ingenuity does seem almost boundless!

When we really try to do everything in a secure manner, often it means sacrificing performance for security. For instance, a CPU without out-of-order execution would not be subject to this leak risk. But it would also run **1.26 to 2.4 times slower**, [according to Bruce Dawson of Google](https://randomascii.wordpress.com/2012/10/25/out-of-order-benefits/).

Ah, how to have our cake and eat it too …

**Sometime in the future:** What is:

- booting up? [Issue 15]
- a cookie? [Issue 8]
- XSS? [Issue 8]
- a CDN? [Issue 8]
- a good reason developers write code and give it away for free online? [Issue 21]
- firmware? [Issue 34]
- OpenType? And what are fonts anyway? [Issue 42]
- What is involved in installing a piece of software? [Issue 48]
- How do apps know where a file starts and ends? [Issue 49]

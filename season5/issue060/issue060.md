**Previously:** A set of instructions can trick a CPU into reordering load instructions so that the data is temporarily loaded into the cache before the instructions are retired. The cache can then be snooped to retrieve the data.

At the heart of the matter is the fact that the OS has no control over the order in which instructions are carried out. Because of this, hackers who understand how the CPU reorders instructions can write malicious code that tricks the CPU into loading precious data into memory for a fraction of a second, during which they can use cache-snooping techniques to read the data.

Before I go into the details of one cache-snooping technique, I want to outline another way that malicious code can get their targeted data into the cache. This exploits another feature, known as speculative execution.

## Speculative execution: the CPU’s way of anticipating

```
010011011011101101000101 …
```

Can you predict the next number in the sequence? Kinda tough …

```
1111111111111111 …
```

How about now? Easier?

We have all been in that workplace situation where we are waiting on a colleague to make a decision. If they choose A, we have to perform one set of routines. If they choose B, we have to perform another set of routines.

If our past experience with this person tells us that there is no pattern to what they will choose in such a situation, it is very difficult to proceed until they have made their choice. However, if they regularly choose A and occasionally choose B, that’s another story. Especially if they take a long time to make their decision.

To speed up the process, we might just carry out the set of routines for A, wait for them to say “I choose A”, then give them the results—*tada*! And if they choose B instead, secretly dump the evidence and curse our luck.

## Another model: the car valet

How would this work with a more concrete example? I could reuse the bank teller model from the Meltdown explanation, but I run the risk of muddling you up since the steps will look very similar. Instead, let’s model a pair of robot car valets instead. This pair still consists of a robot ALU and LSU. The ALU gets the car keys and driver ID from the customer, and asks the driver for their ID number before asking the LSU to retrieve the vehicle. The LSU, well, just parks or retrieves the vehicle.

Let’s exploit this CPU model to find out what kind of car our secretive neighbour drives. I don’t have my neighbour’s ID, but I do know his ID number (23983698576), and I give it to the CPU. It carries out the following instructions:

1. **GET** ID number[23983698576] from customer
2. Verify if I am the car owner *[SLOW]*
3. *IF* verified, **LOAD** car of 23983698576 by driving it to retrieval point and pass keys to customer
4. *IF* not verified, dump data and start over with the next customer

Sounds fair enough. The ALU finds out I am not my neighbour, and I don’t get to see his car. Awww. But let’s wait and see …

## Speculative valeting

10 customers later, the CPU has been processing verified customers only. It goes into speculative execution mode (in a **real CPU**, of course you can’t disable speculative execution just like that; it is always on). Now the CPU works this way:

[1.] **GET** ID number[23983698576] from customer
[2a.] **LOAD** car of 23983698576 by driving it to retrieval point
[2b.] Verify if I am the car owner *[SLOW]*
[3.] *IF* verified, pass car keys to customer
[4.] *IF* not verified, dump data and start over with the next customer

2a and 2b are carried out simultaneously. Have you figured out where the cache is in this model? It’s where the car is temporarily held: at the retrieval point.

10 customers later, the ALU checks my ID, and at the same time the LSU in good faith starts to drive my neighbour’s car to the retrieval point. It is astutely hidden from my direct view. But if I know the mode of operation of this valet beforehand, I have a small window of opportunity before the ALU figures out I’m not the owner and a cache flush occurs (i.e. the LSU removes the car from the retrieval point). Perhaps I could plant a camera there …

**Issue summary:** Speculative execution is a feature that lets the CPU speed up execution if it correctly predicts a decision point. The CPU carries out the operations along the predicted decision branch and loads the results if it predicts correctly.

And there you have it, two CPU features explained with robots. These are well-researched CPU features that have been used in CPUs for a long while … and nobody in the industry thought to thoroughly investigate ways in which this might be exploited for malicious intent, until the security researchers found out first.

You might blame this oversight on Intel, but I think I would blame the unpredictable nature of development. Early forts only needed walls, but not roofs, until catapults were invented. Hardware was invented to run fast, and the internet was designed to be robust, and very few people could predict accurately how they would be exploited for ill.

I was initially planning to write speculative execution and Spectre in two separate issues, but I did not expect to explain speculative execution in just three paragraphs. That would not have been a satisfying newsletter issue, huh. So here it is, speculative execution and Spectre in the same issue.

## What I’ll be covering next

**Next issue:** [LMG S5] Issue 61: Mapping the cache

Okay, I’m done talking about the exploit part of Meltdown and Spectre. The scene freezes, goes into extreme time slowdown mode … the last 5 transactions are on the bank teller’s paper, and the neighbour’s car is at the retrieval point. The bank teller ALU is looking over my ID, checking various things, and the car valet ALU is verifying my ID … the quarry is at hand! Only a split second before they uncover the truth and the quarry is snatched away!

How are we going to snoop that precious cargo? You’ve watched enough heist movies, you know these things don’t happen without exhaustively detailed planning.

Let’s start planning our cache snoop next issue.

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

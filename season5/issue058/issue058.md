**Previously:** The CPU stores data for ready access in the CPU cache. Accessing data from the CPU cache is much faster than accessing data from memory. The CPU cache is managed by the CPU and is invisible to the OS. Programs that need to ensure the data in the cache is “fresh” can perform a cache flush and reload.

In this issue, we look at one feature that CPUs use to speed up processing: out-of-order execution. “Out-of-order” makes it sound like something is broken in the CPU, but it really just means that the CPU instructions it is given are not executed in the same order that they were fed to the CPU.

If you have seen a busy Starbucks joint or Chinese restaurant at work, you would know that menu orders are not always carried out in the same order that they were taken (even if customers are eventually first-come-first-served)!. We do this because a fully staffed Starbucks joint or Chinese restaurant is not a single working unit, but a collection of specialised units.

## CPU execution units

A CPU core is comprised of 3 types of execution units:

- **A**rithmetic **L**ogic **U**nit (**ALU**): THE ALU is responsible for carrying out integer calculations
- **F**loating **P**oint **U**nit (**FPU**): The FPU is responsible for carrying out decimal calculations
- **L**oad/**S**tore **U**nit (**LSU**): The LSU is responsible for loading data from memory into the CPU, or storing data from the CPU into memory ([Issue 55](https://))

An instruction decoding unit in the CPU decodes each instruction and sends it to the appropriate execution unit. All these units can work at the same time, and for maximum performance this is what you want to happen.

## Not all instructions are executed equal(ly)

The CPU has an internal clock (called the **CPU clock**) that regulates when things are done in the CPU. Everything in a CPU takes place in cycles. Every operation takes at least one cycle, but some operations which require more steps will require more cycles.

For instance, the ALU can carry out most operations in one or two cycles, but the FPU often needs four or more cycles to do its work (moving decimals is hard work!). The LSU clock cycle latency varies, depending on which part of the cache you are fetching from (the cache has different regions; some regions are closer to CPU cores while other regions are shared among all the cores and therefore further. I won’t go into deeper detail.)

Keeping all the execution units busy is getting more complex now, eh?

## Minimising wait time in a CPU

Let’s revisit the instructions from [Issue 53]():

```
1 LOAD 1   R1
2 ADD  2   R1, R2
3 MOV  R2, MEM1011
```

The first instruction is to load data from memory, and this is gonna take a little while. The second instruction can’t start yet, so sending it to the ALU immediately after the first instruction will result in some wastage of clock cycles: the ALU will just be sitting there, waiting for data before it can do its thing.

Why not schedule an instruction from another application while waiting, and send instruction 2 to the ALU later when the data is ready? It doesn’t matter if the other application’s instruction came later, if it can be executed now we might as well do it.

This, in a nutshell-issue, is out-of-order execution.

## Analogy: old-school robot bank teller

Let’s model a CPU core as two execution units: an ALU and a LSU. The ALU is a robot bank teller that does what the customer asks, while the LSU is a robot bank teller that retrieves data from and stores data back to the bank’s database (i.e. memory). Two such robot bank tellers work at a teller counter (CPU core)

If a customer needs to check their bank balance, the following instructions need to happen (like I said, this is old-school; no ibanking or ATMs here, because analogy).

1. **GET** ID from customer
2. **LOAD** bank account owner from memory (using ID number)
3. Check that customer is the bank account owner (verifying other details) *[SLOW]*
4. *IF* verified, **LOAD** bank account balance
5. **SEND** bank account balance to customer

If you’re wondering why steps 2 and 4 can’t happen at the same time … congratulations! You already understand out-of-order execution at an intuitive level. If the LSU can carry out steps 2 and 4 at the same time, the ALU can simply provide the bank balance once the customer is authenticated, or discard the information otherwise.

This frees up the LSU, and if the LSU’s load is low enough we might even reduce robotpower and share one LSU between two teller counters, seeding android fears of restructuring and impending robot retrenchment … but let’s stop the analogy here for today.

**Issue summary:** The CPU is comprised of different types of execution units. All the execution units can run at the same time, but they may execute instructions over different numbers of clock cycles. To minimise wait time, CPU instructions are carried out in an order that keeps the execution units busy as often as possible.

Some very smart people might harangue me about micro-ops, or about decode buffers, etc. My only answer to all such concerns are: not necessary at this point. Maybe in a future issue, if it is the linchpin in some layman explanation.

## What I’ll be covering next

**Next issue:** [LMG S5] Issue 59: Meltdown

This little optimisation step, of doing things in an order that keeps the CPU busy, looks innocuous enough. But once we combine it with some features of the cache, it leaves a little loophole that enables an attacker to snoop on data: this is Meltdown. Stay tuned, we’ll get to the meat of Meltdown next issue!

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

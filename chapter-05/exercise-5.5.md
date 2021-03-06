### 5.5 Debugger

####Explain what the following code does: ((n & (n-1)) == 0)

**What does it mean if A & B == 0?**

It means that A and B never have a 1 bit in the same place. So if 
n & (n-1) == 0, then n and n-1 never share a 1. 

**What does n-1 look like (as compared with n**

<pre>
  1101011000 [base 2]
–          1
= 1101010111 [base 2]
</pre>

<pre>
  593100 [base 10]
–      1
= 593099 [base 10]
</pre>

When you subtract 1 from a number, you look at the least significant
bit. If it's a 1 you change it to 0, and you are done. If it's a zero,
you must "borrow" from a larger bit. So, you go to increasingly larger
bits, changing each bit from a 0 to a 1, until you find a 1. You flip
that 1 to a 0 and you are done. 

Thus, n-1 will look like n, except that n's initial 0s will be 1s in
n-1, and n's least significant 1 will be a 0 in n-1. THat is:

<pre>
if   n   = abcde1000 [base 2]
then n-1 = abcde0111 [base 2]
</pre>

**So what does ((n & (n-1)) == 0)) indicate?**

n and n-1 must have no 1s in common. Given that they look like this:

<pre>
if   n   = abcde1000 [base 2]
then n-1 = abcde0111 [base 2]
</pre>

abcde must be all 0s, which means n must look like this: 00001000. The
value n is therefore a power of two. 

**Therefore, ((n & (n-1)) == 0)) checks if n is a power of 2 (or if n is 0).**
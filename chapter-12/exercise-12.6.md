### 12.6 Volatile

#### What is the significance of the keyword "volatile" in C?

**Solution**

The keyword volatile informs the compiler that the value of the variable it is applied to
can change from the outside, without any update done by the code. This may be done by the
operating system, the hardware, or another thread. Because the value can change unexpectedly,
the compiler will therefore reload the value each time from memory. 

A volatile integer can be declared by either of the following statements:

<pre>
int volatile x;
volatile int x;
</pre>

To declare a pointer to a volatile integer, we do the following:

<pre>
volatile int * x;
int volatile * x;
</pre>

A volatile pointer to non-volatile data is rare, but can be done.

<pre>
int * volatile x;
</pre>

If you wanted to declare a volatile variable pointer for volatile memory (both pointer address
and memory contained are volatile), you would do the following:

<pre>
int volatile * volatile x;
</pre>

Volatile variables are not optimized.

Volatile variables are also useful when multi-threaded programs have global variables and any thread
can modify these shared variables. We may not want optimization on these variables. 
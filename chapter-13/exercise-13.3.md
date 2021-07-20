### 13.3 Final, etc.

#### What is the difference between final, finally, and finalize?

**Solution**

Despite their similar sounding names, final, finally and finalize have very 
different purposes. To speak in very general terms, final is used to control
whether a variable, method, or class is "changeable". The finally keyword is
used in a try/catch block to ensure that a segment of code is always executed.
The finalize() method is called by the garbage collector once it determines
that no more references exist. 

Further details on these keywords and methods is provided below.

**final**

The final statement has a different meaning depending on its context. 
- When applied to a variable (primitive): The value of the variable cannot change.
- When applied to a variable (reference): The reference variable cannot point to
any other object on the heap. 
- When applied to a method: The method cannot be overridden. 
- When applied to a class: The class cannot be subclassed. 

**finally**
There is an optional finally block after the try block or after the catch block.
Statements in the finally block will always be executed, even if an exception is
thrown (except if Java VM exists from the try block). The finally block is often
used to write the clean-up code. It will be executed after the try and catch blocks,
but before the control transfers back to its origin. 

**finalize()**
The automatic garbage collector calls the finalize() method just before actually
destroying the object. A class can therefore override the finalize() method from the
Object class in order to define custom behavior during garbage collection. 

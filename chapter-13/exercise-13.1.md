### 13.1 Private Constructor

#### In terms of inheritance, what is the effect of keeping a constructor private?

**Solution**

Declaring a constructor private on class A means you can only access the (private)
constructor if you could also access A's private methods. Who, other than A, can
access A's private methods and constructor? A's inner classes can. Additionally, if
A is an inner class of Q, then Q's other classes can. 

This has direct implications for inheritance, since a subclass calls its parent's
constructor. The class can be inherited, but only by its own or its parent's inner
classes. 
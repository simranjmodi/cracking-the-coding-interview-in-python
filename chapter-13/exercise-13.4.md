### 13.4 Generics vs. Templates

#### Explain the difference between templates in C++ and generics in Java.

**Solution**

Java generics and C++ templates have a number of other differences. These include:
- C++ templates can use primitive types, like int Java cannot and must instead use Integer
- In Java, you can restrict the template's type parameters to be of a certain type. For instance,
you might use generics to implement a CardDeck and specify that the type parameter must extend
from CardGame. 
- In C++, the type parameter can be instantiated, whereas Java does not support this.
- In Java, the type parameter (i.e., the Foo in MyClass<Foo>) cannot be used for static methods and
variables, since these would be shared between MyClass<Foo> and MyClass<Bar>. In C++, these classes
are different, so the type parameter can be used for static methods and variables. 
- In Java, all instances of MyClass, regardless of their type parameters, are the same type. The
type parameters are erased at runtime. In C++, instances with different type parameters are different
types. 

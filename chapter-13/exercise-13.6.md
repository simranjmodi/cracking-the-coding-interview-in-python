### 13.6 Object Reflection

#### Explain what object reflection is in Java and why it is useful. 

**Solution**

Object Reflection is a feature in Java that provides a way to get reflective
information about Java classes and objects, and perform operations such as:
- Getting information about methods and fields present inside the class at runtime
- Creating a new instance of a class
- Getting and setting the object fields directly by getting field reference,
regardless of what the access modifier is. 

**Why Is Object Reflection Useful?**
Three main reasons are:
- It can help you observe or manipulate the runtime behavior of applications.
- It can help you debug or test programs, as you have direct access to methods, constructors, and fields.
- You can call methods by name when you don't know the method in advance. For example, we may let the user pass in a class name, parameters for the constructor, and a method name. You can then use this information to create an object and call a method. Doing these operations without reflection would require a complex series of if-statements, if it's possible at all. 
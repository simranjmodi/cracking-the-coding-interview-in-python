### Shallow vs Deep Copy

#### What is the difference between deep copy and shallow copy? Explain how you would use each.

The difference between shallow and deep copying is only relevant for compound objects (objects that contain other objects, like lists or class instances):

A shallow copy constructs a new compound object and then (to the extent possible) inserts references into it to the objects found in the original.
A deep copy constructs a new compound object and then, recursively, inserts copies into it of the objects found in the original.

Note that shallow copy may cause a lot of programming runtime errors, especially with the creation and deletion of objects. Shallow copy should be used very
carefully and only when a programmer really understands what he wants to do. In most cases, shallow copy is used when there is a need to pass information about
a complex data structure without actual duplication of data. One must also be careful with destruction of objects in a shallow copy. 

In real life, shallow copy is rarely used. Deep copy should be used in most cases, especially when the size of the copied structure is small.
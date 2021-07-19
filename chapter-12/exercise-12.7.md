### 12.7 Virtual Base Class

#### Why does a destructor in base class need to be declared virtual?
**Solution**

Let's think about why we have virtual methods to start with. Suppose we have the following code:

<pre>
class Foo {
    public:
        void f();
};

class Bar : public Foo {
    public:
        void f();
}

Foo * p = new Bar();
p -> f();
</pre>

Calling p -> f() will result in a call to Foo::f(). This is because p is a pointer to Foo,
and f() is not virtual.

To ensure that p -> f() will invoke the most derived implementation of f(), we need to declare
f() to be a virtual function. 

Now, let's go back to our destructor. Destructors are used to clean up memory and resources. 
If Foo's destructor were not virtual, then Foo's destructor would be called, even when p is
really of type Bar. 

This is why we declare destructors to be virtual; we want to ensure that the destructor
for the most derived class is called. 
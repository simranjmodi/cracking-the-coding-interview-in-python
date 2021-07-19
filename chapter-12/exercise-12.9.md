### 12.9 Smart Pointer

#### Write a smart pointer class. A smart pointer is a data type, usually implemented with templates, that simulates a pointer while also providing automatic garbage collection. It automatically counts the number of references to a SmartPointer<T*> object and frees the object of type T when the reference count hits zero.

**Solution**

A smart pointer is the same as a normal pointer, but it provides safety via automatic memory management. It avoids issues like dangling pointers, memory leaks and allocation failures. The smart pointer must maintain a single reference count for all references to a given object.
This is one of those problems that seems at first glance pretty overwhelming, especially if you're not a C++ expert. One useful way to approach the problem is to divide the problem into two parts: (1) outline the pseudocode and approach and then (2) implement the detailed code.
In terms of the approach, we need a reference count variable that is incremented when we add a new reference to the object and decremented when we remove a reference. The code should look something like the below pseudocode:

<pre>
template <class T> class SmartPointer {
    /* The smart pointer class needs pointers to both the object itself and to the
    * ref count. These must be pointers, rather than the actual object or ref count
    * value, since the goal of a smart pointer is that the reference count is
    * tracked across multiple smart pointers to one object. */
    
    T * obj;
    unsigned * ref_count;
}
</pre>

We know we need constructors and a single destructor for this class, so let's add those first.

<pre>
Smart Pointer(T * object) {
    /* We want to set the value of T * object, and set the reference counter to 1. */
}

SmartPointer(SmartPointer<T> & sptr) {
    /* This constructor creates a new smart pointer that points to an existing
    * object. We will need to first set obj and ref_count to pointer to sptr's obj
    * and ref_count. Then, because we created a new reference to obj, we need to
    * increment ref_count. */
}

~SmartPointer(SmartPointer<T> sptr) {
    /* We are destroying a reference to the object. Decrement ref_count. If
    * ref_count is 0, then free the memory created by the integer and destroy the
    * object. */
}
</pre>

There's one additional way that references can be created: by setting one SmartPointer equal to another. 
We'll want to override the equal operator to handle this, but for now, let's sketch the code like this.

<pre>
onSetEquals(SmartPoint<T> ptr1, SmartPoint<T> ptr2) {
    /* If ptr1 has an existing value, decrement its reference count. Then, copy the
    * pointers to obj and ref_count over. FInally, since we created a new
    * reference, we jneed to increment ref_count. */

}
</pre>

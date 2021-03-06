### 12.4 Virtual Functions

#### How do virtual functions work in C++

**Solution**

A virtual function depends on a "vtable" or "Virtual Table". If any
function of a class is declared to be virtual, a vtable is constructed
while stores addresses of the virtual functions of this class. The
compiler also adds a hidden vptr variable in all such cases which 
points to the vtable of that class. If a virtual function is not 
overridden in the derived class, the vtable of the derived class
stores the address of the function in its parent class. The vtable
is used to resolve the address of the function when the virtual 
function is called. Dynamic binding in C++ is performed through the 
vtable mechanism. 

Thus, when we assign the derived class object to the base class pointer, 
the vptr variable points to the vtable of the derived class. This
assignment ensures that the most derived virtual function gets called. 
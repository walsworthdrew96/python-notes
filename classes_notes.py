# 1. What is the main point of OOP in Python?
# OOP is about code reuse--you factor code to minimize redundancy and program by
# customizing what already exists instead of changing code in place or starting
# from scratch.

# 2. Where does inheritance search look for an attribute?
# 1. Instance
# 2. Class of Instance
# 3. Leftmost Superclass
# 4. Next Superclass to the right
# 5. Their superclasses left to right, etc.

# 3. What is the difference between a class object and an instance object?
# 1. One is the blueprint/factory, and the other is the object/product.
# 2. Both class objects and instance objects are namespaces
# (packages of vars that are attributes).
# 3. Operator/Method overloading is defined in the class, but these operators
# and methods are used to process instances, not classes.

# 4. Why is the first argument in a class's method function special?
# The first argument is always "self", which is the same as the implicit "this"
# pointer in other OOP languages. "self" receives the instance object that is
# the implied subject of the method call.
# Since all methods in a class are designed to process instance objects, this is
# the literal definition of Object Oriented Programming, since the methods are
# Object Oriented.

# 5. What is the __init__ method used for?
# The __init__ method is used to initialize the instance objects with a default
# state. It is usually used to also call the __init__ method of the
# superclasses as well, which makes variables for each level of the class object
# tree that the instance object inherits from.

# 6. How do you create a class instance?
# A class instance is made by an expression like: myInstance = MyClass(args)
# This calls the constructors in the class object tree to initialize the object.

# 7. How do you create a class?
# A class is created using a class definition like:
# class MyClass (superclasses):
#   def __init__(self, args):
#       <init body>
#   def otherMethod1(self, args):
#       <otherMethod1 body>

# 8. How do you specify a class's superclasses?
# By providing them in the parentheses following the class name in the class
# definition.

#

<!--==================-->
# Modules are Objects
<!--==================-->
> Modules are instances of a module class
- [Modules are singleton instances of built-in module class](https://stackoverflow.com/questions/43183244/difference-between-module-and-class-in-python)

- In Python, modules are objects (values) and are handled like other objects. Thus, you can pass a module as an argument in a call to a function. Similarly, a function can return a module as the result of a call. A module, just like any other object, can be bound to a variable, an item in a container, or an attribute of an object. For example, the sys.modules dictionary, covered in Module Loading, holds module objects as its values. The fact that modules are ordinary objects in Python is often expressed by saying that modules are first-class objects.

"There are huge differences between classes and modules in Python.Classes are blueprints that allow you to create instances with attributes and bound functionality. Classes support inheritance, metaclasses, and descriptors.Modules can't do any of this, modules are essentially singleton instances of an internal module class, and all their globals are attributes on the module instance. You can manipulate those attributes as needed (add, remove and update), but take into account that these still form the global namespace for all code defined in that module." -- [stack overflow]

<!--==================-->
# Built in Variables
<!--==================-->
- The dunder vars are baked into the module class
- built in variables are surrounded by double underscores
  - built in variables can hold data (class info or object)
    - __name__
    - __class__
  - built in variables can also be methods
    - __init__
    - __del__

<!--==================-->
# Class Anatomy
<!--==================-->
- `__init__` instance constructor
- `built-in vars` inherited from module class
- instance vars: state (inside instance method constructor)
- instance methods: behavior
- static vars/methods

<!--==================-->
# Object Scope
<!--==================-->
- What attributes (state/behavior) an instance obj has access to
- Similar to var/identifier scope (which works in a lexical scope cxt)

<!--==================-->
# Instantiation
<!--==================-->
## _PROCESS_
- `__new__` static method is called to return an uninitialized object to the constructor
- constructor initializes obj by calling `__init__`
- __init__ initializes the instance variables the object needs in its initial state
- The __new__ method returns the new object, which the constructor subsequently uses to call __init__

## _METHOD_
Notice that the speak method definition needs one parameter, conventionally named self. All instance methods must have a self parameter. You can use a name other than self if you don't mind shunning by other Python programmers.

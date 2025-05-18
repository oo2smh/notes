<!--==================-->
# Modules are Objects
<!--==================-->
> Modules are instances of a module class
- [Modules are singleton instances of built-in module class](https://stackoverflow.com/questions/43183244/difference-between-module-and-class-in-python)

- In Python, modules are objects (values) and are handled like other objects. Similarly, a function can return a module as the result of a call. A module, just like any other object, can be bound to a variable, an item in a container, or an attribute of an object. For example, the sys.modules dictionary, covered in Module Loading, holds module objects as its values. The fact that modules are ordinary objects in Python is often expressed by saying that modules are first-class objects.

There are huge differences between classes and modules in Python.Classes are blueprints that allow you to create instances with attributes and bound functionality. Classes support inheritance, metaclasses, and descriptors.

Modules can't do any of this, modules are essentially singleton instances of an internal module class, and all their globals are attributes on the module instance. You can manipulate those attributes as needed (add, remove and update), but take into account that these still form the global namespace for all code defined in that module.

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
- []

<!--==================-->
# Private Variables
<!--==================-->
## _PRIVATE BY CONVENTION_
- No truly private variables. Must rely on other devs to follow convention
- prefix var with `_` or `__`. If you use a dunder prefix, you might get bitten by _name mangling_
- [Mangled by Dunder](https://www.youtube.com/watch?v=0hrEaA3N3lk)
- _Mangle_: To disfigure, to change

> If you do decide to use `__` as your private variables, you can defeat name-mangling by prefixing your caller (instance object) with `_`. [Privacy](https://launchschool.com/books/oo_python/read/classes_objects#privacy)

## _GETTERS AND SETTERS_
- methods that provide *controlled* access to an obj's attributes
- Getters conventionally have the same name as the associated instance variable without leading underscores. Setters conventionally prefix the same name with set_.
  ### Non Property
````py
class Person:
  def __init__(self, age):
    self.age = age

  def age(self):
    return self._age

  def set_age(self, new_age): # setter
    if not isinstance(new_age, int):
      raise TypeError("Age must be an int")
    self._age = new_age
````
  ### Property Decorator
- Another way to use getters and setters. Same results, syntactically different
- **Properties** :Getters created with the @property decorator are known as properties. A setter is simply a property whose value can be reassigned.
- Considered best practices to use

    #### *Usage*
- data validation (ie: type check)
- dynamically compute values
- improve readability/refactoring

````py
class Person:
  def __init__(self, age):
    self.age = age

  @property
  def age(self):
    return self._age

  @age.setter
  def age(self, new_age): # setter
    if not isinstance(new_age, int):
      raise TypeError("Age must be an int")
    self._age = new_age
````


<!--==================-->
# Overview
<!--==================-->
- Built-ins refer to:
  - Dunder Methods
  - Functions
  - Exceptions
  - Types
    - Read only
    - Instance Methods
  - Modules (need to be imported)
- Built in functions are a wrapper around a C function

<!--==================-->
# Theory
<!--==================-->
> [!Caution]
> This is my current understanding of how Python works under the hood. It might be wrong. But it serves as a mental mode

- Built-ins come packaged with the Python language. Built-in functions, exceptions, and types are mostly written in C. All values in Python are objects. `objects` are the superclass for all other objects. There is a C file for all the `builtins`. There is a C file for the `operators`.
  - Python has a `builtins` module and an `operators` module
- The built-in types each have their own corresponding classes. It might not be implemented with Python, but in C.
  - Regardless of the implementation, these built-in types have attributes (vars, methods) that are available to instances
- The standard modules are not written in C, but are written in Python and ships with the Python Interpreter (which has the Python core)
  - Python core: built-in fns, exceptions, tokens

> [!Note]
> `builtins` module and `operator` module and available in Python. These are written in Python and shows how Python's internal implementation might have worked.

<!--==================-->
# Dunder Methods
<!--==================-->
- All built-in methods are designated with `__` to prevent name_collision then aliased to its shorter form
- [Dunder Methods Explained](https://docs.python.org/3/library/functions.html)
- Under the hood, built-in methods are all surrounded with `__` and then allowed to be used without `__`.
- Operators are instance methods on their respective type classes then aliased to their shorthands
- You can also override the default operators in the types

<!--==================-->
# Built-In Fns
<!--==================-->
## _CONVERTER_
### Constructor
```py 🎀 SOB BF CoBB DSR  FT (13)
# Constructors are classes
- str(obj)
- object
- bin(obj)
- bool([obj = False])
- float(fn, iterable)

- complex()
- bytearray([source=b""])
- bytes()

- dict(**kwargs)
- set(iterable)
- range(start, stop, [step = 1])
- frozenset(iterable = set())
- tuple(iterable)
```

### Other
```py 🎀 HOH
- hash(object)
- oct(x)
- hex(x)
```

## _STR_
```py 🎀 FAR CO
chr(i) # ⏎ char
ord(c) # ⏎ char code ord
format(value)
ascii(obj)
repr(obj)
```

## _MATH_
```py 🎀PAR DMM
- pow(base, exp)
- abs(x)
- round(number, ndigits = None)
- divmod(a,b)
- min(iterable, key=None)
- max(iterable, key=None)
```

## _I/O_
```py
- input(prompt)
- print()
- open(file)
```

## _INFO_
```py 🎀 TIL HGL DMV
- type(obj)
- id(obj)
- len(seq)

- help(request)
- globals()
- locals()
- dirs([obj])
- memoryview(object)
- vars(obj)
```

## _CLASS_
```py
- @classmethod
- @staticmethod
- @getter
- @setter
- super
- deleter

- isinstance(obj, classinfo)
- issubclass(class, classinfo)
- hasattr(obj, name)

- getattr(obj, name, default)
- setattr(start, stop, step=None)
- delattr(obj, name)
- property()
```

## _ITERABLE_
### Common Actions
```py
- all(x)
- any(x)
- slice(start, stop, step=None)

- filter(fn, iterable)
- map(fn, iterable, *iterables)
- reversed(seq)
- sort(*, key=None, reverse=False)
- sorted(iterable, key=none, reverse=False)
- sum(iterable, start=0)
- enumerate(iterable, [start=0])
- zip(*iterables, strict=False)
```

### Other
```py
- iter(object, sentinel)
- next(iterator, default)
- aiter(x)
- anext(x)
```

## _DEBUGGGER_
```py
- breakpoint()
- compile()
- eval(...)
- exec(...)
```

<!--==================-->
# Built-In Exceptions
<!--==================-->
- [Exceptions](https://docs.python.org/3/library/exceptions.html)
- BaseException
- Exception
- ArithmeticError
- AssertionError
- LookupError
- AssertionError
- AttributeError
- IndexError
- KeyError
- NameError
- SyntaxError
- IndentationError
  - TabError
- TypeError
- UnboundLocalError
- ValueError

<!--==================-->
# Built-In Types
<!--==================-->
- The built-in types refer to the constructor-fns.
- Many types have literals, but the literals are the same as creating an instance of a type
```py
string1 = str("hi")
string2 = "hi"
print(string1 == string2)
```

## _READ-ONLY_
```py
__dict__
__name__
__class__
__mro__
```

## _NUMERIC INSTANCE METHODS_
```py
- (int/float).isinteger()
```

## _STR INSTANCE METHODS_
```py
- str.islower()
- str.isupper()
- str.isalnum()
- str.isalpha()
- str.isspace()
- str.istitle()
- str.join(iterable)
- str.(l/r)strip()

- str.isnumeric()
- str.isascii()
- str.isprintable()
- str.isdecimal()
- str.isdigit()
- str.isidentifier()

- str.(l/r)split(...)
- str.replace()
- str.capitalize()
- str.swapcase()
- str.title()
- str.casefold()

- str.center(width[, fillchar])
- str.count()
- str.encode(...)
- str.expandtabs(tabsize=8)

- str.startswith(...)
- str.endswith(...)
- str.format(...)
- str.find(...)
- str.formatmap(mapping)
- str.partition()
- str.index(...)
```

## _SET_
```py
- set.issuperset(other)
- set.issubset(other)
- set.union(*others)
- set.intersection(*others)
- set.copy()
- set.add(elem)
- set.remove(elem)
- set.discard(elem)
- set.update(*others)
- set.pop()
- set.clear()
```

## _LIST_
```py
- list.copy()
- list.clear()
- list.fromkeys(iterable, value=None)
- get(key, default=None)
- items()
- keys()
- values()
- pop()
- popitem()
- list.reverse()
- reversed(d)
- update([other])
```

<!--==================-->
# Built-In Modules
<!--==================-->
```md
- os
- flask
- decimal
- numpy
- random
- math
- sys
- statistics
- functool
- logging
- datetime
- tkinter
- json
```

<!--==================-->
# References
<!--==================-->
- [Built-In Types](https://docs.python.org/3/library/stdtypes.html#str.lstrip)
- [Built-In Fns](https://docs.python.org/3/library/functions.html)
- [Built Ins Definition](https://stackoverflow.com/questions/49756646/when-is-a-function-in-a-standard-library-module-called-a-built-in-function)

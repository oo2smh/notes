# 🐧 Tldr
- **What**: Interpreted language with a hybrid programming paradigm. Used often for machine-learning, easy readability, data science, and applications.
- **Why**: To break down the main syntactical elements of the language.
- **How**: By outlining the different syntactical elements with key examples.

## *OUTLINE*
- 🍄‍🟫 Language Core
- 🍊 Std lib
- 🍎 Macro Tools
- 🟣 Concepts

# 🍄‍🟫 Operators/Keywords
## *OPERATORS*
```py
# LAC (logical, assignment, comparison)
logical = True and False == not True or False
comparison = (1 < 2 and 1 <= 1) or (2 > 1 and 1 >= 1) and ("True" != "False")

# Arithmetic, Assign + Arithmetic, String
print(1 + 1 - 1 * 2 / 2**1 % 2)
print("cheer" + "ios")
num = 1 # ++ and -- do not exist in python!
num += 1
print(num)

# Membership
ls1 = [1, 2]
ls2 = [1, 2]
print("is:", ls1 is ls2, "is not:", ls1 is not ls2)
print("in:", 2 in ls1, " not in:", 3 not in ls1)
```

## *CONSTRUCTS*
### Conditionals
```py
# Traditional
age = 0
if age > 19:
    print("twenties")
elif age > 12:
    print("teen")
else:
    print("youngster")

# Short-circuit: this or that
name = username or "Guest"

# Ternary
age = 18
yes, conditional, no = "Adult", age >= 18, "Minor"
status = yes if (conditional) else no
print(status)

# Switch Statement
status = 404
match status:
    case 200:
        print("Success")
    case 404:
        print("Not Found")
    case 500 or 501 or 502:
        print("Server Error")
    case _:   # Wildcard (else)
        print("Unknown Status")
```

### Loops
```py
for num in range(3):
    print(num)

num = 3
while num > 0:
    print(num)
    num -= 1

# comprehensions (used for mapping: loop + change) - list, set, dict
num = [1,2,3,4]
num_simple = [x * 2 for x in num]
num_full = [x * 2 for x in num if x > 2]
print("simple:", num_simple, "complex:", num_full)
```

### Function/Class
```py
def add_two_nums(num1, num2):
    return num1 + num2
print(add_two_nums(1,3))

class Dad:
    def __init__(self, name, hobby):
      self.name = name
      self.hobby = hobby
    def talk(self):
      print("I am dad!")

class Son(Dad):
    def talk(self):
      print("I am son!")

sonny = Son("Sori", "running")
sonny.talk()
```

#  🍊 Type Constructors
## *TYPE CONSTRUCTORS*
> These are builtins that are available at the global scope.

```py .........................
# PRIMITIVES
int(), float()
chr(), str(), ord() # ord converts char to UNICODE numerical value
bool()

# COMPLEX: BASE
list()
dict()
set()
frozenset()
tuple()

# COMPLEX-UTILS: LAZY ITERABLES 🎀 reformed zoomer
range()
enumerate()
filter()
zip()
map()
reversed()
dict.[keys,values,items]
```

> [!note] Confusion between `iterable`, `iterator`, and `__iter__`. `__iter__` is the mechanism/method in which iteration is done. The `__iter__` method is present in both the `iterable` and the `iterator`. When used on the `iterable`, it returns an `iterator`. The `iterator` has 2 notable methods (`__iter__`, `__next__`). The `iterator` object bookmarks the location of the iteration and ensures smooth looping.

# 🍊 Global Namespace Functions
## *INFO*
```py
print()
dirs([obj])
- vars(obj)
isinstance()
issubclass()
type()
id()
# vars
globals()
locals()
vars()
# decorators
- @classmethod
- @staticmethod
- @getter
- @setter
```

## *_I/O_*
```py
- input(prompt)
- print()
- open(file)
```

## *MATH*
```py .........................
sum()
abs()
round(x [, ndigits])
pow(x, y)
min(iterable, *[, key, default])
max(iterable, *[, key, default])
divmod() # combination of division + modulus
``````````````````````````````

## *FUNCTIONAL*
```py
all()
any()
reversed()
sort()
```

# 🍊 Dunder Methods
> Some properties and methods are available nested within other classes. For instance `int`, `str`, etc.

## *CORE DUNDER METHODS*
> [!note] Every type inherits from the base `object` class. Therefore, they all share the DNA of the core dunder methods. Dunder methods are rarely used directly, but offer hooks for functions and operators which uses these magic dunder underneath the hood!

> [!tip] Dunder methods can be overwritten and given unique functionality for a custom class!

```toml
print(dir(object))
print(object.__subclasses__())
print(dir(list))
print(dir(dict))
print(dir(tuple))
```


| | Dunder Method | Triggered by... | Implementation Purpose |
| --- |--- | --- | --- |
| 🧬 | new | MyClass() | `Constructor`: creates object |
| 🧬 | init | obj = MyClass() | `Initializer`: initalizes attributes of object |
| 💬 | doc | help(obj) | `Documentation`: |
| 💬 | repr | repr(obj) | `Dev String`: Official debugging representation. |
| 💬 | str | print(obj) | `User String`: Pretty readable version of the object. |
| ⚖️ | eq, ne |  ==, !=  |     |
| ⚖️ | lt, le, gt, ge |  <, >, <=, >=  |  |
| 🔍 | getattribute | obj.attr | `Gatekeeper`: Intercepts every attribute access. |
| 🔍 | setattr | obj.x = 1 | `Writer`: Logic for assigning values to attributes. |
| 🔍 | `dir` | dir(obj) | `Inspector`: Lists all valid names on the object. |
| ⚙️ | call | obj() | `Callable`: Makes an object act like a function. |
| ⚙️ | sizeof | sys.getsizeof() | `Memory`: Returns internal size of object in bytes. |


# 🍊 ABC
> These are called interfaces in other languages (golang). An `interface` is a type that defines a set of method signatures. Any classes that use the interface `satisfies` the interface.

```py
import collections
print(dir(collections.abc))

# these collections are built in. Must import `collections` to get info about them
```

- The main abstract classes classes from `collections.abc`

|	ABC Interface | Dunder	| Implemented By |
|	--- | ---	| --- |
| Iterable |  iter	| list, tuple, set, dict, str |
| | | range, map, filter, zip, enumerate, reversed |
| Sized |	len |	list, tuple, set, dict, str, range |
| Container |	contains	| list, tuple, set, dict, str (checks substrings) |
| Callable |	call	| function, method, type (classes), classmethod |
| Mapping |	getitem	| list, tuple, str, range |
| Sequence |	getitem, len	| list, tuple, str, range |


```py
# loops automatically runs through these steps!
ls = [1,3]
my_iterator = iter(ls) # returns iterator
print(next(my_iterator))
print(next(my_iterator))
print(ls.__getitem__(1) == ls[1])
print(len([1,2,3]))
print("harry" in {"harry":1, "bob":2})
```

# 🍊 Type-Specific Methods
## *SEQUENCES*
- These are the common actions for sequences
  - Sequences like strings, tuples, lists, ranges
- Sequences (strings, lists) deserve a more in-depth section

```py .........................
x in seq # inclusion
x not in seq # exclusivity
s + t # concatenation of s and t
s * n # repeating s multiplied n times
s[i] # access
s[i] = "info" # assignment
s[i:j:k] # subsequence

s.index(x) # idx of 1st occurrences of x in s
s.count(x) # total number of occurrences of x in s # total number of occurrences of x in s # total number of occurrences of x in s

# these are builtins
len(s)
min(s)
max(s)
````````````````````````````````

## *STRINGS*
```py ......................
# Lookup
str.startswith()
str.endswith()
str.find(sub[, start, end]) # returns the lowest idx where sub is found or -1
str.index(sub [, start, end]) # ValueError when sub not found

# Casing
str.capitalize()
str.casefold()
str.swapcase()
str.lower()
str.upper()

# Removal
str.removeprefix(prefix)
str.removesuffix(suffix)
str.replace(old, new, count=-1) # -1 all occurrences are replaced

# Other Mannipulation
str.(l/r)just(width[, fillchar]) # padding
str.(l/r)strip([chars]) # trimming
str.split()
str.splitln()

# Bool Check
str.islower()
str.istitle()
str.isupper()

str.isalnum()
  str.isascii()
    str.isalpha()
      str.isidentifier()
    str.isspace()

# Numeric
  str.isnumeric()
    str.isdigit()
      str.isdecimal()
```

## *LISTS*
```py
ls = [1, 2, 3]
👺 ls.append(x)
👺 ls.clear()
👺 ls.extend(iterable)
👺 ls.insert(i, x)
👺 ls.pop(i)
👺 ls.remove(x)
👺 ls.reverse()

sort(*, key=None, reverse=False)
ls.copy()
```

## *DICTIONARIES*
- Basic Actions: Create, Remove, Copy, Add, Access
```py ...........................
# BOOLEAN CHECK
key in dict

# Basic Actions
dict.clear()
dict.copy()
dict.update(other)
dict.popitem()
dict.pop(key, default=None)
dict.fromkeys(keys, value=None)
dict.get(key, default=None)

# ARRAYFICATION
dict.items()
dict.keys()
dict.values()
````````````````````````````````

# 🍊 Other Useful modules
- `datetime`, `sys`, `os`, `pytest`, `re`, `math`, `random`, `json`

# 🍎 Macro Tools
- Module is akin to a `file`. It is implemented by being an instance of the instance `module`.
- Package is akin to the `folder`.
- `PIP` is the package manager. `uv`: faster than pip. replaces `venv`
  - `virtual env` is created to isolate dependencies and tether it to a directory.

# 🟣 Concepts
## *EVERYTHING IS AN OBJECT!*
- Every value in Python = object. Each value has a data-type(type) which has an associated class.
- Objects are python's abstraction of data. All data has 3 things
  1. identity is(): object's address in memory
  2. type: possible values of objects in type, operations/methods that object supports
  3. Stored value
    - mutable (atomic obj, static-container object)
    - immutable (container object)
- Even a module is an instance of the `module` class. A class is a specific type of object that acts as a blueprint!

## *MODULES VS CLASSES*
- "There are huge differences between classes and modules in Python.Classes are blueprints that allow you to create instances with attributes and bound functionality. Classes support inheritance, metaclasses, and descriptors.Modules can't do any of this, modules are essentially singleton instances of an internal module class, and all their globals are attributes on the module instance. You can manipulate those attributes as needed (add, remove and update), but take into account that these still form the global namespace for all code defined in that module." -- [stack overflow]

- `__new__` static method is called to return an uninitialized object to the constructor
- constructor initializes obj by calling `__init__`
- __init__ initializes the instance variables the object needs in its initial state

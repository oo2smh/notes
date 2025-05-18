<!--==================-->
# Overview
<!--==================-->
- Python uses the builtin fns extensively
- Prebuilts are common actions on datatypes
  - It can be implemented through operators, builtins, and methods
  1. CORE
  2. SUPPLEMENTARY

<!--==================-->
# Built In Fns
<!--==================-->
- Python's built-in fns
  - implements the `Math`, `Array` and `Type Converter` fns from JS
  - other math functionalities are in the math module

## TYPES (standard)
- Type Converter and Constructor
- Akin and similar to JS constructors
```py .........................
bool()
chr()
str()
ord()
tuple()
list()
dict()
int()
float()
set()
frozenset()
```````````````````````````````

## _OBJECT_
- dunder methods are in all objects
- these aren't usually called directly, but indirectly

```py ..........................
(get/set/del/has)att
callable # fns, methods, classes are callable
````````````````````````````````

  ### Inheritance
```py ............................
isinstance()
issubclass()

# Not called, used as decorators
property
classmethod
staticmethod
``````````````````````````````````

## _MATH_
```py .........................
sum()
abs()
round(x [, ndigits])
pow(x, y)
min(iterable, *[, key, default])
max(iterable, *[, key, default])
divmod() # combination of division + modulus
``````````````````````````````

## _ITERATION_
  ### General
```py ..........................
len()
range() # range 2 values
iter() # returns an iterator
  next()
aiter() # returns an async iter
  anext()
enumerate() # extract idx and elem in iteration
zip() # multi collection iteration

# Rarely Used Explicitly
slice() # usually not used but [start:end:step] is used
````````````````````````````````

  ### Manipulation
```py ...........................
filter()
map()
all() # empty => True
any() # empty => False
reversed() # lists, dicts
sort()
````````````````````````````````

## _INFO_
```py .......................
type()
id()
print()
open() # opens a file
````````````````````````````


## _RARELY USED_
  ### Internals
```py ..........................
# Types
oct()
hex()
bin()
complex()
bytes()
bytearray()
memoryview()

# Other
dir()
hash()
eval()
exec()
complile()

# Vars/Imports
globals()
locals()
vars()
__import__
```````````````````````````````

  ### String Representation
- dif ways to represent a str/bytes
```py ..........................
oct()
hex()
format()
ascii()
repr()
``````````````````````````````

  ### Debugging Builtins
```py ..........................
breakpoint()
help()
``````````````````````````````

<!--==================-->
# C:Number
<!--==================-->
## _BOOLEAN CHECK_
```py .......................
int.is_integer()
isinstance(value, int)
isinstance(value, float)
````````````````````````````
## _INCISION_
```py .......................
# Units right of decimal pt
num = 3.14
round(num, fixedValues) # use round builtin fn
fixedValue = f"{num: .2f}" # use str formatting

# toPrecision (# of significant digits)
preciseValue = f"{number: .3g}"
````````````````````````````

<!--==================-->
# C:Dictionaries
<!--==================-->
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
<!--==================-->
# Sequences
<!--==================-->
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

<!--==================-->
# C:String
<!--==================-->
## _SEARCH_
```py ......................
str.startswith()
str.endswith()

str.find(sub[, start, end])
  str.lfind()
  str.rfind()
# returns the lowest idx where sub is found or -1
str.index(sub [, start, end]) # ValueError when sub not found
````````````````````````````

## _MANIPULATION_
  ### Casing
```py ......................
str.capitalize()
str.casefold()
str.swapcase()
str.lower()
str.upper()

str.expandtabs(tabsize=8) # tab chars replaced by 1+ spaces
````````````````````````````

  ### REMOVAL
```py ......................
str.removeprefix(prefix)
str.removesuffix(suffix)
str.replace(old, new, count=-1) # -1 all occurrences are replaced
````````````````````````````

  ### SIZING
```py .......................
str.just(width[, fillchar]) # padding
  str.ljust(...)
  str.rjust(...)
str.strip([chars]) # trimming
  str.lstrip(...)
  str.rstrip(...)
`````````````````````````````

  ### Transformation
```py ......................
str.encode() # return str encoded to bytes
str.partition(sep) # returns a 3 tuple (before part, sep, after part)
str.split()
str.spliitln()

````````````````````````````

## _BOOL CHECK_
```py ......................
str.islower()
str.istitle()
str.isupper()

str.isalnum()
# Alphabetic
  str.isascii()
    str.isalpha()
      str.isidentifier()
    str.isspace()

# Numeric
  str.isnumeric()
    str.isdigit()
      str.isdecimal()
````````````````````````````

<!--==================-->
# Lists
<!--==================-->
## _BASE ACTIONS_
```py .....................
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
```````````````````````````

## _ITER ACTIONS_
- these are common actions that are done with iterations
  1. iterate, filter, transform
- package `functools`

```py ........................
map()
filter()
any()
all()

import functools
reduce()
```````````````````````````````

<!--==================-->
# Regexp
<!--==================-->
- `re` module
- regexp patttern `r"pattern"`
  - stands for raw strings, but I think of it as strings, but I think of it as regex

```py ........................
import re

text = "Hello world"

re.match(pattern, text)
re.search(pattern, text)
re.findall(pattern, text)
re.sub(pattern, replace, string)
  # subs all occs of pattern with replace string
re.split(pattern, string)
``````````````````````````````

<!--==================-->
# Exceptions
<!--==================-->
- Everything is a subclass of BaseException
  - Exception is a subclass of BaseException

```md .........................
BaseException
  - Exception
    - ValueError
    - SyntaxError
    - LookupError
      - IndexError
      - KeyError
    - ArithmeticError
      - ZeroDivisionError
    - RunttimeError
````````````````````````````````
<!--==================-->
# Date/Time
<!--==================-->
- import `datetime` module
- contains several classes `date, time, datetime, timedelta`

<!--==================-->
# Overview
<!--==================-->
- Every value in Python = object. Each value has a data-type(type) which has an associated class.
- All types are (direct/indirect) subtypes of object. They inheirt the default behavior from object.

- In Python, the terms `object` and `value` can be used interchangeably.
- Terms class = datatype = type (not semantically correct, but used interchangeably)
- Primitives are atomic values
- non-primitives are multi-value items
  - strings can be thought of as multi-value, but it's a coherent chunk so it's considered a primitive

- Since everything in Python is an object, all data-types and structures are instances of a specific class

Objects are python's abstraction of data. All data has 3 things
  1. identity is(): object's address in memory
  2. type: possible values of objects in type, operations/methods that object supports
  3. Stored value
    - mutable (atomic obj, static-container object)
    - immutable (container object)

- Immutable: [number, string, tuples, boolean, None]

> [!Caution]
> If the value of an immutable container object contains reference to a mutable object, the mutable object can change, but the bigger container object is still considered to be immutable. A tuple can contain an immutable object. But the tuple is still considered as an immutable object.
>
> Objects that (can) contain references to other objects are called containers (tuples, lists, dictionaries)

> [!Caution]
> For immutable values, the reference to a value might be reused or a new copy of the value might be created (depends on implementation)
> Immutable objects are guaranteed to have the same identity

- Types can be divided by its kind (whether it's considered atomic or not)
- There are more types than listed here, but these are the most commonly used
- [All the types](https://docs.python.org/3/reference/datamodel.html)

## _PRIMITIVE KIND_
- boolean
- Numbers
  - integers
  - floats
- strings (sequenced)
* NoneType (can be primitive/non-primitive)
* NotImplemented

## _NON-PRIMITIVES_
### Indexed
- range (returned by the range fn)
- tuples
- lists

### Maps & Sets
- dictionaries
- sets (mutable set)
- frozen sets (immutable set)

### Other
- functions

> [!Note]
> Sequences are a type. The `len()` function and indexing can be done on sequences. However, since I decided to group by the criteria of mutability (primitives vs complex), this isn't reflected in the list above.
  - Sequences support:
    1. len()
    2. Indexing
    3. Slicing []

<!--==================-->
# Functions
<!--==================-->
## Decorators
- A special type of fn
- they are functions which modify the functionality of other functions. They help to make our code shorter and more Pythonic. M

<!--==================-->
# Reference
<!--==================-->
- [What are Decorators](https://book.pythontips.com/en/latest/decorators.html)
- [Function Decorators](https://stackoverflow.com/questions/739654/how-do-i-make-function-decorators-and-chain-them-together/1594484#1594484)

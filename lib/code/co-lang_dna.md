<!--==================-->
# 🔑 Keywords
<!--==================-->
## _BIG PICTURE_
- Language classification
- Program Lifecycle
  - Compile Time
    1. Lexing - Tokenization
    2. Parsing - Branching (Compound Constructs) and AST Creation
    3. Semantic Analysis
  - Run-time
    *Closures are created during the creation phase*
    1. Creation Phase
    2. Execution Phase
- Lexical Env (Compile-Time Checks)
  - Tokens (Operators, Literals, Delimiters, Punctation, Reserved
  words, Identifiers, Lang-specific)
  - Magic Constructs (token-like)
  - Compound Constructs
    - Expressions
    - Statements
  - Semantic Analysis (Checks)
    - Type Check
    - Scope check
    - Identifiers Check
    - Fn Parameter/Arguments Check
    - Fn Hoisting (JS)
- Run-Time
  - Stack Frame
  - Line-by-Line
  - Execution Variants
    - Concurrency vs Parallelism
    - Single Thread vs Multi-threaded
    - Synchronous vs Asynchronous
- Prebuilts
  - Built-in Fns
  - Standard-Library

## _LANG CLASSIFICATION_
```md -------------------------
- Compiled, Interpreted or JIT
- Abstraction Levels
  - Low/Mid/High
- Paradigm
  - Imperative (Procedural)
  - Declarative (OOP, Functional)
```

## _TOKENS_
```md -------------------------
- Reserved Words
- Operators
  - Logical (and, or, not)
  - Arithmetic (+ - * / % **)
  - Relational (==, != > < >= <=)
  - Assignment
  - String
  - Bitwise
  - Type/Classification
  - Miscellaneous
- Delimiter ( (), [], {}, "", `` )
- Literals
  1. Simple
    - Numeric (int, floats)
    - String
    - Boolean
    - Nullish (null, None, undefined, etc)
  2. Complex/Aggregate
    - Static Array (used in low-level memory)
    - Dynamic Array (list, slice, array)
    - Map, Object
    - Language Specific Types
- Identifiers
- Punctuation (, ;)
- Other syntax units (magic)
- Whitespace*
```

## _SUGAR CONSTRUCTS_
- These are syntactic sugar. Not necessarily tokens, but still lexed during compile-time
- These are highly dependent on the lang are added for dev productivity (more concise code)

  ### Javascript
```js -------------------------
=> (arrow fn)
... (spread, rest)
`template literals ${with interpolation}`
- default params
- optional chaining
- ternary
```

  ### Python
```py -------------------------
- comprehensions
- f strings (string interpolation)
- ternary operator
- multiple assignment
- unpacking
- property decorator
```

```go -------------------------
- short var declarations
- composite literal
- empty interface
- variadic fn
- multiple returns
```

## _SYTX CONSTRUCTS_
### Expressions
```md -------------------------
- Operators-based
  - Logical
  - Arithmetic
  - Relational
  - Assignment
  - String
  - Types/Classification
  - Primary
  - Miscellaneous
- Fn expressions (lambdas)
- Other
  - List comprehensions (python)
```

### Statements
```md
- Ctrl Flow
  - Jumps
    - Exception Handling
    - Return
    - Yield
  - Conditionals
    - if else statements
    - switch
  - Loops
    - for
    - while-style
- Declarations
  - var
  - fns
  - classes*
- Expression-Statements
  - aka statements with side-effects
- Miscellaneous
```

## _BUILT INS_
- Usually fns that are available in the universe block
- What is implemented as a universe block
```md -------------------------
# Examples
- console.log || fmt.Println()
- len() in python
- sum() in python
```

## _STANDARD LIB_
- set of ready-to-use libraries that ship with a language
```md -------------------------
1. Basic/Core
2. Date/Time
3. Math
4. Network (http)
5. I/O (files)
6. Data Serialization (json)
```
<!--==================-->
# Lang Classification
<!--==================-->
- Compiled vs Interpreted?
- Static vs Dynamic Typing
- Abstraction Levels: Closeness from Machine Code
  - Low-Level: Assembly Language
  - Mid-Level: C, Golang
  - High-Level: More abstraction. Closer to human lang
- Paradigm-Supported
  1. Imperative: Commands (statements) listed in a step-by-step fashion
    - Procedural: Subset of imperative. But the commands are organized into reusable procedures or functions
  2. Declarative: Not how, but what a program does. User-level abstraction. Think git cmds
    - Object Oriented: Structures obj that encapsulates data & behavior. State changes
    - Functional: avoid changing state. No loops,but recursion instead. No loops,but recursion instead.

## _COMPILED/INTERPRETED_
### Steps
1. Lexing: Tokenization -- Lexer
  - Errors: Identify lexical errors: invalid chars
  - Irrevelant chars ignored: comments, whitespace (for most lang)
  - Lexer creates a token stream (a list of tokens) that are passed to the parser
2. Parsing: Syntax analysis -- Parser
  - Tokens are grouped together into meaningful constructs
  - Parser creates an `AST` which is used by the semantic analyzer
3. Semantic analysis -- Semantic Analyzer
  - Type checking
  - Scope Management
    + Fn literals might contain closures.Analysis ensures that the captured variables from closures are accessible and valid within the closure
  - Function/Method calls
    + Checks to make sure num/type of args matches
    + Checks to make sure fns are defined before invoked
  - Ctrl flow analysis
4. Intermediate Code Generation (bytecode)
5. Optimization and Code Linking
6. Code Generation (To machine code)
7. Code Execution (CPU or Interperter)

  ### Who Executes?
- A `Compiler` fulfills steps 1-6. The OS CPU executes the code the machine code after the code is generated
- An `Interpreter` fulfills steps 1-5. It skips step 6 and the interpreter runs the Intermediate Representation (IR) code line-by-line or statement-by-statement
- A `JIT Compiler` both the OS and the interpreter runs the code. The interpreter runs the code statement-by-statement. Meanwhile, the JIT compiler looks for hotspots, pieces of code that are frequently ran

  ### Memory Management During Execution
- Memory management is done during execution
- The stack and the heap are used for memory management during runtime
- In go, the go runtime is attached to the binary exec and it helps with the stack and heap management

## _PYTHON_
- Interpreted/compiled
- Dynamic Type
- High Abstraction
- Multi-Paradigm
  - OOP (Dynamic Inheritance..supports multi-inheritance)
  - Functional
  - Procedural

## _GOLANG_
- Compiled
- Static Type
- Mid Abstraction
- Multi-Paradigm
  - Unique OOP (inheritance-less structs)
  - Functional
  - Procedural

## _JAVASCRIPT_
- JIT compiled
- Dynamic Type
- High Abstraction
- Multi-Paradigm
  - OOP (Prototype-based)
  - Functional
  - Procedural

<!--==================-->
# Program Lifecycle
<!--==================-->
- Programs have 2 phases
  1. Compile-time
    - Lexing
    - Parsing
    - Semantic analysis
  2. Run-time (execution)
    - Call stack, heap
    - garbage collection

- Closures are created during run-time

<!--==================-->
# Tokens
<!--==================-->
## _LITERALS_
  ### Primitives
- Numeric
  - Int
  - Floats
  - Other
- Strings
- Boolean
- Nullish

  ### Complex
- Dynamic arrays
- Maps
- Function
- Language Specific
  - Structs
  - Pointers

  ### JS
```js -------------------------
// primitives
let integer = 1
let float = 1.0
let _NaN = NaN
let infinite = -(Infinity)
let zeroes = -(0)
let big int = 1n
let symbol = Symbol("foo")

let string = "string"
let boolean = true
let undef = undefined
let null = null

// complex
let dyArray = [1, "string", "other"]
let map = {
  a : 1,
  b : 2,
}
function funcT(param) {
  console.log()
}
let set = new Set(1,2,3)
```

  ### Python
```py -------------------------
# Primitives
integer = 1
float = 2.0
string = "string"
boolean = True

# Complex
tupe = (1,2,3,"four", true)
lst = [1,2,3, "four"]
rnge = range(2,7)
dict = {"one": 1, "two": 2}
set = {"a", "b", "c"}
fr_set = fronzenset([1,2,3])
none = None # Special type of noneType

# use type hints for fns only (params, return value) only
def greet(name: str, name2: int) -> bool:
  print("this is a fn")
anon_fn = lambda x: x + 1
```

  ### Golang
```go -------------------------
package main

main () {
  integer := 1
  float := 2.0
  boolean := true
  string := "string"
  rune := "a" // 97
  pointer := &integer

  staticArray := [5]int
  slice :=  []int{1,2,3}
  map := map[string]int{
    "a": 1,
    "b": 2,
  }
  func test(name, name2 int, strings ...str) bool, int {
    fmt.Printf("%v %v %v", name, name2, strings)
    return true, 1.0
  }

  type Fruit struct {
    Name string
    Qty int
  }

  type Quantifiables interface {
    getQty() int
  }

  func (f Fruit) getQty() int {
    return f.Qty
  }
}
```
<!--==================-->
# Reserved Words
<!--==================-->
- words that are used by the language for some special purpose
- reserved words are barred from being used by identifiers (var names)
- In JS, reserved words are divided into keywords (words actively being used by the JS lang & non-keywords)
- In PY, reserved words are
  - There are regular reserved words
  - There are soft keywords (words reserved under specific contexts) `match, case, _ , type`

<!--==================-->
# Operators
<!--==================-->
- special symbols/keywords that let you perform actions on values called operands
- there are some lang-specific operators, but there's usually a set of common operators
```md -------------------------
## Logical
- and `&&`, or `||`, not `!`
- *`??` in js
a
## Assignment `=`
- used to input value into a var

## Relational
- Comparison (aka Lopsided)
  - `>, >=, <, <=`
- Equality/Inequality `==` `!=`

## Arithmetic
- `+ - / %`
- some lang have `**`

## Type/Classification
- Sometimes implemented as a built-in
- usually looks like operator `in, includes, of, etc`

## Miscellaneous
- These operators don't fit into any other categories, * signifies not all lang

- Type* `in, includes, of`
- Fn invocation `()`
- Bracket Notation `[]`
- Dot Notation `.`
- Ternary*
- String Concat*
- Rest and Spread
```

<!--==================-->
# Compound Constructs
<!--==================-->
## _EXPRESSIONS_
- Operator-based
- Fn Expressions
- Special
  - List comprehensions (py)

## _STATEMENTS_
  ### Ctrl Flow
- Jumps
  - Return
  - Exceptions (`try, catch, finally`)
  - Yield
- Conditionals
  - `if/else`
  - `switch`
- Loops
  - `for`
  - `while-style`

  ### Declarations
- Variable
- Constant
- Fn
- Class*
- go/async fns

  ### Expression-Statement
- Statements with side-effects

  ### Miscellaneous
- empty, compound statements

<!--==================-->
# Standard Library
<!--==================-->
- Depending on the lang, some fn may be implemented not as a method, but these
fns should all be there
  - For ex, `length` is implemented
    - Py: `len()` builtin method
    - Go: `len()` builtin method
    - JS: `.length` is a property

## _CORE DATATYPE_
- common non-method actions on datatypes

  ### String, Dy-Array, Dict
    #### Elem Access
- String, Array, Dict
- `[]`

  ### String
    #### Access
- length
- char access
- get substring
- get rune (code pt)

    #### Search
- Anchored
- Inclusion
- All matches
- Indexed Search
- Regexp Search*

    #### Manipulation
- Whitespace
  - Padding
  - Trimming whitespace edges
- Casing (Upper, Lower, TitleCase)
- Replace
- Transform to Array

  ### Dy-Array
    #### Access
- length
- elem Access
- get Subsection

    #### Search
- Inclusion
  - One/Some/Every
- Indexed Search
- Filter

    #### Manipulation
- Add elems
- Remove elems (pop, shift)
- Fill elems
- Transform to String
- Map Transformation

    #### Ordering
- reverse
- sort

  ### Dictionary
    #### Base
- Access O(1)
- length
- copy the dict
- merge 2 dicts
- iterate over a dict

    #### Property Config
- configurable, writable, enumerable
- seal
- freeze

    #### Manipulation
- Add key-value pairs
- Delete pairs
- Update key-value pairs
- Check if key exists

    #### Transform Array
- from keys
- from values
- from entries

  ### Math
- random
- square root

  ## Date/Time
- get current date,time
- set date/time



  <!--==================-->
# Resources
  <!--==================-->
- [Python Lexical Analysis](https://docs.python.org/3/reference/lexical_analysis.html#delimiters)



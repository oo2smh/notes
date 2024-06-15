<!--==================-->
# 🔑 Keywords
<!--==================-->
```md
- Expressions
🎀 ANT FARM PLC (Ant Farm Programmable Logic Controller)
  - Assignment
  - New Keyword
  - Ternary
  - Function
  - Arithmetic
  - Relational
  - Miscellaneous
  - Property Access
  - Logical
  - Classification
🎀 POE
  - Primary
  - Object Initializer
  - Eval
- Statements
  - Control Flow
  - Declarations
  - Miscellaneous
- Expression-Statements
- Syntax Constructs
  - Computed Property
  - Default Syntax
  - Destructuring
  - Rest
  - Spread
```
<!--==================-->
# 🪲 Deets
<!--==================-->
## _Expressions_
> [!Important]
>Expressions are anything that evaluates to a value. The value that it evaluates to is called a `return value`. This includes simple `primary` values such as (1, 'string', true). However, it typically refers to expressions with more than 1 value. Most of the expressions are based off of the operator that it uses. These types of expressions are called `operations`. The other expressions I am calling `other-expressions`. Original I know.

<details><summary>🐝 Operations </summary>

> Operations are expressions that feature an operator. Operators have two main concepts associated with them: `precedence` and `associativity`. Precedence and associativity can be offset by using `()` the grouping operator which has the highest precedence. Associativity is not relevant in most cases either. So I will not mention either one of these concepts. What I will mention are the preferred datatype operands of each operation along with the return value. Coercion will also be mentioned along with any strange quirks.

### Assignment
```toml
[Primary]
usage = "variables"
returns = "Value assigned to the variable on the right hand side"
useful_return = false
associativity = "RTL"

[Gotchas]
let_const = "When used with let || const = does not equate to assignment"
obj_references = "Objects are stored as ref"
```
### New
```toml
usage = 'used to create instances'
cxt = 'constructor fns & class syntax'
returns = 'instance obj'
````

### Ternary
```toml
[Primary]
usage = "var assignment and return values"
returns = "one of 2 values based on truthiness of condition"
useful_return = true

[Gotchas]
prefer_if = "Use if/else if actions need to be performed"
```

### Function
```toml
[Primary]
returns = 'undefined or value following return keyword'
variants = "regular, arrow"
usage = "non hoisted fn usage"

[Gotchas]
arrow_implicit = "arrow fns have single line implicit return"
arrow_xcution = "arrow fns do not have their own exec cxt"
```

### Arithmetic
```toml
[Primary]
returns = 'number'
variants = "+,-,*,/,**,%, ++, --"
usage = "Mathematical operations"
return_value = "number"

[Gotchas]
coercion = "Operands are coerced to numbers"
```

### Relational
```toml
[Primary]
returns = 'boolean'
variants = ["comparison", "equality", "inequality"]
variants.comparison = [">,>=, <,<="]
variants.equality = ["===","=="]
variants.inequality = ["!==", "!="]
usage = "ctrl flow condition, values check"

[General Coercion]
primitiveHierarchy = 'BigInt > Number > String'
NaN = 'NaN as operand always results in false'

[Comparison Coercion]
errors = 'symbols will result in TypeError'
str-str = 'Comparison is lexicographical'
nonStrPrim-Prim = 'Coerced to num. Compared numerically'
nonstr-obj = 'obj:prefers-num coercion'
obj-obj = 'obj:prefers-num coercion'
str-obj = 'obj:prefers str coercion'

[Equality Coercion]
symbol-symbol = 'compared by reference'
obj-obj = 'compared by reference'

[Loose Equality]
nullish = 'null ==(=) undefined and nothing else'
bnb = ['Boolean', 'Number', 'BigInt']
bnb-primitive = 'primitive coerced to Number -> BigInt'
bnb-obj = 'obj:prefers-num coercion'
bnb-str = 'obj:prefers-str coercion'
```

### Miscellaneous
```toml
symbol-variants = ['comma', 'grouping', 'invocation']
keyword-variants = ["delete", "await", "void"]
useful_return = false
```

### Property Access
```toml
[Primary]
variants = "Dot and Bracket Notation"
usage = "Object Access/Assignment. String Idx Access"
returns = "indexed element"
useful_return = true

[Gotchas]
dot_bracket = "Use bracket for dynamic access/assignment. Dot everywhere else"
```

### Logical
```toml
[Primary]
returns = 'boolean'
variants = "&&, ||, !, ??*"
usage = "ctrl flow condition"

[Gotchas]
short_circuits = "when 1st operand is chosen"
nullish = "??. It's a pseudo logical operator"
```

### Classification
```toml
types = ["in", "instanceOf", "typeof"]

[in]
returns = 'boolean'
deets = 'checks if prop is in obj'

[instanceOf]
returns = 'boolean'
deets = 'checks if obj is instanceOf parentObj'

[typeOf]
returns = 'string of type'
deets = 'checks the type of value'
gotchaNaN = 'Not accurate for NaN. Use Number.isNaN()'
gotchaArr = 'Not accurate for Arrays. Use Array.isArray()'
gotchaNum = '+/-Infinity, NaN are all numbers'
gotchaNull = "typeof null => 'object'"
```
</details>

<details><summary>🐝 Other Expressions</summary>

```toml
[Primary]
# primitives, identifiers, this
types = ['primitives', 'identifiers', "this"]

[Object Initializers]
types = 'obj/arr literals {} & []'

[Eval()]
usage = 'avoid. security issues. Redudant'
deets = 'global fn. evaluates arg to value'
```
</details>

## _STATEMENTS_
> [!Important]
> A statement performs an action. It doesn't return a value like an expression. Statements can hold expressions/statements.

### Ctrl Flow
> [!Note]
> By default, code is ran top to bottom, LTR. Left to its devices, that's how code is ran. Ctrl flow statements allow you to overthrow this natural order and move to a different part of code.

<details><summary>🐜 Jumps</summary>

> Jump statements are keywords that transports you to a different part of code. In JS, this movement is in relation to blocks.
```yaml
throw: throws an error, transports you to catch || terminate prog
break: exits loop
continue: exit iteration. Move to next iteration
return: exits fn. Returns value after keyword back to calling fn
```
</details>

<details><summary>🐜 Conditionals</summary>

> Conditionals are forks in the road. If the condition is met, do a. Otherwise, do b.
```yaml
if/[else]/[else if]: og conditional
switch: if condition matches cases, run case block
```
</details>

<details><summary>🐜 Loops</summary>

> Check a condition. As long as it's true, run code block. To prevent running for infinity, loops usually feature an exit condition. The other common parts of loops are `condition`, `ctrl var` and an exit condition. The `for loop` packages up these common parts into one package.

```yaml
while(cond): generic loop
do..while(cond): while loop where block is ran at least once
for(init; cond; afterthought): loop when you know how many times to loop
```
</details>

### Declarations
<details><summary>🐜 Declarations</summary>

```yaml
- var: [let, const, var]
- class: syntactical sugar of fn constructor
- import/export: module
- function: hoisted fns
- async: [async, await]
```
</details>

### Miscellaneous
<details><summary>🐜 Exceptions </summary>

```yaml
try: block that allows you to safely/silently try code
catch: runs with try, catches errors
finally: runs regardless of whether there was an error or not
```
</details>

<details><summary>🐜 Other </summary>

```yaml
empty: no real usage. Ex is for loop with empty block
use strict: enforces stricter rules
with: deprecated.
label: can name your loops to break/continue out in nested loops
compound: conditionals, loops are compound statements
debugger: can set a breakpoint
```
</details>

## _EXPRESSION STATEMENTS_
> Expression statements are a combination of expressions and statements. They are expressions because they return a value and they are statements because they perform some kind of action. What counts as an action is not completely clear to me. What is clear is that var assignments, fn invocations, obj mutation, and any `side effects` mentioned in LS count as an action where statements are concerned.

```yaml
assignment: returns what's assigned, assigns
invocation: returns result of fn, also invokes
delete: returns boolean, mutates obj
(pre/post)increment: return (pre/post)incremented num, reassigns
(pre/post)decrement: return (pre/post)decremented num, reassigns
```

## _SYNTAX CONSTRUCTS_
> These constructs are often later additions. These can be shorthands that combines the function of multiple expressions/statements. Or they can be a more concise way to do something that's previously possible. These do not fit in as neatly into the other boxes of expressions, statements and expression-statements.

```yaml
arrow fn: fn expression with quirks
destructuring: allows for easy multi var declarations
spread: expands contents of iterable into DS or fn invocation
rest prop: rest syntax used as last part of destrcturing syntax
rest param: last param of fn. Bundles args of an array
default param: concise way to set default param in fn param
```
<!--==================-->
# 🧪 Examples
<!--==================-->
```js
// Operations
let x = 3;
let y = x > 3 ? 'a' : 'b'
```

<!--==================-->
# 📗 Reference
<!--==================-->
- [Obj to Primitive Coercion](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures#type_coercion)

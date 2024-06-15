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

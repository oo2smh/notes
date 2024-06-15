<!--==================-->
# 📣 Commands
<!--==================-->
## _CONTEXTS_
> [!Note]
> The regex modes remind me of vim modes. Char classes and grouping are similar and differ in that char classes target 1 char at a time while grouping chars can contain a sequence of characters. Grouping context is also specifically used for capturing groups.

```yaml
Pattern: Default mode. Global scope
Char Class: Targets valid chars and range
Grouping: Multichar selection. Grouped for capturing groups or alternation
```
```js
let pattern = /pattern/
let charClass = /[a-z0-9]/
let grouping = /(cat | dog)/
```

## _METACHARACTERS_
> Special symbols/chars with some functionality
### MetaCharacter Categories
```yaml
Context Setters: Sets matching cxt
Anchors: Match positionally (start/end) of characters
Quantifiers: Specify number or number range
Char Class: Metacharacters used specifically in char class cxt
Other: Don't fit into the other buckets
```
```md
# Context Setters
- `/`, `()`, `[]`

# Anchors
- `^`, `$`

# Quantifiers
- `{}`, `*`, `+`, `?`

# Char Classs
- `^`, `-`

# Other
- `.`, `\`, `|`
```

## _MODIFIERS_
> Options that are placed at the end of a pattern cxt that affects the whole cxt
- `g`: Global flag affects all matches. By default, it's only the 1st match
- `i`: Case insensitive flag
- `m`: Multiline. Changes how `^,$` works. Match end ofeach line within str instead of start/end of whole string

## _SHORTHANDS_
> Predefined char classes. Uppercase version is the inverse/negation of the lowercase shorthand. `\D` = everything that's not `\d`  for example.
```md
- `\d`: [0-9]
- `\w`: [a-z0-9_]
- `\b`: Anchor that matches any `\w` separated by `\W` char
- `\s`: Whitespace char [\n, \r, \t] = newline, carriage return, tab
```

## _ASSERTIONS_
> Special syntax that is comprised of the `main pattern(MP)` and `assertion pattern(AP)`. The target pattern is checked to see if it's preceded/followed by the assertion pattern. If it is, the target pattern is returned. I am specifically referring to `look___ assertions`. Note that MDN considers other regex symbols such as `\b,$,^` to be assertions.

> [!Important]
> The basic syntax of look assertions consists of the `MP` and the `Assertion Syntax (AS)`. The AS consists of the `assertion syntax (?=pattern)`. The pattern is the `assertion pattern`. There are slight differences in the assertion syntax. For lookahead assertions they always start with `(?)`. Positive ends with `=`. Negative ends with `|`. For lookbehind assertions, they always start with `(?<)`. Positive assertions end with `=`. Negative assertion ends with `!`.

- Lookahead `MP(?=AP)`
- Lookbehind `(?<=AP)MP`

These 2 types have a negated version
- Neg(Lookahead): `MP(?|AP)`
- Neg(Lookbehind) `(?<!AP)MP`

```js
let name = "jack will smith";
let posLookahead = /will(?= smith)/
let posLookbehind = /(?<= ack)/
let negLookahead = /will(?=| dog)/
let negLookahead = /will(?=| dog)/
let negLookbehind = /(?=! dog)will/

// Note that there is a space before smith and ack.
// Assertion pattern has to match exactly which includes whitespace.

posLookAhead.test(name) // true
posLookbehind.test(name) // true
negLookAhead.test(name) // true
negLookbehind.test(name) // true
```

## _CAPTURING GROUPS_
> What's a capturing group(CG)? It's a group that is saved and can be referenced later on. By default, with any regex, it is saved to the CG0. For example, the regex `/willy/` will capture the 1st instance of 'willy' and slot that into CG0. You can also explicitly add capturing groups. Whenever you use the `()` metacharacter, you are creating a CG. `/(wi)(lly)/` has 3 capturing groups. Everything between `/ /` is CG0, the match `(wi)` is CG1 and `(lly)` is saved to CG2. You can reference these captured groups to find/replace using `$`. $1 refers to capturing group 1. You can also use capturing groups within the regex itself using `\`. `\0` refers to CG0 within the regex. When the CG is used within the regex, it is referred to as a `backreference`.

<!--==================-->
# 📗 References
<!--==================-->
- [Coding Train: Capturing Groups](https://www.youtube.com/watch?v=c9HbsUSWilw)
- [Coding Train: Backreference](https://www.youtube.com/watch?v=Z66TeSTcP-Q)

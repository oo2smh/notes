<!--==================-->
# 🗺️ Legend
<!--==================-->
```md
⏎: return
[value = 10]: opt param = defaultValue
...(): (...) indefinite amt of params (datatype)
🤡: gotcha
🤬: arguments
❌: error
🚑: param
🚸: actions taken
👺: destructive method
🐛: coercion
()P: (Datatype).prototype
```
<!--==================-->
# 🔮 Syntax
<!--==================-->
> [!Note]
> To make things more concise, I will omit writing out the first part of instance methods/properties. For instance, `String.prototype.at()` will be written as `SP.at()`. This applies only to instance methods/properties. For static methods, I will write out the full name. `Object.keys()` will be written instead of the abbreviated `O.keys()`. This is in order to be able to visually distinguish between static and instance methods.

## _CONSTRUCTORS_
> `Value` parameter can be any datatype. Constructors yank the value and return a new value of their own datatype. `Symbol(value)` will for instance, take the value and return a new symbol. Generally, this is the extent of the functionality of constructors. It is more of than not better to use the literal ways to create values (`{}` to create obj, `[]` to create arrays, `''` for strings, etc). This is more concise and cleaner. However, it is good to be aware that constructors exist.

```js
Symbol(value)  // ⏎ symbol
Boolean(value) // ⏎ boolean
Number(value)  // ⏎ number
BigInt(value)  // ⏎ bigInt
String(value)  // ⏎ string
Object(value)  // ⏎ object
Array(...elemsN) || Array(arrayLength) // ⏎ array
Function([...argumentsN], functionBody) //  ⏎ function
```

## _IMPLICIT COERCIONS_
```js
const validDatatypes = [Symbol, Boolean, Number, BigInt, String, Object, Array, Function]
validDatatypes[#].prototype.valueOf()
validDatatypes[#].prototype.toString()
```

## _CORE_
<details><summary>🐝 String</summary>

### One Offs
> One-offs are properties and methods that I could not fit into any of the other buckets.
```js
String.fromCodePoint(...intN)
SP.length
```
### Search Methods
```js 🎀 SEIM MISL (Search Event Info Management MISL)
SP.startsWith(value)
SP.endsWith(value)
SP.includes(searchString, [fromIdx = 0])
SP.match(regex)
SP.matchAll(regex)
SP.indexOf(searchElem, [fromIdx = 0])
SP.search(regex)
SP.lastIndexOf(searchElem, [fromIdx = 0])
```
### Access
```js 🎀 CACCeSS (Char ACCeSS)
SP.charAt(idx)
SP.at(idx)
SP.codePointAt(idx)
SP.charCodeAt(idx)
SP.slice([startIdx = 0], [endIdx = str.length])
SP.substring([startIndex = 0], [endIndex = str.length])
```
### Manipulation
```js 🎀 PCPR TTT RRTT S (PC Public Relations | Tic Tac Toe | Rotorrest Treatment Table | Sleep)
// ELONGATE
SP.padStart(targetLength, [padding = ' '])
SP.concat(...strN)
SP.repeat(count)
SP.padEnd(targetLength, [padding = ' '])

// TRIM
SP.trim()
  SP.trimStart()
  SP.trimEnd()

// SUBSTITUTE
SP.replace(pattern, replacement)
SP.replaceAll(pattern, replacement)
SP.toUpperCase()
SP.toLowerCase()

// SPLIT into Array (Transmutation to array)
SP.split(separator) // ⏎ array
```
</details> <!---------------------->

<details><summary>🐝 Number</summary>

> Number methods can be roughly divided by their utility (1) Conversion to Number (2) Number Subtype (3) Check Specify Number of Placeholders
```js 🎀 4Is TPTP
Number.isFinite(value)
Number.isInteger(value)
Number.isNaN(value)
Number.isSafeInteger(value)
Number.parseInt(string)
Number.parseFloat(string, [radix = 10])
NP.toFixed([digits = 0])
NP.toPrecision([precision])
```
</details> <!---------------------->

<details><summary>🐝 Object</summary>

> Note that `Arrays` and `Functions` are also considered to be specialized objects. These object methods, therefore, are available to these arrays and functions as well.

```js 🎀 HI CA KEV SIFI
Object.hasOwn(obj, prop)
Object.is(val1, val2)
Object.create(proto, [propsObj])
Object.assign(target, ...sources)
Object.keys(obj)
Object.entries(obj)
Object.values(obj)
Object.seal(obj)
Object.isSealed(obj)
Object.freeze(obj)
Object.isFrozen(obj)
```
</details> <!---------------------->

<details><summary>🐝 Array/Static</summary>

```js Array Static Methods
Array.isArray(value)
Array.of(...elemN)
Array.from(arrayLike, [mapFn(elem, idx)], [thisArg])
```
</details> <!---------------------->

<details><summary>🐝 Array/Instance</summary>

```js 🎀 USPP FSRS JAIS IF(US is peeing | Federal Shortage Restroom Stations Join AIS Fixed Income)
const AP = Array.prototype
🅿️ AP.length
👺 AP.unshift(...elemsN)
👺 AP.shift()
👺 AP.push(...elemsN)
👺 AP.pop()
👺 AP.fill(value, [start = 0], [end = arr.length])
👺 AP.splice(start, [deleteCout = 0], [...items])
👺 AP.reverse()
👺 AP.sort(compareFn(a,b))

   AP.join([separator = ','])
   AP.flat([depth = 1]) //

// String Counterpart
   AP.includes(searchElem, [fromIdx = 0]) // ⏎ boolean
   AP.lastIndexOf(searchElem, [fromIdx = 0])
   AP.indexOf(searchElem, [fromIdx = 0])
   AP.at(idx) // ⏎ elem at given idx
   AP.slice([start = 0], [end = arr.length]) // ⏎ shallow arr copy
```
</details> <!---------------------->

<details><summary>🐝 Array/Higher Order</summary>

```js 🎀 MR RES 5FFFFF
AP.map(callbackFn, [thisArg])
AP.reduce(callback(accumulator, currentValue, currentIdx, array), [initValue = array[0]])
AP.reduceRight(callback(accumulator, currentValue, currentIdx, array), [initValue = array[0]])
AP.every(callbackFn, [thisArg])
AP.some(callbackFn, [thisArg])
AP.forEach(callbackFn, [thisArg])
AP.filter(callbackFn, [thisArg])
AP.find(callbackFn, [thisArg])
AP.findIndex(callbackFn, [thisArg])
AP.flatMap(callbackFn, [thisArg])
```
</details> <!---------------------->

## _OTHER_
<details><summary>🐝 Math</summary>

```js 🎀 SR Military Management Fund CRAp
Math.sqrt(number);
Math.random();
Math.min(num1, num2, num3, num4);
Math.max(num1, num2, num3, num4);
Math.floor(number);
Math.ceil(number);
Math.round(number);
Math.abs(number);
```
</details> <!---------------------->

<details><summary>🐝 RegExp</summary>

> 2 ways to create regex. Normally you want to use *literal notation* `/regexp pattern here/`. However, if you want to pass a dynamic value aka a value stored in a variable, use the *constructor* function using the `new` keyword.
```js
RP = RegExp.prototype
RP.test(value) // ⏎ boolean
```
</details> <!---------------------->

<details><summary>🐝 Date</summary>

```js 🎀 DM HMS FMD (foot mouth disease)
const dateObj = {
  seconds: date.getSeconds(),
  minutes: date.getMinutes(),
  hours: date.getHours(),
  dayOfWeek: date.getDay(),
  dayOfMonth: date.getDate(),
  month: date.getMonth() + 1,
  year: date.getFullYear(),
}
```
</details> <!---------------------->

<details><summary>🐝 Console</summary>

> `Console` object can be accessed from any global object. The goal of `console` is to output to the user. Most of the methods are some form of variation or some way to support this function. In the browser console, these `console` messages are shown in different colors
```js
// CONSOLE
console.warn()
console.error()
console.log()
console.trace([objects]
```
</details> <!---------------------->

<!--==================-->
# 🪲 Deets
<!--==================-->
## _STRINGS_
<details><summary>🐜 One-Offs </summary>

> Unicode is the encoding standard that maps a human readable character like `[a,b,1,2]` into a `code point`. A code point is a numerical representation of the character. Unicode uses hexadecimal (base 16) to represent the characters in a format of `U+xxxx`. UTF-8 and UTF-16 are both encoding systems. UTF-8 and UTF-16 are both encoding system that maps the Unicode code point into a binary machine code. The difference between them is that UTF-8 uses 8 bits to map out the code point while UTF-16 uses 16bits. Thus UTF-16 can encode more characters into binary.
>
> Note that both Unicode and UTF-16 both share the code point as a field. Therefore, in sources like MDN, the Unicode code point is sometimes referred to as the UTF-16 code point. These are referring to the same thing. Additionally, even though the code point is encoded in hexadecimal, decimal based numbers (0-9) are more intuitive for humans. For this reason, methods such as `fromCharCode()` expects a decimal number and it gets converted to its hexademical equivalent.
>
> Surrogate Pairs are used for high value code points. Code points are written in the form `U+xxxx`. Some symbols require more than the 4 number slots. Take the number `U+10000`. This isn't valid and therefore needs to be broken down into multiple code points that are chunked into one whole. `U+10000` = `{U+D800, U+DC00}`.

```toml
[String.fromCodePoint(...intN)]
params = 'UTF-16 code points in decimal format'
return = 'string of code points'
coercion = 'arg -> integer'
errors = 'RangeError if arg is NaN, < 0, or greater than 0x10FFFF'

[SP.length]
return = 'integer of str length in UTF-16 code points'
gotchas = 'surrogate pairs count as length of 2'
```
</details>

<details><summary>🐜 Search Methods</summary>

> All search methods coerce their argument to either a string or regex. Search methods can broadly be divided by their 1st argument. String vs regex. For string-arg methods, their 1st parameter always defaults to `undefined` and there is an optional `pos` param. For regex-arg methods, they have 1 parameter which defaults to `/(?:)/`. This is a `non-capturing group` which is essentially allowing you to use the `()` without capturing the pattern result into a capturing group. Practically speaking you can think of the regex param as defaulting to `''`.

### Search Types
- General Search `SP.includes()`
- Anchored Search `SP.startsWith()` `SP.enddsWith()`
- Indexed Search `SP.indexOf`, `SP.lastIndexOf`, `SP.search()`
- Iterable/Array `SP.match()`, `SP.matchAll()`

```md
# SP.startsWith(searchStr = 'undefined', [pos = 0])
# SP.endsWith(searchStr = 'undefined', [pos = str.length])
# SP.includes(searchStr = 'undefined', [pos = 0])
<!--==================-->
- par-searchStr = 'Any non-regex valid value'
- par-pos = 'position to start search'
- return = 'boolean'
- invalid_args = 'regex -> TypeError'
- coercion = 'arg coerced to str'

# SP.match(regex = /(?:)/)]
<!--==================-->
- return = 'array of matches || null (no matches)'
- coercion = 'arg -> regex'
- gotcha = 'use of g flag to get all matches, otherwise capture 1st match'
- gotcha = 'empty arg -> returns '']'

# SP.matchAll(regex = /(?:)/)]
<!--==================-->
- return = 'iterator obj of matches or empty iterator (no matches)'
- coercion = 'arg -> regex'
- errors = 'g flag is not present'

# SP.indexOf(searchStr = 'undefined', [pos = 0])
# SP.lastIndexOf(searchStr = 'undefined', [pos = 0])
<!--==================-->
- return = 'idx of 1st/last occurrence of searchStr || -1 (not found)'
- coercion = 'arg coerced to str'
- gotcha = 'empty searchStr results in pos'

# SP.search(regex = /(?:)/)
<!--==================-->
- usage = 'regex version of indexOf'
- return = 'idx of 1st match || -1 (not found)'
- coercion = 'arg coerced to regex'
- gotcha = 'g flag has no effect'
```
</details>

<details><summary>🐜 Access Methods</summary>

> There are many methods that do similar things with slight variances. It's good to be aware that these methods exist because other people might use a different method. However, for personal usage, I will default to my preferred way of doing things. For instance, for single character access, I will use `[]` for the most part or `at()` if I want to use negative indices. I will use `codePointAt()` over `charCodeAt()`. Lastly, `slice()` takes precedence over `substring()` because it can accept negative indices and thus makes it more flexible.
```md
# SINGLE CHAR ACCESS
<!--==================-->
param = 'idx integer'
coercion = 'arg -> int'

# SP.charAt(idx)
<!--==================-->
return = 'char at idx || empty str'

# SP.at(idx)
<!--==================-->
special = 'accepts negative idx'
return = 'char at idx || undefined'

# SP.charCodeAt(idx)
<!--==================-->
return = 'utf-16 code pt || NaN'

# SP.codePointAt(idx)
<!--==================-->
return = "utf-16 code pt || undefined"

# MULTIPLE CHAR ACCESS
<!--==================-->
params = '(idxStart = 0, [idxEnd = str.length])'
coercion = 'arg -> int'
gotcha = 'idxStart > str.length || idxEnd > idxStart => empty str'

# SP.slice([idxStart = 0], [idxEnd = str.length])
<!--==================-->
special = 'can accept negative indices'

# SP.substring([idxStart = 0], [idxEnd = str.length])
<!--==================-->
gotcha = 'idxEnd > idxStart => they are swapped'
```
</details>

<details><summary>🐜 Manipulation Methods</summary>

### Elongation
```md
# SP.pad(Start/End)(targetLength, [padString = ' '])
<!--==================-->
return = 'str of targetLength with padString added to start/end'
gotcha = 'if targetLength < str.length => og str'

# SP.concat(...str)
<!--==================-->
coercion = 'args -> str'
return = 'concatenated str'

# SP.repeat(count)
<!--==================-->
return = 'str repeated count times'
errors = 'RangeError, if negative or maximum string length (Infinity)'
```
### Trim
```toml
[SP.trim(), SP.trimStart(), SP.trimEnd()]
# ==================================
return = 'str stripped of whitespace or line terminators (/n,/r,/t)'
```

### Substitution
```toml
[SP.replace(pattern, replacement), SP.replaceAll()]
# ==================================
par-pattern = 'str or regex'
par-replacement = 'str or fn'
return = 'new str with 1st pattern replaced'
gotcha = 'use g flag to replace all patterns'
errors = 'TypeError if replaceAll is missing g flag'

[SP.toLowerCase(), SP.toUpperCase()]
# ==================================
return = 'new str with a-z chars (lower|upper)cased'
```

### To Array
```md
# SP.split(sep, [limit])
<!--==================-->
par-sep = '(str, regex) pattern where split should occur'
coercion = 'sep -> str'
return = 'array of elems'
```
</details>

## _ARRAYS_
<details><summary>🐜 Core Methods</summary>

### Static
```md
# Array.isArray(value)
<!--==================-->
usage = 'a better typeof'
return = 'boolean'

# Array.of(...elemsN)
<!--==================-->
return = 'new Array instance'

# Array.from(arrayLike, [mapFn], [thisArg])
<!--==================-->
par-arrayLike = 'iterable or arrayLike object [map,set,str,nodelist]'
par-mapFn = 'mapFn(elem, idx)'
return = 'new Array instance'
```

### Sole Property
```toml
[AP.length]
# ==================================
return = 'int of # of elems'
gotcha = 'counts empty slots'
errors = 'setting length to neg num or num > 2^32'
```

### Destructive
```md 🎀 USPP FSRS
# AP.(unshift/push)(...elems)
<!--==================-->
action = 'Adds ...elems to calling array (start/end)'
return = 'new length'

# AP.(shift|pop)()
<!--==================-->
action = "Removes last elem"
return = "removed elem || undefined for empty array"

# AP.fill(value, [start = 0], [end = arr.length])
<!--==================-->
action = 'fills range of array with param value'
coercion = 'start/end -> int'
return = 'modified array'

# AP.splice(start = 0, [deleteCount = arr.length], [...itemsN])
<!--==================-->
par-deleteCount = 'elems to delete from start'
par-itemsN = '...items to add from start'
special = 'start can accept neg indices'
return = 'arr containing deleted elems [] (no elem removed)'
coercion = 'start/deleteCount -> int'

# AP.reverse()
<!--==================-->
return = 'arr with elems reversed'

# AP.sort([compareFn(a,b)])
<!--==================-->
return = 'default = lexicographical sort || callbackFn return'
compareFn = 'a = 1st elem, b = next elem'
<!--==================-->
posReturn = 'a should come after b'
negReturn = 'a should come before b'
0orNaN = 'a === b. Og order should be kept'
a-b = 'ascending order'
b-a = 'descending order'
```

### Non-Destructive
```md JF I LISA (Jimmy Fallon I Lisa)
# AP.join(glue = ',')
<!--==================-->
return = 'string separated by glue'
gotcha = 'nullish elems converted to empty str'

# AP.flat([depth = 0])
<!--==================-->
par-depth = 'level to be flattened'
return = 'new array with sub-array elems concatenated to it'
```

```md 🎀 I LISA
# String Counterparts
- These are essentially the same as the str methods. Look above for more info

AP.indexOf(searchElem, [pos = 0])
AP.lastIndexOf(searchElem, [pos = 0])
AP.includes(value)
AP.slice([startIdx = 0], [endIdx = arr.length])
AP.at(idx)
```
</details>

<details><summary>🐜 Higher Order Fns</summary>

> All higher order fns have a `callbackFn(elem, idx, array)` and an optional `[thisArg]` The exception is `reduce` and `reduceRight`. It has an additional param `total/accumulator`. All higher order fns that return an array will return a shallow array. There are no destructive methods in this group.

```md 🎀 MR RES 5FFFFF
# ALL
<!--==================-->
callbackFn(elem,idx,arr) = '1st param'
thisArg = '2nd param'

# AP.map(callback)
<!--==================-->
return = 'new array with each elem transformed from callback'

# AP.(reduce|reduceRight)(reducer(total, elem, idx, arr), [initValue = arr[0]])
<!--==================-->
reducer.total = 'value from prev call of reducer'
reducer.elem = 'current element'
reducer.idx = 'current idx'
initValue = 'total value when reducer is 1st called'
return = 'value from calling reducer over entire array'
error = 'TypeError if initValue is empty and [ ] is empty'
reduceRight = 'starts from the right'

# AP.(every|some)(callback)
<!--==================-->
some = 'false unless callbackFn returns a truthy value for an arr elem'
every = 'true unless callbackFn returns a falsy value for an arr elem'
return = 'boolean'

# AP.forEach(callback)
<!--==================-->
action = 'perform iterative action on every elem'
return = 'undefined'

# AP.find(callback)
<!--==================-->
return = 'returns 1st instance that satisfies testing fn'

# AP.findIndex(callback)
<!--==================-->
return = '1st idx of elem that satisfies the testin fn'

# AP.filter(callback)
<!--==================-->
return = 'shallow arr of all instances that passes testing fn'

# AP.flatMap(callback)
<!--==================-->
return = 'new arr, each elem flattened by depth of 1, transformed by callback'
deets = 'same as calling map() followed by flat()'
```
</details>

## _OBJECTS_

<details><summary>🐜 Identification/Creation</summary>

### Identification
```toml
[Object.hasOwn(obj,prop)]
# ==================================
action = 'tests if prop exists in obj'
return = 'boolean'
# same as OP.hasOwnProperty(prop)

[Object.is(val1, val2)]
# ==================================
deets = 'A better ==='
return = 'boolean'
special = 'works with NaN and nullish val'
```

### Creation
```md
# Object.create(proto, [propsObj])
<!--==================-->
par-proto = 'proto obj of newly created obj'
par-propsObj = 'setting higher own properties in new obj'
special = 'used to set enumerable,writable, configurable settings for props'

# Object.assign(target, ...sources)
<!--==================-->
par-target = 'new return obj'
par-sources = 'objs to extract props to add props to target'
return = 'target obj'
gotcha = 'no dupes in props. Later instances overwrite prev prop'
```
</details>

<details><summary>🐜 ToArray/Fortify </summary>

### To Array
```toml
[Object.keys(obj)]
# ==================================
return = 'arr of obj own-enumerable keys'

[Object.entries(obj)]
# ==================================
return = 'matrix of enumerable [key,value]'

[Object.values(obj)]
# ==================================
return = 'arr of obj own-enumerable values'
```

### Fortify (Seal/Freeze)
```toml
[Object.seal(obj)]
# ==================================
deets = 'prevents extensions. Cannot add new props. Cannot delete existing props'
par-obj = 'obj to seal'
return = 'sealed obj'

[Object.isSealed(obj)]
# ==================================
return = 'boolean'

[Object.freeze(obj)]
# ==================================
return = 'frozen obj'
deets = 'sealed. Existing props not modifiable'
deets = 'Attempt to add will fail silently or throw TypeError(strict mode)'

[Object.isFrozen(obj)]
# ==================================
return = 'boolean'
```
</details>

## _NUMBERS_
<details><summary>🐜 Numbers </summary>

```toml
# Number.isFinite(value)
# Number.isNaN(value)
# Number.isFinite(value)
# Number.isInteger(value)
# Number.isSafeInteger(value)
[All]
# ==================================
return = 'boolean'

[Definitions]
safeInteger = '(-/+)2^53 range'
finite = '[^(+/-)Infinity, NaN]'
```
</details>

## _MATH_
<details><summary>🐜 Math Basic</summary>

```toml
[Math.sqrt(num)]
par-num = 'number >= 0'
gotcha = 'num < 0 => NaN'
return = 'sqrt of num || NaN'

[Math.random()]
# ==================================
return = 'random float between [0,1)'

[Math.(min|max)(...numN)]
# ==================================
coercion = 'Number'
gotcha = 'NaN if any arg is NaN'
min-gotcha = 'Returns Infinity if no args'
max-gotcha = 'Returns -Infinity if no args'
```
</details>

<details><summary>🐜 Rounding</summary>

```md
# Math.round(num)
  * [Math.floor(num)]
  * [Math.ceil(num)]
<!--==================-->
return = 'rounded num'
round = 'IF num > 0.5 => round up ELSE round down'
ceil = 'Always round up'
floor = 'Always round down'

# Math.abs(num)
<!--==================-->
return = 'pos param num'
deets = 'works with floats too'
```
</details>

## _REST_

<details><summary>🐜 RegExp </summary>

```toml
[RP.test(str)]
# ==================================
deets = 'checks if str is in regex instance'
return = 'boolean'
coercion = 'all args coerced to strings'
```
</details>

<details><summary>🐜 Date </summary>

```toml
# all the below have get/set options
[Time Periods]
milliseconds = '[0-999]'
seconds = '[0-59]'
minutes = '[0-59]'
hours = '[0-23]'
day = 'day of week. O indexed'
date = 'day of month'
fullYear = 'year'
```
</details>

<!--==================-->
# 💭 Forum
<!--==================-->
## _ARRAY CONCEPTS_
<details><summary>🐝 Mutate The Caller</summary>

> Some array instance methods directly mutate the caller. These methods are called *destructive*. On the list above, those methods with 👺 are destructive methods. Some destructive methods have a non-destructive counterpart. Unfortunately, browser support (at the time of writing) is not supported everywhere.
```js
AP.sort() = AP.toSorted();
AP.reverse() = AP.toReverse();
```
</details> <!---------------------->

<details><summary>🐜 Handling Empty Slots</summary>

> Arrays with `<empty items>` aka *empty slots* are called *sparse arrays*. These are not *empty* arrays because the slot is being occupied. I like to think of empty slots as filled air. It still occupies the space, but it isn't used in any meaningful way. `Empty items` are handled by array methods in different ways. Generally speaking, empty slots are counted for length/index and action is taken for removal, copy, and adding operations. Thus, `pop()` will remove an `empty item` if it's the last idx elem. `concat()` will copy the `empty item` to its shallow array. In other methods, however, it is ignored. For instance, the callbackFn is skipped for functions like `forEach(), map(), etc` It is also ignored for the `flat()` method.
```js
// Length counts empty slot
let array = Array(2);
array.length // ⏎ 2
// Treated as an Indexed Slot
let emptyTreatment = [concat(), indexOf(), lastIndexOf(), reverse(), slice(), sort(), splice()]
let emptyTreatment2 = [pop(), push(), shift(), unshift()]
// Treats Empty Items as Undefined
let undefinedTreatment = [find(), includes(), join(), fill()]
// Treats as a Falsy Value
let falsyTreatment = [every(), filter(), some()]
// Skips callBack fn on Empty Slots
let skipsEmpty = [forEach(), map(), reduce(), reduceRight(), flat()]
// Other Behaviors
```
</details> <!---------------------->

<details><summary>🐝 Shallow vs Deep Copy</summary>

> In JS, only shallow copies are created. A *shallow* copy means that object references are copied. Contrast that with a deep copy where the values of an object are copied, and saved to a different memory location. After creation, both items are distinct in a deep copy. A shallow copy is a copy whose properties share the same references as the source object from which the copy was made. Therefore, if you mutate the reference from the source copy, the change is reflected in the copy/copies as well. JS array methods either mutate the caller or return a shallow copy.
```js
const originalArray = [1, 'string', {a: 0, b: 2}];
const copyArray = [...originalArray];

copyArray[0] = 500;
originalArray[2].a = 'updated value';

console.log({originalArray, copyArray});
```
</details> <!---------------------->

## _OTHERS_
<details><summary>🐜 Errors</summary>

> There are many subclasess of errors in js. Errors are often used with `throw,catch,finally`. The subclasses are an object themselves, but the 3 most common are:
1. SyntaxError
2. ReferenceError
3. TypeError

```yaml
SyntaxError: violates syntax rules
  - (punctuation, whitespace, valid characters)
ReferenceError: var/fn that doesn't exist
TypeError: value retrieval/action on the wrong type
   - access props on values without properties `undefined` `null`
   - invoking a non function
   - reassignment to constant variable
```
</details> <!---------------------->


<details><summary>🐜 Math.Random (min-max)</summary>

> Below I will briefly explain how the Math formula to get a random number between `min` and `max` is formulated
```js
Math.floor(Math.random() * (max - min + 1))
```
```js
1. Scale up random * max
// To reach upperbound
Math.random() * (max)

2. Limit to Integers Math.floor
Math.floor(Math.random() * max);

3. Offset Math.floor
// Floor always rounds down by 1. Upperbound will never be reached
Math.floor(Math.random() * max + 1)

4. Establish Lower Bound
Math.floor(Math.random() * (max + 1) + min
/* The lower bound right now is `0`. We want to make sure that it's always the
`min` we specify. We'll add the `min` to ensure that it's always at least
`min`. This fixes the `min` value, but in fixing `min` we mess up the upper
bound `max value`.
*/

5. Fix Upper Bound Value
Math.floor(Math.random() * (max + 1 - min) + min) // This works!
/* In adding the `min` value, we changed the possible upper-bound output. We
want to keep the `min` value intact while also limiting the upper `max`. On
step 4, the upper bound output is `max + min`. We want to subtract `min`. Where
we subtract min is important too!
*/
```
</details> <!---------------------->

<!--==================-->
# 🧪 Examples
<!--==================-->
## _STRINGS_
<details><summary>🐜 String.fromCharCode</summary>

```js
// STATIC
String.fromCharCode(97, 98); // 'ab'
String.fromCharCode('aa'); // '\x00'
String.fromCharCode('zz'); // '\x00'
String.fromCharCode(0); // '\x00'
String.fromCharCode(1); // '\x01'
String.fromCharCode(true); // '\x01'
```
</details>


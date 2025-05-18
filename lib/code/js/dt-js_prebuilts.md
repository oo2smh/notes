<!--==================-->
# Overview
<!--==================-->
- Some languages use built-in functions, JS doesn't implement many useful fns
- Broken down into 2 main categories
  1. Core
  2. Supplementary

## _CORE_
Core built in objects are based off of the datatype that exist in JS
- Core members will be prefixed with C
- [Number, Object, String, Array]

## _SUPPLEMENTARY_
Other built in objects in JS not tied to the datatypes
- Supplemntary members will be prefixed with S
- [Math, Regexp, JSON, Set, Date, Error]

<!--==================-->
# Constructors
<!--==================-->
> `Value` parameter can be any datatype. Constructors yank the value and return a new value of their own datatype. `Symbol(value)` will for instance, take the value and return a new symbol. Generally, this is the extent of of a constructor's functionality. It is more often than not better to use the literal ways to create values (`{}` to create obj, `[]` to create arrays, `''` for strings, etc). This is more concise and cleaner. However, it is good to be aware that constructors exist.

```js .........................
Symbol(value)  // ⏎ symbol
Boolean(value) // ⏎ boolean
Number(value)  // ⏎ number
BigInt(value)  // ⏎ bigInt
String(value)  // ⏎ string
Object(value)  // ⏎ object
Array(...elemsN) || Array(arrayLength) // ⏎ array
Function([...argumentsN], functionBody) //  ⏎ function
`````````````````````````````````

<!--==================-->
# Implicit Coercions
<!--==================-->
```js ...............................
const validDatatypes = [Symbol, Boolean, Number, BigInt, String, Object, Array, Function]
validDatatypes[#].prototype.valueOf()
validDatatypes[#].prototype.toString()
`````````````````````````````````````

<!--==================-->
# C:Number
<!--==================-->
- 🎀 4Is TPTP
  - Glasses wearing mathematical student inside of a tipi inside of a smaller tipi
    - It's cold and he's getting numb. He has fins, parsley and a knife
- 🏺 [Boolean Check, Parsing, Incision]

## _BOOLEAN CHECK_
- Number check 1st
- Then number subtype check
```js .................................
// 🎀 FINS
Number.isFinite(val)
Number.isInteger(val)
Number.isNaN(val)
Number.isSafeInteger(val)
``````````````````````````````````````

## _PARSING_
- Coerce arg into string
- Will return a stringified num
- It will return a decimal number equivalent
- Radix = max amt of digits available for each place value
  - binary(2), decimal(10), hexadecimal(16) are common

### Pitfalls
- Will parse until it hits an error & return results of parsed data
  - If it cannot parse any number from str, it returns `NaN`
- Leading whitespace is ignored
- Radix = [2-36]
  - If radix is undefined, 0, or not a valid integer, it uses the default of 10
  - If radix is a valid integer, but out of range, it returns undefined
  - If radix begins with `0x || 0X`, it assumes a radix of 16

```js ................................
Number.parseInt(str)
Number.parseFloat(str, [radix = 10])
````````````````````````````````````

## _INCISION_
- 🎀 Incision requires precision and is an instance method
- Instance methods
- returns a stringified num
- toFixed looks at the number of placeValues to the right of the `.`
- toPrecision looks at all of the placeValues (significant placeValues)
- valid Ranges
  - [0-100] toFixed
  - [1-100] toPrecision
- Out of Range --> RangeError
- Non-number --> TypeError
- Syntax Error --> If used on a number not stored in var

### Pitfalls
- Number used must be stored in a variable
  - This is b/c the JS Engine gets confused when it see a number literal and `.`
  - It doesn't know if you are declaring a float or using the dot method
- It will add and return 0s as placeholders if you put a number greater than
the digits held by the input num
- It rounds the answer if you specify a number less than the input

```js ..............................
Np.toFixed([digits = 0])
Np.toPrecision([precision = String(num).length])
````````````````````````````````````

<!--==================-->
# C:Object (Dict)
<!--==================-->
- 🎀 HHI CA KEV, 3I FPS DaviD GoGGins
  - Looking into a purple snowglobe object
    - Waving to kevjumba while stuttering my H's in CA.
    - He has an extra bionic eye. Playing a shooting game with fast FPS.
    - David Goggins is also there

```js ...................................
// BOOLEAN CHECK
Op.hasOwnPrototype(prop) // ⏎ boolean
Object.hasOwn(obj, prop) // ⏎ boolean
Object.is(val1, val2) // ⏎ boolean (better ===)

// OBJECT CREATION
Object.create(proto, descriptors) // nuanced Object creator
Object.assign(targetObj, ...sourceObj) // Object combiner
// only copies enumerable and own properties

// ARRAYIFICATION
Object.keys(obj)
Object.entries(obj)
Object.values(obj)

// PROPERTY MOD
Object.isExtensible(obj)
Object.isSealed(obj)
Object.isFrozen(obj)

Object.freeze(obj)
Object.preventExtensions(obj)
Object.seal(obj)
/*
- preventExtensions: extensible: false (X add)
- seal: extensible: false, configurable: false (X add, delete)
- freeze: extensible: false, configurable: false, writable: false (X add, delete, modify)
*/

// OTHER
Object.defineProperty(obj, prop, descriptor)
Object.defineProperties(obj, props)
Object.getOwnPropertyNames(obj) // ⏎ an array of names (like Object.keys(obj))
Object.getPrototypeOf(obj)
Object.groupBy(iterable, fn) // good for getting an array of Objects and returning an object with properties containing arrays
``````````````````````````````````````

## Object Descriptors
- Object properties ships with built-in flags called descriptors.
- Descriptors come in 2 flavors
  1. Data
  2. Accessor

### Data Descriptors
- [value, configurable, enumerable, writable]
- `configurable`: if false --> prop may not be deleted
- other attributes cannot be changed
  - if writable = true
    - `value` can be changed
    - `writable` can be changed to false
- `enumerable`: if true --> prop can be enumerated/iterated through
- `value`: associated with the property. Defaults to undefined
- `writable`: allow reassignment through the assignment operator (=)

### Accessor
- `get`: fn which serves as the getter for the property. If there is no getter,
the return value of the property will be used
- `set`: fn which serves as the setter for the property or undefined if there
is no setter.

<!--==================-->
# C:String
<!--==================-->
- 🏺 [One-offs, Access, Search, Manipulation]

## _ONE_OFFS_
- 🎀 LF
- One-offs are the outliers. The only property and useful relevant static method

```js ..............................
- String.fremCodePoint(...codePts) // ⏎ char(s) at codePt
- SP.length // ⏎ integer
````````````````````````````````````

## _ACCESS_
- 🎀 BC ACCeSS
- Use the methods that use the default behavior or are supercharged by allowing negative idx

  ### Default Behavior
- All access parameters are idx and expect integers
- If (arg is a non-valid integer)
  - the default value is used
- If (arg is out-of-range)
  - `undefined` is used

  ### Support Negative Idx
- at(idx)
- slice(startIdx, endIdx)

  ### Anomalies
- charAt(idx) returns `""` when out of range
- charCodeAt(idx) returns `NaN` when out of range
- [] when it's a non-valid integer returns `undefined`
- substring
  - uses 0 as default when any is NaN or a non-valid integer
  - flips 2args is endIdx > startIdx args

```js ................................
// single char access
- [idx = 0]*
- charAt(idx = 0)*
- at(idx = 0)

// code point access
- charCodeAt(idx = 0)*
- codePointAt(idx = 0)

// multichar access
- slice([startIdx = 0], [endIdx = str.length - 1])
- substring([startIdx = 0], [endIdx = str.length - 1])
````````````````````````````````````````````

## _SEARCH_
- 🎀 SEIM MISL
- 🏺 = primary categorization, 🏷️ = tags (2ndary category)
- 🏺 [str, regex]
- 🏷️ [General(boolean, idx), Anchored, Iterable]

  ### String Search
- (searchStr = "undefined")
- searchStr is coerced to a str
- `SP.method(searchStr, [pos = 0])`

  ### Regexp Search
- `SP.method(regex=/(?:)/)`
  - empty non-capturing group
    - since it's empty it doesn't match any chars

```js ...................................
SP.startsWith(value)
SP.endsWith(value)
SP.includes(searchString, [fromIdx = 0])
SP.match(regex)
SP.matchAll(regex)
SP.indexOf(searchElem, [fromIdx = 0])
SP.search(regex)
SP.lastIndexOf(searchElem, [fromIdx = 0])
````````````````````````````````````````

## Manipulation
- 🎀 PCPR TTT RRTT S (PC Public Relations | Tic Tac Toe | Rotorrest Treatment Table | Sleep)

```js ...................................
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
``````````````````````````````````````
<!--==================-->
# C:Array
<!--==================-->
## _ONE OFFS_
```js ...............................
Array.isArray(value)
Array.of(...elemN)
Array.from(arrayLike, [mapFn(elem, idx)], [thisArg])
````````````````````````````````````

## _INSTANCES_
```js ............................
const AP = Array.prototype
🅿️  AP.length
👺 AP.unshift(...elemsN)
👺 AP.shift()
👺 AP.push(...elemsN)
👺 AP.pop()
👺 AP.fill(value, [start = 0], [end = arr.length])
👺 AP.splice(start, [deleteCount = 0], [...items])
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
``````````````````````````````````

## _HIGHER ORDER_
```js ..............................
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
````````````````````````````````````

<!--==================-->
# S:Math
<!--==================-->
- 🎀 SR Military Management Fund CRAp

```js ..................................
Math.sqrt(number);
Math.random();
Math.min(num1, num2, num3, num4);
Math.max(num1, num2, num3, num4);
Math.floor(number);
Math.ceil(number);
Math.round(number);
Math.abs(number);
`````````````````````````````````````````

<!--==================-->
# S:Regexp
<!--==================-->
- 2 ways to create a regex
  1. Literal notation /regex pattern/
  2. Constructor fn with `new` keyword

```js ...........................
RP.test(value)
``````````````````````````````````

<!--==================-->
# S:Date
<!--==================-->
- 🎀 DM HMS FMD (foot mouth disease)

```js ..............................
const dateObj = {
  seconds: date.getSeconds(),
  minutes: date.getMinutes(),
  hours: date.getHours(),
  dayOfWeek: date.getDay(),
  dayOfMonth: date.getDate(),
  month: date.getMonth() + 1,
  year: date.getFullYear(),
}
````````````````````````````````````

<!--==================-->
# S:Console
<!--==================-->
- output to the user
- console mgs are shown in diff colors

```js ............................
console.warn()
console.error()
console.log()
console.trace([objects])
``````````````````````````````````

<!--==================-->
# S:Error
<!--==================-->

```yaml ............................
SyntaxError: violates syntax rules
  - (punctuation, whitespace, valid characters)
ReferenceError: var/fn that doesn't exist
TypeError: value retrieval/action on the wrong type
   - access props on values without properties `undefined` `null`
   - invoking a non function
   - reassignment to constant variable
`````````````````````````````````````

<!--==================-->
# Strawberry (string, arrays)
<!--==================-->
- 🎀 LILI AS
- Strings & Arrays have many similarities to strings
- I grouped both as being in the strawberry group, however, it can also be grouped into a `sequence` group

```md ................................
* bracket notation []
- length
- includes()
- lastIndexOf()
- indexOf()

- at()
- slice()
````````````````````````````````````

<!--==================-->
# Encoding (char to bytes)
<!--==================-->
- Encoding standard (dict): Unicode. Yellow Pg dict
- Encoding system: `UTF-8, UTF-16`. Implementation of Encoding standard
- Surrogate pairs: high value code pts (requires multiple code pts) and hunked into 1 whole `U+100000` = `{U+D800, U+DC00}`
- Code Pt is present in both the encoding standard & system

<!--==================-->
# Array Concepts
<!--==================-->
## _MUTATE THE CALLER_
> Some array instance methods directly mutate the caller. These methods are called *destructive*. On the list above, those methods with 👺 are destructive methods. Some destructive methods have a non-destructive counterpart. Unfortunately, browser support (at the time of writing) is not supported everywhere.

```js ..............................
AP.sort() = AP.toSorted();
AP.reverse() = AP.toReverse();
`````````````````````````````````````

## _EMPTY SLOTS_
> Arrays with `<empty items>` aka *empty slots* are called *sparse arrays*. These are not *empty* arrays because the slot is being occupied. I like to think of empty slots as filled air. It still occupies the space, but it isn't used in any meaningful way. `Empty items` are handled by array methods in different ways. Generally speaking, empty slots are counted for length/index and action is taken for removal, copy, and adding operations. Thus, `pop()` will remove an `empty item` if it's the last idx elem. `concat()` will copy the `empty item` to its shallow array. In other methods, however, it is ignored. For instance, the callbackFn is skipped for functions like `forEach(), map(), etc` It is also ignored for the `flat()` method.


```js .......................................
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
`````````````````````````````````````````````

## _SHALLOW VS DEEP COPY_
> In JS, only shallow copies are created. A *shallow* copy means that object references are copied. Contrast that with a deep copy where the values of an object are copied, and saved to a different memory location. After creation, both items are distinct in a deep copy. A shallow copy is a copy whose properties share the same references as the source object from which the copy was made. Therefore, if you mutate the reference from the source copy, the change is reflected in the copy/copies as well. JS array methods either mutate the caller or return a shallow copy.

```js ......................................
const originalArray = [1, 'string', {a: 0, b: 2}];
const copyArray = [...originalArray];

copyArray[0] = 500;
originalArray[2].a = 'updated value';

console.log({originalArray, copyArray});
`````````````````````````````````````````````

<!--==================-->
# Examples
<!--==================-->
## _NUMBER_
  ### Parsing Methods
```js ..................................
// EXAMPLES
Number.parseInt("101", 2) // 5
Number.parseInt("321", 2) // NaN (only 0,1 avaliable in binary)
Number.parseInt("103", 2) // 2 (parses up to 10 then halts)
Number.parseInt("103", undefined) // 103 ()
Number.parseInt("103", 999) // NaN
Number.parseFloat("103.23", 999) // 103.23
````````````````````````````````````````

  ### Incision Methods
```js ...................................
23.toFixed() // SyntaxError
let num = 23.001
num.toFixed() // "23"
num.toFixed(999) // RangeError
num.toFixed(5) // 23.00100
num.toPrecision(1) // 2
````````````````````````````````````````

<!--==================-->
# References
<!--==================-->
> [!Important]
> [Visual Figjam representation](https://www.figma.com/board/OCKKQ9Z2JDiNW1aQWUTeHd/js-standardLibrary?node-id=0-1&t=E1rzdR5aLwOMXgYK-1)


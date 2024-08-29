<!--==================-->
# Overview
<!--==================-->
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
# C:Number
<!--==================-->
- 🎀 4Is TPTP
  - Glasses wearing mathematical student inside of a tipi inside of a smaller tipi
    - It's cold and he's getting numb. He has fins, parsley and a knife
- 🏺 [Boolean Check, Parsing, Incision]

## _BOOLEAN CHECK_
- Number check 1st
- Then number subtype check
```js
// 🎀 FINS
Number.isFinite(val)
Number.isInteger(val)
Number.isNaN(val)
Number.isSafeInteger(val)
```
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

```js
Number.parseInt(str)
Number.parseFloat(str, [radix = 10])
```

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

```js
Np.toFixed([digits = 0])
Np.toPrecision([precision = String(num).length])
```
<!--==================-->
# C:Object
<!--==================-->
- 🎀 HHI CA KEV, 3I FPS DaviD GoGGins
  - Looking into a purple snowglobe object
    - Waving to kevjumba while stuttering my H's in CA.
    - He has an extra bionic eye. Playing a shooting game with fast FPS.
    - David Goggins is also there
```js
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
```

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
# C:STRING
<!--==================-->
- 🏺 [One-offs, Access, Search, Manipulation]

## _ONE_OFFS_
- 🎀 LF
- One-offs are the outliers. The only property and useful relevant static method
```js
- String.fremCodePoint(...codePts) // ⏎ char(s) at codePt
- SP.length // ⏎ integer
```

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

```js
// single char access
- [idx = 0]*
- charAt(idx = 0)*
- at(idx = 0)

// code point access
- charCodeAt(idx = 0)*
- codePointAt(idx = 0)

// multichar access
- slice([startIdx = 0], [endIdx = str.length - 1])
- substring([startIdx = 0], [endIdx = str.length - 1])*
```
## _SEARCH METHODS_
- 🎀 SEIM MISL
- 🏺 = primary categorization, 🏷️ = tags (2ndary category)
- 🏺 [str, regex]
- 🏷️ [General(boolean, idx), Anchored, Iterable]

### String Search
- (searchStr = "undefined")
- searchStr is coerced to a str

<!--==================-->
# Examples
<!--==================-->
## _NUMBER_
### Parsing Methods
```js
// EXAMPLES
Number.parseInt("101", 2) // 5
Number.parseInt("321", 2) // NaN (only 0,1 avaliable in binary)
Number.parseInt("103", 2) // 2 (parses up to 10 then halts)
Number.parseInt("103", undefined) // 103 ()
Number.parseInt("103", 999) // NaN
Number.parseFloat("103.23", 999) // 103.23
```

### Incision Methods
```js
23.toFixed() // SyntaxError
let num = 23.001
num.toFixed() // "23"
num.toFixed(999) // RangeError
num.toFixed(5) // 23.00100
num.toPrecision(1) // 2
```

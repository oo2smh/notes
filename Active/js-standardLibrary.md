<!--==================-->
# 📑 Outline
<!--==================-->
1. Legend
2. Syntax
3. Deets
4. Examples

<!--==================-->
# 🗺️ Legend
<!--==================-->
```yaml
proto: prototype
ϟ: static method
⏎: return
value = 10: opt param
🤡: gotcha
🤬: arguments
❌: error
🚑: param
🚸: actions taken
👺: destructive method
🐛: coercion
```

<!--==================-->
# 🔮 Syntax
<!--==================-->
> The `Syntax` section covers the name of the method/property and specifies the return value. If it exists within a `prototype` property then it is an instance property/method. If not, it's a static method/property. This section covers the syntax name, parameters, return values, and if it mutates the caller. All other information and concepts will be covered in `Deets`.

> All instance methods will be written with `(Built-In).prototype` omitted. This is done in the name of brevity. Static methods will be written in their long form `Number.isFinite()`.
<!--~~~~~~~~~~~~~~~~~~-->

## _CONSTRUCTORS_
> Constructor fns convert their `value` argument into a new value of their respective datatype. Array constructor fn is unique in that in if one integer argument is passed, an array of size integer is created. Function constructor has security vulnerabilities and should not be used. Object constructor should be avoided since the object literal syntax is more concise and easier to understand.
<!--~~~~~~~~~~~~~~~~~~-->

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
___.prototype.valueOf()
___.prototype.toString()
___ = [Symbol, Boolean, Number, BigInt, String, Object, Array, Function]
```

## _CORE_
<details><summary>🐝 String/Main</summary>

> String methods can generally be broken down into 3 main groups. Search actions (regex, substring, anchoredSearch (`startsWith, endsWith`), manipulation (case changes, replacing, trimming), transformation into an array (`.split( )`). There is also one instance property (`length`). If not specified, the string method returns a new string.

> The 2 static string methods both take an integer and convert it to their Unicode counterpart. `String.fromCodePoint` has more functionality in that it works with surrogate pairs. It's not important to know what these are. Just use `fromCodePoint` when you need a method that goes from code point to Unicode char.
<!--~~~~~~~~~~~~~~~~~~-->

```js Static Methods
⭐ String.fromCodePoint(...intN)
// ⏎ Unicode char
```
```js
// 🎀 RPP TTTriple CSS LATTE RIMS RIMS (22)
// STRING.PROTOTYPE.
const SP = String.prototype
SP.repeat(count)
SP.padStart(targetLength, [padding = ' '])
SP.padEnd(targetLength, [padding = ' '])
SP.trim()
  SP.trimStart()
  SP.trimEnd()
SP.codePointAt(idx) // ⏎ code pt at given idx
SP.startsWith(string) // ⏎ boolean
SP.slice([startIdx = 0], [endIdx = str.length])
SP.length // ⏎ integer
SP.at(idx) // ⏎ char at idx
SP.toUpperCase()
SP.toLowerCase()
SP.endsWith(string) // ⏎ boolean
SP.replace(pattern, replacement)
SP.includes(searchString, [fromIdx = 0]) // ⏎ boolean
SP.match(regex) // ⏎ array or null
SP.split(separator) // ⏎ array
SP.replaceAll(pattern, replacement)
SP.indexOf(searchElem, [fromIdx = 0]) // ⏎ first idx where searchStr is found
SP.matchAll(regex) // ⏎ iterable or empty iterable obj
SP.search(regex) // ⏎ boolean
```
</details> <!---------------------->

<details><summary>🐜 Strings/2nd Rate Methods</summary>

> These methods are good to know since other developers might use it. Generally speaking however, I will avoid using these because they are outclassed by the newer/more feature-rich alternative
<!--~~~~~~~~~~~~~~~~~~-->
```js Second Rate Methods
// String Rejects
// These are 2nd rate methods
// 🎀 CCC SS
SP.concat(...strN)
SP.charAt(idx) // ⏎ char at idx
SP.charCodeAt(idx) // ⏎ UTF16 int of char
SP.substring([startIndex = 0], [endIndex = str.length])
String.fromCharCode(..intN)
// ⏎ Unicode char
```
</details> <!---------------------->

<details><summary>🐝 Number</summary>

> Number methods can be roughly divided by their utility (1) Conversion to Number (2) Number Subtype (3) Check Specify Number of Placeholders
<!--~~~~~~~~~~~~~~~~~~-->
```js
// 🎀 4Is TPTP
Number.isFinite(value)   // ⏎ boolean
Number.isInteger(value)  // ⏎ boolean
Number.isNaN(value)      // ⏎ boolean
Number.isSafeInteger(value) // ⏎ boolean
  // safeInt = -(2^53 - 1) to 2^53 - 1
Number.parseInt(string) // ⏎ parsed stringified int or NaN
Number.parseFloat(string, [radix = 10]) // ⏎ parsed stringified float or NaN
NP.toFixed([digits = 0]) // ⏎ string representing # using fixed pt notation
NP.toPrecision([precision]) // ⏎ int specifying number of significant digits
  // if precision is omitted, behaves as toString(). Non-int value is rounded to nearest int
```
</details> <!---------------------->


<details><summary>🐝 Object</summary>

> Note that `Arrays` and `Functions` are also considered to be specialized objects. These object methods, therefore, are available to these arrays and functions as well.

> If you freeze an object, is it sealed as well? Yes. `📟 sealed`: Cannot delete properties. `📟 frozen`: Cannot delete or modify existing properties
<!--~~~~~~~~~~~~~~~~~~-->
> ```js
> const obj = {a: 1, b: 2};
> Object.freeze(obj);
> console.log(Object.isSealed(obj));
> ```
```js
// 🎀 HI CA KEV SIFI
// Types of actions: Creation, Identification, Transformation to array, Seal/Freeze
Object.hasOwn(obj, prop) // ⏎ boolean if prop exists in obj
  // replacement for Object.prototype.hasOwnProperty(prop)
Object.is(val1, val2) // ⏎ boolean
Object.create(proto, [propsObj]) // ⏎ new objwith specified protoObj and propertiesObj
Object.assign(target, ...sources) // ⏎ targetObj after enumerable own prop from ...sources are added
Object.keys(obj) // ⏎ array of strings of obj's own enumerable string-keyed prop keys
Object.entries(obj) // ⏎ matrix: array of subarrays
Object.values(obj) // ⏎ array of values
Object.seal(obj) // ⏎ obj passed into fn
// new props cannot be added. existing props cannot be removed. Can be modified
Object.isSealed(obj) // ⏎ boolean
Object.freeze(obj) // ⏎ obj passed into fn
  // freezing prevents adding, deleting, and modifying props of obj
Object.isFrozen(obj) // ⏎ boolean
```
</details> <!---------------------->

<details><summary>🐝 Array/Static</summary>

```js Array Static Methods
// Array Static
Array.isArray(value) // ⏎ boolean
Array.of(...elemN) // ⏎ new Array instance. Same as Array(), but can create an array with 1 integer elem
Array.from(arrayLike, [mapFn(elem, idx)], [thisArg]) // ⏎ new Array instance
```
</details> <!---------------------->

<details><summary>🐝 Array/Instance</summary>

```js Array Instance Methods
// 🎀 LuFFy SUP I PISS JARS
// All starts with Array.prototype
const AP = Array.prototype
🅿️ AP.length // ⏎ integer
👺 AP.fill(value, [start = 0], [end = arr.length]) // ⏎ modified array filled with value
   AP.flat([depth = 1]) // ⏎ new arr with sub-array elements
👺 AP.shift() // ⏎ removed elem
👺 AP.unshift(...elemsN) // ⏎ new length
👺 AP.pop() // ⏎ removed elem
   AP.indexOf(searchElem, [fromIdx = 0])
👺 AP.push(...elemsN) // ⏎ new length
   AP.includes(searchElem, [fromIdx = 0]) // ⏎ boolean
   AP.slice([start = 0], [end = arr.length]) // ⏎ shallow arr copy
👺 AP.splice(start, [deleteCout = 0], [...items]) // ⏎ array containing deleted elems
   AP.join([separator = ',']) // ⏎ a str separated by separator
   AP.at(idx) // ⏎ elem at given idx
👺 AP.reverse() // ⏎ ref to original object
👺 AP.sort(compareFn(a,b)) // ⏎ ref to original object
// a = 1st comparison elem, b = 2nd comparison elem
// sorted lexicographically
```
</details> <!---------------------->

<details><summary>🐝 Array/Higher Order</summary>

```js
// ⏎ 🎀 MR RES 5FFFFF
// Rest of this have a callbackFn(elem, idx, array), [thisArg]
AP.map(callbackFn, [thisArg])
AP.reduce(callback(accumulator, currentValue, currentIdx, array), [initValue = array[0]])
  // if initValue is empty, it becomes array[0] and the 1st current value is array[1]
  // callback is often called a reducer
AP.reduceRight(callback(accumulator, currentValue, currentIdx, array), [initValue = array[0]])
  // starts currentValue from end of array
AP.every(callbackFn, [thisArg]) // ⏎ boolean, false if any elem evaluates to false
AP.some(callbackFn, [thisArg]) // ⏎ boolean, true if any elem evaluates to true
AP.forEach(callbackFn, [thisArg]) // ⏎ undefined
AP.filter(callbackFn, [thisArg]) // ⏎ shallow array of elems that pass the test
AP.find(callbackFn, [thisArg]) // ⏎ 1st elem in array that satisfies the provided testing function or undefined
AP.findIndex(callbackFn, [thisArg]) // ⏎ 1st idx of 1st elem in array that satisfies provided test conditions
AP.flatMap(callbackFn, [thisArg]) // ⏎ new aray with each elem of callbackFn and flattened to a depth of 1
```
</details> <!---------------------->

## _OTHER_
<details><summary>🐝 Math</summary>

```js
// 🎀 SR Military Management Fund CRAp
Math.sqrt(number); // 🚑 number  0
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
<!--~~~~~~~~~~~~~~~~~~-->
```js
RP = RegExp.prototype
RP.test(value) // ⏎ boolean
```
</details> <!---------------------->

<details><summary>🐜 Date</summary>

```js
// 🎀 DM HMS FMD (foot mouth disease)
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

<details><summary>🐜 Console</summary>

> `Console` object can be accessed from any global object. The goal of `console` is to output to the user. Most of the methods are some form of variation or some way to support this function. In the browser console, these `console` messages are shown in different colors
<!--~~~~~~~~~~~~~~~~~~-->
```js
// CONSOLE
console.warn()  // orange/yellow
console.error() // red
console.log() // no background color
console.trace([objects]: // outputs a stack trace. 🚑 [objects] are also outputted with the stack trace if specified
```
</details> <!---------------------->

<!--==================-->
# 🪲 Deets
<!--==================-->
## _ARRAY CONCEPTS_
<details><summary>🐝 Mutate The Caller</summary>

> Some array instance methods directly mutate the caller. These methods are called *destructive*. On the list above, those methods with 👺 are destructive methods.

> Some destructive methods have a non-destructive counterpart. Unfortunately, browser support (at the time of writing) is not supported everywhere.
<!--~~~~~~~~~~~~~~~~~~-->
```js
AP.sort() = AP.toSorted();
AP.reverse() = AP.toReverse();
```
</details> <!---------------------->

<details><summary>🐜 Handling Empty Slots</summary>

> Arrays with `<empty items>` aka *empty slots* are called *sparse arrays*. These are not *empty* arrays because the slot is being occupied. I like to think of empty slots as filled air. It still occupies the space, but it isn't used in any meaningful way. `Empty items` are handled by array methods in different ways. Generally speaking, empty slots are counted for length/index and action is taken for removal, copy, and adding operations. Thus, `pop()` will remove an `empty item` if it's the last idx elem. `concat()` will copy the `empty item` to its shallow array. In other methods, however, it is ignored. For instance, the callbackFn is skipped for functions like `forEach(), map(), etc` It is also ignored for the `flat()` method.
<!--~~~~~~~~~~~~~~~~~~-->
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

> In JS, only shallow copies are created. A *shallow* copy means that object references are copied. Contrast that with a deep copy where the values of an object are copied, and saved to a different memory location. After creation, both items are distinct in a deep copy. A shallow copy is a copy whose properties share the same references as the source object from which the copy was made. Therefore, if you mutate the reference from the source copy, the change is reflected in the copy/copies as well.

> JS array methods either mutate the caller or return a shallow copy.
<!--~~~~~~~~~~~~~~~~~~-->
```js
const originalArray = [1, 'string', {a: 0, b: 2}];
const copyArray = [...originalArray];

copyArray[0] = 500;
originalArray[2].a = 'updated value';

console.log({originalArray, copyArray});
```
</details> <!---------------------->

## _OTHERS_
> There are other built in objects that aren't counterparts to JS datatypes. I will be going over some of the most useful ones. The built in objects that I cover can be remembered with the acronym 🎀 RED CSM MJ `Regexp, Error, Date, Console, Set, Map, Math, JSON`. Out of these, most don't have frequent uses, but these are objects that are good to be aware of.

<details><summary>🐜 Errors</summary>

```md
There are many subclasss of errors in js. The subclasses are an object themselves, but the 3 most common are:
 1. `SyntaxError`: When code violates the syntax rules (punctuation, whitespace, valid characters)
 2. `ReferenceError`: attempt to use a variable or function that doesn't exist
 3. `TypeError:` value retrieval/action on the wrong type
   - accessing property on values without properties `undefined` `null`
   - calling something that isn't a function
   - reassignment to constant variable
This built in object is frequently used with the `throw, catch` and sometimes `finally` statements. You can also create your own
```
</details> <!---------------------->

<details><summary>🐜 Date</summary>

Date has 3 main useful functions that are commonly used.
   1. CREATE DATE OBJ: creation of `new Date()`
   2. GET: `(instanceObj).get(timeofDay)`
   3. SET: `(instanceObj).set(timeOfDay)`

```md
## Zero Indexed
These are zero indexed. Ie: January = 0
 - `Date.getMonth()` is zero indexed so January is 0. Always add 1
 - `Date.getDay()`: It returns the day of the week. Monday = 1, Sunday = 7. Not the day of the month
   - To get the day of the month, use `(instanceObj).getDate()`. It's weirdly named.

## Setting Time
When you use a `____.set-timeFrame()`, you have to input a number as an argument. Each timeframe has a valid range. If you input a number greater than the range, it will simply use the remainder operator on the `parameter` and return the result.
  - `setSeconds(), setMinutes()`: 0–60.`
  - `setHours()`: 0–24
  - `setDate()` : 1–31
  - `setMonth()`: 1–12.
```
</details> <!---------------------->

<details><summary>🐜 Math</summary>

> Math provides additional features for working with the `Number` value.
 > 1. Trigonometry and More advanced arithmetic (square root, exponentiation)
 > 2. Min, Max of Numbers
 > 3. Random Number Generation
 > 4. Number Rounding Manipulation (`round, floor, ceil, abs`)

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
# 📟 EXAMPLES
<!--==================-->
<details><summary>🧪 Strings</summary>

```js
let string = 'string';
let match = string.match(/ri/);
let matchAll = string.matchAll(/[ng]/~g);
let searchNG = string.search(/[ng]/);~

let atNeg2 = string.at(-2);
let startsWith = string.startsWith('str');
let startsWithFalse = string.startsWith('St');
let endsWith = string.endsWith('g', 4);
let endsWithFalse = string.endsWith(' ' , 2);
let indexOfN = string.indexOf('n');
let includes = string.includes('ring');

let stringLower = 'I AM NOT SCREAMING'.toLowerCase();
let stringUpper = 'I am screaming'.toUpperCase();

let sliceString = string.slice(1);
let substring = string.substring(1);
let trimString = (`   string   `).trim();

let replaceS = string.replace('str', 'chachi');
let replaceIng = string.replace('ing', 'ay');
et replaceAll = string.replaceAll(/s/g, 'replaced');

let stringSplit = string.split('');
let stringInvalidSeparator = string.split('-');

console.log({string, atNeg2, startsWith, startsWithFalse, endsWith, endsWIthFalse, indexOfN, includes});
console.log({stringLower, stringUpper});
console.log( {sliceString, substring, trimString, replaceS, replaceIng, stringSplit, stringInvalidSeparator, replaceAll});
```
</details> <!---------------------->

<details><summary>🧪 Number</summary>

```js
 let digit = 123.4567;
 let toFixed = digit.toFixed(5); //123.45670
 let toPrecision = digit.toPrecision(5); // 123.46❗️
 let isNaN = Number.isNaN(digit); // false
 let parseFloat = Number.parseFloat(digit); // 123.4567
 let parseInt = Number.parseInt(digit); // 123
 let parseIntBinary = Number.parseInt(digit, 2); // 1❗️
 let numberMethod = Number('123abc'); // NaN

 console.log({digit, toFixed, toPrecision, isNaN, parseFloat, parseInt, parseIntBinary, numberMethod});
```
</details> <!---------------------->

<details><summary>🧪 Object</summary>

```js
// Object.create()
let obj = {a: 123, b: true};
let obj2 = {d: 'dope'};
let createdObj = Object.create(Object.prototype, {
  a: {
    value: 123,
    writable: true,
    enumerable: true,
    configurable: true
  },
  b: {
    value: true,
    enumerable: true,
  }
});
```js
//Object.hasOwn()
let grandparentObject = {grandpasAge: 80, grandmasAge: 75};
let parentObject = {momsLove: '50%', dadsLove: '50%', photoBook: {year1: 'birthday photo', year2: 'laughing photo'}};
let childObject = {toy: 'transformers', game: 'roblox'};
Object.setPrototypeOf(childObject, parentObject);
Object.setPrototypeOf(parentObject, grandparentObject);

console.log(2, Object.hasOwn(childObject, 'toy'));
console.log(3, Object.hasOwn(childObject, 'momsLove'));

//___isPrototypeOf(object) instance method
console.log(4, Object.getPrototypeOf(childObject));
console.log(5, Object.isPrototypeOf(childObject));
console.log(6, Object.getPrototypeOf(childObject) === Object.isPrototypeOf(childObject));
console.log(7, parentObject.isPrototypeOf(childObject));
console.log(8, {rando: 1}.isPrototypeOf(childObject));

// Object.is()
console.log(1,Object.is(+0, -0));
```
```js
const kitchenware = {bowls: 3, cups: 5, spoons: 12};
const array = [1,2,3,4];
const kitchenwareKeys = Object.keys(kitchenware);
const kitchenwareValues = Object.values(kitchenware);
const kitchenwareEntries = Object.entries(kitchenware);

const arraysAreObjectsToo = Object.keys(array);
const stringPrimAsParam = Object.entries('test');
console.log({kitchenwareKeys, kitchenwareValues, kitchenwareEntries, array, stringPrimAsParam});

const deskSetup = {laptop: 1, monitor: 1, keyboard: 1, mouse: 1};
console.log(Object.seal(deskSetup));
console.log(Object.isSealed(deskSetup));
// delete deskSetup.mouse; Error b/c deskSetup is sealed
console.log(Object.freeze(deskSetup))
console.log(Object.isFrozen(deskSetup));
```
</details> <!---------------------->

<details><summary>🧪 Arrays</summary>

```js
const array = [1, null, 3, 'string'];
console.log(1, array.length = 6);
console.log(2, array.shift());
console.log(3, array.unshift(0,1));
console.log(4, array.pop());
console.log(5, array.push('last item'));
console.log(6, array.includes(undefined));
console.log(7, array.slice(0,4));
console.log(8, array.splice(1, 1, 2));
console.log(9, array.join('-'));
console.log(10, array.at(-2));
console.log(11, array.reverse());
console.log(12, array.sort())
console.log(13, array.sort( (b,a) = a - b));
console.log(13, array.sort( (a,b) = b = a));

/* Explanations
1. specifying extra length add <empty items wheras shortening length removes items from the end
3,5. You can add multiple elements with push() and unshift()
6. <empty item is counted as `undefined` by includes()
12. default sort is ascending (a,b) = a - b
13. compareFn = a  b: This means it should show up in descending order
*/
```
</details> <!---------------------->


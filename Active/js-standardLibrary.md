<!---------------------->
# OUTLINE
<!---------------------->
1. Legend
2. Commands
  - [Constructors, Implicit Coercions, Core, Other]
3. Deets
4. Examples

<!---------------------->
# LEGEND
<!---------------------->
```yaml
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

<!---------------------->
# 📣 COMMANDS
<!---------------------->
- [Constructors, Implicit Coercions, Core, Other]

## CONSTRUCTORS
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

## IMPLICIT COERCIONS
```js
______.prototype.valueOf()
______.prototype.toString()
______ = [Symbol, Boolean, Number, BigInt, String, Object, Array, Function]
```

## CORE
```js
// 🎀 REP PP TTTriple CCC SSS LATTE RIMS RIMS (27)
String.prototype.repeat(count)
String.prototype.padStart(targetLength, [padding = ' '])
String.prototype.padEnd(targetLength, [padding = ' '])
String.prototype.trim()
  String.prototype.trimStart()
  String.prototype.trimEnd()
String.prototype.concat(...strN)
String.prototype.charAt(idx) // ⏎ char at idx
String.prototype.charCodeAt(idx) // ⏎ UTF16 int of char
String.prototype.startsWith(string) // ⏎ boolean
String.prototype.slice([startIdx = 0], [endIdx = str.length])
String.prototype.substring([startIndex = 0], [endIndex = str.length])
String.prototype.length // ⏎ integer
String.prototype.at(idx) // ⏎ char at idx
String.prototype.toUpperCase()
String.prototype.toLowerCase()
String.prototype.endsWith(string) // ⏎ boolean
String.prototype.replace(pattern, replacement)
String.prototype.includes(searchString, [fromIdx = 0]) // ⏎ boolean
String.prototype.match(regex) // ⏎ array or null
String.prototype.split(separator) // ⏎ array
String.prototype.replaceAll(pattern, replacement)
String.prototype.indexOf(searchElem, [fromIdx = 0]) // ⏎ first idx where searchStr is found
String.prototype.matchAll(regex) // ⏎ iterable or empty iterable obj
String.prototype.search(regex) // ⏎ boolean

// 🎀 4Is TPTP
Number.isFinite(value)   // ⏎ boolean
Number.isInteger(value)  // ⏎ boolean
Number.isNaN(value)      // ⏎ boolean
Number.isSafeInteger(value) // ⏎ boolean
  // safeInt = -(2^53 - 1) to 2^53 - 1
Number.parseInt(string) // ⏎ parsed stringified int or NaN
Number.parseFloat(string, [radix = 10]) // ⏎ parsed stringified float or NaN
Number.prototype.toFixed([digits = 0]) // ⏎ string representing # using fixed pt notation
Number.prototype.toPrecision([precision]) // ⏎ int specifying number of significant digits
  // if precision is omitted, behaves as toString(). Non-int value is rounded to nearest int

// 🎀 HI CA KEV SIFI
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

// Array Static
Array.isArray(value) // ⏎ boolean
Array.of(...elemN) // ⏎ new Array instance. Same as Array(), but can create an array with 1 integer elem
Array.from(arrayLike, [mapFn(elem, idx)], [thisArg]) // ⏎ new Array instance

// 🎀 LuFFy SUP I PISS JARS
🅿️  Array.prototype.length // ⏎ integer
👺 Array.prototype.fill(value, [start = 0], [end = arr.length]) // ⏎ modified array filled with value
   Array.flat([depth = 1]) // ⏎ new arr with sub-array elements
👺 Array.prototype.shift() // ⏎ removed elem
👺 Array.prototype.unshift(...elemsN) // ⏎ new length
👺 Array.prototype.pop() // ⏎ removed elem
   Array.prototype.indexOf(searchElem, [fromIdx = 0])
👺 Array.prototype.push(...elemsN) // ⏎ new length
   Array.prototype.includes(searchElem, [fromIdx = 0]) // ⏎ boolean
   Array.prototype.slice([start = 0], [end = arr.length]) // ⏎ shallow arr copy
👺 Array.prototype.splice(start, [deleteCout = 0], [...items]) // ⏎ array containing deleted elems
   Array.prototype.join([separator = ',']) // ⏎ a str separated by separator
   Array.prototype.at(idx) // ⏎ elem at given idx
👺 Array.prototype.reverse() // ⏎ ref to original object
👺 Array.prototype.sort(compareFn(a,b)) // ⏎ ref to original object
  // a = 1st comparison elem, b = 2nd comparison elem
  // sorted lexicographically

// ⏎ 🎀 MR RES 5FFFFF
// Rest of this have a callbackFn(elem, idx, array), [thisArg]
Array.prototype.map(callbackFn, [thisArg])
Array.prototype.reduce(callback(accumulator, currentValue, currentIdx, array), [initValue = array[0]])
  // if initValue is empty, it becomes array[0] and the 1st current value is array[1]
  // callback is often called a reducer
Array.prototype.reduceRight(callback(accumulator, currentValue, currentIdx, array), [initValue = array[0]])
  // starts currentValue from end of array
Array.prototype.every(callbackFn, [thisArg]) // ⏎ boolean, false if any elem evaluates to false
Array.prototype.some(callbackFn, [thisArg]) // ⏎ boolean, true if any elem evaluates to true
Array.prototype.forEach(callbackFn, [thisArg]) // ⏎ undefined
Array.prototype.filter(callbackFn, [thisArg]) // ⏎ shallow array of elems that pass the test
Array.prototype.find(callbackFn, [thisArg]) // ⏎ 1st elem in array that satisfies the provided testing function or undefined
Array.prototype.findIndex(callbackFn, [thisArg]) // ⏎ 1st idx of 1st elem in array that satisfies provided test conditions
Array.flatMap(callbackFn, [thisArg]) // ⏎ new aray with each elem of callbackFn and flattened to a depth of 1
```

## OTHER
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

// CONSOLE
console.warn()  // orange/yellow
console.error() // red
console.log() // no background color
console.trace([objects]: // outputs a stack trace. 🚑 [objects] are also outputted with the stack trace if specified
```
<!---------------------->
# 🪲 DEETS
<!---------------------->
## CONSTRUCTORS
- Primitive constructor fns convert value and return the new value
- Array constructor fn has 2 variants
- Function constructor has security vulnerabilities and should not be used
- Object constructor is longer than the object literal so should not be used

## NUMBER
Number methods can be roughly divided by their utility.
- Conversion to Number
- Number Subtype Check
- Specify Number of Placeholders

## STRING
- Search actions
  - Regex Search
  - Substring search
  - Anchored search (starts/endsWith)
- Manipulation
  - Case Changes (lowercase, UPPERCASE)
  - Replacing
  - Trimming
- Coercion
  - Into array

## SIMPLE OBJECT
- Note that `Arrays` and `Functions` are also considered to be specialized objects. These object methods, therefore, are available to these arrays and functions as well.

### Main Actions
- Object Creation
- Object Identification
- Transformation into an array
- Sealing / Freezing

- If you freeze an object, is it sealed as well?
Yes. `📟 sealed`: Cannot delete properties. `📟 frozen`: Cannot delete or modify existing properties

```js
const obj = {a: 1, b: 2};
Object.freeze(obj);
console.log(Object.isSealed(obj));
```

## ARRAY CONCEPTS
1. Mutate the Caller?
  - some methods change its calling object while others create a copy object to modify
2. Handling Empty Slots
  - `Sparse arrays` are arrays that contain `<empty items>`. Different methods deal with `<empty items>` differently
3. Deep vs Shallow Copy
  - JS array methods only create shallow copies. That means that nested objects will be copied by reference. Changing the nested object in either the copy or original object will bring changes to both objects

### Caller Mutation?
- Certain methods mutate the calling array. Most return a shallow copy

### Sparse Arrays and Empty Items
#### Treats Empty Items as Undefined
- `find()`, `includes()`, `join()`, `fill()`

#### Simple: Includes Empty Items
1. `concat()`: Treats empty items as regular items and includes them in the resulting concatenated array.
2. `indexOf()`/`lastIndexOf()`: Empty items are treated just like any other item > in the array. They are matched using strict equality (`===`).
3. `reverse()`: Reverses the order of elements in the array, including empty items.
4. `slice()`: Returns a shallow copy of a portion of an array into a new array. Empty items are preserved in the slice.
5. `sort()`: Sorts the elements of an array in place and returns the sorted array. Empty items are included in the sorting process.
6. `splice()`: Adds and/or removes elements from an array. Empty items are treated like any other item and can be added, removed, or replaced.

#### Higher Order Fns
 7. `every()`: An empty item is treated as a falsy value, so it can cause `every()` to return `false` if the callback function expects a truthy value.
 8. `filter()`: Filters out empty items based on their truthiness. Empty items are considered falsy and are excluded from the filtered array.
 9. `forEach()`: Processes empty items like any other item in the array, passing them as arguments to the provided callback function.
 10. `map()`: Transforms each element of the array using a mapping function. Empty items are included in the mapped array if the mapping function returns a non-empty value.
 11. `reduce()` and `reduceRight()`: Treat empty items as regular items in the reduction process. The initial value and accumulated result will depend on how the reduction function handles empty items.
 12. `some()`: Returns `true` if at least one element in the array passes the test implemented by the provided function. An empty item is treated as falsy and can cause `some()` to return `false` if the callback function expects a truthy value.

### Deep Vs Shallow Copy
Making a `deep copy` means copying an exact replica of another object. After the creation of the copy, the original and copy are completely distinct. Making a change to the original does not affect the copy. Making a `shallow copy`, on the other hand means copying the outer husk only. It means copying only primitives as values and copying any nested objects as references.

In a shallow copy, therefore, when you change a primitive value, that change is distinct to the object itself. However, if you alter a nested object, that change is reflected on both the original and copy objects

```js
const originalArray = [1, 'string', {a: 0, b: 2}];
const copyArray = [...originalArray];

copyArray[0] = 500;
originalArray[2].a = 'updated value';

console.log({originalArray, copyArray});
```

## OTHERS: REGEXP, ERROR, CONSOLE
There are other built in objects that aren't counterparts to JS datatypes. I will be going over some of the most useful ones. The built in objects that I cover can be remembered with the 🎀 RED CSM MJ `Regexp, Error, Date, Console, Set, Map, Math, JSON`. Out of these, most don't have frequent uses, but these are objects that it's good to be aware of. I will specifically cover methods from `Date, Math and JSON` here.

### Regexp, Error, Console
#### Regexp
2 ways to create regexp
     1. `literal notation`: `/(regexp pattern here)/`
     2. `constructor`: using the `new` keyword
I won't be going over any of the methods here. `regexp` is often paired with strings to create more nuanced searches

#### Errors
There are many subclasss of errors in js. The subclasses are an object themselves, but the 3 most common are:
 1. `SyntaxError`: When code violates the syntax rules (punctuation, whitespace, valid characters)
 2. `ReferenceError`: attempt to use a variable or function that doesn't exist
 3. `TypeError:` value retrieval/action on the wrong type
   - accessing property on values without properties `undefined` `null`
   - calling something that isn't a function
   - reassignment to constant variable
This built in object is frequently used with the `throw, catch` and sometimes `finally` statements. You can also create your own

#### Console
`Console` object can be accessed from any global object. The goal of `console` is to output to the user. Most of the methods are some form of variation or some way to support this function. In the browser console, these `console` messages are shown in different colors

## OTHERS: DATE
Date has 3 main useful functions that are commonly used.
   1. CREATE DATE OBJ: creation of `new Date()`
   2. GET: `(instanceObj).get(timeofDay)
   3. SET: `(instanceObj).set(timeOfDay)`

### Some Weird Responses
 - `Date.getMonth()` is zero indexed so January is 0. Always add 1
 - `Date.getDay()`: It returns the day of the week. Monday = 1, Sunday = 7. Not the day of the month
   - To get the day of the month, use `(instanceObj).getDate()`. It's weirdly named.

### Set Date
When you use a `____.set-timeFrame()`, you have to input a number as an argument. Each timeframe has a valid range. If you input a number greater than the range, it will simply use the remainder operator on the `parameter` and return the result.
  - `setSeconds(), setMinutes()`: 0–60.`
  - `setHours()`: 0–24
  - `setDate()` : 1–31
  - `setMonth()`: 1–12.

## OTHERS: MATH
Main Functionalities
Math provides additional features for working with the `Number` value.
   1. Trigonometry and More advanced arithmetic (square root, exponentiation)
   2. Min, Max of Numbers
   3. Random Number Generation
   4. Number Rounding Manipulation (`round, floor, ceil, abs`)

### Random Number Between Min – Max
```js
let min = 5;
let max = 10;

let randomNumber = Math.floor(Math.random() * (max - min + 1))
+ min;
console.log(randomNumber);
```

#### Components Needed for Equation
To get a random number between a specified `min` and `max` value, you need 3 components.
   1. `Math.floor()` to round the decimal to an integer. Most of the times, you want to return an `Integer` between `min` and `max`
   2. `Math.random()` to randomize the chosen number
   3. `min/max` values  to set the upper bounds
The question is how to rearrange these into an equation so that it limits the range to `min–max`. When coming up with the equation, it's good to think of the lower and upper bounds of your output. Make sure that your equation never crosses these boundaries.

#### Explaining the Equation
 1. Scale Up Math.random()
 `Math.random()` only gets a random float number from `0–0.999`. We want to scale this up so that it's able to reach the upper bound. We do this by multiplying by the range.
 ```js
 let min = 5;
 let max = 10;

 Math.random() * max
 0 * (10 - 1) // Lower Bound: 0
 0.99 * (10 - 1) // Upper Bound: 9.99
 ```
 2. Math.floor(): Limit Output to Integers & Not Floats
 We're getting values from `0–max`. One problem that we're having, however, is that we're including floats. We only want integers. We solve this problem, by using a rounding method. Uh-oh. Now the upper-bound is 8.
 ```js
 Math.floor(Math.random() * max); // gives us a value form (0 – 9)
 ```
 3. Inclusive Max? Do you want to include max as a possible output?
 Since we're using `Math.floor()`, it will always nerf the value by 1. `Math.floor(9.9999) = 0`. As our code stands now, it is excluding the `max` value. If we want to include it. We have to add `1` to counteract against `Math.floor()'s` impact
 ```js
   Math.floor(Math.random() * (max + 1)) // 0 – 10
 ```
 4. Min Setup: Establish the lower-bound
 The lower bound right now is `0`. We want to make sure that it's always the `min` we specify. We'll add the `min` to ensure that it's always at least `min`. This fixes the `min` value, but in fixing `min` we mess up the upper bound `max value`.
 ```js
 Math.floor(Math.random() * (max + 1) + min);  // min – (max + min);
 ```
 5. Fix Upper Bound Value
  In adding the `min` value, we changed the possible upper-bound output. We want to keep the `min` value intact while also limiting the upper `max`. On step 4, the upper bound output is `max + min`. We want to subtract `min`. Where we subtract min is important too!

  ```js
  Math.floor(Math.random() * (max + 1) + min - min) // This takes us back to step 3..
  Math.floor(Math.random() * (max + 1 - min) + min) // This works!
  Math.floor(Math.random() * (max - min + 1) + min) // Refactor and move the min to be with max
  ```

  ```js
  // Final Equation
  Math.floor(Math.random() * (max - min + 1) + min);
  ```
<!---------------------->
# 📟 EXAMPLES
<!---------------------->
## STRINGS
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

## NUMBERS
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

## OBJECTS
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
// Object.is()
console.log(1,Object.is(+0, -0));

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

## ARRAYS
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

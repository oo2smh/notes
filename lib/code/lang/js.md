# 🐧 Tldr
- **What**: Interpreted language with a hybrid programming paradigm. Used mainly in web dev.
- **Why**: To break down the main syntactical elements of the language.
- **How**: By outlining language core, std lib, macro tools, and concepts.

## *OUTLINE*
- 🍄‍🟫 Language Core
- 🍊 Std lib
- 🍎 Macro Tools
- 🟣 Concepts

# 🍄‍🟫 Operators/Keywords
```js
// SEMICOLON AND ASI (only use on multistatement, () [] starting statements )
let num = 1; let abc = "abc"; // need semicolons here
(1 + 2) == (2 + 1)

// LCACA (logical, comparison, assignment, concat, arithmetic)
let logical = true && !false  == true || false;
let comparison = (1 > 0 && 0 >= 0) && (0 < 1 && 0 <= 0);
let concat = "cheer" + "ios";
let arithmetic = ["+ - * / % **"];
console.log(logical, comparison, concat, arithmetic);

// MEMBERSHIP
let loose = 1 == true
let strict = 1 === true
console.log(loose, strict)
console.log(new Number(1) instanceof Number)
console.log(new Object({a:1, b:2}) instanceof Object)

// VARIABLES
const YOU = "cannot change"
num = "global var"
{ let block_scoped = 2}
console.log(num)
try {
  YOU = "reassigned"
  console.log(YOU, num, block_scoped ?? "not valid")
} catch {
  console.log("❌")
}


// SHORTHANDS
  // assignment (duo action assignments)
let num = 1
num += 1; num -= 1; num *= 1; num /= 1
console.log(["num", num]);
```

# 🍄‍🟫 Constructs
## CONDITIONALS
```js
let gender = "male"
if (gender == "female") {
  console.log("👧🏻")
} else if (gender == "male") {
  console.log("🧔🏻")
} else {
  console.log("🐵")
}

let gender = 0 ? "🧔🏻" : "👧🏻"
console.log(gender)

const pet = "dog"
switch (pet) {
  case "cat":
    console.log("🐱")
    break
  case "dog":
    console.log("🐶")
    break
  default:
    console.log("❓")
}
```

## Loops
```js
for (let i=0; i < 5; i+=1) {
  console.log(i);
}

let num = 0;
while (num < 5) {
  console.log(num);
  num += 1;
}

num = 0;
do {
  console.log(num);
  num+=1
} while (num < 5)
```

## Functions/Classes
```js
function print_msg(msg) {
  console.log(msg)
}
print_msg("hello world")

class Animal {
constructor(name, legs) {
    this.name = name
    this.legs = legs
  }

  speak() {
    console.log("Animal makes a sound")
  }
}

class Dog extends Animal {
  speak() {
    console.log("woof")
  }
}

const happy = new Dog("happy", 4)
console.log(happy.name)
happy.speak()
***```***

#  🍊 Type Constructors
> [!note] > `Value` parameter can be any datatype. Constructors yank the value and return a new value of their own datatype. `Symbol(value)` will for instance, take the value and return a new symbol. Generally, this is the extent of of a constructor's functionality. It is more often than not better to use the literal ways to create values (`{}` to create obj, `[]` to create arrays, `''` for strings, etc). This is more concise and cleaner. However, it is good to be aware that constructors exist.

```js
// PRIMITIVES
Number("42")    // 42
String(123)     // "123"
Boolean(0)      // false

// COMPLEX: BASE
Array()
Object()
Function()
Set()
```

# 🍊 Sequence Attributes
## *SHARED*
```yaml
* bracket notation []
- length
- includes()
- lastIndexOf()
- indexOf()
- at()
- slice()
```

## *STRING*
```js
// ACCESS AND INFO
s = "joyful"
codept = String.fromCodePoint(97,98,99) // ⏎ char(s) at codePt
console.log(s.codePointAt(0), codept,  s.length, s.at(-1), s.slice(1))

// SEARCH
s = "joyful"
s1 = s.startsWith("jo")
s2 = s.endsWith("ful")
s3 = s.includes("oy", fromIdx = 1)
s4 = s.indexOf("j")
s5 = s.lastIndexOf("f", fromIdx = 1)
s6 = s.search(regex)
s7 = s.match(regex)
s8 = s.matchAll(regex)
console.log(s1, s2, s3, s4, s5)

// MANIPULATE
// elongate
SP.padStart(targetLength, [padding = ' '])
SP.concat(...strN)
SP.repeat(count)
SP.padEnd(targetLength, [padding = ' '])

// trim
SP.trim()
  SP.trimStart()
  SP.trimEnd()

// substitute
SP.replace(pattern, replacement)
SP.replaceAll(pattern, replacement)
SP.toUpperCase()
SP.toLowerCase()

// transform to array
SP.split(separator) // ⏎ array
```

## *ARRAY*

```js ...............................
// Creation
Array.isArray(value)
Array.of(...elemN)
Array.from(arrayLike, [mapFn(elem, idx)], [thisArg])

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

// HIGHER ORDER
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

# 🍊 Other Attributes
## *OBJECT*

```js ...................................
// BOOLEAN CHECK
OP.hasOwnPrototype(prop) // ⏎ boolean
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

// OTHER
Object.defineProperty(obj, prop, descriptor)
Object.defineProperties(obj, props)
Object.getOwnPropertyNames(obj) // ⏎ an array of names (like Object.keys(obj))
Object.getPrototypeOf(obj)
Object.groupBy(iterable, fn) // good for getting an array of Objects and returning an object with properties containing arrays
``````````````````````````````````````

## *DATE*
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

## *MATH*
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

## *NUMBER*
```js .................................
// 🎀 FINS
Number.isFinite(val)
Number.isInteger(val)
Number.isNaN(val)
Number.isSafeInteger(val)
``````````````````````````````````````

# 🍎 Errors
```yaml ............................
SyntaxError: violates syntax rules
  - (punctuation, whitespace, valid characters)
ReferenceError: var/fn that doesn't exist
TypeError: value retrieval/action on the wrong type
   - access props on values without properties `undefined` `null`
   - invoking a non function
   - reassignment to constant variable
`````````````````````````````````````

# 🍎 Array Concepts
## _MUTATE THE CALLER_
> Some array instance methods directly mutate the caller. These methods are called destructive. On the list above, those methods with 👺 are destructive methods. Some destructive methods have a non-destructive counterpart. Unfortunately, browser support (at the time of writing) is not supported everywhere.

```js ..............................
AP.sort() = AP.toSorted();
AP.reverse() = AP.toReverse();
`````````````````````````````````````

## _EMPTY SLOTS_
> Arrays with `<empty items>` aka empty slots are called sparse arrays. These are not empty arrays because the slot is being occupied. I like to think of empty slots as filled air. It still occupies the space, but it isn't used in any meaningful way. `Empty items` are handled by array methods in different ways. Generally speaking, empty slots are counted for length/index and action is taken for removal, copy, and adding operations. Thus, `pop()` will remove an `empty item` if it's the last idx elem. `concat()` will copy the `empty item` to its shallow array. In other methods, however, it is ignored. For instance, the callbackFn is skipped for functions like `forEach(), map(), etc` It is also ignored for the `flat()` method.


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
> In JS, only shallow copies are created. A shallow copy means that object references are copied. Contrast that with a deep copy where the values of an object are copied, and saved to a different memory location. After creation, both items are distinct in a deep copy. A shallow copy is a copy whose properties share the same references as the source object from which the copy was made. Therefore, if you mutate the reference from the source copy, the change is reflected in the copy/copies as well. JS array methods either mutate the caller or return a shallow copy.

```js ......................................
const originalArray = [1, 'string', {a: 0, b: 2}];
const copyArray = [...originalArray];

copyArray[0] = 500;
originalArray[2].a = 'updated value';

console.log({originalArray, copyArray});
`````````````````````````````````````````````
******
# 🍎 Call Stack
## *_STACK FRAME VS EXECUTION CONTEXTS_*
> [!Note]
> `Stack Frame` vs `Execution Context` are they the same thing? Long story short, I don't know. Either the stack frame is a bigger container that holds the execution context, or they are separate entities that are pushed onto the call stack. For now, I have decided to think of them as 2 separate components. The reason for this being is that whenever I read about `execution context`, it is talking the creation phase and execution phase. When I look up stack frame however, it is talking about how it holds the return address, function arguments/parameters. The fact that different things are mentioned causes me to think they are different buckets.

## *_TYPES OF EXECUTION CONTEXTS_*
There are 2 types of execution contexts and they are similar except for a few key differences.

```md
Global Execution Context
- Creates a `global object` (Window in browser) during the creation phase
  - Global object has additional properties/methods (ie: `Window.console`)
- Stays on the call stack until the end of script
- This keyword is loaded only on the global execution context

Function Execution Context
- The Environment record has an additional `arguments` property
- Popped off the stack at the end of the function
```

## Phases
> [!Caution]
> There are nouns that refer to a period of time(day, hour, week, month). In JS, there are certain terms that refer to a period of time. `Creation Phase` and `Execution Phase` are obvious in that they refer to the span of time when a specific type of action is being performed.`TDZ` is a little harder to dissect. Some people say it is a concrete block of inaccessible data that physically exists. Others say it is a specific period where variables declared with `let/const` exists, but cannot be accessed. To me the latter definition makes sense. `TDZ` is a period of time when `let/const` variables exist, but cannot be accessed. So I will approach `TDZ` as such (as a period of time)

## Creation Phase
> This is the 1st part of the execution context. Memory allocation is created for local variables. JS sets up the structure for scope chain through the outer lexical env reference. The function itself and its outer lexical environment are bundled and form a `closure`. This `closure` is used whenever there needs to be variable resolution. This closure lives in the heap.

```md
* Execution context is pushed onto the call stack (This *creates the fn* in the perspective of the js engine)
* Memory Allocation: Stored in Env Record
  - Hoisting: Moved to the top
    - `Var` declared variables are hoisted and initialized to `undefined`
    - Fn declarations are hoisted in their entirety
  - `Let/const` variables are declared but not initialized to any value. They remain in a state called `TDZ` until the execution phase.
    - Under the hood, using bytecode, variables with `let/const` are assigned to the value of `TheHole` which refers to an absence of value.
* Closures are created
  - Outer Environment Record points to parent fn's reference
  - `Closure`: combination of a fn bundled together with references to its lexical env. Practically speaking, this means fns retain variables from parent scope even after parent fn has finished executing.
    - Closure is essentially environment record and its outer lexical environment that is given a name (fn identifier)
```

> Closure is a concrete noun. It exists in reality. It is not a noun describing an abstract concept like love or peace. Closure is a combination of a function with its outer lexical environment.
>
> Often times, people will define closures by its effects. For instance, they might say closure is the ability of an inner function to remember its parent function even after the parent function has executed. This is true. > This is more aptly described as one capability of a closure. It describes what a closure does. It does not define what a closure is.
</details>

## *EXECUTION PHASE*
> During the execution phase, the interpreter goes line by line and executes code. Whenever there is a `=` operator the affected variable is assigned a value. If no value is given, the variable is initialized to `undefined`. Statements are executed. Further function calls are pushed to the call stack.

> The closure lives in the heap. But if it persists unnecessarily, it consumes memory. There has to be a better way. JS garbage collection can detect closures that aren't used and then `mark and sweep` them. Generally speaking, if a function doesn't have any inner functions, the closure does not need to persist. It can be garbage collected when a function is finished running. If however, an inner function exists, the closure should remain within the heap because it might be of use in the future. Note that closures only pertain to functions. It does not pertain to other block scopes.

</details>

## *_VARIABLE RESOLUTION_*
When variables do not exist in the current scope, the JS engine can traverse through the `outer lexical environment` reference to look for that variable. Multiple `outer lexical environments` strung together is called a scope chain. Scope is simply where a variable is defined and can be accessed. There is local and global scope. Local scope can further be broken down into block or function scope. Let/const are always block scoped. When let/const exists within a function. They are scoped to the `block {}` of the function aka the function body. It's okay to say that they are scoped to the function in this case.

## *_ERROR MANAGEMENT_*
`TypeError` or `ReferenceError` might be thrown in the call stack. Generally speaking, `SyntaxError` occurs during the parsing step when the `AST` is created. When an error is thrown a `stack trace` is also provided to the user. Simply put, the stack trace will output the line/character where the error is first encountered. It will also throw a report of the active stack frames on the call stack when the error was encountered.

# 🧪 Examples
```js
let x = 10;
const y = 20;
var z = 30;

function greeting(username) {
  console.log('Hello.');
  function personalGreeting() {
    console.log(`Hello ${username}.`)
  }
}

greeting('eddy') // (ln:14)
```

## *_CREATION PHASE_*
```js
const callstack = [];

const initStackFrame = {
  parameters: null
  arguments: {length:0}
  returnAddress = 0; // line # where fn is invoked
}

const globalExecContext = {
  lexicalEnvironment = {
    environmentRecord: {
      x: 'TheHole',
      y: 'TheHole',
      greeting: function(username) {
        console.log('Hello.');
        function personalGreeting() {
          console.log(`Hello ${username}.`)
        }
      }
    },
    variableEnvironment: {
      z: undefined
    },
    outerEnvironment: null,
    this: 'Global Object'
  }
}

callStack.push(initStackFrame, globalExecContext);
```

## *_EXECUTION PHASE_*
```js
const callstack = [];

// FEC
const stackFrame = {
  parameters: {0: username, length: 1},
  arguments: {0: 'eddy', length: 1},
  returnAddress = 14; // line # where fn is invoked
}

const fnExecContext = {
  lexicalEnvironment: {
    environmentRecord: {
      'arguments': {0: 'eddy', length: 1}
      username: 'eddy'
      personalGreeting: function() {
        console.log(`Hello ${username}`);
      }
    }
  }
}

// GEC
const initStackFrame = {
  parameters: null
  arguments: {length:0}
  returnAddress = 0; // line # where fn is invoked
}

const globalExecContext = {
  lexicalEnvironment = {
    environmentRecord: {
      x: 10,
      y: 20,
      greeting: function(username) {
        console.log('Hello.');
        function personalGreeting() {
          console.log(`Hello ${username}.`)
        }
      }
    },
    variableEnvironment: {
      z: 30
    },
    outerEnvironment: null,
    this: 'Global Object'
  }
}

callStack.push(stackFrame, fnExecContext);
```

# 📗 References
- [How JS Handles Let/Const Under The Hood in Bytecode](https://www.youtube.com/watch?v=MZYDzfxyxic)
- [Why is there a TDZ?](https://2ality.com/2015/10/why-tdz.html)
- [Closures MDS](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Closures)
- [This Binding](https://medium.com/nerd-for-tech/understanding-this-binding-in-javascript-86687397c76d)

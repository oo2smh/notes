<!--==================-->
# 🔑 Keywords
<!--==================-->
```md
- Call stack
- Stack Frame
- Execution Context
- Stack Trace
- Creation Phase
- Execution Phase
- Hoisting
- Closures
- Environment Record
- Global Object
- This keyword
- Outer Lexical Reference
- Arguments property
- Scope
- Scope Chain
- Variable Resolution
```
<!--==================-->
# 🪢 Cxns
<!--==================-->
```md
- Stack Frame, Execution Cxt
- Closures, Environment Records, Outer Lexical Env Reference
- Outer Lexical Env, Scope Chain
- Variable Resolution, Closures
- Hoisting, Var
- Temporal Dead Zone, Creation Phase, Execution Phase
```

<!--==================-->
# 🪲 Deets
<!--==================-->
## _STACK FRAME VS EXECUTION CONTEXTS_
> [!Note]
> `Stack Frame` vs `Execution Context` are they the same thing? Long story short, I don't know. Either the stack frame is a bigger container that holds the execution context, or they are separate entities that are pushed onto the call stack. For now, I have decided to think of them as 2 separate components. The reason for this being is that whenever I read about `execution context`, it is talking the creation phase and execution phase. However, when I look up stack frame, it is talking about how it holds the return address, function arguments/parameters. The fact that different things are mentioned causes me to think they are different buckets.

## _TYPES OF EXECUTION CONTEXTS_
There are 2 types of execution contexts and they are similar except for a few key differences.

Global Execution Context
- Creates a `global object` (Window in browser) during the creation phase
  - Global object has additional properties/methods (ie: `Window.console`)
- Stays on the call stack until the end of script
- This keyword is loaded only on the global execution context

Function Execution Context
- The Environment record has an additional `arguments` property
- Popped off the stack at the end of the function

## _PHASES_
> [!Caution]
> There are nouns that refer to a period of time(day, hour, week, month). In JS, there are certain terms that refer to a period of time. `Creation Phase` and `Execution Phase` are obvious in that they refer to the span of time when a specific type of action is being performed.`TDZ` is a little harder to dissect. Some people say it is a concrete block of inaccessible data. Others say it is a specific period where variables declared with `let/const` existed but cannot be accessed. To me the latter definition makes sense. `TDZ` is a period of time when `let/const` variables exist, but cannot be accessed. So I will approach `TDZ` as such (as a period of time)

<details><summary>🐝 Creation Phase</summary>

> This is the first part of the execution context. Memory allocation is created for local variables. JS sets up the structure for scope chain through the outer lexical env reference. The function itself and its outer lexical environment are bundled and form a `closure`. This `closure` is used whenever there needs to be variable resolution. This closure lives in the heap.
- Execution context is pushed onto the call stack (This *creates the fn* in the perspective of the js engine)
- Memory Allocation: Stored in Env Record
  - Hoisting: Moved to the top
    - `Var` declared variables are hoisted and initialized to `undefined`
    - Fn declarations are hoisted in their entirety
  - `Let/const` variables are declared but not initialized to any value. They remain in a state called `TDZ` until the execution phase.
    - Under the hood, using bytecode, variables with `let/const` are assigned to the value of `TheHole` which refers to an absence of value.
- Closures are created
  - Outer Environment Record points to parent fn's reference
  - `Closure`: combination of a fn bundled together with references to its lexical env. Practically speaking, this means fns retain variables from parent scope even after parent fn has finished executing.
    - Closure is essentially the fn reference (identifier), environment record, and its outer lexical environment.

> [!Important]
> Closure is a concrete noun. It exists in reality. It is not a noun describing an abstract concept like love or peace. Often times, people will define closures by its effects. For instance, they might say closure is the ability of an inner function to remember its parent function even after the parent function has executed. This is true. This is more aptly described as one capability of a closure. It describes what a closure does. It does not define what a closure is.
</details>

<details><summary>🐝 Execution Phase</summary>

> During the execution phase, the interpreter goes line by line and executes code. Whenever there is a `=` operator the variable is updated. If no value is given, the variable is initialized to `undefined`. Statements are executed. Further function calls are pushed to the call stack.

> [!Note]
> The closure lives in the heap. But if it persists unnecessarily, it consumes memory. There has to be a better way. JS garbage collection can detect closures that aren't used and then `mark and sweep` them. Generally speaking, if a function doesn't have any inner functions, the closure does not need to persist. It can be garbage collected when a function is finished running. If however, an inner function exists, the closure should remain within the heap because it might be of use in the future. Note that closures only pertain to functions. It does not pertain to other block scopes.

</details>

## _VARIABLE RESOLUTION_
When variables do not exist in the current scope, the JS engine can traverse through the `outer lexical environment` reference to look for that variable. Multiple `outer lexical environments` strung together is called a scope chain. Scope is simply where a variable is defined and can be accessed. There is local and global scope. Local scope can further be broken down into block or function scope. Let/const are always block scoped. When let/const exists within a function. They are scoped to the `block {}` of the function aka the function body. It's okay to say that they are scoped to the function in this case.

## _ERROR MANAGEMENT_
`TypeError` or `ReferenceError` might be thrown in the call stack. Generally speaking, `SyntaxError` occurs during the parsing step when the `AST` is created. When an error is thrown a `stack trace` is also provided to the user. Simply put, the stack trace will output the line/character where the error is first encountered. It will also throw a report of the active stack frames on the call stack when the error was encountered.

<!--==================-->
# 🧪 Examples
<!--==================-->
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

## _CREATION PHASE_
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

## _EXECUTION PHASE_
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

<!--==================-->
# 📗 References
<!--==================-->
- [How JS Handles Let/Const Under The Hood in Bytecode](https://www.youtube.com/watch?v=MZYDzfxyxic)
- [Why is there a TDZ?](https://2ality.com/2015/10/why-tdz.html)
- [Closures MDS](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Closures)
- [This Binding](https://medium.com/nerd-for-tech/understanding-this-binding-in-javascript-86687397c76d)

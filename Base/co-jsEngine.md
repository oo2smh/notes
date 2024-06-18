<!--==================-->
# 🔑 Keywords
<!--==================-->
>The purpose of this note is to identify and categorize the various players inside of the JS engine. It identifies who these players are and their main role in the runttime environment. Other notes will focus in on the specific departments of this note in much greater detail. Here I attempt ot present a bird's eye view of the JS engine.

```md
- Source Code
- Machine Code
- Host Environment
- JS Engine
- V8 Engine
- Ignition
- Bytecode Generator
- Baseline Compiler
- Interpreter
- Bytecode Handler
- Turbofan
- Profiler
- Lexer
- Parser
- AST
- Tokenization
- Call Stack
- Stack Frame
- Execution Context
- Global Object
- this keyword
- Lexical Environment
- Variable Environment
- Environment Record
- arguments property
- Outer Lexical Env Reference
- This binding
- Global Execution Context
- Function Execution Context
- Heap
- Garbage Collection
- Closures
- JS Standard Library
- Web APIS
- Event Loop
- Microtask Queue
- Task Queue
```
<!--==================-->
# 🪢 Cxns
<!--==================-->
```md
- Source, Machine code
- Ignition, Turbofan
- Call Stack, Interpreter, Heap
- Global Execution Cxt, Function Execution Context
- Stack Frame, Execution Context
- Lexical Env, Variable Env
```

<!--==================-->
# 🪲 Deets
<!--==================-->
CPUS only understand binary (0,1) and do not understand programming languages such as Javascript. It needs an engine to parse through and convert the source code that programmers write into machine code. In JS, this engine lives within a bigger host environment (browser, server). The engine itself has different flavors for how it is implemented. The different flavors are V8(Chrome), Spidermonkey(Firefox), Chakra(IE). V8 engine is the most common, so I will focus on the V8 JS engine's implementation. The V8 engine does not live in isolation, but lives among other entities that the host environment provides. These include the `JS Standard Library`, `Web APIS`, `Event Loop`, `Task Queue`, and `Microtask Queue`. These extra entities supercharge JS allowing it to perform more actions.

Within the JS engine itself, there are 4 main departments. Within the actual engine it might not be arranged as neatly as I talk about it here, but I find it easier to chunk it into 4 groups. The groups are:
1. Parsing Department
2. Management
3. Call Stack
4. Heap

## _PARSING DEPARTMENT_
Source code must first be parsed or read by the JS engine. There are 2 main actors here: the `lexer` and the `parser`. Both of these programs are aware of JS syntax and constructs. The lexer first breaks down the source code into `tokens` in a process called tokenization. Tokens are atomic elements of a language. The biggest token groups that exist for JS are: literals, reserved words, operators, identifiers, variables and special symbols(punctuation, comments). When there is an element that is not able to be tokenized, the lexer flags it as being invalid JS and throws a `SyntaxError`. Otherwise, if there are no errors, it passes the tokens onto the parser. The parser gathers the tokens and creates the `AST` or `Abstract Syntax Tree`. The abstract syntax tree is a hierarchical, tree-like structure that groups the tokens into meaningful chunks. The tokens are thus placed along the branches (which metaphorically can be thought to represent the larger syntax constructs). The larger constructs are the different types of expressions, statements, and other syntax constructs. If the parser catches any errors at this time, it can throw a `SyntaxError` much like its sibling, the lexer. Otherwise, it passes the data of the AST to the next step of the chain.

> [!Note]
> The `AST` is important in that it creates nodes of the major syntax constructs in a language. Not only is it useful for the JS engine, its mechanism is used for linting and formatting. Popular linters and formatters such as eslint and prettier relies on the data from the `AST` to perform syntax highlighting and throw errors. In `treesitter` (through some plugins), you can dive in and have access to the `AST`.

## _MANAGEMENT_
> [!Note]
> Generally there are 2 ways to execute code: through interpretation and compilation. There are benefits and tradeoffs to both. First, interpretation is when one line/statement is executed at a time. The obvious benefit is that there is no initial prep time and it can get started. They can get to work right away. The downsides is that there is a limit on high performance. As codebases get larger, running one line/statement at a time might be slow. The other method of execution is compilation. This method entails parsing through all of the code converting it into machine code and then executing the code all at once. Compilers have a longer initial startup time, but fast execution. Instead of choosing one route, JS engines today mix and match both. The V8 engine entails both interpreters and complilers. Although JS is traditionally considered an interpreted language, there's no reason why it can't benefit from compilation too!

`Ignition` is a module within the JS engine in charge of 2 main things. First, a submodule called the `bytecode generator` looks at the AST and converts it into bytecode. The `bytecode generator` can be thought of as a baseline compiler. `Bytecode` is an `intermediate representation (IR)`. All that means is that it's not quite machine code and it's not source code. It's somewhere in the middle. Bytecodes are easier to digest and faster to process than sourcecode so most engines transfrom their AST into bytecode first. Next, the interpreter runs though the code one line/statement at a time. While it's running, another module called the `Turbofan` looks at the bytecodes that are being interpreted to look for patterns (commonly used snippets/other areas for optimization). The `profiler` submodule of Turbofan highlights these lines with patterns also called `hotspots`. Then another submodule of `Turbofan`, the compiler transforms the `hotspots` into machine code. If/when the interpreter runs into these hotspot regions, `Turbofan` already has the optimized machine code ready and does not need to recompiile. To sum it all up, `Ignition` initially complies to bytecode and interprets or runs the bytecode line by line. As the interpreter is working, `Turbofan` identifies areas that can be optimized and compiles the `hotspots` into machine code. If `Turbofan` does not find any areas for optimization, the bytecode handler of ignition creates its own machine code.

## _CALL STACK_
A stack is a `LIFO` data structure where objects are pushed in and popped out. The call stack is a data structure that manages function calls. In the bigger picture, it assists the interpreter module of Ignition as it runs through the code. As a function is called/invoked a `stack frame` and `execution context` are pushed onto the call stack. There are 2 types of `execution contexts`: global and function. The global execution context is pushed onto the call stack when the script is first loaded. For the most part these 2 execution contexts are similar. The difference are as follows:

The `stack frame` keeps track of the return address, function parameters/arguments. The Execution context is comprised of the `Lexical environment` and the `Variable Environment`. Each environment has three properties: `Environment Record` where all of the local variables and their assigned values are stored, the outer lexical reference which allows for the usage of the `scope chain` and the value of this in the context of the function.

> [!Note]
> Some call the `Lexical/Var Environment` as `Lexical/Var Object`. It's an alias to the same thing. `The Variable Environment` keeps track of variables declared with the keyword `var`. The `Lexical Environment` was created with the creation of the `let/const` keyword. If I had to guess a separate environment was created to handle the `TDZ` of `let/const`

> [!Important]
> The call stack does more than keep track of the currently running function. It helps with `var management`, `this binding`, `closures` and `hoisting`. This deserves more elaboration in a separate note.

> The built in objects of JS's standard library exists in global scope. It is provided by the host application. The actual implementation is hard to understand, but for me, it seems easier to think of the JS standard library being inputted into the Global Execution context alongside the Global object (window in browsers)

## _HEAP_
The heap is a designated area where objects live in Javascript. The only exception are function declarations which live directly on the call stack because of hoisting (This needs to be fact-checked). Every so often (depending on implementation), the garbage collector takes care of unused objects. Closures are also saved in the heap (although this depends on how you define stack/heap). Because objects live in the heap, variables do not store the actual object, but a reference to the object in memory/heap.

When an object does not have a property, similar to the `scope chain` (created by the chain of `outer lexical environment` references) the `protoypical chain` is traversed to have `property resolution`. The end object is `null` and if it does not have the property, JS returns undefined. The `prototypical-chain` relies on `prototypical inheritance` which deserves more elaboration in a separate note.

<!--==================-->
# 📗 References
<!--==================-->
- [What is Ignition?](https://stackoverflow.com/questions/54957946/what-does-v8s-ignition-really-do)
- [3 Parts of JIT Compiler](https://medium.com/@minhaz217/lets-understand-the-javascript-just-in-time-compiler-jit-and-how-the-v8-engine-works-ff6276d131a1#:~:text=The%20interpreter%20in%20the%20V8,inline%20caching%20and%20other%20optimizations%2e)
- [Big Picture V8 Engine](https://medium.com/@minhaz217/lets-understand-the-javascript-just-in-time-compiler-jit-and-how-the-v8-engine-works-ff6276d131a1#:~:text=The%20interpreter%20in%20the%20V8,inline%20caching%20and%20other%20optimizations%2e)
- [Closures in heap/stack](https://stackoverflow.com/questions/29225834/where-are-variables-in-a-closure-stored-stack-or-heap)
- [Garbage collector only Sweeps Heap](https://stackoverflow.com/questions/31698747/does-the-js-garbage-collector-clear-stack-memory)

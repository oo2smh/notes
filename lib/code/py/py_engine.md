<!--==================-->
# Interpreted or Compiled
<!--==================-->
"When you run a Python file from the command line, the Python compiler reads and converts the code into a form the computer understands. The compiled code is called byte code. Once the byte code is available, it gets passed to the interpreter, which executes the code." -- LS PY Intro Book

"A compiler is a software tool that translates human-readable source code into machine-executable code. The process of compilation involves several stages, including:"
    * lexical analysis
    * syntax analysis (parsing)
    * semantic analysis
    - code generation
    - optimization
 -- [dev.to]

Similar to JS, Python is broken down into tokens and formed back up into an AST. The first few steps of compilation, therefore is engaged by interpreted languages like JS and Python. It can be argued, therefore that the parsing,lexing, and semantic analysis phases count as full *compilation* step since technically the whole program is read. It is then transformed into byte-code which is easier for the interpreter to examine. Depends on how you define it, but undoubtedbly, interpreted languages at the very least, engage in the initial stages of compilation.

<!--==================-->
# References
<!--==================-->
## _INTERPRETED/COMPILED_
- [Python is both interpreted and compiled](https://www.scaler.com/topics/why-python-is-interpreted-language/)
- [JS is also interpreted/compiled](https://dev.to/robiulhr/is-javascript-compiled-or-interpreted-language-l20)

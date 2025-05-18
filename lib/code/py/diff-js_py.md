<!--==================-->
# General
<!--==================-->
- Py is stricter when it comes to errors
- Js is forgiving and more loose
- Py seems to focus much more on conciseness
- Py seems like more thought was put into its creation. More sensible defaults. JS is quirky (created in 10 days)
- Py is slow. JS is faster, but not as fast as compiled languages. (both are interpreted languages)
- JS lives in a host env (browser/node)
  - interpreter provided by host env
- Py is independent (Language itself comes built with an interpreter)

<!--==================-->
# Python is Stricter
<!--==================-->
## _ARGUMENTS_
- additional arguments
  - js ignores
  - py raises an error
- too few arguments
  - js sets to undefined
  - py raises an error

<!--==================-->
# Coercion
<!--==================-->
- Js coerces much more

<!--==================-->
# Truthy & Falsy Values
<!--==================-->
- JS: 🎀FUN NEO (false, undefined, null, NaN, "", 0)
- PY: (0s, False, None, Empty ("",[],()))

<!--==================-->
# Logical Operators
<!--==================-->
- [and or not] [&& || !]
- Both return last evaluated value

<!--==================-->
# Loops
<!--==================-->
- python doesn't have do-while loops!
  - have to reconstruct it using while loops + break condition

````py
condition = True
while condition:
  # block to run

  answer = input("Play again (y/n)")
  if answer == "n":
    condition = False
````

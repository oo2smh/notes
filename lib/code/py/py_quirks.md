<!--==================-->
# Scope
<!--==================-->
- [LS Scope Exercises (1-5)](https://launchschool.com/exercise_sets/7f3d1745)
- variable has to be defined before it is used
- only fns and modules scope variables. NOT ctrl-flow statements like `if/else`

```py
def scope_test():
    if True:
        foo = "Hello"
    else:
        bar = "Goodbye"

    print(foo)
    print(bar)
scope_test()
```
```py
if True:
    my_value = 20

print(my_value) # 20

if False:
   second_value = 40

print(second_value) # NameError second_value is not defined
```

- Both foo and bar are technically in scope. Else block never runs, therefore bar is left unassigned. The UnboundLocalError message is printed.
- [Clause Scope?](https://launchschool.com/books/python/read/functions_methods)


<!--==================-->
# Fns vs Methods
<!--==================-->
```py
import math
print(math.sqrt(5))           # 2.23606797749979
```
- Not a method although it looks like one. `Math` is technically a reference to a `module` object. We're not using it to perform operations on the module object. Sole purpose of the `math` object is to tell Python where to look for these fns.
- `sqrt` (is a static method) in the math module. Math module is an instance of the module object.

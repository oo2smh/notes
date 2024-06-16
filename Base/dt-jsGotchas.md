```js [Operator Precedence Weird Behavior]
console.log(1) || console.log(2) && console.log(3) || console.log(4)

// This is the same as:
console.log(1) || (console.log(2) && console.log(3)) || console.log(4)
```
- Prcedence simply adds grouping together

```js [For Loop has its own scope?]
let x = 'global'

for (let x = 0; x < 3; x++) {
  let x = 3;
  console.log('for', x);
}

x = 0
while (x < 3) {
  let x = 3;
  console.log('while', x);
  x++;
}
```
- For loop seems to have loop condition scope and iteration scope
- While loop's incrementer increments local var x and thus loop runs forever


<!--==================-->
# 📗 References
<!--==================-->
- [Operator Precedence Changes Grouping](https://stackoverflow.com/questions/46506098/why-does-short-circuit-evaluation-work-when-operator-precedence-says-it-shouldn/46506130#46506130)

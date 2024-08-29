<!--==================-->
# Basic Loop Patterns
<!--==================-->
## _POINTERS_
  ### Types
1. Coupled pointer.
  - Use if you are going to traverse in a predictable way (every element, every nth elem)

  - pointer is tied to the loop itself (for loop)
  - pointer moves by itself based on the loop logic (afterthought)
2. Decoupled pointer
  - use if you need more ctrl over your traversal
  - Examples: while, do/while
  - more control since pointer is not tied to the loop
  - move the pointer based on a condition(s)

## Find all combos (Brute Force Method)
- Nested loop to find all possible combos
  - Pairs = (N^2)
  - Complexity grows if you need to find triplets (N^3)

## Best Match Pattern
- 1D collection: find/filter by criteria(s). Best-match-pattern
  - Single Criteria
    - exact-match: find element that equals 0
    - superlatives (min,max,largest, smallest)
    - other: even/odd, contains(x)
  - Multi-criteria: More than 1 criteria for the find element
  ### Variable Usage
  - bestMatch (initialized to worst-case)
  - currentMatch
  - bestCriteria
  - currCriteria
  - bestCriteria2*
  - currCriteria2*

## Boolean Short-Circuit Traversal Pattern
- Used for problems that expect boolean as output
- Traverse the entire array and if there is an element that breaks criteria(s) return false
- Otherwise, complete traversal of array means all element meets the criterias, hence return true

## _BUILD-UP VAR_
- usually declared outside of loop

  ### CONSOLIDATION
  - a single value is being changed
  - sum, product

  ### ACCUMULATION (ADDITIVE)
  - " ", [], Adding elements or chars to a collection

<!--==================-->
# Hash Map
<!--==================-->
## _CHECK FOR PROPERTY EXISTENCE_
```js
if (prop in obj)
if (Object.hasOwn(prop, obj))
if (obj.hasOwnProperty(prop))
```

<!--==================-->
# Big O Notation
<!--==================-->
- Big o notation
  - how input scales as it grows
  - drop the factor(aka coefficient) and and constant
  - drop smaller terms in a sum
  - A way to rate algorithm
    - time/space

## _BEST TO WORSE_
- O(1)  performance doesn't scale with input size
- log2(n) --> Reducing input size by 2 at each step
- linear
- polynomial O(n^c)
- O(c^n)
- n = input size
- c = some constant

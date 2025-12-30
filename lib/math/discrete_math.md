# 1 LOGIC AND PROOFS
- ⚡ basis of reasoning. used in ai, programming, algorithms, circuit building, etc
- 🥊 understand definitions and be able to prove arguments

## Logic
- `Proposition`: statement that is either true or false
  - formed through `logical operators` and `variables`
    - `or (|,v), not (~,!), and (^)`
      - disjunction, negation, disjunction
    - propositional notation of `p(roposition),q(conseQuence)`
  - conditional: if p then q or biconditional (p if and only if q)
    - Types: inverse, converse, implication(conditional), contrapositive
  ### Types
    - `Tautology`: always true
    - `Contradiction`: always false
    - `Contingency`: neither a tautology or a contradiction
    - There are many more such laws
- `Predicate`: Dynamic statement where you can plugin different values using variables
  - Used with the `universal`, `existential`, `uniqueness` quantifiers

## Proofs
- `Inference`: using logic to derive a new statement (conclusion) from preexisting premises
- `Premises`: preceding statements
- `Argument`: series of statements that ends with a conclusion
- `Fallacies`: common forms of incorrect reasoning
- Rules of inference
  - There are many (these are algebraic manipulation of the proposition)
- `Proof`: logical argument that shows step by step why a math statement is true
  - `Postulates`: statements in a proof that we assume to be true
- `Theorem`: proven mathematical statement. A valid proof
  - `Truth table`: visual way to see all the outcomes of a proposition.
  - Use propositional laws and rules of inference to manipulate and prove your argument
- `Corollary`: theroem established from another theorem
- `Conjecture`: aka hypothesis. Statement that is supposed to be true based on partial evidence, or a heuristic argument

> [!Note] `Proof` shows the evidence of a `Theroem`!

- Ways of proving
  - Direct, contradiction, contrapositive
  - Induction

  ---

# 2 STRUCTURES: SETS, FNS, SEQUENCES, SUMS, MATRICES
- ⚡ provides useful structures and shorthands when dealing with collections
- 🥊 identify syntax and the tradeoffs of each structure

## Sets
- `Sets`:  unordered structure that contains only unique objects called `elements`
  - denoted with {} and sets are named after capital letters (ie: A: {1,2,3})
- `Intervals`: sets can have limits (inclusive) or [exclusive] (ie: (1,2), [1,2])
- `Cardinality`: size of set, shown in |(# here)|
- There are a lot of laws called `set identities` used to manipulate sets to take on a different form
### Special Sets
- `null`: empty set
- `singleton`: 1 item set
- `universal`: set containing all possible items
  - `complement`: the set formed by U - A (U = universe, A = subset)
- `superset`: parent set
- `subset`: child set
- `power set`: a higher order set, contains all subsets of the original set
  - note null set is included here!
- `multiset`: collection where an element can be duplicated

> [!Note]: Truth tables are used for propositons just as venn diagrams are used in sets
### Set Operations
- `Union`: combination of 2+ sets
- `Difference`: set containing items that are in A but not in B (A - B)
- `Intersection`: set containing both elements in A and B
- `Principle of inclusion/exclusion`: idea that helps you count elements in a union of sets
  - count the # of each individual set then subtract the intersection
### Tuples: Showing Order Within Sets
- `Tuples`: ordered collection.
  - 2 pair tuple is called `ordered pair`
- `Cartesian product`: subsets containing all possible combinations
  - `Relation`: any selection of tuples from the tool sample set of a Cartesian product. Can also be the full set itself

> [!Warning] A cartesian product is also a relation where you choose all items from a selection pool.

## Functions
- ⚡ allows you to dynamically choose values in a set and perform operation(s) to get an output. Aka a mapping of input (set 1) to output (set 2)
- `Domain`: set of all possible input values
- `Codomain`: set of all possible output values
- `Range`: specifies the limits of the output value
- `1 to 1 fn`: every element in codomain is mapped to by at most 1 domain element
- `Inverse fn`: a function that reverses the output of the original function
  - f(x) = x * 2, f^-1(x) = x / 2

## Sequences
- ⚡ allows you to have an ordered list. Usually, problems involve finding the nth term in the sequence following a pattern or function
- `Sequence`: ordered list of elements, aka function from a subset of a set of integers,
  - 🧪 Fibonacci sequence
- `Recurrence relation`: a way of expressing a sequence using 1+ preceding term(s)
- `Iteration`: 1 round of applying a function/operation to an item
- `Closed formula`: can figure out the nth term directly, without consulting previous terms. (ie: f(n) = n).
  - you can plug and play. Whereas in a sequence like the fibonacci sequence, you have to rely on previous terms to calculate the present

## Summation
- ⚡ common action of adding that occurs in a sequence
- It has its own sign Σ (sigma)
  - [lower limit, upper limit], function

## Matrices
- rectangular, 2d+ array of numbers
- compact way to visualize and write a complex structure involving 2+ dimensions

---

# ALGORITHMS
- ⚡ allows us to contrast diff algorthm by complexity and choose the most optimal solution(s)
- 🥊 write/read pseudocode, able to identify/read complexity of code, use the diff sorting/searching algos, understand when to use each programming strategy

## Pseudocode
- `Pseudocode`: fake code written in plain English (demonstrated below)
- `Algorithm`: set of instructions

## Common Problems:
  - find the best match/path in a collection
    - min/max
      1. temp var `best_match` to `+-Infinity`
        - opposite of what you're trying to find
          - -Infinity for max and +Infinity for min
      2. iterate & compare each element `curr_elem`
        - if `curr_elem > best_match` => set `best_match = curr_elem`
  - list all subsets
    - temp var `subsets` to hold all sets
    - iterate through set
      - for each item of set (nested loop):
        - temp var `curr_subset`
        - push curr item to `curr_subset`
        - if `curr_subset` is not inside `subsets`, push it
  - search problems
    1. linear search
    2. binary search
    3. jump search (`2 crystal ball prob`)
  - sort problems
    - bubble, insertion, quicksort, mergesort
  - string matching
  - greedy algorithms (optimization problem)
    - best choice at each step
    - `cashier's algorithm`: before calculators, cashiers had to quickly return the change. They would choose the best choice at each step
     - 🧪 change = 67cents: grab 2quarters, dime, nickel, and 2 cents
        - at each step cashier grabs the largest coin to get to the goal
        - grab the change using the fewest amount of coins

## Measuring Complexity
- ⚡ can measure time/space complexity: aka how fast and how much memory is consumed during each step
- best, average and worst case scenarios. Usually the worst case is used (`Big O notation`)

## Algorithm Strategies
### General Problem Solving Techniques
- construct a mental model
  - try to use a structure that best maps to your mental model
    - tree, graph, permutations, set, dicts, finite state machines
  - map the problem to a category and then go over the details
- ⚡ general way of approaching problems
  - these are different from programming paradigms (which are used to structure code)
    - imperative, declarative, oop, functional
### Other Techniques
- divide and conquer
- brute force
- greedy algorithm
- dynamic programming
- recursive
- graph based

---

# NUMBER THEORY AND CRYPTOGRAPHY
- ⚡ computer memory, encryption/decryption,
- 🥊 conversion between the different numbers
- 🥊 arithmetic (-+*/) with non-decimal numerical systems
- 🥊 modular exponentiation
  - `fast modular exponentiation`
  - `fermat's little theorem`: used in cryptography. Pick a random number a and if the test fails, the num is not prime. If it doesn't fail, the number is likely prime

## Division and Modulo: 2 sides of the same coin

- Dividend, divisor, quotient, remainder
  - dividend / divisor = quotient & remainder
  - this is shown with the division algorithm
- `a | b`: a divides b. B(divisor) / a  == integer w/ no remainder
  - 🧪 3 | 5 = 5/3 has a remainder of 2 => false
- `Congruence`: a ≡ b (mod m) if and only if a (mod m) = b (mod m)
### Large Numbers with Modulo
- ⚡ try to see if fermat's theorem applies and then try fast exponentiation
- modulo properties allows us to restructure mod problems and are the basis for
```modulo properties
- `modulo multiplication property` = `(a⋅b)mod m = [(a mod m)⋅(b mod m)]mod m`
- `modulo exponentiation property` = `(a^b)modm = ((a mod m)^b)mod m
```

1. `Fermat's little theorem`: useful for computing large remainder modulo p of large powers of integers.
  - 🧪 7^222 mod 11: 7^10 ≡ 1 (mod 11)
    - 7^222 = 7^22⋅10+2 = (7^10)^22 * 7^2 ≡ (1)^22 ⋅ 49 ≡ 5 (mod 11).
2. `Fast exponentiation`: aka `binary exponentiation`. Write the exponent in binary and square the base until the digit is 1.
  - 🧪 3^13
    - 13 = 1101 in binary
    - work from right to left

``` fermat's little theorem
a^(p−1) ≡ 1(modp)
- gcd(a,p)=1 condition has to be met
- a = integer not divisible by p
- p = prime number
- a and p are usually chosen randomly in a smart way in cryptography
```

## Numerical Representation: Different Bases
- ⚡ diff numerical systems are better suited for certain tasks
- binary (2), decimal (10), hexadecimal (16)
  - decimal is intuitive for humans
  - binary is intuitive for computers
    - octal/hexadecimal both allow us to represent binary in a more compact form
    - of these 2 hexadecimal is more commo

## Primes and GCD
- ⚡ used heavily in cryptography: finding the largest prime
- `Prime`: integer > 1 that is divisible ONLY by 1 and itself
- `Prime factorization`: process of breaking down a number into a product of prime integers
  - 🧪 60 = 2^2 * 3 * 5
  - ⛏️ `tree method`: divide by smallest prime number until you can't factor any more

``` tree method
        60
      /    \
     2      30
          /    \
         2      15
              /    \
             3      5
```

> [!Note] Factor ?== divisor ?== modulus
> They are the same!
> factors = used in *, divisor = used in /, modulus = used in %
> Focus is different, but they are 3 sides of the same coin!
### GCD
- `GCD`: greatest common divisor between 2 numbers
  - a `divisor/factor` cannot exceed the sq_root(number)
    - 🧪 81 => GCD cannot exceed 9
  - ⛏️ `Euclidean Algorithm` and `Extended Euclidean Algorithm`

## Applications of Number Theory
- 🥊 understand and know how to encrypt/decrypt keys
- 🥊 understand how to use RSA encryption
- 🥊 understand the role of the hashing function
### Cryptography
- ⚡ factoring large numbers is computationally heavy (aka secure), it is easy to multiply 2 prime numbers. `1 way difficulty` is the heart of cryptography
- `RSA`: a populary type of encryption system that relies on modular exponentiation. The modulus (modulo divisor) is the product of 2 large primes
  - to encrypt someone knows the modulus and the exponent
  - `public key system`: knowing how to encrypt does not help you decrypt
    - `encrypt`: to enshroud or obscure the msg
    - `decrypt`: to uncover, define the true message
  - `relatively prime`: aka `coprime`: two numbers have a gcd of 1
    - ⛏️ `Euler's totient function`: used to show you how many numbers are coprime to n
- it's hard to factor the product of the 2 big prime numbers
- public key 🔒: (n, e), private key 🚪: (n, d)
  - keys are tuples of 2 digits

```RSA
- encryption key (n, e) where n = pq
  - pq are 2 large primes,
  - n = modulus calculated by multiplying 2 large prime together
  - e = encryption exponent is relatively prime to (p-1)(q-1)
  - d = decryption exponent (private)

```
### Hashing Function
- used so that memory locations can be accessed quickly while maintaining an intuitive storage structure (key-value pair dict)
- most hashing functions use modulus under the hood
---

# INDUCTION & RECURSION
- ⚡ automated way of repeating steps: induction for testing & recursion for iterating

## Induction
- 🎪 dominoes or infinite ladder
- `well-ordering-prop`: every non-empty set of natural numbers has at least 1 property
- has 3 parts: basis & inductive steps
  - `basis` = starting point, prove that the foundation is solid, P(1)
  - `inductive hypothesis` = assume P(k) to be true
  - `inductive step` =  prove P(k+1) to be true
- `strong induction`: basis step + assume that if P(j) is true for all 0 < j <= k then k+1 is true
  - you assume that all prev cases prior to k is true
  - useful when P(k+1) depends on multiple earlier values
  - 🧪 in an infinite ladder. you can grab the 1st rung. You can also grab 2 rungs higher. Let's say k = 5. Assume you can climb rungs 1-5. Since you can climb rung 4. You can reach rung 6...etc
  -

#  SOURCES
- [Rosenberg Textbook 1-8,13](/home/hamin/Downloads/Engineering-Books-main/wgu/Discrete-Math.pdf)
1. Algorithms
- [primeagen fem](https://frontendmasters.com/courses/algorithms/introduction/)
2. Number Theory & Cryptography
    - [Khan Academy: Modular arithmetic Chapter](https://www.khanacademy.org/computing/computer-science/cryptography/modarithmetic/a/what-is-modular-arithmetic)
    - [how rsa crptography works](https://www.youtube.com/watch?v=qph77bTKJTM)
3. Induction and Recursion
    - [induction: recursive formula](https://www.youtube.com/watch?v=iqpeZXAqFrw)
    - [Trev Tutor: Induction](https://www.youtube.com/watch?v=Tm2PJPvAULs)
4. Counting
5. Probability
6. Modeling Computation

# REDDIT GUIDES
1. [Prep Guide](https://www.reddit.com/r/WGU/comments/18a922p/ultimate_study_guide_for_discrete_math_ii_c960_at/)

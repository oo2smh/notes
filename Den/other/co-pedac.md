<!--==================-->
# 🔑 Keywords
<!--==================-->
```md
* PEDAC
  - PPP
  - ABC
* Abstraction
- Domain/Range
- Input Validation
* Data Structure
- Abstract Data Type
* Algorithm
  - Buzzwords
  - Abstraction Levels
```
<!--==================-->
# 🪲 Deets
<!--==================-->
## _PROBLEM SOLVING MODELS_
> Launch School introduces a mental framework to systemize problem solving. It uses PEDAC an acronym for problem-solving. ABC and PPP are my personal adaptations to the PEDAC process which creates additional chunks around the PE/DA steps of PEDAC. In the end, they are all the same framework.

- `PEDAC` = Understand Problem, Examples, Data Structures, Algorithm, Code with intent
- `ABC` =  Acclimate/Align to the prob, Buckets Blueprint (write a plan), Code & Console.log
- `PPP` = Prep (PE steps), Plan (DA steps), Produce (C step)

## _ASSUMPTIONS_
> The problem typically does not give enough info. Looking at the examples and text, some assumptions need to be made. Ask your interviewer to clarify any ambiguities that you may have. Here are some things to be on the lookout for separated by the common datatype that you may encounter.

<details> <summary>🐝 General Lookouts</summary>

```md
- Lower/Upper Bounds of Values
  * `Domain`: Possible input values
  * `Range`: Possible output values
  - Use interval notation from mathematics [exclusive] and (inclusive) to specify possible values
- Input Validation
  - Can we assume that the input is always a certain data type?
    - If we can assume the data type, can we assume that within that data type, it won't be a weird value such as `0, -0, <0, '', []`?
- Term Definitions
  - Examples: word, palindrome,adjacent, consecutive, etc
```
</details> <!---------------------->

<details> <summary>🐝 Strings</summary>

```md
- Empty String
- Case Sensitivity
- Valid Values
- Alphabetical (a-z)
- Whitespace (space, new-line break, tab stop)
- Digits (0-9)
- Punctuation (.?!,;)
- Special characters (#$%)
```
</details> <!---------------------->

<details> <summary>🐝 Numbers</summary>

```md
- Integer or Float?
- +/- 0
- Negative numbers
- NaN, +/- Infinity
- Precision: Rounding
- If the answer is a float, should the output be rounded to the tenth place? Hundreth?_
  - Float rounding error. There can't be a perfect representation of certain decimal based numbers using binary
```
</details> <!---------------------->

<details> <summary>🐝 Objects</summary>

```md
- Return the same input object || new obj ref?
```
</details>

## _DATA_
> As presented by Launch School, the *Data Structure* section consists of any intermediate data structure aka collections that might be needed to go from input to output. Everyone agrees on this, but there seems to be some discrepancy on what people put here. I broadened this category to hold all intermediate variables not just collections. This includes simple variable containers such as counters and tallies. I like to think of this section as the buckets section.

> Data structures are a bigger topic in computer science. I don't want to go too much into detail at this stage, but learned a little bit out of scope to better understand this section. Specifically, I learned about `ADT` and `Data structures.`

Look at the output. If it's a data structure, you know that you will need that data structure a a certain point. Ask yourself, what data structure will help you reach the output. Is sequence important? Use an array. Is it better approached from a key-value pair approach? Use a hash map.

<details> <summary>🐜 ADT vs Data Structures</summary>

- `Abstract Data Type(ADT)` = Conceptual model of the expected operations and possible values of a data type. It's told from the point of view of the user. The ('what') a datatype should do and not how it's implemented
  - Lists (Sequence), Dictionary (Key value), Stack, Queue, Graph, Tree, Set
- `Data Structure` = The how a ADT gets implemented in the real world. From the point of view of the implementer
  - Static Arrays, Dynamic Arrays, Linked List, Hash Map, Adjacency List
</details> <!---------------------->

## _ALGORITHM_
<details><summary>🐝 Abstraction Layers</summary>

> Info can be broken down from more general to more specific. Start off with a bird's eye view and generally zoom into the details. There are generally 3 layers of `abstraction`. Within each layer, you wanna `decompose` and break down the steps into chunks. Make sure to keep each chunk appropriately abstracted for its layer. Stay in the top 2 layers when writing the algorithm. Don't overcrowd your algorithm with unnecessary complexity.
1. High Level Overview (ELI5)
2. Programming Speak (Language agnostic)
3. Language implementation (Language specific syntax & quirks)
</details> <!---------------------->

<details><summary>🐝 Buzzwords</summary>

> Using the right verbs can help ensure that you stay at the right abstraction layer. There are programming specific words such as loops or conditionals. There are language specific words such as when referring to a specific syntax. Use general verbs for the high level overview to ensure that you stay abstracted. Using the abstraction layers from the previous section, try to use verbs that match the appropriate abstraction level.
```yaml 🐜
# HIGH LEVEL BUZZWORDS
Variables: Create, Store
Collections: Select/Filter, Transform, Traverse/Search, Sort, Update, Remove
Loops: Repeat, Traverse/Search
Conditionals: Check, Test, Verify, Confirm
Operations: Calculate, Count, Combine
Other: Return, Output, Prompt

# MID LEVEL BUZZWORDS
Variables: Set, Get/Retrieve, Initialize
Collections: Iterate, Push, Pop, Append,
Loops: Iterate, For, While
Conditionals: If, Else if
Operations: Increment, Decrement

# LOW LEVEL BUZZWORDS
# Syntax specific words referring to specific methods/operators
Copy: Spread, concat
Variable: let, const
Looping: forEach, for..in, for..of
```
</details> <!---------------------->

<details><summary>🐝 Problem Solving Approach</summary>

```md
> Start off with the brute-force approach if you don't see any patterns, decompose into smaller steps and try to find any subprocesses.
- Pattern Finding
- Categorize the problem from your mental library
- Simplify the problem & solution
- Mix & Match algorithms to try to find a solution
```
</details> <!---------------------->

<details><summary>🐜 General Patterns</summary>

```md
1. Brute Force
2. Decomposition: Divide and Conquer, Dynamic Programming, Branch and Bound
3. Approximation: Greedy, Heuristic Approximation
```
</details> <!---------------------->

<details><summary>🦋 Formatting Pseudocode</summary>

> Formatting is not a huge deal when writing the algorithm. At the same time, having a consistent way of writing the algorithm can provide a sense of consistency and comfort when confronted with a new problem.
```yaml
# VISUAL MARKERS
# Visual markers are placed in gutters
# Placed before each step
(@): subprocess at that step
(*): difficult or most important step of algorithm
(?): unsure about this step

# PREFIXES
# placed before var for additional info
# used with separator (:)
in:(name): input:(inputName)
ou:(name): output:(outputName)
i:(elem): iteration(elemName)
v:(name): variable(varName)
```
</details> <!---------------------->

## _CODE WITH INTENT_
- Think about the algorithm in the context of your programming language
- Features/constraints of language
- Characteristics of data structures
- Built in method or function
- Syntax/ general patterns
- Code with intent. Log often
- Write implementation notes as necessary
- Create any test cases as needed
- Keep a mental note of variable scope of subprocesses
- Subprocesses are declared in global scope, but they are often called within the main process function
  - Keep track of which scope a variable is. Creating subprocesses and not having global variables can at times lead to scope confusion.
- Comment out extra test cases as needed and keep 1 test case.

<!--==================-->
# 🎪 CIRCUS
<!--==================-->
## _ADT AND DATA STRUCTURE TO BUILDINGS_
> To give an analogy, I like to think of ADTs as a blueprint for a building. The architect thinks about what the building should be: the entryways the exits, etc. However, the building itself is not built. This is similar to ADTS. ADTS provide a conceptual basis for what data structures should be without implementing it. *Data Structures*, on the other hand, are the implementation of ADTs. It is equivalent to an architect creating a building prototype that adheres to the safety standards and all the key points from the ADTS. Lastly, programming languages are akin to decorations placed after the building is created. Structurally, the Data Structure (building) all follow the same ADTs. However, the decorations (picture frames, paint, etc) differ between programming languages.

<!--==================-->
# 🧪 EXAMPLE
<!--==================-->
```js
/* [Start time]
INPUT: {datatype} varName: additional details about the input
OUTPUT: {datatype} varName: additional deets about output
RULES
- Enter term specifics here
- Check if input validation is needed
- Enter implicit assumptions
- Enter explicit requirements here
EXAMPLES:
- Base example here (1,2) -> 3
- Edge examples (2,3) -> 4
GOAL: Rephrase the question in your own words
------------------------------
DATA/BUCKETS/INTERMEDIATES
- {array} nameOfArray: description of array if provided
- {string} nameOfString: tally

PROCESS
  CREATE v:counter
  UPDATE the variable
@ CALCULATE the product of 3 * 3 -- @subprocessName
* VERIFY that product = 9
  - TRUE: ADD 1 to counter
  - FALSE: SUBTRACT 1 to counter
  RETURN counter variable

@Subprocess #1
  CREATE stuff here
  CHECK if it's true
    TRUE: PERFORM an action
    FALSE: PERFORM another action
*/

```


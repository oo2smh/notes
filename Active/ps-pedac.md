<!---------------------->
# OUTLINE
<!---------------------->
1. Keywords
2. Deets
3. Circus
4. Examples

<!---------------------->
# KEYWORDS
<!---------------------->
- PEDAC
  - ABC
  - PPP
- Decomposition
- Assumptions
- Abstraction
- Domain/Range
- Input Validation
- Data Structure
  - Data Structures
  - Abstract Data Type
- Algorithm
  - Buzzwords
  - Abstraction Levels

<!---------------------->
# DEETS
<!---------------------->
## MODELS OF PROBLEM SOLVING
Launch School introduces a mental framework to systemize problem solving. It uses PEDAC an acronym for problem-solving. ABC and PPP are my personal adaptations to the PEDAC process which creates additional chunks around the PE/DA steps of PEDAC. In the end, they are all the same framework.

* `PEDAC` = Understand Problem, Examples, Data Structures, Algorithm, Code with intent
* `ABC` =  Acclimate/Align to the prob, Buckets Blueprint (write a plan), Code & Console.log
* `PPP` = Prep, Plan, Produce

## ASSUMPTIONS
The problem typically does not give enough info. Looking at the examples and text, some assumptions need to be made. Ask your interviewer to clarify any ambiguities that you may have.

### General Lookouts
- Possible Range of Values
  * `Domain`: Possible input values
  * `Range`: Possible output values
  - Use interval notation from mathematics [exclusive] and (inclusive) to specify possible values
- Input Validation
  - Can we assume that the input is always a certain data type?
  - If we can assume the data type, can we assume that within that data type, it won't be a weird value such as 0, -0, <0, '', [], etc?
- Definitions of terms
  - Examples: word, palindrome,adjacent, consecutive, etc
### Strings
- Empty String
- Case Sensitivity
- Valid Values
  - Alphabetical (a-z)
  - Whitespace (space, new-line break, tab stop)
  - Digits (0-9)
  - Punctuation (.?!,;)
  - Special characters (#$%)
### Number
- What Values?
  - Integer or Float
  - +/- 0
  - Negative numbers
  - NaN, +/- Infinity
- Precision: Rounding
  - If the answer is a float, should the output be rounded to the tenth place? Hundreth?_
  - Float rounding error. There can't be a perfect representation of certain decimal based numbers using binary
### Object
- Return same input object ref or new obj ref

## DATA
As presented by Launch School, the *Data Structure* section consists of any intermediate data structure aka collections that might be needed to go from input to output. Everyone agrees on this, but there seems to be some discrepancy on what people put here. I broadened this category to hold all intermediate variables not just collections. This includes simple variable containers such as counters and tallies. I like to think of this section as the buckets section.

### Background
Data structures are a bigger topic in computer science. I don't want to go too much into detail at this stage, but learned a little bit out of scope to better understand this section. Specifically, I learned about `ADT` and `Data structures.`

- `Abstract Data Type(ADT)` = Conceptual model of the expected operations and possible values of a data type. It's told from the point of view of the user. The ('what') a datatype should do and not how it's implemented
  - [Lists (Sequence), Dictionary (Key value), Stack, Queue, Graph, Tree, Set]
- `Data Structure` = The how a ADT gets implemented in the real world. From the point of view of the implementer
  - [ {Array: [Static, Dynamic] }, Linked List, Hash Map, Adjacency List ]

### Practical Usage
Look at the output. If it's a data structure, you know that you will need that data structure a a certain point. Ask yourself, what data structure will help you reach the output. Is sequence important? Use an array. Is it better approached from a key-value pair approach? Use a hash map.

## ALGORITHM
### Layers of Abstraction
Info can be broken down from more general to more specific. Start off with a bird's eye view and generally zoom into the details. There are generally 3 layers of `abstraction`. Within each layer, you wanna `decompose` and break down the steps into chunks. Make sure to keep each chunk appropriately abstracted for its layer. Stay in the top 2 layers when writing the algorithm. Don't overcrowd your algorithm with unnecessary complexity.

1. High Level Overview (ELI5)
2. Programming Speak (Language agnostic)
3. Language implementation (Language specific syntax & quirks)

### Buzzwords
Using the right verbs can help ensure that you stay at the right abstraction layer. There are programming specific words such as loops or conditionals. There are language specific words such as when referring to a specific syntax. Use general verbs for the high level overview to ensure that you stay abstracted
  1. High Level: [Create, Store, Select, Sort, Repeat, Count, Search/Traverse, Insert, Combine, Return, Calculate , Remove, Transform, Find, Output, Update, Copy, Prompt, Check, Verify]
  2. Mid Level: [Set, Get/Retrieve, Iterate, Increment, Decrement, Initialize, Push, If, For, While, For]
  3. Language Specific: [Spread, Use Object.keys, Let, Const, etc]

### Approach to Problem Solving
Start off with the brute-force approach if you don't see any patterns. Decompose into smaller steps and try to find any subprocesses.
1. Pattern Finding
  - Categorize the problem from your mental library
  - Simplify the problem & solution
  - Mix & Match algorithms to try to find a solution

### Patterns
1. Brute Force
2. Decomposition
  - Divide and Conquer
  - Dynamic Programming
    - Branch and Bound
3. Approximation
  - Greedy
  - Heuristic Approximation

## CODE WITH INTENT
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

<!---------------------->
# CIRCUS
<!---------------------->
## ADT AND DATA STRUCTURE TO BUILDINGS
To give an analogy, I like to think of ADTs as a blueprint for a building. The architect thought about what the building should be: the entryways the exits, etc. However, the building itself is not built. *Data Structures* are the implementation of the concept, the blueprint. Lastly, even with the blueprint, there might be liberties taken by the construction company. That's likened to the language implemntation of each data structure.

<!---------------------->
# EXAMPLE
<!---------------------->
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

# VISUAL MARKERS
- Visual markers can be used to provide extra clues to steps in my algorithm
@ = subprocess at that step
* = difficult or most important step of algorithm
? = unsure about this step

# PREFIXES
- Use prefixes followed by the separator (:) to indicate variables in the algorithm. You can be much more specific about what type of variable it is too
in:counter = input:(nameOfInputVar)
ou:name = output:(name of output)
i:elem = iteration elem
v: varName

@Subprocess #1
  CREATE stuff here
  CHECK if it's true
    TRUE: PERFORM an action
    FALSE: PERFORM another action
*/
```

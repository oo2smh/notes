<!--==================-->
# 🍢 Classification
<!--==================-->
Problems can be classified by their datatype. I like to call these the problem `genre`. A problem, especially a more involved one could fit into more than one of these genres. It's akin to movies where it could be both drama/comedy.

There are also `subgenres` of problems. These are also types of problems that often exist within the main genres. Continuing with the movie analogy, an action movie can have multiple subgenres of spy, thriller, video games, etc. Likewise, problems can also have sub-genres.

## _CLASSIFICATION METHODS_
- [Data Structures Types](https://www.designgurus.io/course-play/grokking-data-structures-for-coding-interviews/doc/types-of-data-structures)
- `Genres`: Refers to a problem's linearity and their dominant datatype (Number, String, Array, Map, Set)
  - `Linear`: Data is arranged in a sequential order. 0-9. From one node, there is one adjacent to the left and right.
    - 🧪 String, Array, Linked list, Stacks, Queue,
  - `Nonlinear`: There are multiple ways to traverse the structure.
    - 🧪 Graph, Tree, etc
  -
- `Subgenres`: Any other form of not necessarily tied to the dominant datatype that is used.
  - Matrix
  - Combinatorics
    - Longest/Shortest of some requirement
      - Requirement (k length)
  - Subset
- `Theme`: Main gist of a feeling. Your intuition. Gut feeling solution. Big idea. It can be summed up in 1 or few words. Often it refers to the main theme(s) used to solve a problem. Aka the high level overview
  - "This is a sorting problem. This is a hash-table problem"
- `Archetypes`: These are the clearest demonstration of a concept or problem. Example includes the use of `two sum` to show 2 pointers.
- `Tags`: Additional forms of categorization

- Classify the problem by `(Genre)(Subgenre(s))(Tags)`
  - 🧪 (Linear/string)(Combinatorics/subarray/bestMatch)
  - 🧪 (Linear/array)(Combinatorics/Arrangement)(String Processing)

## _COMBINATORICS_
- [Discrete Mathematics Explained](https://www.youtube.com/watch?v=q4L-wUF3yig)
Combinatorics is a topic within discrete mathematics that deals with counting/rearranging a part of the whole.
 - The `part` can vary in it characteristics

  ### Parts
Let's assume that the whole is = [1 2 3 4 5]

- There are 2 main factors when dividing up the part of the whole.
  1. Is it connected (contiguous)?
  2. Does order matter?
- I will list the grouping of the parts by the frequency in which they show up

    #### Contiguous, Ordered (Subarray, substring..)
- `Sub/Sub(collectionName)`: Order matters. Getting a contiguous slice of the whole
  - VALID: [1 2], [1,2,3], [1 2 3 4 5]
  - INVALID: [1 3] (not connected)
  - 🧪 Subarray, Substring
  * A common subgroup is called the `best-match pattern`
    - common words include superlatives [longest, smallest, min, max] or words that signify containment [contains, includes]
    - good candidates for `sliding window` pattern

    #### Non-contiguous, Ordered (Subsequence)
  - A subsequence contains the original order of the collection, but it doesn't have to be contiguous
  - VALID: [1 4], [1 2 5]
  - INVALID: [2 1]

    #### Non-contiguous, (Unordered) (Cobmos)
  - Order doesn't matter. Looks at inclusion of element not the order
    - People use this word loosely to mean subsequence sometimes. Ask for clarification when this term is used
  - VALID: [1 2], [1 3] === [3 1]
  - [1 3] and [3 1] would be considered 1 combo because they both include 1 and 3
- `Permutation`
  - Will give you the greatest amt of parts
  - Looks at both inclusion and arrangement of part
  - [1 2], [2 1], [1 3]...
  - Unlike combos, [1 2] and [2 1] both count as diff permutations cause the order differs

<!--==================-->
# 👊 TOOLBOX
<!--=================-->
- `Paradigm Shift`: A way of thinking to help solve the problem.
  - Divide and conquer
- `Guidelines`: These are the general patterns that are used in virtually all problems
  - Nested loop
  - Comparison between 2 collections
  - Edge Case + Main Logic
  - In place vs out of place
- `Techniques`: Akin to plot devices. These are the moving force behind solving problems. There are 2 broad groups of techniques 1. Standardized (Data Structures) 2. Other
  1. Framing (Structure)
    - Data Structure
    - Helper Variables
      - State trackers
      - Build up (Accumulation)
- `Formulas`: Certain techniques are often used together. If so, the techniques are chunked together and given a name. These are called formulas.
- `Tricks`: Language specific, syntactical methods that allow you to solve a problem in a neat, concise and/or effient way.
  - built in sort() method
  - destructuring swap
  - set data structure
- `Pitfalls`: Common stuck points, confusion and difficulty in a problem. These are good to be aware of before attempting problems as it can be a headache if you are ensnared in it during problem-solving
  - loop final elem exclusion
  - missing/misplaced braces
  - scope confusion
- Certain methods/operators are often used in tandem to solve a particular problem. These can also be shorthands to concisely solve an issue (`ie: destructuring to swap`).

It's beneficial to remember these combinations as its own chunk. I like to think of these as `techniques`, `combos` or `composite procedures`.

<!--==================-->
# TECHNIQUES
<!--==================-->
These are what everyone refers to as patterns. You should be able to associate a prob's classification (genre,subgenre) with the technique()

## _BEST MATCH_
- used for combinatorics (subsequence) problems
- used for problems that have a superlative word (biggest, smallest, min, max) and for words like (contains, includes)
- A valid match passes the criteria(s) given by the problem
  - smallest value of k length (2 criterias)
- involves looking at each match currentMatch and comparing it with the bestMatch
- usually involves auxilary vars
  - v:bestMatch, v:currentMatch
  - might include vars for criterias (bestMatchLength, currMatchLength)

## _2 POINTERS_
- [2 Pointers Breakdown](https://interviewing.io/two-pointers-interview-questions)
- A general approach of having 2 variables pointing to diff positions of a collection
- A for loop gives you a pointer, but its definition is determined in its inception
  - meaning it will only move at the pattern specified during creation

 ### What is a Pointer?
- a pointer in programming, refers to variables. To reduce confusion with this definition, I will call the pointers from the 2 pointers pattern, `iteration-pointers`. IPs are variables that hold the position of a collection.

- How many pointers in this example?
```js
for (let i = 0; i < arr.length; i++) {
  console.log(i);
}
```
- If you want more ctrl over a pointer, you can decouple it from the loop.
 - This means to declare the variable outside of the loop
```js
let secondPointer = arr.length - 100;
for (let i = 0; i < arr.length; i++) {
  if (arr[i] !== arr[secondPointer]) return "not a palindrome";
}
```
  ### Usage
- Used to more effectively traverse an array

  ### Types
- 2-pointer patterns can be broken down by the position, movement and/or the comparison between the pointers.
1. Fixed 2 Pointers (Nested Loop)
  - Inefficient. Used to gather all subsequences
  - Outer var i (remains fixed for the duration of inner loop) and the inner var moves
2. Sliding Window
3. Rivaling 2 Pointers
  - Start both pointers at opposite ends and move them til they touch
  - Usage:
    - reversing an array (in-place swaps)
    - palindrome check
    - pluck 2 items (sorted array)
      - (Determine if there are 2 items in collection that sums to k)
4. Partioning
    - Divides the whole into partitions. Helps with space complexity b/c instead of creating/storing leftPartition, midPartition, rightPartition, etc, you use the input collection and refer to its positions.
    - [2 Pointer Partition Guide](https://www.reddit.com/r/leetcode/comments/18g9383/twopointer_technique_an_indepth_guide_concepts/)
    - sort a structure of 3 elements (ie: 0, 1, 2)
5. Dual Structure
  - 1 pointer for 1 data structure, 1 pointer for a different data structure
    - used in the implementation of the merge-sort functionality
6. Fast & Slow Pointers
  - Used to check if there is a cycle in a linked list

### SLIDING WINDOW
- [Sliding Window Explained](https://www.youtube.com/watch?v=MK-NZ4hN7rs&t=2s)
- infamous, one of the most common implementation of the 2 pointers
- Using the 2 pointers, you create a slice (all elems between left-pointer and right-pointer)
- Used in `best-match problems`
  1. Fixed Sliding Window
  2. Dynamic Sliding Window
  3. Dynamic Sliding Window with Auxilary Data Structure

<!--==================-->
# TRICKS
<!--==================-->
Tricks are neat,syntactical shorthands used for common procedures

## _SWAPS_
```js
let arr = [1,2,3]
[arr[0], arr[1]] = [arr[1], arr[0]];
console.log(arr) [2,1,3];
// Lefthand side is reassignment. arr[0] is reassigned to arr[1] and arr[1] is reassigned to arr[0].
```

## _MIN/MAX BETWEEN 2_
```js
let bestMatch = Math.max(currentMatch, bestMatch)
let bestMatch = Math.min(currentMatch, bestMatch)
```
<!--==================-->
# Pitfalls
<!--==================-->
## _LINEAR COLLECTION TRAVERSAL_
- [One-Off](https://interviewing.io/arrays-interview-questions#common-mistakes-in-interviews-featuring-arrays)
- Off by one errors
- Out of bounds




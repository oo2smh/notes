# Tldr 🐧
- **What**: The patterns and methods of problem solving.
- **Why**: Done via `algorithms`. Many algorithms are common and feature
  a `data structure`, a common implementation of an adt
- **How**: Through code. Mainly through ctrl flow statements (conditionals,
  loops)

# Terms 📗
- `Algorithm`: Recipe. A series of steps.
- `Adt`: Abstract Data Type. Theoretical/conceptual model that describes *what* a datatype does NOT *how*.
  - `Primitive`: Simple. Baked into a language. (Int, boolean, etc).
  - `Complex`: Collections. Often used in data structures/algorithms.
- `Data structure`: practical implementation of an *ADT*.
- `Technique/Pattern`: Does not involve the use of a data structure.
  - [2 pointers, sliding window, dynamic programming]
- `Tricks`: Shorthands. Syntactical shorthands. Min-max. Faster swap. Comprehensions.
- `Genres`: Way of organizing a problem based on dominant data structure, technique, prob-type, subgenres.
  1. Sorting
  2. Recursive
  3. Dynamic Programming


# Organization
> Physical memory is stored in a contiguous region called RAM 🚎. The data structure that maps most closely to the physical memory is an array

## *DS: LINEAR (SEQUENTIAL)*
- Linked List
- Arrays

## *DS: NONLINEAR (NON-SEQUENTIAL)*
- Hash Map
- Pathing
  - Trees
    - Binary
    - Non-binary
  - Graphs

## *VAR: IDENTIFIERS*
### Loop Idx Pointers
> Pointer is an overloaded term. Academically, it refers to a signpost pointing to a memory address. Algorithmically, the term "pointer" it refers to a marker that points to an idx. In both cases, a pointer is a marker/signpost that points to the memory address/idx that holds the value. It does not refer to the value itself. An element/value is the actual value that is stored in the memory address/idx.

- `i,j,d`: loop "scout/traversal" pointers
- `L/R, L/M/H`: common positional pointers (left, right, low, mid, high)
- `lidx`: len(IN) - 1
- `p1, p2, p3`: other pointers as needed

### Loop Idx Values
> The values stored by the idx pointers. Add _val to the identifier or use common predefined names

- `(i/j/d)_val`
- `prev_val, curr_val`

d
### Node-Based Pointers
> In other ds that use nodes (linked lists, trees, graphs, etc) the pointer can be thought of as using the academic definition of a pointer. It points to the memory address. These are usually used as an attribute of a class

- `prev,curr,next`: linked list
- `src/dst | henad/tail`: acts as the `bounder pointer` similar to `L/M/H` in loops

### Node-Based Values
> It might be convenient to store the values stored in the elements as variables. This reduces cognitive load. This is optional.

- `child, parent, sibling`: parent = curr.prev c, lchild = curr.left, rchild = curr.right

### Other Common Variables
- AGGREGATION:
  - `best_val, min_val, max_val`
  - `sum, product`
  - `counter_map, hset`
- `res, tmp`


# Sorting 🧮
> Common/solved issue that exemplifies that a problem can have multiple solutions

## *TERMS*
- `Round/Row`: Outer loop (i)
- `Run/Col`: Lv2 loop (j)
- `Sweep/Depth`: Lv3 loop. Hardly used (k)
- `Cell/Elem`: general way to refer to a value at the pointer
- `Pointer`: var that stores the memory address of another value


| Sort Algo 📜 | Worst Time ⌛ | Avg Time ⏲️ | Space 🌌 |
| --- | --- | --- | --- |
| `Bubble` | n^2 | n^2 | 1 |
| `Selection` | n^2 | n^2 | 1 |
| `Insertion` | n^2 | n^2 |1 |
| `Merge` | nlog(n) | nlog(n) | n |
| `Quick` | n^2 | nlog(n) | log(n) |
| `Bucket` | n^2 | n + k | n |


## *PSEUDOCODE*
> Common convention in many languages is to make start (inclusive), end (exclusive). So this will be my default.

```md
# BUBBLE SORT (in place) -- ROUND: bubble largest val to end. RUN: swap/move larger val with smaller
- FOR i [0, len(in) - 2)
  - FOR j [1, len(in) - i)
    - IF j-1_val > j_val: SWAP j-1_val with j_val


# SELECT SORT (in place) -- ROUND: swap smallest val to left. RUN: identify idx of min_val
- FOR i [0, len_IN)
  - min_idx = i
  - FOR j [0, len_IN)
    - IF j_val < min_val: min_idx = j
  - SWAP j_val with min_val

# INSERTION SORT -- ROUND: Swap i_elem to proper position in left sorting region. RUN: capture idx of swap position
- FOR i [1, len_IN)
- FOR j [i-1, 0]: -- rev
  - IF J




```

## *N^2 ALGORITHMS (BUBBLE, SELECTION, INSERTION)*
```py
def bubble_sort(ls):
    """ROUND: Place the local max-value towards the end
         RUN: Swap adjacent values to 'bubble' the shift the larger value to the right
        PERF: O(n^2). Simplest to implement.
    """

    n = len(ls) - 1
    for i in range(0, n):
        for j in range(0, n-i):
            if ls[j] > ls[j+1]:
                ls[j], ls[j+1] = ls[j+1], ls[j]
    return ls

def select_sort(ls):
    """ROUND: Swap the indices of ith-elem with local_min elem
         RUN: Find local min idx by comparing
        PERF: O(n^2). Each run does less. Cond/Finding min (2 actions) < swapping (3 actions)
    """
    n = len(ls)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if ls[j] < ls[min_idx]:
                min_idx = j
        ls[i], ls[min_idx] = ls[min_idx], ls[i]
    return ls

def insertion_sort(ls):
    """ROUND: Get ith-elem (🎯) sorted/placed into left sorting region.
         RUN: Move 🎯 left until left until Left value is smaller than 🎯
        PERF: O(n^2). Each run has a good chance of not needing to run through entire sorted list.
    """
    for i in range(len(ls)):
        for j in range(i, 0,-1):
            if ls[j] < ls[j-1]:
                ls[j], ls[j-1] = ls[j-1], ls[j]
                continue
            break
    return ls

```

## *MERGE*
```py
def merge_sort(ls):
    # base case
    if len(ls) <= 1:
        return ls

    # pre
    mid = len(ls) // 2

    # recursive (split)
    l = merge_sort(ls[:mid])
    r = merge_sort(ls[mid:])

    # post (merge)
    return merge(l, r)

def merge(l, r):
    res = []
    i, j = 0, 0 # 2 pointers to compare smallest items of l, r
    while i < len(l) and j < len(r):
        if l[i] < r[j]:
            res.append(l[i])
            i += 1
        else:
            res.append(r[j])
            j += 1
    return res + l[i:] + r[j:]  # silently fails if idx is out of bound
```

## *QUICK*
```py
def quickSort(arr: list[int], s: int, e: int) -> list[int]:
    if e - s + 1 <= 1:
        return arr

    pivot = arr[e]
    left = s # pointer for left side

    # Partition: elements smaller than pivot on left side
    for i in range(s, e):
        if arr[i] < pivot:
            tmp = arr[left]
            arr[left] = arr[i]
            arr[i] = tmp
            left += 1

    # Move pivot in-between left & right sides
    arr[e] = arr[left]
    arr[left] = pivot

    # Quick sort left side
    quickSort(arr, s, left - 1)

    # Quick sort right side
    quickSort(arr, left + 1, e)

    return arr
```

## *BUCKET*
```py
def bucketSort(arr):
    # Assuming arr only contains 0, 1 or 2
    counts = [0, 0, 0]

    # Count the quantity of each val in arr
    for n in arr:
        counts[n] += 1

    # Fill each bucket in the original array
    i = 0
    for n in range(len(counts)):
        for j in range(counts[n]):
            arr[i] = n
            i += 1
    return arr
```
********
# Techniques
## *2 POINTERS*
> 2 different types. Duet and Window. Duet compares the 2 values located at the 2 pointers and takes an action. Window looks at the region that are contained BETWEEN the 2 pointers. The 2 pointers act as the bounds for a region.

- Duet pointers can be placed at different locations. Common placement patterns include `adjacent`, `ends` (head/tail), `fast/slow`. `Fast/slow`.

### *Remove Duplicates*
```py
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l = 1
        for r in range(1, len(nums)):
            if nums[r] != nums[r - 1]:
                nums[l] = nums[r]
                l += 1
        return l
```

### *Remove Target Element*
```py
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # 2 pointers: l (update-pointer): moves on update
        # r (baked-in pointer) triggers update on non-2
        l = 0
        for v in nums:
            if v != val:
                nums[l] = v
                l += 1
        return l

```

# Stack
## *BALANCED PARENTHESIS*
> problem about considering all of the possibilities.

```py
class Solution:
    def isValid(self, s: str) -> bool:
        matches = {"(": ")", "{": "}", "[": "]"}
        stack = []

        for char in s:
            if char in "([{":
                stack.append(char)
            elif char in ")}]":
                if not stack or (stack and char != matches[stack[-1]]): # in stack and invalid
                    return False
                stack.pop() # in stack and valid
        return not stack
```

## *MIN STACK*
> adding an additional partner stack that keeps track of min values.
```py
# key is appending/popping from min stack when you append/pop to main stack
   def push(self, val: int) -> None:
        # push and set new min
        self.stack.append(val)
        if self.min_stack:
            minimum = min(self.min_stack[-1], val)
            self.min_stack.append(minimum)
        else:
            self.min_stack.append(val)

    def pop(self) -> None:
        # pop from both stacks
        self.stack.pop()
        self.min_stack.pop()
```



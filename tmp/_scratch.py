info = {
    "why sorting?": "it's a common problem. It shows the power of algorithms and highlights that there are multiple solutions to the same prob",
    "iteration_terms": { "round/row": "each outer-loop iteration", "run/col": "each inner-loop iteration", "sweep/depth": "level 3 loops. hardly used"},
    "elem_terms": {"cell/elem": "general way to refer to val",
                   "(i/j/k)-cell/elem": "way to talk about the values for each scope",
                   "ibis🦢": "ith elem", "jellyfish🪼": "jth element", "kiwi🥝": "kth element",
                   }
}

nums = [4,1,2,3,5,0,6]

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
    n = len(ls)
    for i in range(n):
        for j in range(i, 0,-1):
            if ls[j] < ls[j-1]:
                ls[j], ls[j-1] = ls[j-1], ls[j]
                continue
            break
    return ls


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

def quick_sort(ls):
    pass

print(merge_sort(nums))

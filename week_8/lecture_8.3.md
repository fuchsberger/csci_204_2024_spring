# Big O on Recursion

**Acknowledgement:** Thanks to Prof. Lee for providing the notes for today.

```python
def add(list_a, list_b):
  if len(list_a) == len(list_b):
    for i in range(len(list_a)):
      list_a[i] += list_b[i]
      return list_a
  else:
    return []
```
What is the runtime of this `add` function?
- When the two input lists have the same length: `O(n)`
- When they don't: `O(1)`


## Best, Worst, and Average Cases
Depending on the input, the algorithm may have a dierent runtime.
When the input produces the best runtime, we can it the best case analysis.
- Similarly, when it produces the worst runtime, we have the worst case analysis.
- Averaging out all the possibilities, we obtain the average case analysis, which is
hard to do.
- In most algorithm analysis, we focus on the worst case analysis, and occasionally the best case.

### Example: Factorial
```python
# Iterative Appraoch
def fact(n):
  ans = 1
  if n > 1:
    for i in range(1, n+1):
      ans *= i
  return ans
```
```python
# Recursive Appraoch
def fact(n):
  # base case
  if n == 0: return 1
  # recursive cases
  return n * fact(n - 1)
```

For the iterative one, it is obvious line 5 is repeated `n` times, hence the runtime is `O(n)`. But, how do we count the number of operators" in the recursive version?

We can count how many times it calls itself (line 5), which is n times. So, the recursive version is also `O(n)`.

### Example: Filenames
Check out the filename algorithm from `lecture_8.2.md`

How do we determine the runtime complexity of the above functions? We need to ask what is the varying input size? the size of **paths**. That is the total number of items under this folder and its sub-folders. That also describes how many times the recursive function calls itself. i.e., `O(n), n:` # of items.

### Example: Root finding
Check out the root finding algorithm from `lecture_8.2.md`

Let's take a look into the root nding function. In each iteration, the length is divided by 2. So, lines 8-12 are repeated log2 n times. i.e., O(log n). Same to the recursive version.

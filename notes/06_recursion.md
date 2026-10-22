# Recursion — Short Notes

## What is recursion?

Recursion is a technique where a function calls itself to solve a smaller
version of the same problem. A recursive function needs:

1. A **base case** that stops the calls.
2. A **recursive case** that moves toward the base case.

```python
def count_down(n):
    if n == 0:          # base case
        return
    print(n)            # work
    count_down(n - 1)   # smaller problem
```

## Head and tail recursion

- **Head recursion:** the recursive call happens before the main work. The
  work is performed when calls return, so output is commonly reversed.

  ```python
  def print_increasing(n):
      if n == 0:
          return
      print_increasing(n - 1)  # recursive call first
      print(n)                 # work afterward
  ```

- **Tail recursion:** the recursive call is the last operation in the
  function. The work happens before the next call.

  ```python
  def print_decreasing(n):
      if n == 0:
          return
      print(n)                 # work first
      print_decreasing(n - 1)  # last operation
  ```

Both versions above make `n` calls, so they take **`O(n)` time** and use
**`O(n)` auxiliary space** for the call stack. Python does not optimize tail
recursion, so tail recursion does not reduce stack space in Python.

## How to calculate time and space complexity

For a recursive function:

1. Let `n` be the input size.
2. Count the work done in one call, excluding recursive calls.
3. Count how many recursive calls are made and how much smaller the input
   becomes.
4. Write a recurrence and simplify it.
5. For space, count the maximum number of active calls (**recursion depth**)
   and extra objects held at the same time.

Common examples:

- One call on a problem of size `n - 1` with constant work:
  `T(n) = T(n - 1) + O(1)` → **`O(n)` time**.
- Two calls on problems of size `n - 1`:
  `T(n) = 2T(n - 1) + O(1)` → **`O(2^n)` time**.
- Two calls on problems of size `n / 2`:
  `T(n) = 2T(n / 2) + O(n)` → **`O(n log n)` time**.

The stack space is usually the recursion depth. Therefore, a linear chain of
calls has **`O(n)` space**, while a divide-and-conquer algorithm can have
`O(log n)` stack space if calls return before another branch remains active.
Also include memory used by copied slices, lists, or other temporary objects.

---

# Recursive String Reversal — Detailed Notes

## 1. Original recursive approach

```python
def reverse_recursive(s):
    if len(s) <= 1:
        return s
    return reverse_recursive(s[1:]) + s[0]

print(reverse_recursive("hello"))  # olleh
```

### How it works

Each call reverses everything after the first character, then adds the first character to the end.

For `"hello"`:

```text
reverse("hello") → reverse("ello") + "h"
                 → reverse("llo") + "e" + "h"
                 → ...
                 → "olleh"
```

### Complexity

- **Time: `O(n²)`** — `s[1:]` copies characters, and concatenation builds strings of increasing lengths. Across all calls, this does work proportional to `1 + 2 + ... + n`, which is `O(n²)`.
- **Auxiliary space: `O(n²)`** — every recursive call holds its own sliced string (`"ello"`, `"llo"`, `"lo"`, and so on). These slices remain alive together while the calls are waiting for deeper calls to return. Their combined size is `O(n²)`.
- The **recursion stack alone** is `O(n)`. The slices are what raise the total auxiliary space to `O(n²)`.

> Space complexity normally measures the maximum extra memory needed at one time (peak live memory), not the sum of every allocation over the whole run. In this function, the slices are simultaneously live, so they really do contribute `O(n²)` peak auxiliary space.

## 2. Recursive version with less extra space

Avoid slicing by passing an index:

```python
def reverse_recursive(s, i=0):
    if i == len(s):
        return ""
    return reverse_recursive(s, i + 1) + s[i]

print(reverse_recursive("hello"))  # olleh
```

- **Time: `O(n²)`** — repeated string concatenation copies increasingly long results.
- **Auxiliary space: `O(n)`** — the recursion stack is `O(n)`, and the intermediate returned strings require at most `O(n)` live space at a time.

This improves space use, but not time complexity.

## 3. Recursive version with `O(n)` time

Strings are immutable in Python, so convert the string to a list and swap characters in place:

```python
def reverse_recursive(s):
    chars = list(s)

    def reverse_chars(left, right):
        if left >= right:
            return
        chars[left], chars[right] = chars[right], chars[left]
        reverse_chars(left + 1, right - 1)

    reverse_chars(0, len(chars) - 1)
    return "".join(chars)

print(reverse_recursive("hello"))  # olleh
```

- **Time: `O(n)`** — each character is involved in at most one swap.
- **Auxiliary space: `O(n)`** — the character list uses `O(n)` space, and the recursive stack uses `O(n)` space.

## 4. Most practical Python option

If recursion is not a requirement, use Python's slice reversal:

```python
def reverse_string(s):
    return s[::-1]

print(reverse_string("hello"))  # olleh
```

- **Time: `O(n)`**
- **Auxiliary space: `O(n)`** for the reversed result.

## Remember

- Count the **recursion stack**.
- Count extra objects, such as slices or lists.
- Space complexity means peak extra memory, not total memory allocated over the entire execution.

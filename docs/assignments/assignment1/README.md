# Sequence Selector

## Problem Overview

This assignment focuses on implementing methods to operate on data structures that implement the `Sequence` abstract base class. Each method is clearly specified, is independent of the other methods, and is designed to provide relatively simple functionality. So, this is a great context in which to practice systematic, disciplined development and test-based verification.

## The `SequenceSelector` methods

You must correctly implement all the method bodies of the provided `Selector.py`file. Your implementation must adhere **exactly** to the API of the methods, as described in the provided source code comments and as described below.

```python
class SequenceSelector:
  def min(seq, key = None)
  def max(seq, key = None)
  def kmin(seq, k, key = None)
  def kmax(seq, k, key = None)
  def range(seq, low, high, key = None)
  def ceiling(seq, k, key = None) 
  def floor(seq, k, key = None)
  def search(seq, target, key = None)
```

**Refer to the `Selector.py` source code file for the complete specification of each method's required behavior.** For an overview of each method, brief descriptions and example calls are provided below. While these methods should independent of any specific data type, in each example the variables are integers. The definitions of "less than", "greater than," and "equal to" for values are defined by either the data in the sequence or the member variable selected by the key (which is optional for the client, as demonstrated by the example methods calls below). The following are examples of keys that may be passed in by the client.


```python
def key_function(value):
  '''Return the x member variable of the input value'''
  return value.x

# Return the x member variable of the input value (but using a lambda)
lambda_key_variable = lambda value: value.x
```

### The `min` method

This method selects the minimum value from a given sequence. Examples:

`seq` | `min(seq)`
----- | -----------------
[2, 8, 7, 3, 4] | 2
[5, 9, 1, 7, 3] | 1
[8, 7, 6, 5, 4] | 4
[8, 2, 8, 7, 3, 3, 4] | 2


### The `max` method

This method selects the maximum value from a given sequence. Examples:

`seq` | `max(seq)`
----- | -----------------
[2, 8, 7, 3, 4] | 8
[5, 9, 1, 7, 3] | 9
[8, 7, 6, 5, 4] | 8
[8, 2, 8, 7, 3, 3, 4]| 8


### The `kmin` method

This method selects the k-th minimum (smallest) value from a given sequence.
A value is the k-th minimum if and only if there are exactly k - 1 distinct
values strictly less than it in the sequence. Note that `kmin(seq, 1)
== min(seq)` and `kmin(seq, len(seq)) == max(seq)`.
Examples:

`seq` | `k` | `kmin(seq, k)`
----- | --- | ---------------------
[2, 8, 7, 3, 4] | 1 | 2
[5, 9, 1, 7, 3] | 3 | 5
[8, 7, 6, 5, 4] | 5 | 8
[8, 2, 8, 7, 3, 3, 4]| 3 | 4


### The `kmax` method

This method selects the k-th maximum (largest) value from a given sequence.
A value is the k-th maximum if and only if there are exactly k - 1 distinct
values strictly greater than it in the sequence. Note that `kmax(seq, 1) == max(seq)` and `kmax(seq, len(seq)) == min(seq)`.
Examples:

`seq` | `k` | `kmax(seq, k)`
----- | --- | --------------------
[2, 8, 7, 3, 4] | 1 | 8
[5, 9, 1, 7, 3] | 3 | 5
[8, 7, 6, 5, 4] | 5 | 4
[8, 2, 8, 7, 3, 3, 4] | 3 | 4


### The `range` method

This method selects all values from a given sequence that are greater than or
equal to `low` and less than or equal to `high`.

`seq` | `low` | `high` | `range(seq, low, high)`
----- | ----- | ------ | ------------------------------ 
[2, 8, 7, 3, 4] | 1 | 5 | [2, 3, 4]
[5, 9, 1, 7, 3] | 3 | 5 | [5, 3]
[8, 7, 6, 5, 4] | 4 | 8 | [8, 7, 6, 5, 4]
[8, 2, 8, 7, 3, 3, 4] | 3 | 7 | [7, 3, 3, 4]


### The `floor` method

This method selects from a given sequence the largest value that is less than or
equal to `k`. Examples:

`seq` | `k` | `floor(seq, k)`
----- | ----- | ------------------------
[2, 8, 7, 3, 4] | 6 | 4
[5, 9, 1, 7, 3] | 1 | 1
[8, 7, 6, 5, 4] | 9 | 8
[8, 2, 8, 7, 3, 3, 4] | 5 | 4


### The `ceiling` method

This method selects from a given sequence the smallest value that is greater than
or equal to `k`. Examples:

`seq` | `k` | `ceiling(seq, k)`
----- | ----- | --------------------------
[2, 8, 7, 3, 4] | 1 | 2
[5, 9, 1, 7, 3] | 7 | 7
[8, 7, 6, 5, 4] | 0 | 4
[8, 2, 8, 7, 3, 3, 4] | 5 | 7

### The `search` method

This methods searches for a target in the given sequence and returns the index
of the first element that matches target, or `None` of the target does not
exist within the sequence. Examples:

`seq` | `target` | `search(seq, target)`
----- | ----- | ------------------------
[2, 8, 7, 3, 4] | 2 | 0
[5, 9, 1, 7, 3] | 1 | 2
[8, 7, 6, 5, 4] | 9 | None
[8, 2, 8, 7, 3, 3, 4] | 3 | 4


## Notes and Other Requirements

- The `Selector.py` source code file is provided in the `startercode` folder in Vocareum. You can download `Selector.py` from Vocareum and work on your local machine.

- The comments provided in `Selector.py` describe the required behavior of each method.

- All parameters to your methods must remain unmodified.

- You may add any number of additional helper methods that you like, but you may not change the signature of any pre-defined methods.

- If you want to run the tests you wrote at the bottom of `Selector.py` in Vocareum, you can do so by typing the command `python Selector.py` into the terminal at the bottom. 

- You can type the command `python` into Vocareum's terminal to get an interactive shell that will immediately run individual lines of Python code you type (you can end this interactive shell with `ctrl+d`). This is a great way to quickly test how/if individual operations of Python work as you expect.

- You may not use sorting in any method, except for `kmin` and `kmax`.

- You do not have to use sorting in `kmin` and `kmax`, but doing so makes the solution more straightforward. If you choose to use sorting in these two methods, you must do so by calling the built-in `sorted()` function and you are allowed at most two calls to this function - at most one in `kmin` and at most one in `kmax`. Be sure not to use the `list.sort()` method, as this is only defined for the list class (and not other classes that implement the Sequence abstract base class).

- When Python's built-in `sorted()` function is called on a sequence (or iterable) that contains duplicate values, it keeps them in their original order (even when you call `sorted(seq, reverse=True)` to sort in descending order). However, this can lead to some interesting side effects when sorting based on a key value, as elements may not be compared in their entirety.

- For all methods where comparison is performed against an input parameter (range, ceiling, floor, search), you should assume that the input parameters are directly comparable with the value extracted by the key function from each sequence element. For example, say we called search on a list of books (with values for title, author, and pages) and the key parameter specifies that comparisons should be done on the basis of title. You should expect that the target parameter provided by the client is just the title, rather than an entire book object you would need to pass through the key function.

- Checking the key parameter passed in by the client is outside the scope of this assignment. In other words, if the client passes in something erroneous as a key (e.g., a non-callable object or a function that produces an error when applied on the data) you should allow the natural errors that may occur without intervention. This is fairly standard practice, as catching these exceptions in your code may actually make it more difficult to use, when compared to allowing the user to see the exceptions that get raised, as Python's built in error messages are typically helpful on their own.

## Acknowledgements
This assignment is based on a similar Java assignment developed by Dr. Dean Hendrix.
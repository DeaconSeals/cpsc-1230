
# Hands-On: Efficiency and Empirical Analysis

This activity focuses on empirically measuring a program's running time.
Before attempting this activity, you should complete the Efficiency note set
and the *Empirical Analysis* section of the Algorithm Analysis note set.

After completing this activity you should

- Be able to measure the running time of programs.
- Be able to describe factors that affect running time.
- Be able to to characterize a program's time complexity.


## Measuring running time

Python provides the [`time` module](https://docs.python.org/3/library/time.html) for measuring time and handling time-based data. For measuring Python code, the most commonly used function is [`time.time()`](https://docs.python.org/3/library/time.html#time.time), which returns a floating point number representing the number of seconds since January 1, 1970, 00:00:00 (UTC)---also known as [Unix time](https://en.wikipedia.org/wiki/Unix_time).

To measure how long function `foo` takes to run we could do the following:

```python
start = time.time()
foo()
elapsed_time = time.time() - start
```


## Improving performance: avoid unnecessary work

The crux of making code more efficient is avoiding unnecessary work. Sometimes
this can mean being more careful in how the code is written; for example,
making sure a search algorithm terminates as soon as the result of the search
is known.

The two contain functions below illustrate this idea.

```python
def contains_a(a, target):
'''A linear search that exits only after scanning the entire list.'''
   found = False
   for value in a:
      if value == target:
         found = True
   return found

def contains_b(a, target):
'''A linear search that exits as soon as the result of the search is known.'''
   for value in a:
      if value == target:
         return True
   return False
```

On average, we would expect `contains_b` to perform better than `contains_a` since
it exits the loop and returns `True` as soon as `target` is found. This is an
example of efficiency improvements we should always make, mainly because the
code is just ... *better*. That's a subjective judgment, but I think most of
us would agree that `contains_b` is more efficient *and* more appealing.

Note that the worst-case performance of both `contains_a` and `contains_b` is the
same - both will examine every element of the list before terminating. But on
"average-case" searches we should see a performance difference.


## Characterizing time complexity

More important than measuring running time *per se* is being able to
characterize an algorithm's *time complexity*. The time complexity of an
algorithm dictates how **scalable** the algorithm is; that is, whether or not
the algorithm's running time will be practical as the problem size increases.

A concrete way to think about scalability is to ask the question "*What
happens to running time if the problem becomes twice as large as it currently
is?*" Is our algorithm still useful if the problem size we expect suddenly
doubles? What if it doubles again? Characterizing the algorithm's time
complexity is the first step in understanding the algorithm's scalability.

One approach to characterizing time complexity is to empirically answer the
doubling questions above by timing the implemented algorithm on increasing
problem sizes. By making observations of how the running time is affected by
doubling the size of the input, we can predict what the algorithm's time
complexity is. (Strictly speaking, the notion of time makes sense for an
*implemented* algorithm - a program - but not for an *algorithm*. We could
perhaps speak in terms of the "work" or "computational steps" required by an
algorithm, but "time" only makes sense when referring to a running program.
Even so, the terms *time complexity* and *time* are used in the context of
algorithms and we are expected to implicitly understand the distinction.)

The time complexity of many algorithms can described by a polynomial function.
That is, the time complexity function *T(N)* is proportional to some
polynomial function *f(N) = N^k*. The function *f* is called the *order of
growth* of the algorithm's time complexity since the amount of work required
by the algorithm as the problem size increases grows in proportion to the
function *f*. For example, *f(N) = N^2* would characterize a *quadratic*
growth rate.

If we were to implement an algorithm with polynomial time complexity in a Java
method, we could empirically discover its *order of growth* by recording the
running time of the method as we systematically increase the problem size
(*N*) by a factor of two, as shown in the following table.

| **N**   | **T(N)**    | **Ratio**       |
| :---:   | :---:       | :---:           |
| N       | T(N)        |                 |
| 2N      | T(2N)       | T(2N) / T(N)    |
| 4N      | T(4N)       | T(4N) / T(2N)   |
| 8N      | T(8N)       | T(8N) / T(4N)   |
| ...     | ...         | ...             |
| 2^k x N | T(2^k x N)  | T(2^k x N) / T(2^(k-1) x N) |

Since we know that the time complexity *T(N)* is proportional to a polynomial
function and since we're doubling *N* on each step, the values in the
**Ratio** column will approach a constant value approximately equal to *2^k*.
Solving for *k* would then give us the degree of the polynomial that
characterizes this algorithm's time complexity. For example, the following
table suggests that the underlying algorithm being timed has time complexity
proportional to *N^2*.

| **N** |     **T(N)** (sec.) |    **Ratio**    |
|  ---: |     -------------:  |    ---------:   |
|   250 |              0.061  |                 |
|   500 |              0.042  |          1.35   |
|  1000 |              0.112  |          2.67   |
|  2000 |              0.340  |          3.04   |
|  4000 |              1.298  |          3.82   |
|  8000 |              5.334  |          4.11   |
| 16000 |             21.880  |          4.10   |
| 32000 |             85.763  |          3.92   |
| 64000 |            345.634  |          4.03   |

Of course not all algorithms have polynomial time complexity. Common orders of
growth that we will see in this course include *log N*, *N*, *N log N*, *N^2*,
*N^3*, *2^N*, and *N!*. For the purposes of this lab, however, we will
restrict ourselves to talking about algorithms with time complexity
proportional to a *polynomial*. (*f(N) = N^k* for *k* > 0)


## Submission

The submission page for this activity asks you to apply your understanding of empirical analysis of time complexity to a problem and then submit it for a grade.

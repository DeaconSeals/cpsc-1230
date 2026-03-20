# Hands-On: Sorting

This activity focuses on four common sorting algorithms and sample
implementations. After completing this activity you should

* Understand the selection sort algorithm.
* Understand the insertion sort algorithm.
* Understand the quicksort algorithm.
* Understand the merge sort algorithm.


## Watching sorts work

Sorting was the subject of one of the first attempts at software visualization
(see Ron Baecker's [Sorting Out Sorting](https://youtu.be/SJwEwA5gOkM) from
1981). The behavior of sorting algorithms lends itself well to a visual
depiction, so canned animations of sorting remain popular. Below are three
good examples.

- [`http://www.sorting-algorithms.com/`](http://www.sorting-algorithms.com/)
- [`https://visualgo.net/en/sorting?slide=1`](https://visualgo.net/en/sorting?slide=1)
- [`https://www.cs.usfca.edu/~galles/visualization/ComparisonSort.html`](https://www.cs.usfca.edu/~galles/visualization/ComparisonSort.html)


## Selection sort

*Selection sort* is a conceptually simple sorting algorithm, but it is not 
scalable, with *O(N^2)* time complexity in the best, average, and worst cases. 
Here's a [description from Wikipedia](https://en.wikipedia.org/wiki/Selection_sort):

> The algorithm divides the input list into two parts: the sublist of items already sorted, which is built up from left to right at the front (left) of the list, and the sublist of items remaining to be sorted that occupy the rest of the list. Initially, the sorted sublist is empty and the unsorted sublist is the entire input list. The algorithm proceeds by finding the smallest (or largest, depending on sorting order) element in the unsorted sublist, exchanging (swapping) it with the leftmost unsorted element (putting it in sorted order), and moving the sublist boundaries one element to the right.


## Insertion sort

*Insertion sort* is a conceptually simple sorting algorithm with time complexity 
that varies according to how the input is arranged initially. If the input is either 
in reverse order or random order, insertion sort has *O(N^2)* time complexity and 
is thus not scalable to large data sets. But if the input is sorted or - more 
importantly - *almost* sorted, then insertion sort has *O(N)* time complexity and is 
very useful on large inputs. Here's a 
[description from Wikipedia](https://en.wikipedia.org/wiki/Insertion_sort):

> Insertion sort iterates, consuming one input element each repetition, and growing a sorted output list. Each iteration, insertion sort removes one element from the input data, finds the location it belongs within the sorted list, and inserts it there. It repeats until no input elements remain.
>
> Sorting is typically done in-place, by iterating up the array, growing the sorted list behind it. At each array-position, it checks the value there against the largest value in the sorted list (which happens to be next to it, in the previous array-position checked). If larger, it leaves the element in place and moves to the next. If smaller, it finds the correct position within the sorted list, shifts all the larger values up to make a space, and inserts into that correct position.


## Quicksort

The *quicksort* algorithm isn't as conceptually simple as insertion sort or
selection sort, but it is far more efficient. Although it has a worst-case
time complexity that is *O(N^2)*, quicksort's average and best case time
complexity is *O(N log N)*. The worst-case can typically be avoided, so
quicksort is one of the most commonly used sorting algorithms, even for large
data sets. Here's a 
[description from Wikipedia](https://en.wikipedia.org/wiki/Quicksort).

> Quicksort is a divide and conquer algorithm. Quicksort first divides a large array into two smaller sub-arrays: the low elements and the high elements. Quicksort can then recursively sort the sub-arrays.
>
> The steps are:
>
> 1. Pick an element, called a pivot, from the array.
> 2. Partitioning: reorder the array so that all elements with values less than the pivot come before the pivot, while all elements with values greater than the pivot come after it (equal values can go either way). After this partitioning, the pivot is in its final position. This is called the partition operation.
> 3. Recursively apply the above steps to the sub-array of elements with smaller values and separately to the sub-array of elements with greater values.

### Partition

The actual work of rearranging elements of the array in quicksort is
accomplished by *partitioning* array elements around a *pivot* value. It's
important that you understand this process in detail. There are different
strategies for partitioning, and different strategies for selecting the pivot
value. For this course both strategies are simple and straightforward. Namely,
the first element of an array segment is selected as the pivot value.

- Note that shuffling the array before calling `qsort` doesn't guarantee a *good* pivot value, but is considered helpful. So, here are some important questions to think about.

   - What makes a *good* pivot value?
   - What makes a *bad* pivot value?
   - What would be the *best* pivot value for a given array?
   - If the shuffling doesn't guarantee good pivot values, what does it do?


## Merge sort

The *merge sort* algorithm isn't as conceptually simple as insertion sort or
selection sort, but it is far more efficient. Merge sort's time complexity is
*O(N log N)* in all cases, and it is therefore a very scalable algorithm. In
fact, merge sort is one of the most commonly used sorting algorithms, even for
large data sets. Here's a 
[description from Wikipedia](https://en.wikipedia.org/wiki/Merge_sort):

> Conceptually, a merge sort works as follows:
>
> 1. Divide the unsorted list into n sublists, each containing 1 element (a list of 1 element is considered sorted).
> 2. Repeatedly merge sublists to produce new sorted sublists until there is only 1 sublist remaining. This will be the sorted list.


### Merge

The actual work of rearranging elements of the array in merge sort is
accomplished by *merging* elements from two sorted halves of an array into
another array. It's important that you understand this process in detail. Note
that merging typically requires a lot of extra memory - a second array of the
same size as the original.


## Submission

The submission page for this activity asks you to apply your understanding of
these sorting algorithms to a problem and then submit it for a grade.


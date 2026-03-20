
# Efficiency, Sorting, Divide & Conquer, and Recursion


---

# Efficiency

We begin this module by examining the idea of **efficiency**. Efficiency seems
like it would be an important aspect of our solutions, but it is necessary to
first clearly define what we mean by the term and then decide how we can
define, measure, and ensure it in the software that we build.



### Introduction to Efficiency

For as long as people have been building machines and automating tasks, they
have wanted to find ways of making things faster. The same is true in
software, but as we will see in this video, we have to exercise caution and
know when efficiency actually matters and how best to achieve it.

>[*Video: Introduction to Efficiency*](https://auburn.hosted.panopto.com/Panopto/Pages/Viewer.aspx?id=7d7091cc-8817-4dea-931f-b4130123aed3)

### Linear Search: Avoiding Wasted Time and Effort

This video illustrates our working definition of efficiency in the context of
two different linear search methods. The difference between the two methods is
one of efficiency, but perhaps not the type of efficiency difference that
truly matters.

>[*Video: Linear Search*](https://auburn.hosted.panopto.com/Panopto/Pages/Viewer.aspx?id=27e84a59-4294-4f77-aab6-b4130123ae54)

### Binary Search: Improving the Worst Case

Making significant improvements in efficiency often involves taking a
fundamentally different approach to solving a problem. This video illustrates
this principle by developing binary search as a more efficient alternative to
linear search.

>[*Video: Binary Search*](https://auburn.hosted.panopto.com/Panopto/Pages/Viewer.aspx?id=8ed5d7e8-449d-4bbc-8632-b4130123ae7f)


### Time Complexity: Characterizing Efficiency

Now that we have a good understanding of efficiency and have seen an approach
to achieving it, this video will lay the groundwork for describing and
characterizing the efficiency of the programs that we create.

>[*Video: Time Complexity*](https://auburn.hosted.panopto.com/Panopto/Pages/Viewer.aspx?id=4a21bc75-4917-420b-a147-b4130123aea8)



---

# Algorithm Analysis

**Algorithm analysis** is a formal approach to measuring and describing the
time complexity of our algorithms. An understanding of algorithm analysis will
allow us to predict the performance of algorithms and programs, compare
competing solutions to the same problem, publish performance guarantees for
our software, and gain insight into techniques for designing efficient
algorithms.


### Introduction to Algorithm Analysis

This video sets the stage for the exploration of algorithm analysis by
discussing its importance and providing a real-life illustration of its
relevance.

>[*Video: Algorithm Analysis Introduction*](https://auburn.hosted.panopto.com/Panopto/Pages/Viewer.aspx?id=38608ec2-e6b3-41e0-9b05-b4130123b4b5)


### Empirical Analysis

One approach to algorithm analysis is an empirical one -- that is, we can run
software under different conditions, collect running time data, and then draw
conclusions from our analysis of that data. This video discusses one
particular type of empirical analysis that is often straightforward to perform
and yields useful information.

>[*Video: Empirical Analysis*](https://auburn.hosted.panopto.com/Panopto/Pages/Viewer.aspx?id=cbb77fb0-986d-4753-95f4-b4130123bdc4)


### Mathematical Analysis

A more general approach to algorithm analysis is one that is based on counting
the operations performed by an algorithm and using the resulting expression to
describe the algorithm’s underlying time complexity. This video introduces a
simplified mathematical analysis for algorithms.

>[*Video: Mathematical Analysis*](https://auburn.hosted.panopto.com/Panopto/Pages/Viewer.aspx?id=d36ac95e-4b08-43a0-ae3d-b4130123c895)


### Analysis of Binary Search

This video illustrates how we can apply the mathematical approach to algorithm
analysis to describe the time complexity of binary search.

>[*Video: Analysis of Binary Search*](https://auburn.hosted.panopto.com/Panopto/Pages/Viewer.aspx?id=bcab1199-d73a-434b-9ec7-b4130123ca9a)


### Growth Rate and Asymptotic Analysis

The approaches we have taken to algorithm analysis have allowed us to describe
the time complexity of an algorithm. The most important aspect of the time
complexity function is its **growth rate**; that is, how rapidly the amount of
work increases as a function of the problem size. This video discusses the
idea of growth rate and introduces big-O notation as a standard way of
describing time complexity and growth rates.

>[*Video: Asymptotic Analysis*](https://auburn.hosted.panopto.com/Panopto/Pages/Viewer.aspx?id=8859b6f4-97f1-48c4-8d48-b4130123d06c)


### Calculating Big-O

This video introduces a common technique for quickly describing the time
complexity of source code in terms of big-O. This technique abstracts and
simplifies the mathematical/counting approach we used earlier.

>[*Video: Big-O Analysis*](https://auburn.hosted.panopto.com/Panopto/Pages/Viewer.aspx?id=1239ec3a-daa2-4274-9c04-b4130123d170)



---

# Sorting: Part 1

Sorting is a simple problem that plays a surprisingly important role in modern
computing. We will discuss and analyze four sorting algorithms, and along the
way we will discover a new approach to solving problems (a new solution
pattern) as well as a new approach to expressing our solutions.


### Introduction to Sorting

Sorting has a long history in computing and still plays an important role.
This video will present a context for sorting that directly relates to our
discussion of efficiency and scalability, and will then set the stage for
close examination of different sorting algorithms.

>[*Video: Sorting Introduction*](https://auburn.hosted.panopto.com/Panopto/Pages/Viewer.aspx?id=a15aff3a-d257-40c5-b973-b4130123d711)


### Selection Sort

This video presents and analyzes one of the most intuitive and easy to
understand sorting algorithms: selection sort. We will appreciate selection
sort for its simplicity, but we will quickly come to understand why it isn’t
usable in practical applications.

>[*Video: Selection Sort*](https://auburn.hosted.panopto.com/Panopto/Pages/Viewer.aspx?id=be7169b8-4609-4352-9409-b4130123db1d)


### Insertion Sort

Insertion sort is another intuitive and easy to understand sorting algorithm.
Like selection sort, it is not scalable enough to use widely in practice, but
it has an interesting special case that makes it very efficient in certain
situations.

>[*Video: Insertion Sort*](https://auburn.hosted.panopto.com/Panopto/Pages/Viewer.aspx?id=f066b0b8-c590-494b-8535-b4130123e5ac)


### Sorting More Efficiently

Selection sort and insertion sort are simple but not scalable. This video asks
us to consider how we might sort more efficiently. One answer to this question
will lead us to discover a new approach to solving problems.

>[*Video: Sorting More Efficiently*](https://auburn.hosted.panopto.com/Panopto/Pages/Viewer.aspx?id=4ec4c36a-860d-42b2-a0ea-b4130123f073)



---

# Recursion

Recursion is different approach to expressing the solutions to problems. Based
on the idea of self-reference, recursion is a powerful alternative to
iteration that is important to master and understand.


### Introduction to Recursion

Recursion can sometimes be difficult to understand, especially the first time
you encounter it. This video introduces recursive computation in the context
of a simple, easy to understand, real-life example.

>[*Video: Recursion Introduction*](https://auburn.hosted.panopto.com/Panopto/Pages/Viewer.aspx?id=fc2a59a8-a93a-47fd-9b70-b41301247bac)


### Factorial

This video continues to develop a recursive approach to computation in the
context of the factorial function from mathematics.

>[*Video: Factorial*](https://auburn.hosted.panopto.com/Panopto/Pages/Viewer.aspx?id=da22d860-d0b4-40c0-ad7f-b4130124a64e)


### Tower of Hanoi

Most often thought of as a brain teaser or puzzle, the Tower of Hanoi problem
offers another example of a problem that is naturally solved recursively.

>[*Video: Tower of Hanoi*](https://auburn.hosted.panopto.com/Panopto/Pages/Viewer.aspx?id=51375090-eae0-4484-86cd-b4130124bb34)


### Array Search

This video revisits two familiar algorithm - linear search and binary search -
but this time in the context of recursion. Seeing how to express these
algorithms recursively should help solidify the idea of recursion and help you
become more comfortable expressing solutions in this way.

>[*Video: Recursive Search*](https://auburn.hosted.panopto.com/Panopto/Pages/Viewer.aspx?id=d5a28d9b-4097-48d4-9ddf-b413012504b2)



---

# Sorting: Part 2


### Divide-and-Conquer

Divide and conquer is a problem-solving strategy that can lead to efficient
and elegant solutions to certain problems. This video introduces the divide
and conquer strategy and illustrates its use to solve a familiar problem.

>[*Video: Divide-and-Conquer*](https://auburn.hosted.panopto.com/Panopto/Pages/Viewer.aspx?id=b7356741-7ac2-464a-9216-b4130123f424)


### Merge Sort

This video describes merge sort - a very efficient and widely-used sorting
algorithm that is based on the divide and conquer strategy.

>[*Video: Merge Sort*](https://auburn.hosted.panopto.com/Panopto/Pages/Viewer.aspx?id=7d560d62-b541-417b-9512-b413012404b5)


### Quicksort

This video describes quicksort, one of the most efficient and widely-used
sorting algorithms. Like merge sort, quicksort is based on the divide and
conquer strategy but applies it in a different way.

>[*Video: Quicksort*](https://auburn.hosted.panopto.com/Panopto/Pages/Viewer.aspx?id=da1ad537-f1aa-4227-944a-b413012423d6)


### Sorts in the JCF / Stability

This video examines the sorting algorithms that are implemented in methods
available in the Python. The concept of sort stability is also introduced and
its practical importance is illustrated with an example.

>[*Video: Stability*](https://auburn.hosted.panopto.com/Panopto/Pages/Viewer.aspx?id=0fe8c8fb-2b9f-403c-b06e-b413012431b8)

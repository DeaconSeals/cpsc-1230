
# Search Trees and Binary Heaps


---

# Search Trees

### Trees

All the ideas presented in this module are based on the concept of trees: data
structures that organize elements into a hierarchy. We begin by learning about
the basic idea of trees, and then refine and extend those ideas into various
specialized forms.

> [*Video: Tree overview*](https://auburn.hosted.panopto.com/Panopto/Pages/Viewer.aspx?id=a10f1979-31df-496c-a882-b42801527ae1)

### Binary Trees

Binary trees are those trees where the number of children per node is limited
to at most two. Most of the trees that we will discuss in this module are
binary.

> [*Video: Binary trees*](https://auburn.hosted.panopto.com/Panopto/Pages/Viewer.aspx?id=e742a6ad-9d76-4a0f-94f4-b42801529427)

### Binary Search Trees

This lecture material presents a type of binary tree in which we impose a
total order on all the nodes - a binary search tree.

> [*Video: Introduction to BSTs*](https://auburn.hosted.panopto.com/Panopto/Pages/Viewer.aspx?id=073d9c2f-133d-4ca2-a383-b4280152aa6c)

> [*Video: Searching for values in BSTs*](https://auburn.hosted.panopto.com/Panopto/Pages/Viewer.aspx?id=5a3768ec-985c-43fb-8c77-b4280152c42b)

> [*Video: Adding values to BSTs*](https://auburn.hosted.panopto.com/Panopto/Pages/Viewer.aspx?id=ba5f857f-a125-41cf-a429-b4280152db11)

> [*Video: Removing values from BSTs*](https://auburn.hosted.panopto.com/Panopto/Pages/Viewer.aspx?id=2a14abbd-c031-473a-93db-b42801522405)

> [*Video: Balance in BSTs*](https://auburn.hosted.panopto.com/Panopto/Pages/Viewer.aspx?id=90bda1e3-1166-4a4f-a0c5-b42801522460)


### AVL Trees

For a binary search tree to offer good performance it must be balanced. These
lecture materials present one type of balanced binary search tree called an
AVL tree.

> [*Video: Introduction to AVL trees*](https://auburn.hosted.panopto.com/Panopto/Pages/Viewer.aspx?id=d23c1bb7-41ea-4d5d-9213-b428015223df)

> [*Video: Rebalancing in AVL trees*](https://auburn.hosted.panopto.com/Panopto/Pages/Viewer.aspx?id=5871f697-44e2-4fde-890e-b42801522431)

> [*Video: Adding values to AVL trees*](https://auburn.hosted.panopto.com/Panopto/Pages/Viewer.aspx?id=a79b43f1-7a55-4f70-80a2-b428015227fc)

> [*Video: Removing values from AVL trees*](https://auburn.hosted.panopto.com/Panopto/Pages/Viewer.aspx?id=ce03b664-c9bb-4ebf-a897-b42801522a42)

> [*Video: AVL tree summary*](https://auburn.hosted.panopto.com/Panopto/Pages/Viewer.aspx?id=f8df18d1-a7da-4480-b1d2-b42801522ef4)


### Red-Black Trees

These lecture materials present an alternative approach to balancing binary
search trees - Red-Black trees. While not particularly relevant to Python,
Red-Black trees are the data structures used by the Java Collections Framework
to provide a balanced search tree (`java.util.TreeMap`, `java.util.TreeSet`).

> [*Video: Introduction to red-black trees*](https://auburn.hosted.panopto.com/Panopto/Pages/Viewer.aspx?id=239229eb-5e77-4799-a554-b42801522fa0)

> [*Video: Adding values to red-black trees*](https://auburn.hosted.panopto.com/Panopto/Pages/Viewer.aspx?id=03512b87-e9ba-4809-b0c2-b42801523154)

> [*Video: Red-black tree - adding example*](https://auburn.hosted.panopto.com/Panopto/Pages/Viewer.aspx?id=64920487-c675-4a73-9e84-b4280152321d)

> [*Video: Red-black tree summary*](https://auburn.hosted.panopto.com/Panopto/Pages/Viewer.aspx?id=0196d4b6-ac99-4ae5-9f53-b4280152327f)


### Multiway Search Trees

These lecture materials present a non-binary version of a balanced search
tree. We call these "multiway search trees" since each node can have more than
two children.

> [*Video: Multiway search trees*](https://auburn.hosted.panopto.com/Panopto/Pages/Viewer.aspx?id=5b8993f9-706c-4a29-9ee0-b42801523573)


---

# Binary Heaps

Binary heaps are tree structures that are used to support efficient access to
the maximum or minimum element of a collection. Rather than imposing a total
order on the nodes, a binary heap imposes a partial order. 

### Introduction

These lecture materials provide an overview of binary heaps, how they are
organized, and how they are implemented.

> [*Video: Binary Heap Introduction*](https://auburn.hosted.panopto.com/Panopto/Pages/Viewer.aspx?id=1297ddcb-35c7-42a0-8182-b42801523741)

### Adding and removing values

These lecture materials discuss how to add and remove values in a binary heap.

> [*Video: Adding and removing*](https://auburn.hosted.panopto.com/Panopto/Pages/Viewer.aspx?id=b9be8fa5-cd6a-4e4f-97bd-b42801523772)

### Application: Sorting

A clever application of binary heaps is found in sorting. Heapsort is an
optimal comparison sort that uses the idea of a max heap to achieve O(log N)
time complexity. Note: this lecture contains pseudocode that more closely
resembles C and Java than Python. This isn't meant to be syntactically correct
code in any particular language and you should still be able to follow the
algorithm.

> [*Video: Heapsort*](https://auburn.hosted.panopto.com/Panopto/Pages/Viewer.aspx?id=5ffba75e-2ec2-41f8-a20d-b42801524be6)

### Application: Huffman's Algorithm

Huffman's algorithm uses a min heap to generate a variable length encoding for
the characters found in a text file. This is the basis of one approach to text
compression. Note: this lecture contains pseudocode that more closely
resembles C and Java than Python. This isn't meant to be syntactically correct
code in any particular language and you should still be able to follow the
algorithm.

> [*Video: Huffman's Algorithm*](https://auburn.hosted.panopto.com/Panopto/Pages/Viewer.aspx?id=2f921f89-8883-4a25-b0dc-b428015264f0)



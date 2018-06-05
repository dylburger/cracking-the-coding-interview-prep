[Link to problem statement](https://www.hackerrank.com/challenges/ctci-find-the-running-median/problem)

We use a heap to keep a collection of numbers. Why? We want to efficiently sort a list of numbers. [This article](https://medium.com/basecs/heapify-all-the-things-with-heap-sort-55ee1c93af82) summarizes this:

> It turns out that binary heaps are often used for no other purpose than efficient sorting. Many programs will rely on heap sort since it happens to be one of the most efficient ways to sort an array.

We need an efficient way to sort our heap so that we can find the median.

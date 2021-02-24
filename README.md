# Sorting Algorithm Visualization program

A Simple program (still work in progress) to show how different sorting algorithms work.
The main idea of the program is to write code that consists of different sorting algorithms
to better understand how they work from code side. Plus on top of that to better understand 
the importance of Big O notation for algorithms.

[Big_O_Notation](https://en.wikipedia.org/wiki/Big_O_notation)
[Sorting_algorithms](https://en.wikipedia.org/wiki/Sorting_algorithm)


## Sorting Algorithms included:

- Bubble Sort
- Insertion Sort
- Merge Sort
- Quick Sort

### Code in short

1. Asks user for a numbers to generate the shuffled list
2. Then asks user to pickthe sorting algorithm to use for sorting operation
3. Makes the list of numbers and shuffles them randomly
   1. Note that the list consists of unique and whole numbers only
4. Runs the algorithm with the shuffled list of numbers and sorts them
5. (for now) shows a graph with two plots
   1. Shuffled list of numbers before sorting
   2. Sorted list of numbers


## To-do

- [ ] Add Timsort Algo
- [ ] Fix the mergeSort error
- [ ] Add Selection Sort Algo
- [ ] Animations of the sorting process (matplotlib.animation)
- [ ] Add timing of each algorithm
  - [ ] Compare algorithm runtime
- [ ] Fix the 
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

### Sorting Algorithm runtime:
#### 

| Sorting Algo / Samples | 10 |	100   |  1000  |  10000 |
| --- | --- | --- | --- | --- |
| Bubble |  0.0028108999999858   |	0.188403899999912 |	20.895675100000062   |	22.05723540000008 |
|  Insertion  |	0.0016550000000279   |	0.1850954999999885 |	19.09637620000012 |	21.24320380000017 |
|  Merge |	0.0005453999999645   |	0.0082380999999713   |	0.1313644999997905   |	0.3478566999999657 |
|  Quick |	0.00064210000005  |	0.0061302000001433   |	0.1041278000000147   |	0.0704792999999881   |


## To-do

- [ ] Add Timsort Algo
- [x] Fix the mergeSort error
- [ ] Add Selection Sort Algo
- [ ] Animations of the sorting process (matplotlib.animation)
- [x] Add timing of each algorithm
  - [ ] Compare algorithm runtime
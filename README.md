# Sorting Algorithm Visualization program

A Simple program (still work in progress) to show how different sorting algorithms work.
The main idea of the program is to write code that consists of different sorting algorithms
to better understand how they work from code side. Plus on top of that to better understand 
the importance of Big O notation for algorithms.

Reading:

1. [Big_O_Notation](https://en.wikipedia.org/wiki/Big_O_notation)
2. [Sorting_algorithms](https://en.wikipedia.org/wiki/Sorting_algorithm)


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

#### Tables presented below compare the compute time of each algorithm

##### Time measuring process:

   1. Each algorithm is timed on 4 different lengths of unsorted lists
      1. N = [10, 100, 1000, 10000]
   2. Every algo is given 5 tries to sort the mixed lists, each itteration time is noted
   3. To time duration of computing for each time timer() is used.

   NOTE: Take in consideration that each list before sorting is shuffled at random.

#### Average time( in seconds ) of 5 attempts for each length of lists:

| Sorting Algo / Samples | 10 |	100   |  1000  |  10000 |
| --- | --- | --- | --- | --- |
|  Bubble |  0.00281   |	0.18840 |	20.89567   |	22.057235 |
|  Insertion  |	0.00165   |	0.18509 |	19.09637 |	21.24320 |
|  Merge |	0.00054   |	0.00823   |	0.13136   |	0.34785 |
|  Quick |	0.00064  |	0.00613   |	0.10412   |	0.07047   |

#### Fastest time (in seconds) for each length of mixed list:

| Sorting Algo / Samples | 10 |	100   |  1000  |  10000 |
| :---: | :---: | :---: | :---: | :---: |
|  Bubble   |  0.000028759999941030402 |  0.00240310000008314  |  0.17228555999995473  |  20.657596600000034   |
Insertion	0.000015419999954247032	0.001843959999951	0.16192941999993307	19.96031856000004
Merge	0.00003758000002562767	0.00070378000009438	0.0092524999999568	0.19752495999996428
Quick	0.000056459999996150145e-05	0.0006364000000302599	0.00736017999997782	0.07143655999998368



## To-do

- [ ] Add Timsort Algo
- [x] Fix the mergeSort error
- [ ] Add Selection Sort Algo
- [ ] Animations of the sorting process (matplotlib.animation)
- [x] Add timing of each algorithm
  - [ ] Compare algorithm runtime
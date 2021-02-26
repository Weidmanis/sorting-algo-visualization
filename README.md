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

## Code in short

1. Asks user for a numbers to generate the shuffled list
2. Then asks user to pickthe sorting algorithm to use for sorting operation
3. Makes the list of numbers and shuffles them randomly
   1. Note that the list consists of unique and whole numbers only
4. Runs the algorithm with the shuffled list of numbers and sorts them
5. (for now) shows a graph with two plots
   1. Shuffled list of numbers before sorting
   2. Sorted list of numbers


## Sorting Algorithm runtime:

### Tables presented below compare the compute time of each algorithm

#### Time measuring process:

   1. Each algorithm is timed on 4 different lengths of unsorted lists
      1. N = [10, 100, 1000, 10000]
   2. Every algo is given 5 tries to sort the mixed lists, each itteration time is noted
   3. To time duration of computing for each time timer() is used.

   NOTE: Take in consideration that each list before sorting is shuffled at random.


#### Average time( in seconds ) of 5 attempts for each length of lists:

| Sorting Algo / Samples | 10 |	100   |  1000  |  10000 |
| :---: | :---: | :---: | :---: | :---: |
| Bubble |	2.88e-05 |	0.0024031   |	0.1722856   |	20.6575966  |
|  Insertion | 1.54e-05 |	0.001844 |	0.1619294   |	19.9603186  |
|  Merge |  3.76e-05 |  0.0007038   |	0.0092525   |	0.197525 |
|  Quick |	5.65e-05 |	0.0006364   |	0.0073602   |	0.0714366   |


#### Fastest time (in seconds) for each length of mixed list:

| Sorting Algo / Samples | 10 |	100   |  1000  |  10000 |
| :---: | :---: | :---: | :---: | :---: |
|  Bubble   |  2.25e-05 |	0.0018519   |	0.166483 |	17.7672266  |
| Insertion |	1.08e-05 |	0.0014479   |	0.143619 |	19.0963762  |
|  Merge |	2.84e-05 |	0.0005267   |	0.007969 |	0.1294501   |
|  Quick |	4.97e-05 |	0.0005902   |	0.0041144   |	0.0577716   |


#### Slowest time for each algo and length of mixed list:

| Sorting Algo / Samples | 10 |	100   |  1000  |  10000 |
| :---: | :---: | :---: | :---: | :---: |
|  Bubble   |	3.14e-05 |	0.0028201   |	0.1884039   |	22.0572354  |
|  Insertion   |	2.37e-05 |	0.0026792   |	0.1850955   |	21.2432038  |
|  Merge |	6.59e-05 |	0.0011274   |	0.0105777   |	0.3478567   |
|  Quick |	6.67e-05 |	0.0006758   |	0.0100411   |	0.1041278   |

Its clearly visable that as the list length increases Bubble and Insertion sort algorithms are starting to slow down. Therefore Bubblesort is ok to use for short lists/datasets, but when it comes for large amounts of data that needs sorting Merge or Quick sort can do it much quicker


## To-do

- [ ] Add Timsort Algo
- [x] Fix the mergeSort error
- [ ] Add Selection Sort Algo
- [ ] v2 of sorting-...py with yield instead of return
- [ ] Animations of the sorting process (matplotlib.animation)
- [x] Add timing of each algorithm
  - [x] Compare algorithm runtime
  - [ ] Time with 100000, 1000000 samples in a list (might take some time)
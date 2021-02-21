import random
import timeit
import matplotlib.pyplot as plt
import matplotlib.animation as animation

import sys
sys.setrecursionlimit(10000)


#Bubble sort
def bubble_sort(shuffled):
    """ Bubble sort algorithm """

    # Make a copy of unsorted list
    bubble_s = shuffled.copy()
    N = len(shuffled)

    # If there is only one numb in the list then sorting is done
    if len(bubble_s) == 1:
        return bubble_s

    # Loop through the unsorted list
    for i in range(N):
        already_sorted = True

        for j in range(N - i - 1):
            if bubble_s[j] > bubble_s[j+1]:
                bubble_s[j], bubble_s[j+1] = bubble_s[j+1], bubble_s[j]

                already_sorted = False

        if already_sorted:
            break

    return bubble_s

def insertion_sort(shuffled):
    """ Insertion Sort algo """

    insert_s = shuffled.copy()
    N = len(shuffled)

    for i in range(1, len(insert_s)):
        j = i

        while j > 0 and insert_s[j] < insert_s[j-1]:
            insert_s[j], insert_s[j-1] = insert_s[j-1], insert_s[j]
            j -= 1
    
    return insert_s

def merge(left, right):
    """ Merge_sort helper fcn, that does the merging """

    # if left array empty return right array
    if len(left) == 0:
        return left

    # if right array empty return left array
    if len(right) == 0:
        return left

    # set merge_s (the sorted list) to be empty
    merge_s = []
    indx_left = indx_right = 0

    while len(merge_s) < len(left) + len(right):
        if left[indx_left] <= right[indx_right]:
            merge_s.append(left[indx_left])
            indx_left += 1
        else:
            merge_s.append(right[indx_right])
            indx_right += 1

        if indx_right == len(right):
            merge_s += left[indx_left:]
            break
        
        if indx_left == len(left):
            merge_s += right[indx_right]
            break

    return merge_s

def merge_sort(shuffled):
    """ Fcn to split the input list in left,right arrays """

    # Check if input array is longer than 2 instances
    # otherwise its already sorted
    if len(shuffled) < 1:
        return shuffled

    # Find the midpoint for the array using floor division
    midp = len(shuffled) // 2

    # left = merge_sort(shuffled[:midp])
    # right = merge_sort(shuffled[midp:])

    return merge(
        left = merge_sort(shuffled[:midp]), 
        right = merge_sort(shuffled[midp:]))

def quick_sort(shuffled):
    pass

def tim_sort(shuffled):
    pass

def selection_sort(shuffled):
    pass


# Ask User to enter a number to determine range
N = int(input("Enter a number of integers to sort: "))

# pick_algo = input("Pick which sorting algo you would like to see:\n\n\
#     - for Bubble Sort algo type 'b'\n\
#     - for Insertion Sort algo type 'i'\n\
#     - for Merge Sort algo type 'm'\n\
#     - for Quick Sort algo type 'q'\n\
#     - for Selection Sort algo type 's'\n\
#     - for Timsort algo type 't'\n\
#     Your choice?: ")

# Generate numbers
# x + 1, cause range(N) == 0,1,2,...,N-1
numbers = [x + 1 for x in range(N)]

# Make a copy of numbers list and shuffle it
shuffled = numbers.copy()
random.shuffle(shuffled)


# IF/ELIF/ELSE loop to pick the algorithm
# if pick_algo == 'b':
#     bubble_sort(shuffled)
# elif pick_algo == 'i':
#     insertion_sort(shuffled)
# elif pick_algo == 'm':
#     merge_sort=(shuffled, N)
# elif pick_algo == 'q':
#     pass
# elif pick_algo == 's':
#     pass
# elif pick_algo == 't':
#     pass
# else:
#     print("Invalid algo was picked")

import pandas as pd
import numpy as np
from timeit import default_timer as timer
import random

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
        return right

    # if right array empty return left array
    if len(right) == 0:
        return left

    # set merge_s (the sorted list) to be empty
    merge_s = []
    index_left = index_right = 0

    while len(merge_s) < len(left) + len(right):

        if left[index_left] <= right[index_right]:
            merge_s.append(left[index_left])
            index_left += 1
        else:
            merge_s.append(right[index_right])
            index_right += 1

        if index_right == len(right):
            merge_s += left[index_left:]
            break
        
        if index_left == len(left):
            merge_s += right[index_right:]
            break

    return merge_s

def merge_sort(shuffled):
    """ Fcn to split the input list in left, right arrays """

    # Check if input array is longer than 2 instances
    # otherwise its already sorted
    if len(shuffled) < 2:
        return shuffled

    # Find the midpoint for the array using floor division
    midpoint = len(shuffled) // 2
    
    return merge(
        left=merge_sort(shuffled[:midpoint]),
        right=merge_sort(shuffled[midpoint:]))

def quick_sort(shuffled):
    """ Quick sort algorithm """

    # Check if the shuffled list isn't shorter than 2 int
    if len(shuffled) < 2:
        return shuffled

    # Create empty low, same, high lists
    low, same, high = [], [], []

    # Select the pivot element randomly
    pivot = shuffled[random.randint(0, len(shuffled) - 1)]

    # loop through the shuffled
    for item in shuffled:
        if item < pivot:
            low.append(item)
        elif item == pivot:
            same.append(item)
        elif item > pivot:
            high.append(item)
        
    # return the finished list
    return quick_sort(low) + same + quick_sort(high)


algos = ['Bubble', 'Insertion', 'Merge', 'Quick']
fcns = [bubble_sort, insertion_sort, merge_sort, quick_sort]

time = []
Ns = [1000]
bubble, insert, merg, quick = [],[],[],[]
res = []

for i in Ns:
    
    numbers = [x+1 for x in range(i)]
    mixed = numbers.copy()

    for function in fcns:
        for i in range(1,2):

            random.shuffle(mixed)

            start = timer()
            function(mixed)
            time = timer() - start
            res.append(time)

print(res)

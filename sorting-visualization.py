# https://github.com/nrsyed/sorts/blob/master/python/sorts.py
# https://realpython.com/sorting-algorithms-python/


import random
import timeit
import matplotlib.pyplot as plt
import matplotlib.animation as animation

#Bubble sort
def bubble_sort(shuffled, N):
    """ Bubble sort algorithm """

    # Make a copy of unsorted list
    bubble_s = shuffled.copy()

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

def insertion_sort(shuffled, N):
    """ Insertion Sort algo """

    insert_s = shuffled.copy()

    for i in range(1, len(insert_s)):
        j = i

        while j > 0 and insert_s[j] < insert_s[j-1]:
            insert_s[j], insert_s[j-1] = insert_s[j-1], insert_s[j]
            j -= 1
    
    return insert_s

def merge_sort(shuffled, N):
    pass



# Ask User to enter a number to determine range
N = int(input("Enter a number of integers to sort: "))

pick_algo = input("Pick which sorting algo you would like to see:\n\n\
    - for Bubble Sort algo type 'b'\n\
    - for Insertion Sort algo type 'i'\n\
    - for Merge Sort algo type 'm'\n\
    - for Quick Sort algo type 'q'\n\
    - for Selection Sort algo type 's'\n\
    Your choice?: ")

# Generate numbers
# x + 1, cause range(N) == 0,1,2,...,N-1
numbers = [x + 1 for x in range(N)]

# Make a copy of numbers list and shuffle it
shuffled = numbers.copy()
random.shuffle(shuffled)



# IF/ELIF/ELSE loop to pick the algorithm



# bubble_s = bubble_sort(shuffled,N)
insert_s = insertion_sort(shuffled,N)
fig = plt.figure(figsize=(10,6))

# plt.bar(bubble_s,height = bubble_s,width = 4)
plt.bar(insert_s,height = insert_s, width =4)
plt.show()

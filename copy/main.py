# Analysis of Algorithms - CSCI 323
# Assignment Number (Assignment 1)
# Mahfuz Uddin
# If applicable, any students with which you collaborated (allowed, but must be acknowledged)
# If applicable, any websites/texts from which you got code (allowed, but must be acknowledged)

import random
import time
import timeit
import prettytable
from prettytable import PrettyTable

Integer count=0;

def make_dum_data(n):
    dumb_data = []
    for x in range(n):
        dumb_data.append(random.randint(0, n * 1000))
    return dumb_data


def insertion_sort(low, n, array):
    for i in range(low + 1, n + 1):
        val = array[i]
        j = i
        while j > low and array[j - 1] > val:
            array[j] = array[j - 1]
            j -= 1
        array[j] = val


def partition_with_start(start, end, array):
    # Initializing pivot's index to start
    pivot_index = start
    pivot = array[pivot_index]

    # This loop runs till start pointer crosses
    # end pointer, and when it does we swap the
    # pivot with element on end pointer
    while start < end:

        # Increment the start pointer till it finds an
        # element greater than pivot
        while start < len(array) and array[start] <= pivot:
            start += 1

        # Decrement the end pointer till it finds an
        # element less than pivot
        while array[end] > pivot:
            end -= 1

        # If start and end have not crossed each other,
        # swap the numbers on start and end
        if start < end:
            array[start], array[end] = array[end], array[start]

    # Swap pivot element with element on end pointer.
    # This puts pivot on its correct sorted place.
    array[end], array[pivot_index] = array[pivot_index], array[end]

    # Returning end pointer to divide the array into 2
    return end


def partition_with_middle(start, end, array):
    # Initializing pivot's index to start
    pivot_index = int((start + end) / 2)
    pivot = array[pivot_index]

    # This loop runs till start pointer crosses
    # end pointer, and when it does we swap the
    # pivot with element on end pointer
    while start <= end:

        # Increment the start pointer till it finds an
        # element greater than pivot
        while start < len(array) and array[start] < pivot:
            start += 1

        # Decrement the end pointer till it finds an
        # element less than pivot
        while array[end] > pivot:
            end -= 1

        # If start and end have not crossed each other,
        # swap the numbers on start and end
        if start <= end:
            array[start], array[end] = array[end], array[start]
            start += 1
            end -= 1

    # Returning end pointer to divide the array into 2

    return start


def partition_with_end(start, end, array):
    # Initializing pivot's index to start
    pivot_index = end
    pivot = array[pivot_index]

    # This loop runs till start pointer crosses
    # end pointer, and when it does we swap the
    # pivot with element on end pointer
    while start <= end:

        # Increment the start pointer till it finds an
        # element greater than pivot
        while end >= start and array[end] >= pivot:
            end -= 1;

        # Decrement the end pointer till it finds an
        # element less than pivot
        while array[start] < pivot:
            start += 1;

        # If start and end have not crossed each other,
        # swap the numbers on start and end
        if start <= end:
            array[end], array[start] = array[start], array[end]

    # Swap pivot element with element on end pointer.
    # This puts pivot on its correct sorted place.
    array[start], array[pivot_index] = array[pivot_index], array[start]

    # Returning end pointer to divide the array into 2
    return start


def partition_with_random(start, stop, array):
    pivot = start  # pivot

    # a variable to memorize where the
    i = start + 1

    # partition in the array starts from.
    for j in range(start + 1, stop + 1):

        # if the current element is smaller
        # or equal to pivot, shift it to the
        # left side of the partition.
        if array[j] <= array[pivot]:
            array[i], array[j] = array[j], array[i]
            i = i + 1
    array[pivot], array[i - 1] = array[i - 1], array[pivot]
    pivot = i - 1
    return pivot


def partitionrand(start, end, array):
    # Generating a random number between the
    # starting index of the array and the
    # ending index of the array.
    randpivot = random.randrange(start, end)

    # Swapping the starting element of
    # the array and the pivot
    array[start], array[randpivot] = array[randpivot], array[start]
    return partition_with_random(start, end, array)


# The main function that implements QuickSort
def quick_sort_middle(start, end, array):
    if start < end:
        # p is partitioning index, array[p]
        # is at right place
        p = partition_with_middle(start, end, array)

        # Sort elements before partition
        # and after partition
        quick_sort_middle(start, p - 1, array)
        quick_sort_middle(p + 1, end, array)


def quick_sort_start(start, end, array):
    if start < end:
        # p is partitioning index, array[p]
        # is at right place
        p = partition_with_start(start, end, array)

        # Sort elements before partition
        # and after partition
        quick_sort_start(start, p - 1, array)
        quick_sort_start(p + 1, end, array)


def quick_sort_end(start, end, array):
    if start < end:
        # p is partitioning index, array[p]
        # is at right place
        p = partition_with_end(start, end, array)

        # Sort elements before partition
        # and after partition
        quick_sort_end(start, p - 1, array)
        quick_sort_end(p + 1, end, array)


def quick_sort_random(start, end, array):
    if start < end:
        # pivotindex is the index where
        # the pivot lies in the array
        pivotindex = partitionrand(start, end, array)

        # At this stage the array is
        # partially sorted around the pivot.
        # Separately sorting the
        # left half of the array and the
        # right half of the array.
        quick_sort_random(start, pivotindex - 1, array)
        quick_sort_random(pivotindex + 1, end, array)


def quick_sort_hybrid(low, high, array):
    while low < high:

        # If the size of the array is less
        # than threshold apply insertion sort
        # and stop recursion
        if high - low + 1 < 10:
            insertion_sort(low, high, array)
            break

        else:
            pivot = partition_with_end(low, high, array)

            # Optimised quicksort which works on
            # the smaller arrays first

            # If the left side of the pivot
            # is less than right, sort left part
            # and move to the right part of the array
            if pivot - low < high - pivot:
                quick_sort_hybrid(low, pivot - 1, array)
                low = pivot + 1
            else:
                # If the right side of pivot is less
                # than left, sort right side and
                # move to the left side
                quick_sort_hybrid(pivot + 1, high, array)
                high = pivot - 1


timedata_for_middle = []
timedata_for_start = []
timedata_for_end = []
timedata_for_random = []
timedata_for_hybrid = []


def timer(theFunction, timedata_for_x, n):
    for test in range(5):
        dum_data = make_dum_data(n)
        t = timeit.timeit(lambda: theFunction(0, len(dum_data) - 1, dum_data), number=1)
        timedata_for_x.append(t)


table = PrettyTable(['timedata_for_middle', 'timedata_for_start', 'timedata_for_end',
                     'timedata_for_random', 'timedata_for_hybrid'])
timer(quick_sort_middle, timedata_for_middle, 10)
timer(quick_sort_start, timedata_for_start, 10)
timer(quick_sort_end, timedata_for_end, 10)
timer(quick_sort_random, timedata_for_random, 10)
timer(quick_sort_hybrid, timedata_for_hybrid, 10)

for x in range(0, 5):
    table.add_row([timedata_for_middle[x], timedata_for_start[x], timedata_for_end[x],
                   timedata_for_random[x], timedata_for_hybrid[x]])
print("This data is for 5 trails of each quick sort with input size 10")
print(table)

timedata_for_start.clear()
timedata_for_end.clear()
timedata_for_middle.clear()
timedata_for_random.clear()
timedata_for_hybrid.clear()
table = PrettyTable(['timedata_for_middle', 'timedata_for_start', 'timedata_for_end',
                     'timedata_for_random', 'timedata_for_hybrid'])
timer(quick_sort_middle, timedata_for_middle, 100)
timer(quick_sort_start, timedata_for_start, 100)
timer(quick_sort_end, timedata_for_end, 100)
timer(quick_sort_random, timedata_for_random, 100)
timer(quick_sort_hybrid, timedata_for_hybrid, 100)

for x in range(0, 5):
    table.add_row([timedata_for_middle[x], timedata_for_start[x], timedata_for_end[x],
                   timedata_for_random[x], timedata_for_hybrid[x]])

print("This data is for 5 trails of each quick sort with input size 100")
print(table)

timedata_for_start.clear()
timedata_for_end.clear()
timedata_for_middle.clear()
timedata_for_random.clear()
timedata_for_hybrid.clear()
table = PrettyTable(['timedata_for_middle', 'timedata_for_start', 'timedata_for_end',
                     'timedata_for_random', 'timedata_for_hybrid'])
timer(quick_sort_middle, timedata_for_middle, 1000)
timer(quick_sort_start, timedata_for_start, 1000)
timer(quick_sort_end, timedata_for_end, 1000)
timer(quick_sort_random, timedata_for_random, 1000)
timer(quick_sort_hybrid, timedata_for_hybrid, 1000)

for x in range(0, 5):
    table.add_row([timedata_for_middle[x], timedata_for_start[x], timedata_for_end[x],
                   timedata_for_random[x], timedata_for_hybrid[x]])

print("This data is for 5 trails of each quick sort with input size 1000")
print(table)
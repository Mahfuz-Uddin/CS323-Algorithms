# Analysis of Algorithms - CSCI 323
# Assignment Number (Assignment 1)
# Mahfuz Uddin
#quick sort code used from geeksforgeeks

import random
import timeit
from prettytable import PrettyTable

count = 0


def make_dum_data(n):
    dumb_data = []
    for x in range(n):
        dumb_data.append(random.randint(0, n * 1000))
    return dumb_data


def insertion_sort(low, n, array):
    global count
    for i in range(low + 1, n + 1):
        val = array[i]
        j = i
        count += 2
        while j > low and array[j - 1] > val:
            array[j] = array[j - 1]
            j -= 1
        array[j] = val
    print(int(72/7))

def partition_with_start(start, end, array):
    global count
    # Initializing pivot's index to start
    pivot_index = start
    pivot = array[pivot_index]

    # This loop runs till start pointer crosses
    # end pointer, and when it does we swap the
    # pivot with element on end pointer
    count += 1
    while start < end:
        count += 1

        # Increment the start pointer till it finds an
        # element greater than pivot
        count += 2
        while start < len(array) and array[start] <= pivot:
            start += 1
            count += 1

        # Decrement the end pointer till it finds an
        # element less than pivot
        count += 1
        while array[end] > pivot:
            end -= 1
            count += 1

        # If start and end have not crossed each other,
        # swap the numbers on start and end
        count += 1
        if start < end:
            array[start], array[end] = array[end], array[start]

    # Swap pivot element with element on end pointer.
    # This puts pivot on its correct sorted place.
    array[end], array[pivot_index] = array[pivot_index], array[end]
    # Returning end pointer to divide the array into 2
    return end


def partition_with_random(start, stop, array):
    global count
    pivot = start  # pivot

    # a variable to memorize where the
    i = start + 1

    # partition in the array starts from.
    for j in range(start + 1, stop + 1):

        # if the current element is smaller
        # or equal to pivot, shift it to the
        # left side of the partition.
        count += 1
        if array[j] <= array[pivot]:
            array[i], array[j] = array[j], array[i]
            i = i + 1
    array[pivot], array[i - 1] = array[i - 1], array[pivot]
    pivot = i - 1
    return pivot


def partitionrand(start, end, array):
    randpivot = random.randrange(start, end)
    array[start], array[randpivot] = array[randpivot], array[start]
    return partition_with_random(start, end, array)


def quick_sort_start(start, end, array):
    global count
    count += 1
    if start < end:
        # p is partitioning index, array[p]
        # is at right place
        p = partition_with_start(start, end, array)

        # Sort elements before partition
        # and after partition
        quick_sort_start(start, p - 1, array)
        quick_sort_start(p + 1, end, array)


def quick_sort_random(start, end, array):
    global count
    count += 1
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
    global count
    count += 1
    while low < high:

        # If the size of the array is less
        # than threshold apply insertion sort
        # and stop recursion
        count += 1
        if high - low + 1 < 10:
            insertion_sort(low, high, array)
            break
        else:
            pivot = partition_with_random(low, high, array)
            count += 1
            if pivot - low < high - pivot:
                quick_sort_hybrid(low, pivot - 1, array)
                low = pivot + 1
            else:
                quick_sort_hybrid(pivot + 1, high, array)
                high = pivot - 1


timedata_for_start = []
comparisons_for_start = []
timedata_for_random = []
comparisons_for_random = []
timedata_for_hybrid = []
comparisons_for_hybrid = []


def timer(theFunction, timedata_for_x, comparisons_for_x, n):
    global count
    for test in range(5):
        dum_data = make_dum_data(n)
        t = timeit.timeit(lambda: theFunction(0, len(dum_data) - 1, dum_data), number=1)
        timedata_for_x.append(t)
        comparisons_for_x.append(count)
        count = 0


table = PrettyTable(['Time_For_Pivot_At_Start', 'Comparisons_For_Pivot_At_Start', 'Time_For_Pivot_At_Random',
                     'Comparisons_For_Pivot_At_Random',
                     'Time_For_Pivot_At_RandomHybrid', 'Comparisons_For_Pivot_At_RandomHybrid'])
timer(quick_sort_start, timedata_for_start, comparisons_for_start, 100)
timer(quick_sort_random, timedata_for_random, comparisons_for_random, 100)
timer(quick_sort_hybrid, timedata_for_hybrid, comparisons_for_hybrid, 100)

for x in range(0, 5):
    table.add_row([timedata_for_start[x], comparisons_for_start[x], timedata_for_random[x], comparisons_for_random[x],
                   timedata_for_hybrid[x], comparisons_for_hybrid[x]])
print("This data is for 5 trails of each quick sort with input size 100")
print(table)

timedata_for_start.clear()
timedata_for_random.clear()
timedata_for_hybrid.clear()
comparisons_for_hybrid.clear()
comparisons_for_random.clear()
comparisons_for_start.clear()
table = PrettyTable(['Time_For_Pivot_At_Start', 'Comparisons_For_Pivot_At_Start', 'Time_For_Pivot_At_Random',
                     'Comparisons_For_Pivot_At_Random',
                     'Time_For_Pivot_At_RandomHybrid', 'Comparisons_For_Pivot_At_RandomHybrid'])
timer(quick_sort_start, timedata_for_start, comparisons_for_start, 1000)
timer(quick_sort_random, timedata_for_random, comparisons_for_random, 1000)
timer(quick_sort_hybrid, timedata_for_hybrid, comparisons_for_hybrid, 1000)

for x in range(0, 5):
    table.add_row([timedata_for_start[x], comparisons_for_start[x], timedata_for_random[x], comparisons_for_random[x],
                   timedata_for_hybrid[x], comparisons_for_hybrid[x]])

print("\n\nThis data is for 5 trails of each quick sort with input size 1000")
print(table)

timedata_for_start.clear()
timedata_for_random.clear()
timedata_for_hybrid.clear()
comparisons_for_hybrid.clear()
comparisons_for_random.clear()
comparisons_for_start.clear()
table = PrettyTable(['Time_For_Pivot_At_Start', 'Comparisons_For_Pivot_At_Start', 'Time_For_Pivot_At_Random',
                     'Comparisons_For_Pivot_At_Random',
                     'Time_For_Pivot_At_RandomHybrid', 'Comparisons_For_Pivot_At_RandomHybrid'])
timer(quick_sort_start, timedata_for_start, comparisons_for_start, 10000)
timer(quick_sort_random, timedata_for_random, comparisons_for_random, 10000)
timer(quick_sort_hybrid, timedata_for_hybrid, comparisons_for_hybrid, 10000)

for x in range(0, 5):
    table.add_row([timedata_for_start[x], comparisons_for_start[x], timedata_for_random[x], comparisons_for_random[x],
                   timedata_for_hybrid[x], comparisons_for_hybrid[x]])

print("\n\nThis data is for 5 trails of each quick sort with input size 10000")
print(table)

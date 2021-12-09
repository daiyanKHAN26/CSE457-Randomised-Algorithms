import time
import random
import numpy as np
from numpy.random import default_rng

# A global variable 'totalCom' is set up to keep
# track of total number of comparisons made to 
# sort the array using quicksort
totalCom = 0

# Quicksort Algorithm:
# Method is defined to implement quicksort algorithm
# where it takes 3 inputs = array (a), starting index
# of array (i), ending index of array (j)
def quicksort(a, i, j):
    if i < j:

      # index position of the pivot relative to the array
        p_ind = rand(a, i, j)

      # Array is split into two halves, and theLeft and 
      # right halves of the array are sorted seperately,
      # giving us a partially sorted array
        quicksort(a, i, p_ind - 1)
        quicksort(a, p_ind + 1, j)

# Random Pivot Generator:
# Method to pick a random pivot value, and set as
# first element of array to sort
def rand(a, i, j):

  # Pick a random number between array range i to j
    pivot = random.randrange(i, j)

  # swap pivot value with current first index value
  # and call partition method
    (a[i], a[pivot]) = (a[pivot], a[i])
    return partition(a, i, j)


# Partition: 
# Method to partition arrays. Values smaller than chosen
# pivot is stored in the array on the left of the pivot,
# and values larger than pivot are stored on its right.
# Total number of comparisons is incremented for every 
# comparison made between array values.
def partition(a, i, j):
    global totalCom
    pivot = i
    print('Pivot = ', a[pivot]) # print chosen pivot value
    count = 0
    x = i + 1 # array start position

    # if current index value is less than or equal
    # to pivot value, then shift to left of partition
    for j in range(i + 1, j + 1):
        if a[j] <= a[pivot]:
            (a[x], a[j]) = (a[j], a[x])
            x = x + 1
            count += 1

    # print the number of comparisons 
    # every time a new pivot is picked        
    print ('No. of comparisons:', count)
    totalCom += count
    (a[pivot], a[x - 1]) = (a[x - 1], a[pivot])
    pivot = x - 1
    return (pivot)

########################################################

### DRIVER CODE ###

# Random number generator:
# Generate an array of unique random numbers 
# between range 0 to n-1, array length = size,
# set replace==false to get unique values

print('# Random Array Generator #')
rng = default_rng()
n = int(input('Enter end value of range: '))
s = int(input('Enter length of array: '))
array = rng.choice(n+1, size=s, replace=False) 
print('\n Unsorted array :',array)
time.sleep(1)

# Begin quicksort algorithm
print('\n **** Start Quicksort ****')
time.sleep(1)
quicksort(array, 0, len(array) - 1)
print('\n')
print('Sorted array: ',array)
print('Total no. of comparisons: ',totalCom)

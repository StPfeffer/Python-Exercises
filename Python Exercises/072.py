from math import floor
from random import randint
from time import time


def binarySearch(list, target, low = None, high = None):
    if low is None:
        low = 0
    if high is None:
        high = len(list) - 1

    if high < low: # target is not in the list
        return -1
    
    midpoint = (low + high) // 2

    if list[midpoint] == target:
        return midpoint
    elif target < list[midpoint]:
        return binarySearch(list, target, low, high = midpoint - 1)
    else:
        return binarySearch(list, target, midpoint + 1, high)


# Solution


def binSearch(li, element):
    bottom = 0
    top = len(li) - 1
    index = -1

    while top >= bottom and index == -1:
        mid = int(floor((top + bottom) / 2.0))

        if li[mid] == element:
            index = mid
        elif li[mid] > element:
            top = mid - 1
        else:
            bottom = mid + 1

    return index


def generateRandomList(e): # not necessary for the exercise, but useful
    """Return a random generated list, where 'e' is the number of elements in the list.
    """
    length = e

    sorted_list = set()
    while len(sorted_list) < length:
        sorted_list.add(randint(-3 * length, 3 * length))
    sorted_list = sorted(list(sorted_list))

    return sorted_list


def naiveSearch(list, target): # not necessary for the exercise, just for fun
    for i in range(len(list)):
        if list[i] == target:
            return i
    
    return -1


def searchTest(n):
    """Check the runtime of both binary search methods.
    \nUse a random generated list of length 1000000.
    """
    length = 1000000

    sorted_list = set()
    while len(sorted_list) < length:
        sorted_list.add(randint(-3 * length, 3 * length))
    sorted_list = sorted(list(sorted_list))

    start = time()
    for target in sorted_list:
        binarySearch(sorted_list, target)
    end = time()
    print(f"binarySearch time: {(end - start)} seconds.")

    start = time()
    for target in sorted_list:
        binSearch(sorted_list, target)
    end = time()
    print(f"binSearch time: {(end - start)} seconds.")

    if n:
        start = time()
        for target in sorted_list:
            naiveSearch(sorted_list, target)
        end = time()
        print(f"naiveSearch time: {(end - start)} seconds.")


print("""[ 1 ] Generate a custom size sorted list and search for an input value.
[ 2 ] Check the runtime of both binary search methods. Use a random generated sorted list thas has 1000000 elements.
[ 3 ] WARNING! Check the runtime of both binary search methods and a naive search. Use a random generated sorted list that has 1000000 elements. This will take a while.""")
option = int(input("Enter your option: "))
if option == 1:
    list_size = generateRandomList(int(input("Enter the size of the list: ")))
    target = int(input("Enter the number that you want to search in the list: "))
    target_index = binarySearch(list_size, target)

    if target_index == -1:
        print(f"Value {target} not found in the list")
    else:
        print(f"Found {target} at index {target_index} in the list!")

    # print(binSearch(list_size, target)) # solution print
elif option == 2:
    searchTest(0)
elif option == 3:
    searchTest(1)
else:
    pass

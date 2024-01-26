''' Quicksort example adopted from
https://pythonschool.net/data-structures-algorithms/quicksort/
for CSCI 204
Xiannong Meng
2017-09-05
'''
def partition(myList, start, end):
    pivot = myList[start]
    left = start+1
    right = end
    done = False
    while not done:
        while left <= right and myList[left] <= pivot:
            left = left + 1
        while myList[right] >= pivot and right >=left:
            right = right -1
        if right < left:
            done= True
        else:
            # swap places
            temp=myList[left]
            myList[left]=myList[right]
            myList[right]=temp
    # swap start with myList[right]
    temp=myList[start]
    myList[start]=myList[right]
    myList[right]=temp
    return right

def quicksort(myList, start, end):
    if start < end:
        # partition the list
        pivot = partition(myList, start, end)
        # sort both halves
        quicksort(myList, start, pivot-1)
        quicksort(myList, pivot+1, end)
    return myList

from random import *

def test_quicksort(n):
    a = []
    for i in range(n):
        a += [randint(0, 100)]
    if n < 50:
        print('presort : ', a)
    quicksort(a, 0, len(a) - 1)
    if n < 50:
        print('postsort : ', a)

# result on polairs 2017-09-05
#test_quicksort(25)
#test_quicksort(100)      # real/user/sys 0.049/0.018/0.010
#test_quicksort(10000)     # real/user/sys 0.516/0.460/0.006
#test_quicksort(20000)     # real/user/sys 0.801/0.760/0.007

# result on xmeng 2020-01-28
#test_quicksort(25)
#test_quicksort(100)      # real/user/sys 0.049/0.020/0.009
#test_quicksort(10000)     # real/user/sys 0.117/0.058/0.011
test_quicksort(20000)     # real/user/sys 0.224/0.163/0.008

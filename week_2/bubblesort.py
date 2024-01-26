'''Adopted for CSCI 204 from
http://interactivepython.org/runestone/static/pythonds/SortSearch/TheBubbleSort.html
Xiannong Meng
2017-09-05
Updated timing
2020-01-28
'''
from random import *
def bubble_sort(alist):
    for passnum in range(len(alist)-1,0,-1):
        for i in range(passnum):
            if alist[i]>alist[i+1]:
                temp = alist[i]
                alist[i] = alist[i+1]
                alist[i+1] = temp

def test_bubble_sort(n):
    a = []
    for i in range(n):
        a += [randint(0, 100)]
    bubble_sort(a)

# running time on 2017-09-05 on polaris
#test_bubble_sort(100)       # real/user/sys 0.071/0.03/0.007
#test_bubble_sort(10000)     # real/user/sys 9.165/0.087/0.007
#test_bubble_sort(20000)     # real/user/sys 35.484/35.420/0.005

# running time on 2020-01-28 on xmeng
#test_bubble_sort(100)       # real/user/sys 0.048/0.017/0.011
#test_bubble_sort(10000)     # real/user/sys 4.824/4.762/0.013
test_bubble_sort(20000)     # real/user/sys 19.285/19.225/0.013

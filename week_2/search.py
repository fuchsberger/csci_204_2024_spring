def search1(arr, x):
    for i in range(len(arr)):
        if x == arr[i]:
            return i
    return -1


def search2(arr, x):
    low = 0
    high = len(arr) - 1
    mid = 0

    while low <= high:

        mid = (high + low) // 2

        if arr[mid] < x:
            low = mid + 1

        elif arr[mid] > x:
            high = mid - 1

        else:
            return mid
    return -1


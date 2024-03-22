def selection_sort(sequence):
    # TODO: Activity 1
    # loop through all indexes (excluding last)
        # keep track of current index
        # loop through all index between current and last
            # find smallest in remaining elements
        # swap if found smallest is smaller than then current
    return sequence

def insertion_sort(sequence):
    # TODO: Activity 2

    # loop through all indexes
        # keep track of current index and next element
        # shift curent element forward until no longer smaller element at that position
    return sequence

def bubble_sort(sequence):
    # TODO: Activity 3

    swapped = True
    
    while swapped:
        swapped = False

        for i in range(0, len(sequence)-1):
            if sequence[i] > sequence[i+1]:
                swap(sequence, i, i+1)
                swapped = True

    return sequence

def shell_sort(sequence):
    # TODO: Activity 4

    return sequence

def swap(sequence, idx_1, idx_2) -> None:
    sequence[idx_1], sequence[idx_2] = sequence[idx_2], sequence[idx_1]

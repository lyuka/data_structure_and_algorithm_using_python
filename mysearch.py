def binarySearch( theValues, target ):
    # Start with the entire sequence of elements.
    low = 0
    high = len(theValues) - 1

    # Repeatedly subdivide the sequence in half until the target is found.
    while low <= high:
        mid = ( high + low ) // 2
        if theValues[mid] == target:
            return True
        elif target < theValues[mid]:
            high = mid - 1
        else:
            low = mid + 1

    return False

# Performs a recursive binary search on a sorted sequence.
def recBinarySearch( theSeq, target, first, last ):
    if first > last:
        return False
    else:
        mid = ( last + first ) // 2
        if theSeq[mid] == target:
            return True
        elif target < theSeq[mid]:
            return recBinarySearch( theSeq, target, first, mid - 1)
        else:
            return recBinarySearch( theSeq, target, mid + 1, last )

if __name__ == '__main__':
    l_value = [2, 4, 5, 10, 13, 18, 23, 29, 31, 51, 64]
    t_value = 10
    print 'binary search using loop: '
    print binarySearch(l_value, t_value)

    print 'bianry search using recursive: '
    print recBinarySearch( l_value, t_value, 0, len(l_value) )

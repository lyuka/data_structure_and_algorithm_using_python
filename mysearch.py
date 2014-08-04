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

if __name__ == '__main__':
    l_value = [2, 4, 5, 10, 13, 18, 23, 29, 31, 51, 64]
    t_value = 10
    print binarySearch(l_value, t_value)

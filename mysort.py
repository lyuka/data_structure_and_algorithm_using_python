# ===================Bubble Sort=====================================
# Sorts a sequence in ascending order using the bubble sort algorithm.
def bubbleSort( theSeq ):
    n = len( theSeq )
    for i in range( n-1 ):
        for j in range( n-i-1 ):
            if theSeq[j] > theSeq[j+1]:
                tmp = theSeq[j]
                theSeq[j] = theSeq[j+1]
                theSeq[j+1] = tmp

        print 'iter ' + str(i+1)
        for ele in theSeq:
            print ele,
        print ''

# ====================Selection Sort====================================
# Sorts a sequence in ascending order using the selection sort algorithm
def selectionSort( theSeq ):
    n = len( theSeq )
    for i in range( n-1 ):
        smallNdx = i
        for j in range( i+1, n ):
            if theSeq[j] < theSeq[smallNdx ]:
                smallNdx = j

        if smallNdx != i:
            tmp = theSeq[i]
            theSeq[i] = theSeq[smallNdx]
            theSeq[smallNdx] = tmp

        print 'iter ' + str(i+1)
        for ele in theSeq:
            print ele,
        print ''

# ===================Insertion Sort======================================
# Sorts a sequence in ascending order using the insertion sort algorithm.
def insertionSort( theSeq ):
    n = len( theSeq )
    for i in range(1, n):
        value = theSeq[i]

        pos = i
        while pos > 0 and value < theSeq[pos-1]:
            theSeq[pos] = theSeq[pos-1]
            pos -= 1

        theSeq[pos] = value

        print 'iter ' + str(i)
        for j in range(i+1):
            print theSeq[j],
        print ''

# ===================Merge Sort 01=======================================
# Merges two sorted lists to create and return a new sorted list.
def mergeSortedLists( listA, listB ):
    newList = list()
    a = 0
    b = 0

    # Merge the two lists together until one is empty
    while a < len( listA ) and b < len( listB ):
        if listA[a] < listB[b]:
            newList.append( listA[a] )
            a += 1
        else:
            newList.append( listB[b] )
            b += 1

    # If listA contains more items, append them to newList.
    while a < len( listA ):
        newList.append( listA[a] )
        a += 1

    # Or if listB contains more items, append them to newList.
    while b < len( listB ):
        newList.append( listB[b] )
        b += 1

    return newList

# Sorts a Python list in ascending order using the merge sort algorithm.
def MergeSort( theList ):
    # Check the base case - the list contains s single item.
    if len( theList ) <= 1:
        return theList
    else:
        mid = len( theList ) // 2
        leftHalf = MergeSort( theList[ :mid ] )
        rightHalf = MergeSort( theList[ mid: ] )
        newList = mergeSortedLists( leftHalf, rightHalf )
        for ele in newList:
            print ele,
        print ''
        return newList

# ========================Merge Sort 02==================================
# Sorts a virtual subsequence in ascending order using merge sort.
def recMergeSort( theSeq, first, last, tmpArray ):
    if first == last:
        return
    else:
        mid = ( first + last ) // 2
        recMergeSort( theSeq, first, mid, tmpArray )
        recMergeSort( theSeq, mid+1, last, tmpArray )
        mergeVirtualSeq( theSeq, first, mid+1, last+1, tmpArray )
        for ele in tmpArray:
            print ele,
        print ''

# Merges the two sorted virtual sublists: [left...right) [right..end)
def mergeVirtualSeq( theSeq, left, right, end, tmpArray ):
    a = left
    b = right
    m = 0
    while a < right and b < end:
        if theSeq[a] < theSeq[b]:
            tmpArray[m] = theSeq[a]
            a += 1
        else:
            tmpArray[m] = theSeq[b]
            b += 1
        m += 1

    while a < right:
        tmpArray[m] = theSeq[a]
        a += 1
        m += 1

    while b < end:
        tmpArray[m] = theSeq[b]
        b += 1
        m += 1

    for i in range( end - left ):
        theSeq[i+left] = tmpArray[i]

# a wrapper function for the virtual subsequence merge sort
def mergeVirtualSort( theSeq ):
    from myarray import myArray

    n = len( theSeq )
    tmpArray = myArray(n)
    recMergeSort( theSeq, 0, n-1, tmpArray )

# ===========================Quick Sort===============================
# Sorts an array or list using the recursive quick sort algorithm
def quickSort( theSeq ):
    n = len( theSeq )
    recQuickSort( theSeq, 0, n-1 )

# The recursive implementation using virtual segments.
def recQuickSort( theSeq, first, last ):
    if first >= last:
        #for i in range(len(theSeq)):
        #    print theSeq[i],
        #print ''
        return
    else:
        #pivot = theSeq[first]
        pos = partitionSeq( theSeq, first, last )
        for i in range(first, pos):
            print theSeq[i],
        print ''
        print theSeq[pos]
        for i in range(pos+1, last+1):
            print theSeq[i],
        print ''
        print '======='
        recQuickSort( theSeq, first, pos-1 )
        recQuickSort( theSeq, pos+1, last )
        

def partitionSeq( theSeq, first, last ):
    pivot = theSeq[first]
    print 'current pivot: %d' % pivot
    left = first + 1
    right = last
    #print left, right
    while left <= right:
        # Find the first key larger than the pivot
        while left < right and theSeq[left] < pivot:
            left += 1
        # Find the last key smaller than the pivot
        while right >= left and theSeq[right] >= pivot:
            right -= 1
        # Swap the two keys
        if left < right:
            tmp = theSeq[left]
            theSeq[left] = theSeq[right]
            theSeq[right] = tmp
        elif left == right:
            break
    if right != first:
        theSeq[first] = theSeq[right]
        theSeq[right] = pivot
    return right


# =======================module test===================================
if __name__ == '__main__':
    theSeq = [10, 51, 2, 18, 4, 31, 13, 5, 23, 64, 29]
    print 'Bubble Sort: '
    bubbleSort(theSeq)
    
    theSeq = [10, 51, 2, 18, 4, 31, 13, 5, 23, 64, 29]
    print 'Selection Sort: '
    selectionSort(theSeq)

    theSeq = [10, 51, 2, 18, 4, 31, 13, 5, 23, 64, 29]
    print 'Insertion Sort: '
    insertionSort(theSeq)

    theSeq = [10, 51, 2, 18, 4, 31, 13, 5, 23, 64, 29]
    print 'Merge Sort: '
    sortedSeq = MergeSort( theSeq )
    for ele in sortedSeq:
        print ele,
    print ''

    theSeq = [10, 51, 2, 18, 4, 31, 13, 5, 23, 64, 29]
    print 'Merge Sort ( using virtual subsequence )'
    mergeVirtualSort( theSeq )
    for ele in theSeq:
        print ele,
    print ''

    theSeq = [10, 51, 2, 18, 4, 31, 13, 5, 23, 64, 29]
    print 'Quick Sort: '
    quickSort( theSeq )
    for ele in theSeq:
        print ele,
    print ''

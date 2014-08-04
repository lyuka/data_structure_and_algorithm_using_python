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

if __name__ == '__main__':
    #theSeq = [10, 51, 2, 18, 4, 31, 13, 5, 23, 64, 29]
    #print 'Bubble Sort: '
    #bubbleSort(theSeq)
    
    #theSeq = [10, 51, 2, 18, 4, 31, 13, 5, 23, 64, 29]
    #print 'Selection Sort: '
    #selectionSort(theSeq)

    #theSeq = [10, 51, 2, 18, 4, 31, 13, 5, 23, 64, 29]
    #print 'Insertion Sort: '
    #insertionSort(theSeq)

    list_a = [10, 51, 2, 18, 4]
    list_b = [31, 13, 2, 23, 64, 29]
    selectionSort(list_a)
    insertionSort(list_b)
    merged_list = mergeSortedLists(list_a, list_b)
    for ele in merged_list:
        print ele,
    print ''

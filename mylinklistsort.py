# Sorts a linked list
from mylinklist import ListNode, traversal, append_node, insert_sorted

# ===================Insertion Sort==============
def llistInsertonSort( origList ):
    if origList is None:
        return None
    

    newList = None
    while origList is not None:
        curNode = origList
        origList = origList.next
        curNode.next = None
        newList = _addToSortedList( newList, curNode)
    return newList

def _addToSortedList( newList, curNode ):
    newList = insert_sorted( newList, curNode.data )
    return newList

# ===================Merge Sort======================
def llistMergeSort( theList ):
    if theList is None:        # none node
        return None

    if theList.next is None:   # only one node, return
        return theList
    
    rightList = _splitLinkedList( theList )
    leftList = theList

    #print leftList.data, rightList.data
    
    leftList = llistMergeSort( leftList )
    rightList = llistMergeSort( rightList )

    theList = _mergeLinkedLists( leftList, rightList )

    return theList

def _splitLinkedList( subList ):
    midPoint = subList
    curNode = midPoint.next

    #Iterate through the list until curNode falls off the end.
    while curNode is not None:
        curNode = curNode.next     # curNode move once
        if curNode is not None:
            midPoint = midPoint.next   # midPoint move once
            curNode = curNode.next     # curNode move twice

    rightList = midPoint.next
    midPoint.next = None

    return rightList

def  _mergeLinkedLists( subListA, subListB ):
    newList = ListNode( None )
    newTail = newList

    while subListA is not None and subListB is not None:
        if subListA.data <= subListB.data:
            newTail.next = subListA
            subListA = subListA.next
        else:
            newTail.next = subListB
            subListB = subListB.next

        newTail = newTail.next
        newTail.next = None

    if subListA is not None:
        newTail.next = subListA
    else:
        newTail.next = subListB

    return newList.next

if __name__ == '__main__':
    head = None
    tail = None
    ( head, tail ) = append_node( head, tail, 23 )
    ( head, tail ) = append_node( head, tail, 2 )
    ( head, tail ) = append_node( head, tail, 51 )
    ( head, tail ) = append_node( head, tail, 18 )
    ( head, tail ) = append_node( head, tail, 4 )
    ( head, tail ) = append_node( head, tail, 31 )
    traversal( head )
    print '=======Insertion Sort======='
    origList = head
    sortedList = llistInsertonSort( origList )
    traversal( sortedList )

    print '=======Merge Sort==========='
    head = None
    tail = None
    ( head, tail ) = append_node( head, tail, 23 )
    ( head, tail ) = append_node( head, tail, 2 )
    ( head, tail ) = append_node( head, tail, 51 )
    ( head, tail ) = append_node( head, tail, 18 )
    ( head, tail ) = append_node( head, tail, 4 )
    ( head, tail ) = append_node( head, tail, 31 )
    traversal( head )
    origList = head
    #traversal( origList )
    sortedList = llistMergeSort( origList )
    traversal( sortedList )

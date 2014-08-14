class CListNode:
    def __init__( self, data ):
        self.data = data
        self.next = None

def traverse( listRef ):
    curNode = listRef
    done = listRef is None
    while not done:
        curNode = curNode.next
        print curNode.data,
        done = curNode is listRef
    print ''

def searchCircularList( listRef, target ):
    curNode = listRef
    done = listRef is None
    while not done:
        curNode = curNode.next
        if curNode.data == target:
            return True
        else:
            done = curNode is listRef or curNode.data > target
    return False


def sortedInsert( listRef, value ):
    newNode = CListNode( value )
    if listRef is None:      # empty list
        listRef = newNode
        newNode.next = newNode
    elif value < listRef.next.data:   # insert in front
        newNode.next = listRef.next
        listRef.next = newNode
    elif value > listRef.data:   # insert in back
        newNode.next = listRef.next
        listRef.next = newNode
        listRef = newNode
    else:
        preNode = None
        curNode = listRef
        done = listRef is None
        while not done:
            preNode = curNode
            curNode = curNode.next
            done = curNode is listRef or curNode.data > value
        newNode.next = curNode
        preNode.next = newNode
    return listRef

def remove( listRef, target ):
    assert listRef is not None, "No Node in the link list."
    preNode = None
    curNode = listRef
    done = listRef is None
    while not done:
        preNode = curNode
        curNode = curNode.next
        if curNode.data == target:
            if preNode is curNode:
                listRef = None
                return listRef
            preNode.next = curNode.next
            if curNode is listRef:
                listRef = preNode
            return listRef
        else:
            done = curNode is listRef or curNode.data > target
    return listRef

if __name__ == '__main__':
    #node_a = CListNode(1)
    listRef = None
    
    value = input('insert node( finished with -1): ')
    while value != -1:
        listRef = sortedInsert(listRef, value)
        traverse( listRef )
        value = input('insert node( finished with -1): ')
        
    
    target = input('remove node( finished with -1): ')
    while target != -1:
        listRef = remove( listRef, target )
        traverse( listRef )
        target = input('remove node( finished with -1): ')
        

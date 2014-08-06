class ListNode:
    def __init__( self, data ):
        self.data = data
        self.next = None

def traversal( head ):
    curNode = head
    while curNode is not None:
        print curNode.data,
        curNode = curNode.next
    print ''

def unorderedSearch( head, target ):
    curNode = head
    while curNode is not None and curNode.data != target:
        curNode = curNode.next
    return curNode is not None

def sortedSearch( head, target ):
    curNode = head
    while curNode is not None and curNode.data < target:
        if curNode.data == target:
            return True
        else:
            curNode = curNode.next
    return False

def insert_sorted( head, data ):
    preNode = None
    curNode = head
    while curNode is not None and data > curNode.data:
        preNode = curNode
        curNode = curNode.next

    newNode = ListNode( data )
    newNode.next = curNode
    if curNode is head:
        head = newNode
    else:
        preNode.next = newNode
    return head
    
def prepend_node( head, data ):
    newNode = ListNode( data )
    newNode.next = head
    head = newNode
    return head

def remove_node_no_tail( head ,target ):
    preNode = None
    curNode = head
    while curNode is not None and curNode.data != target:
        preNode = curNode
        curNode = curNode.next

    if curNode is not None:
        if curNode is head:
            head = curNode.next
        else:
            preNode.next = curNode.next
    return head

def append_node( head, tail, data ):
    newNode = ListNode( data )
    if head is None :
        head = newNode
    else:
        tail.next = newNode
    tail = newNode
    return head, tail

def remove_node( head, tail, target ):
    preNode = None
    curNode = head
    while curNode is not None and curNode.data != target:
        preNode = curNode
        curNode = curNode.next

    if curNode is not None:
        if curNode is head:
            head = curNode.next
        else:
            preNode.next = curNode.next
        if curNode is tail:
            tail = preNode
    return head, tail
            

if __name__ == '__main__':
    a = ListNode(1)
    head = a
    tail = a

    #append nodes
    for i in range(2, 10):
        (head, tail) = append_node( head, tail, i )
    print 'append nodes: '
    traversal( head )

    #remove node
    print 'remove 9: '
    (head, tail) = remove_node( head, tail, 9 )
    traversal( head )
    print 'remove 3: '
    (head, tail) = remove_node( head, tail, 3 )
    traversal( head )

    print '==========================================='
    
    b = ListNode(10)
    head = b
    
    #prepend nodes    
    for i in range(11, 20):
        head = prepend_node( head, i )
    print 'prepend nodes: '
    traversal( head )

    # remove node without tail
    print 'remove 16: '
    head = remove_node_no_tail( head , 16 )
    traversal( head )

    print '============================================'
    
    c = ListNode(20)
    head = c

    # generate sorted list
    print 'insert element in ascend manner '
    for ele in [23, 22, 25, 21, 29, 33]:
        head = insert_sorted( head, ele )
    traversal( head )

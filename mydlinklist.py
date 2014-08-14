class DListNode:
    def __init__( self, data ):
        self.data = data
        self.next = None
        self.prev = None

def traversal( head ):
    curNode = head
    while curNode is not None:
        print curNode.data,
        curNode = curNode.next
    print ''

def revTraversal( tail ):
    curNode = tail
    while curNode is not None:
        print curNode.data,
        curNode = curNode.prev
    print ''

# Search the target in an ordered double list with probe reference,
# which left in the last search operation.
def searchWithProbe( head, tail, probe, target ):
    # Make sure the list is not empty
    if head is None:
        return False
    # If probe is null, initialize it to the first node.
    elif probe is None:
        probe = head

    if target < probe.data:
        while probe is not None and target <= probe.data:
            if target == probe.data:
                return True
            else:
                probe = probe.prev
    else:
        while probe is not None and target >= probe.data:
            if target == probe.data:
                return True
            else:
                probe = probe.next

    return False


# Insert a value into an ordered double linked list
def sortedInsert( head, tail, value ):
    newnode = DListNode( value )
    if head is None:
        head = newNode
        tail = head
    elif value <= head.data:
        newnode.next = head
        head.prev = newnode
        head = newnode
    elif value >= tail.data:
        newnode.prev = tail
        tail.next = newnode
        tail = newnode
    else:
        node = head
        while node is not None and node.data < value:
            node = node.next

        newnode.next = node
        newnode.prev = node.prev
        node.prev.next = newnode
        node.prev = newnode

    return head, tail

# Remove a node from an order double linked list
def sortedRemove( head, tail, target ):
    curNode = head
    #print head.data
    #print curNode.data
    while curNode is not None and curNode.data < target:
        #print curNode.data
        curNode = curNode.next
    #print curNode.data
    if curNode is not None and curNode.data == target:
        if curNode is head:
            curNode.next.prev = None
            head = curNode.next
        elif curNode is tail:
            curNode.prev.next = None
            tail = curNode.prev
        else:
            curNode.next.prev = curNode.prev
            curNode.prev.next = curNode.next
            curNode.next = None
            curNode.prev = None

    return head, tail

if __name__ == '__main__':
    a = DListNode(1)
    head = a
    tail = a

    value = input("insert value( finished with -1 ): ")
    while value != -1:
        ( head, tail ) = sortedInsert( head, tail, value )
        value = input("insert value( finished with -1 ): ")
    traversal( head )
    revTraversal( tail )
    
    target = input("search target: ")
    probe = None
    print searchWithProbe( head, tail, probe, target )
    print probe

    target = input("remove target( finished with -1 ): ")
    while target != -1:
        ( head, tail ) = sortedRemove( head, tail, target )
        traversal( head )
        revTraversal( tail )
        target = input("remove target( finished with -1 ): ")

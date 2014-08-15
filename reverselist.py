# Print the contents of a singly linked list in reverse order.
def printListBF( head ):
    numNodes = 0
    curNode = head
    while curNode is not None:
        curNode = curNode.next
        numNodes += 1

    for i in range( numNodes ):
        curNode = head
        
        for j in range( numNodes - i - 1 ):
            curNode = curNode.next

        print curNode.data,
    print ''

# Print the contents of a linked list in reverse order using a stack
def printListStack( head ):
    from lliststack import Stack

    s = Stack()

    # Iterate through the list and push each item onto the stack
    curNode = head
    while curNode is not None:
        s.push( curNode.data )
        curNode = curNode.next

    # Repeatedly pop the items from the stack and print them
    while not s.isEmpty():
        item = s.pop()
        print item,
    print ''

# Print the contents of a linked list using recursion.
def printListRecur( node ):
    if node is not None:
        printListRecur( node.next )
        print node.data,
        #print ''


if __name__ == '__main__':
    from mylinklist import ListNode, traversal, prepend_node

    head = None
    print "input value, -1 ended: "
    value = input()
    while value != -1:
        head = prepend_node( head, value )
        value = input()
    traversal( head )

    print "print the list in reverse order with brute-force: "
    printListBF( head )

    print "print the list in reverse order with a stack: "
    printListStack( head )

    print "print the list in reverse order in a reverse way: "
    #curr_node = head
    printListRecur( head )

# Implements the Bag ADT using a singly linked list.

class Bag:
    # Constructs an empty bag.
    def __init__( self ):
        self._head = None
        self._size = 0

    # Returns the number of items in the bag
    def __len__( self ):
        return self._size

    # Determins if an item is contained in the bag.
    def __contains__( self, target ):
        curNode = self._head
        while curNode is not None and curNode.item != target:
            curNode = curNode.next
        return curNode is not None

    # Adds a new item to the bag.
    def add( self, item ):
        newNode = _BagListNode( item )
        newNode.next = self._head
        self._head = newNode
        self._size += 1

    # Remove an instance of the item from the bag.
    def remove( self, item ):
        preNode = None
        curNode = self._head
        while curNode is not None and curNode.item != item:
            preNode = curNode
            curNode = curNode.next

        # The item has to be in the bag to remove it.
        assert curNode is not None, "The item must be in the bag."

        # Unlink the node and return the item.
        self._size -= 1
        if curNode is self._head:
            self._head = curNode.next
        else:
            preNode.next = curNode.next
        return curNode.item

    # Returns an iterator for traversing the list of items.
    def __iter__( self ):
        return _BagIterator( self._head )

# Defines a private storage class for creating list nodes.
class _BagListNode( object ):
    def __init__( self, item ):
        self.item = item
        self.next = None

# Defines a linked list iterator for the Bag ADT.
class _BagIterator:
    def __init__( self, listHead ):
        self._curNode = listHead

    def __iter__( self ):
        return self

    def next( self ):
        if self._curNode is None:
            raise StopIteration
        else:
            item = self._curNode.item
            self._curNode  = self._curNode.next
            return item


if __name__ == '__main__':
    bag_list = Bag()
    bag_list.add(3)
    bag_list.add(4)
    bag_list.add(5)

    print len(bag_list)
    for item in bag_list:
        print item,
    print ''

    print 4 in bag_list
    rm_ele = input('please input the element needed to be removed: ')
    if rm_ele not in bag_list:
        print 'invalid input, please input another elemnt: '
        rm_ele = input('please input the element needed to be removed: ')
    bag_list.remove(rm_ele)

    print len(bag_list)
    for item in bag_list:
        print item,
    print ''

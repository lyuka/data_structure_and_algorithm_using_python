# implementation of the Map ADT using a binary search tree.
from lliststack import Stack

class BSTMap:
    # Creates an empty map instance.
    def __init__( self ):
        self._root = None
        self._size = 0

    # Returns the number of entries in the map.
    def __len__( self ):
        return self._size

    # Returns an iterator for traversing the keys in the map.
    def __iter__( self ):
        return _BSTMapIterator( self._root )

    # Determines if the map contains the given key.
    def __contains__( self, key ):
        return self._bstSearch( self._root, key ) is not None

    # Returns the minimum key in the map
    def __min__( self ):
        node = self._bstMinimum( self.root )
        assert node is not None, "Empty Map"
        return node.key
    
    # Returns the maximum key in the map
    def __max__( self ):
        node = self._bstMaximum( self.root )
        assert node is not None, "Empty Map"
        return node.key
    
    # Returns the value associated with the key.
    def valueOf( self, key ):
        node = self._bstSearch( self._root, key )
        assert node is not None, "Invalid map key."
        return node.value

    # Adds a new entry to the map or replaces the value of an existing key.
    def add( self, key, value ):
        # Find the node containing the key, if it exists.
        node = self._bstSearch( self._root, key )
        # If the key is already in the tree, update its value.
        if node is not None:
            node.value = value
            return False
        else:
            self._root = self._bstInsert( self._root, key, value )
            self._size += 1
            return True

    # Removes the map entry associated with the given key.
    def remove( self, key ):
        assert key in self, "Invalid map key."
        self._root = self._bstRemove( self._root, key )
        self._size -= 1
        
    # Helper method that recursively searches the tree for a target key.
    def _bstSearch( self, subtree, target ):
        if subtree is None:            # base case
            return None
        elif target < subtree.key:     # target is left of the subtree root
            return self._bstSearch( subtree.left, target )
        elif target > subtree.key:     # target is right of the subtree root.
            return self._bstSearch( subtree.right, target )
        else:                          # base case
            return subtree

    # Helper method for finding the node containing the minium key.
    def _bstMinimum( self, subtree ):
        if subtree is None:
            return None
        elif subtree.left is None:
            return subtree
        else:
            return self._bstMinimum( subtree.left )

    # Helper method for finding the node containing the maximum
    def _bstMaximum( self, subtree ):
        if subtree is None:
            return None
        elif subtree.right is None:
            return subtree
        else:
            return self._bstMaximum( subtree.right )

    # Helper method that inserts a new item, recurively.
    def _bstInsert( self, subtree, key, value ):
        if subtree is None:
            subtree = _BSTMapNode( key, value )
        elif key < subtree.key:
            subtree.left = self._bstInsert( subtree.left, key, value )
        elif key > subtree.key:
            subtree.right = self._bstInsert( subtree.right, key, value )
        return subtree

    # Helper method that removes an existing item recursively.
    def _bstRemove( self, subtree, target ):
        # Search for the item in the tree.
        if subtree is None:
            return subtree
        elif target < subtree.key:
            subtree.left = self._bstRemove( subtree.left, target )
            return subtree
        elif target > subtree.key:
            subtree.right = self._bstRemove( subtree.right, target )
            return subtree
        # We found the node containing the item
        else:
            if subtree.left is None and subtree.right is None:   # a leaf
                print 'Node %d is a leaf.' % subtree.key
                return None
            elif subtree.left is None or subtree.right is None:   # node with one child
                print 'Node %d has one child.' % subtree.key
                if subtree.left is not None:
                    return subtree.left
                else:
                    return subtree.right
            else:   # node with two children
                print 'Node %d has two children.' % subtree.key
                successor = self._bstMinimum( subtree.right )
                subtree.key = successor.key
                subtree.value = successor.value
                #print subtree.key, subtree.value
                subtree.right = self._bstRemove( subtree.right, successor.key )
                return subtree

# Storage class for the binary search tree nodes of the map.
class _BSTMapNode:
    def __init__( self, key, value ):
        self.key = key
        self.value = value
        self.left = None
        self.right = None

# An iterator for the binary search tree using a software stack.
class _BSTMapIterator:
    def __init__( self, root ):
        self._theStack = Stack()
        # traverse down to the node containing the smallest key during
        # which each node along the path is pushed onto the stack
        self._traverseToMinNode( root )

    def __iter__( self ):
        return self

    # Returns the next item from the BST in key order.
    def next( self ):
        # If the stack is empty, we are done..
        if self._theStack.isEmpty():
            raise StopIteration
        else:
            # The top node on the stack contains the key.
            node = self._theStack.pop()
            key = node.key
            # If this node has a subtree rooted as the right child, we must
            # fiind the node in that subtree that contains the smallest key.
            # Again, the nodes along the path are pushed onto the stack.
            if node.right is not None:
                self._traverseToMinNode( node.right )
            return key

    def _traverseToMinNode( self, subtree ):
        if subtree is not None:
            self._theStack.push( subtree )
            self._traverseToMinNode( subtree.left )


if __name__ == '__main__':
    stu_map = BSTMap()
    id_list = [60, 12, 90, 4, 41, 71, 100, 1, 29, 84, 23, 37]
    name_list = ['Lee', 'Ryuka', 'James', 'Bell', 'Modric', \
                 'Gece', 'Huang', 'ZZ', 'GaoL', 'Rene', \
                 'Diamond', 'ZhaoXR']
    for i in range( len(id_list) ):
        key = id_list[i]
        value = name_list[i]
        #print key, value
        stu_map.add( key, value )
        #print key, stu_map.valueOf( key )

    print '========================================='
    print 'all added: '
    print 'root: ',
    print stu_map._root.key, stu_map._root.value
    print 'minimum key in the map: ',
    print min(stu_map)
    print 'maximum key in the map: ',
    print max(stu_map)
    print 'length of the map: ',
    print len(stu_map)
    for key in stu_map:
        print key, stu_map.valueOf( key )
        
    print '========================================='
    print 'remove key 1: '
    stu_map.remove( 1 )
    for key in stu_map:
        print key, stu_map.valueOf( key )
    print 'length of the map: ',
    print len(stu_map)

    print '========================================='
    print 'remove key 71: '
    stu_map.remove( 71 )
    for key in stu_map:
        print key, stu_map.valueOf( key )
    print 'length of the map: ',
    print len(stu_map)

    print '========================================='
    print 'remove key 12: '
    stu_map.remove( 12 )
    for key in stu_map:
        print key, stu_map.valueOf( key )
    print 'length of the map: ',
    print len(stu_map)

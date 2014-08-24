from lliststack import Stack

# Contants for the balance factors.
LEFT_HIGH  = 1
EQUAL_HIGH = 0
RIGHT_HIGH = -1

# Implementation of the Map ADT using an AVL tree.
class AVLMap:
    def __init__( self ):
        self._root = None
        self._size = 0

    def __len__( self ):
        return self._size

    def __contains__( self, key ):
        return self._bstSearch( self._root, key ) is not None

    def add( self, key, value ):
        node = self._bstSearch( self._root, key )
        if node is not None:
            node.value = value
            return False
        else:
            ( self._root, tmp ) = self._avlInsert( self._root, key, value )
            self._size += 1
            #print self._root.key, self._root.left, self._root.right
            return True

    def valueOf( self, key ):
        node = self._bstSearch( self._root, key )
        assert node is not None, "Invalid map key."
        return node.value

    def remove( self, key ):
        assert key in self, "Invalid map key."
        ( self._root, tmp ) = self._avlRemove( self._root, key )
        self._size -= 1

    def __iter__( self ):
        return _BSTMapIterator( self._root )

    def _avlRemove( self, key ):
        pass

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

    # Rotats the pivot to the right around its left child
    def _avlRotateRight( self, pivot ):
        C = pivot.left
        pivot.left = C.right
        C.right = pivot
        return C

    # Rotates the pivot to the left around its right child.
    def _avlRotateLeft( self, pivot ):
        C = pivot.right
        pivot.right = C.left
        C.left = pivot
        return C

    # Rebalance a node when its left subtree is higher.
    def _avlLeftBalance( self, pivot ):
        # Set C to point to the left child of the pivot.
        C = pivot.left
        # See if the rebalancing is due to case 1.
        if C.bfactor == LEFT_HIGH:
            pivot.bfactor = EQUAL_HIGH
            C.bfactor = EQUAL_HIGH
            pivot =self. _avlRotateRight( pivot )
            return pivot
        # Otherwise, a balance from the left is due to case 2.
        else:
            G = C.right
            if G.bfactor == LEFT_HIGH:
                pivot.bfactor = RIGHT_HIGH
                C.bfactor = EQUAL_HIGH
            elif G.bfactor == EQUAL_HIGH:
                pivot.bfactor = EQUAL_HIGH
                C.bfactor = EQUAL_HIGH
            else:
                pivot.bfactor = EQUAL_HIGH
                C.bfactor = LEFT_HIGH
            G.bfactor = EQUAL_HIGH
            # Perform the double rotation.
            pivot.left = self._avlRotateLeft( C )
            pivot = self._avlRoateRight( pivot )
            return pivot

    # Rebalance a node when its right subtree is higher
    def _avlRightBalance( self, pivot ):
        C = pivot.right
        # See if the  rebalancing is due to case 3.
        if C.bfactor == RIGHT_HIGH:
            pivot.bfactor = EQUAL_HIGH
            C.bfactor = EQUAL_HIGH
            pivot = self._avlRotateLeft( pivot )
            return pivot
        # Otherwise, a balance from the right is due to case 4.
        else:
            G = C.left
            if G.bfactor == LEFT_HIGH:
                pivot.bfactor = RIGHT_HIGH
                C.bfactor = EQUAL_HIGH
            elif G.bfactor == EQUAL_HIGH:
                pivot.bfactor = EQUAL_HIGH
                C.bfactor= EQUAL_HIGH
            else:
                pivot.bfactor = EQUAL_HIGH
                C.bfactor = LEFT_HIGH
            G.bfactor = EQUAL_HIGH
            # Perform the double rotation.
            pivot.right = self._avlRotateRight( C )
            pivot = self._avlRotateLeft( pivot )
            return pivot

    # Recursive method to handle the insertion into an AVL tree.
    # The function returns a tuple containing a reference to the
    # root of the subtree and a boolean to indicate if the subtree
    # grew taller.
    def _avlInsert( self, subtree, key, newitem ):
        if subtree is None:
            subtree = _AVLMapNode( key, newitem )
            taller = True

        # Is the key already in the tree?
        elif key == subtree.key:
            return ( subtree, False )

        # navigate to the left.
        elif key < subtree.key:
            (subtree.left, taller) = self._avlInsert( subtree.left, key, newitem )
            #print subtree.key, subtree.left, subtree.right
            if taller:
                if subtree.bfactor == LEFT_HIGH:
                    subtree.left = self._avlLeftBalance( subtree )
                    taller = False
                elif subtree.bfactor == EQUAL_HIGH:
                    subtree.bfactor = LEFT_HIGH
                    taller = True
                else:
                    subtree.bfactor = EQUAL_HIGH
                    taller = False
        # Otherwise, navigate to the right.
        elif key > subtree.key:
            (subtree.right, taller) = self._avlInsert( subtree.right, key, newitem )
            #print subtree.key, subtree.left, subtree.right
            if taller:
                if subtree.bfactor == LEFT_HIGH:
                    subtree.bfactor = EQUAL_HIGH
                    taller = False
                elif subtree.bfactor == EQUAL_HIGH:
                    subtree.bfactor = RIGHT_HIGH
                    taller = True
                else:
                    subtree.right = self._avlRightBalance( subtree )
                    taller = False
        return ( subtree, taller )

# Storage class for creating the AVL tree node.
class _AVLMapNode:
    def __init__( self, key, value ):
        self.key = key
        self.value = value
        self.bfactor = EQUAL_HIGH
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
    stu_map = AVLMap()
    id_list = [60, 12, 90, 4, 41, 71, 100, 1, 29, 84, 23]
    name_list = ['Lee', 'Ryuka', 'James', 'Bell', 'Modric', \
                 'Gece', 'Huang', 'ZZ', 'GaoL', 'Rene', \
                 'Diamond']
    #stu_map.add( id_list[0], name_list[0] )
    #stu_map.add( id_list[1], name_list[1] )
    #stu_map.add( id_list[2], name_list[2] )
    for i in range( len(id_list) ):
        key = id_list[i]
        value = name_list[i]
        #print key, value
        stu_map.add( key, value )
        #print stu_map._root.key
        #print key, stu_map.valueOf( key )

    for i in range( len(id_list) ):
        key = id_list[i]
        value = name_list[i]
        print key, value
        node = stu_map._bstSearch( stu_map._root, key )
        node_left = node.left
        node_right = node.right
        if node_left is not None:
            print '<-', node_left.key, node_left.value
        if node_right is not None:
            print '->', node_right.key, node_right.value
    #stu_map.add( 37, 'ZXR')

    print '========================================='
    print 'all added: '
    print 'length of the map: ',
    print len(stu_map)
    #for key in stu_map:
    #    print key, stu_map.valueOf( key ) 

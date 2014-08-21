# The storage class for creating binary tree nodes.
class BinTreeNode:
    def __init__( self, data ):
        self.data = data
        self.left = None
        self.right = None
        
# ============ Depth-first traversal ===============
# 1. Preorder Traversal
def preorderTrav( subtree ):
    if subtree is not None:
        print subtree.data,
        preorderTrav( subtree.left )
        preorderTrav( subtree.right )

# 2. Inorder Traversal
def inorderTrav( subtree ):
    if subtree is not None:
        inorderTrav( subtree.left )
        print subtree.data,
        inorderTrav( subtree.right )

# 3. Postorder Traversal
def postorderTrav( subtree ):
    if subtree is not None:
        postorderTrav( subtree.left )
        postorderTrav( subtree.right )
        print subtree.data,

# ============ Breadth-first traversal ===============
def breadthFirstTrav( bintree ):
    from listqueue import Queue
    # Create a queue and add the root node to it.
    q = Queue()
    q.enqueue( bintree )

    # Visit each node in the tree.
    while not q.isEmpty():
        # Remove the next node from the queue and visit it.
        node = q.dequeue()
        print node.data,

        # Add the two children to the queue.
        if node.left is not None:
            q.enqueue( node.left )
        if node.right is not None:
            q.enqueue( node.right )

if __name__ == '__main__':
    root = BinTreeNode( 'A' )
    nodeB = BinTreeNode( 'B' )
    nodeC = BinTreeNode( 'C' )
    nodeD = BinTreeNode( 'D' )
    nodeE = BinTreeNode( 'E' )
    nodeF = BinTreeNode( 'F' )
    nodeG = BinTreeNode( 'G' )
    nodeH = BinTreeNode( 'H' )
    nodeI = BinTreeNode( 'I' )
    nodeJ = BinTreeNode( 'J' )

    root.left = nodeB
    root.right = nodeC
    nodeB.left = nodeD
    nodeB.right = nodeE
    nodeC.left = nodeF
    nodeC.right = nodeG
    nodeE.left = nodeH
    nodeG.left = nodeI
    nodeG.right = nodeJ

    print 'Preorder Traversal: '
    preorderTrav( root )
    print ''
    
    print 'Inorder Traversal: '
    inorderTrav( root )
    print ''

    print 'Postorder Traversal: '
    postorderTrav( root )
    print ''

    print 'Breadth-first Traversal: '
    breadthFirstTrav( root )
    print ''

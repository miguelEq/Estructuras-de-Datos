class Tree():
    def __init__(self,elem=None, right=None, leaf=None):
        self._nLeaf = leaf
        self._nRight = right
        self._node = elem
    @property
    def node(self):
        return self._node
    @node.setter 
    def node(self,value):
        self._node = value    
    @property    
    def right(self):
        return self._nRight     
    @property
    def leaf(self):
        return self._nLeaf
    def addRight(self,tree):
         self._nRight = tree 
    def addLeaf(self,tree):
         self._nLeaf = tree 
    def isLeaf(self,tree):
        if(tree.node != None and tree.isNil(tree.right) and tree.isNil(tree.leaf)):
            return True
        else:
            return False
    def isNil(self,tree):
        if(tree.node == None):
            return True
        else:
            return False 

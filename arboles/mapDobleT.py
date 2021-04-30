from tree import Tree

#type: (Tree) -> int
#Complejidad O(n)
def mapDobleT(tree):
    if(tree.isNil(tree)):
        return 
    if(tree.isLeaf(tree)):
        tree.node = tree.node * 2
        return
    tree.node = tree.node * 2        
    mapDobleT(tree.right)
    mapDobleT(tree.leaf)  
def printTree(tree):
    if(tree.isNil(tree)):
        print("nil")
        return
    if(tree.isLeaf(tree)):
        print("leaf")
        return    
    print("root {}".format(tree.node))
    print("child right")
    printTree(tree.right)
    print("child leaf")
    printTree(tree.leaf)
tree1=Tree(1,Tree(2,Tree(),Tree()),Tree(3,Tree(4,Tree(),Tree()),Tree(5,Tree(),Tree()))) 
printTree(tree1)
print("ejecuto mapDobleT")
mapDobleT(tree1)
printTree(tree1)
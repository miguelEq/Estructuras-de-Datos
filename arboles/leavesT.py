from tree import Tree

#type: (Tree) -> int
#Complejidad O(n)
def leavesT(tree):
    if(tree.isNil(tree)):
        return 0
    if(tree.isLeaf(tree)):
        return 1
    return leavesT(tree.right) + leavesT(tree.leaf)    

tree1=Tree(1,Tree(2,Tree(),Tree()),Tree(3,Tree(3,Tree(),Tree()),Tree(5,Tree(),Tree()))) 
print("Ejecuto leavesT  {}".format(leavesT(tree1)))                   

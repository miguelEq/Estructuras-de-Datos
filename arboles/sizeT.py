from tree import Tree

#type: (Tree) -> int
#Complejidad O(n)
def sizeT(tree):
    if(tree.isNil(tree)):
        return 0
    if(tree.isLeaf(tree)):
        return 1
    return 1 + sizeT(tree.right) + sizeT(tree.leaf)        

tree1=Tree(1,Tree(2,Tree(),Tree()),Tree(3,Tree(4,Tree(),Tree()),Tree(5,Tree(),Tree()))) 
print("size de un tree {}".format(sizeT(tree1)))

from tree import Tree

#type: (Tree) -> int
#Complejidad O(n)
def heightT(tree):
    if(tree.isNil(tree)):
        return 0
    if(tree.isLeaf(tree)):
        return 1
    return 1 + max(heightT(tree.right),heightT(tree.leaf))

tree1=Tree(1,Tree(2,Tree(),Tree()),Tree(3,Tree(3,Tree(),Tree()),Tree(5,Tree(),Tree()))) 
print("Ejecuto heightT  {}".format(heightT(tree1)))                   


from tree import Tree

#type: (Tree) -> List[]
#Complejidad O(n)
def treeToList(tree):
    if(tree.isNil(tree)):
        return []
    if(tree.isLeaf(tree)):
        return [tree.node]
    return treeToList(tree.leaf) + [tree.node] + treeToList(tree.right)


tree1=Tree(1,Tree(2,Tree(),Tree()),Tree(3,Tree(4,Tree(),Tree()),Tree(5,Tree(),Tree()))) 
print("Ejecuto treeToList  {}".format(treeToList(tree1)))                   

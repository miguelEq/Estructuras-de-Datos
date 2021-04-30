from tree import Tree

#type: (Tree,elem) -> int
#Complejidad O(n)
def aparicionesT(tree,x):
    if(tree.isNil(tree)):
        return 0
    if(tree.isLeaf(tree)):
        if(tree.node == x):
            return 1
        else:
            return 0
    if(tree.node == x):
        return 1 + aparicionesT(tree.right,x) + aparicionesT(tree.leaf,x) 
    else:
        return aparicionesT(tree.right,x) + aparicionesT(tree.leaf,x) 

tree1=Tree(1,Tree(2,Tree(),Tree()),Tree(3,Tree(3,Tree(),Tree()),Tree(5,Tree(),Tree()))) 
print("Ejecuto aparicionesT  {}".format(aparicionesT(tree1,3)))                   
           
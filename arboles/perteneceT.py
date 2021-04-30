from tree import Tree

#type: (Tree,elem) -> bool
#Complejidad O(n)
def perteneceT(tree,x):
    if(tree.isNil(tree)):
        return False
    if(tree.isLeaf(tree)):
        return tree.node == x 
    if(tree.node == x):
        return True
    else:
        return perteneceT(tree.right,x) or perteneceT(tree.leaf,x)
        
tree1=Tree(1,Tree(2,Tree(),Tree()),Tree(3,Tree(4,Tree(),Tree()),Tree(5,Tree(),Tree()))) 
print("Ejecuto pertenceT a tree el elemento {}".format(perteneceT(tree1,31)))
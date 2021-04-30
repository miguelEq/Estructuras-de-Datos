from tree import Tree

#type: (Tree) -> int
#Complejidad O(n)
def suma(tree):
    if(tree.isNil(tree)):
        return 0
    if(tree.isLeaf(tree)):
        return tree.node    
    return tree.node + suma(tree.right) + suma(tree.leaf)

tree1=Tree(1,Tree(2,Tree(),Tree()),Tree(3,Tree(4,Tree(),Tree()),Tree(5,Tree(),Tree()))) 
print("Suma de un tree {}".format(suma(tree1)))

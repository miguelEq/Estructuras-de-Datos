from tree import Tree
#type: (Tree) -> List[List[]]
#Complejidad O(n.m) n recorro todo el arbol y m la cantidad de veces que llamo a addToAlllists
def todosLosCaminos(tree):
    if(tree.isNil(tree)):
        return []
    if(tree.isLeaf(tree)):
        return [[tree.node]]
    izq=todosLosCaminos(tree.leaf)
    der=todosLosCaminos(tree.right) 
    return addToAlllists(izq + der,tree.node)
#Complejidad O(n)    
def addToAlllists(lss,x):
    if(lss == []):
        return []
    lsaux= lss[0] 
    lsaux.append(x)
    return [lsaux] + addToAlllists(lss[1:],x)              

tree1=Tree(1,Tree(2,Tree(6,Tree(),Tree()),Tree(7,Tree(),Tree())),Tree(3,Tree(4,Tree(),Tree()),Tree(5,Tree(),Tree()))) 
print("Ejecuto todosLosCaminos  {}".format(todosLosCaminos(tree1)))                   

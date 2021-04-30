from tree import Tree

#type: (Tree,int) -> List[]
#Devuelve los elementos en el nivel n en una lista,root es level 0
#Complejidad O(n)
def levelN(tree,n):
    if(tree.isNil(tree)):
        return []
    if(n==0):
       return [tree.node]
    else:
       return levelN(tree.right,n-1) + levelN(tree.leaf,n-1) 

tree1=Tree(1,Tree(2,Tree(),Tree()),Tree(3,Tree(4,Tree(),Tree()),Tree(5,Tree(),Tree()))) 
print("Ejecuto levelN  {}".format(levelN(tree1,2)))                   


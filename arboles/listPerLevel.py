from tree import Tree
from levelN import levelN
from heightT import heightT
#type: (Tree) -> List[List]
#Devuelve una lista  por cada level del arbol
#Complejidad O(n*m)  listPerLevelAux cuesta mas que heightT
def listPerLevel(tree):
    return listPerLevelAux(tree,heightT(tree)-1)
#Complejidad O(n*m) m es la cantidad de niveles y n es lo que cuesta levelN
def listPerLevelAux(tree,n):
     if(n== -1):
         return []
     return listPerLevelAux(tree,n-1) + [levelN(tree,n)]     

tree1=Tree(1,Tree(2,Tree(),Tree()),Tree(3,Tree(4,Tree(),Tree()),Tree(5,Tree(),Tree()))) 
print("Ejecuto listPerLevel  {}".format(listPerLevel(tree1)))                   

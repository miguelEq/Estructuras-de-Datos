from tree import Tree
#type: (Tree) -> List[]
#Devuelve una lista con los elementos de la rama mas larga
#Complejidad O(n)
def ramaMasLarga(tree):
    return ramaMasLargaAux(tree,[])
def ramaMasLargaAux(tree,ls):
      if(tree.isNil(tree)):
          return ls
      if(tree.isLeaf(tree)):
          return ls + [tree.node]
      izq = ramaMasLargaAux(tree.leaf,ls + [tree.node]) 
      der = ramaMasLargaAux(tree.right,ls + [tree.node])
      if(len(izq)> len(der)):
          return izq
      else:
          return der

tree1=Tree(1,Tree(2,Tree(4,Tree(6,Tree(),Tree(7,Tree(),Tree())),Tree()),Tree()),Tree(3,Tree(4,Tree(),Tree()),Tree(5,Tree(),Tree()))) 
print("Ejecuto ramaMasLarga  {}".format(ramaMasLarga(tree1)))                   

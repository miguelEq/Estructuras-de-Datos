#type: (list[int]) -> int
#Precondicion: Al menos hay 1 elemento
#Complejidad O(n)
def minimo(ls):
    if(len(ls) == 1):
        return ls[0]
    return min(ls[0],minimo(ls[1:]))    
#Complejidad O(n)
def minimoImperativa(ls):
     m=ls[0]
     for elem in ls:
         if(m > elem):
             m= elem
     return m

lista=[5,4,3,2,1,2]

print("forma recursiva {} ".format(minimo(lista)))    

print("forma imperativa {} ".format(minimoImperativa(lista)))    

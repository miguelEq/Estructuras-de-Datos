#type: (list[elem],int) -> list[elem]
#Precondicion: n es menorigual a la longitud de la lista 
#Complejidad O(n)
def sinLosPrimeros(ls,n):
    if(n == 0):
        return ls
    return sinLosPrimeros(ls[1:],n-1)
#Complejidad O(n)
def sinLosPrimerosImperativa(ls,n):
     return ls[n:]

lista=[5,4,3,2,1,2]

print("forma recursiva {} ".format(sinLosPrimeros(lista,5)))    

print("forma imperativa {} ".format(sinLosPrimerosImperativa(lista,3)))    

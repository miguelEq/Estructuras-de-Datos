#type: (list[elem],int) -> list[elem]
#Precondicion: n es menorigual a la longitud de la lista 
#Complejidad O(n)
def losPrimeros(ls,n):
    if(n == 0):
        return []
    return [ls[0]] + losPrimeros(ls[1:],n-1)
#Complejidad O(n)
def losPrimerosImperativa(ls,n):
    lsres=[]
    for i in range(0,n):
        lsres.append(ls[i])
    return lsres    

lista=[5,4,3,2,1,2]

print("forma recursiva {} ".format(losPrimeros(lista,5)))    

print("forma imperativa {} ".format(losPrimerosImperativa(lista,3)))    

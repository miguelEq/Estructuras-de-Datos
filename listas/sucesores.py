# type: (list[int]) -> list[int]
#Compeljidad O(n)
def sucesores(ls):
    if([]== ls):
        return []
    return [ls[0] + 1 ] + sucesores(ls[1:])
#Compeljidad O(n)
def sucesoresImperativa(ls):
    lsres=[]
    for i in ls:
        lsres.append(i + 1)
    return lsres    

lista=[1,2,3,4,5,6,7,8,9,10]    

print("forma recursiva {} ".format(sucesores(lista)))    

print("forma imperativa {} ".format(sucesoresImperativa(lista)))    

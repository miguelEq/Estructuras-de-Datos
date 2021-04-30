#type: (list[]) -> list[]
#Complejidad O(n)
def reversa(ls):
    if(ls == []):
        return ls
    return reversa(ls[1:]) + [ls[0]] 
#Complejidad O(n)
def reversaImperativa(ls):
    lsres=[]
    for i in range(0,len(ls)):
        lsres.append(ls[len(ls)-(i+1) ]) 
    return lsres    

lista=[1,2,3,4,5,4,6]

print("forma recursiva {} ".format(reversa(lista)))    

print("forma imperativa {} ".format(reversaImperativa(lista)))    

 
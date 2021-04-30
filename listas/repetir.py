#type: (elem,int) -> list[elem]
#Complejidad O(n)
def repetir(n,a):
    if(a==0):
        return []
    return [n] + repetir(n,a-1) 
#Complejidad O(n)
def repetirImperativa(n,a):
    lsres=[]
    for i in range(0,a):
        lsres.append(n)
    return lsres    

print("forma recursiva {} ".format(repetir(4,5)))    

print("forma imperativa {} ".format(repetirImperativa(6,3)))    
   
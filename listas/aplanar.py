# type: (list[list]) -> list
#Complejidad  O(n)
def aplanar(lss):
    if(lss == []):
        return []
    return lss[0] + aplanar(lss[1:])     
#Complejidad  O(n)
def aplanarImperativa(lss):
    lsres=[]   
    for ls in lss:
        lsres += ls
    return lsres

lista=[[1,2,3],[4,5,6],[7,8,9]]

print("forma recursiva {} ".format(aplanar(lista)))    

print("forma imperativa {} ".format(aplanarImperativa(lista)))    

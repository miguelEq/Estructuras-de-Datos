# type: (list[int],int) -> list[int]
#Complejidad O(n) 
def menoresA(ls,elem):
    if(ls == []):
        return []
    if(ls[0] < elem):
        return [ls[0]] + menoresA(ls[1:],elem)
    else:
        return menoresA(ls[1:],elem)       
#Complejidad O(n) 
def menoresAImperativa(ls,elem):
    lsres=[]
    for e in ls:
        if(e < elem):
            lsres.append(e)
    return lsres        

lista=[1,2,3,4,5,4,6]

print("forma recursiva {} ".format(menoresA(lista,55)))    

print("forma imperativa {} ".format(menoresAImperativa(lista,4)))    

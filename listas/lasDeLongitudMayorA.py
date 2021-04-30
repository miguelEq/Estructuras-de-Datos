# type: (list[list],int) -> list[list]
#Complejidad O(n)
def lasDeLongitudMayorA(lss,size):
    if(lss == []):
        return []
    if(len(lss[0]) > size):
        return [lss[0]] + lasDeLongitudMayorA(lss[1:],size)
    else:
        return lasDeLongitudMayorA(lss[1:],size)
#Complejidad O(n)
def lasDeLongitudMayorAImperativa(lss,size):
     lssres=[]
     for ls in lss:
         if(len(ls) > size):
             lssres.append(ls)
     return lssres        

lista=[[1,2,3],[4],[5,4],[6]]

print("forma recursiva {} ".format(lasDeLongitudMayorA(lista,2)))    

print("forma imperativa {} ".format(lasDeLongitudMayorAImperativa(lista,4)))    
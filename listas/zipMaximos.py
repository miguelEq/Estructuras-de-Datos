#type: (list[],list[]) -> list[]
#Dadas dos listas de enteros, devuelve una lista donde el elemento en la posicion n 
# es el máximo entre el elemento n de la primera lista y de la segunda lista, teniendo 
# en cuenta que las listas no necesariamente tienen la misma longitud.
#Complejidad O(n)
def zipMaximos(ls1,ls2):
    if(ls1 == []):
        return ls2
    elif(ls2 == []):
        return ls1
    elif(ls1[0] > ls2[0]):
        return [ls1[0]] + zipMaximos(ls1[1:],ls2[1:])
    else:
        return [ls2[0]] + zipMaximos(ls1[1:],ls2[1:])
#Complejidad O(n)
def zipMaximosImperativa(ls1,ls2):
    lsres=[]
    if(len(ls1) > len(ls2)):
        for i in range(0,len(ls2)):
            if(ls1[i] > ls2[i]):
                lsres.append(ls1[i])
            else:    
                lsres.append(ls2[i])
        return lsres + ls1[len(ls2):]
    else:  
        for i in range(0,len(ls1)):
            if(ls1[i] > ls2[i]):
                lsres.append(ls1[i])
            else:    
                lsres.append(ls2[i])
        return lsres + ls2[len(ls1):]

lista=[1,2,3,4,5,4,6]
lista2=[5,4,3,2,1]

print("forma recursiva {} ".format(zipMaximos(lista,lista2)))    

print("forma imperativa {} ".format(zipMaximosImperativa(lista,lista2)))    

# type: (list[],elem) -> bool
#Complejidad O(n)
def apariciones(ls,elem):
    if(ls == []):
        return 0
    if(ls[0] == elem):
        return 1 + apariciones(ls[1:],elem)
    else:
        return apariciones(ls[1:],elem)
#Complejidad O(n)
def aparicionesImperativa(ls,elem):
    cant=0
    for e in ls:
        if(e == elem):
            cant += 1
    return cant 

lista=[1,2,3,4,5,4,6]

print("forma recursiva {} ".format(apariciones(lista,55)))    

print("forma imperativa {} ".format(aparicionesImperativa(lista,4)))    





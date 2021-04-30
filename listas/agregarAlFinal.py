# type: (list[],elem) -> list[]
#Complejidad O(n)
def agregarAlFinal(ls,elem):
    return ls + [elem] 
#Complejidad O(n)
def agregarAlFinalImperativa(ls,elem):     
    return ls + [elem]

lista=[1,2,3,4,5,4,6]

print("forma recursiva {} ".format(agregarAlFinal(lista,55)))    

print("forma imperativa {} ".format(agregarAlFinalImperativa(lista,4)))    

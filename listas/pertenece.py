# type: (list[],elem) -> bool
#Complejidad  O(n)
def pertenece(ls,elem):
     if(ls == []):
         return False
     if(ls[0] == elem):
         return True
     else:
         return pertenece(ls[1:],elem) 
#Complejidad  O(n)
def perteneceImperativa(ls,elem):
    index=0
    while(index < len(ls) and ls[index] != elem):
        index += 1                
    return index != len(ls)


lista=[1,2,3,4,5,6,7,8,9,10]    

print("forma recursiva {} ".format(pertenece(lista,55)))    

print("forma imperativa {} ".format(perteneceImperativa(lista,6)))    

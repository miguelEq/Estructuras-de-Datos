# type: (list[int]) -> int
#Compeljidad O(n)
def longitud(ls):
    if(ls == []):
        return 0
    return 1 + longitud(ls[1:])
#Compeljidad O(n)
def longitudImperativa(ls):
    size=0
    for i in ls:
        size += 1
    return size    

lista=[1,2,3,4,5,6,7,8,9,10]    

print("forma recursiva "+ str(longitud(lista)))    

print("forma recursiva "+ str(longitudImperativa(lista)))    

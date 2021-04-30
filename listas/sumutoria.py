# type: (list[int]) -> int
#Compeljidad O(n) 
def sumatoria(ls):
    if(ls == []):
        return 0
    return ls[0] + sumatoria(ls[1:]) 
#Compeljidad O(n)
def sumatoriaImperativa(ls):
    res=0
    for i in ls:
      res += i 
    return res   

lista=[1,2,3,4,5,6,7,8,9,10]    

print("forma recursiva "+ str(sumatoria(lista))) 

print("forma imperativa "+ str(sumatoriaImperativa(lista))) 

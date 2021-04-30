#type: (int) -> int
#Complejidad O(n)
def cuentaRegresiva(n):
    if(n == 0):
        return []
    return [n] + cuentaRegresiva(n-1)
#Complejidad O(n)
def cuentaRegresivaImperativa(n):
    lsres=[]
    for i in range(0,n):
      lsres.append(n-i)
    return lsres 

print("forma recursiva {} ".format(cuentaRegresiva(4)))    

print("forma imperativa {} ".format(cuentaRegresivaImperativa(6)))    

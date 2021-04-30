# type: (list[bool]) -> bool
# Todos los elementos son True
#Compeljidad O(n)
def conjuncion(ls):
    if(ls == []):
        return True
    return ls[0] and conjuncion(ls[1:])
#Compeljidad O(n)
def conjuncionImperativa(ls):
    index=0
    res=True
    while(index < len(ls) and res):
        res = ls[index]
        index += 1
    return index == len(ls)    

listaF=[True,False,True]
listaT=[True,True,True]

print("forma recursiva {} ".format(conjuncion(listaF)))    
print("forma recursiva {} ".format(conjuncion(listaT)))    

print("forma imperativa {} ".format(conjuncionImperativa(listaF)))    
print("forma imperativa {} ".format(conjuncionImperativa(listaT)))    

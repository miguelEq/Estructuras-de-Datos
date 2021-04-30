# type: (list[bool]) -> bool
# algun elemento es True
#Compeljidad O(n)
def disyuncion(ls):
    if(ls == []):
        return False
    if (ls[0]):
        return ls[0] 
    else:
        return disyuncion(ls[1:])
#Compeljidad O(n)
def disyuncionImperativa(ls):
    index=0
    while(index < len(ls) and not(ls[index])):
        index += 1
    return index != len(ls)

listaT=[False,False,True] 
listaF=[False,False,False]

print("forma recursiva {} ".format(disyuncion(listaF)))    
print("forma recursiva {} ".format(disyuncion(listaT)))    

print("forma imperativa {} ".format(disyuncionImperativa(listaF)))    
print("forma imperativa {} ".format(disyuncionImperativa(listaT)))    


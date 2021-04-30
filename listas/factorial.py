#type: (int) -> int
#Complejidad O(n)
def factorial(n):
    if(n == 0):
        return 1
    return n*factorial(n-1)
#Complejidad O(n)
def factorialImperativa(n):
    res=n
    if(n == 0):
        return 1
    for e in range(1,n):
        res = res * (n-e)
    return res

print("forma recursiva {} ".format(factorial(4)))    

print("forma imperativa {} ".format(factorialImperativa(3)))    

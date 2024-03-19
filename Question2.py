#Resultado si utilizar recursividad
"""
n=int(input("Introduzca un numero para calcular su factorial"))
factorial=1
for i in range(1,n+1):
    factorial*=i

"""



#print(factorial)
    
def factorialnum(number):
        if number ==0:
              return 1
        return number * factorialnum(number-1)

print(factorialnum(8))

def binarioDecimal(n):
    ns=str(n)
    nsr=len(ns)-1
    valor=0
    for numero in ns:
        if numero=='1':
            valor+=2**nsr
        nsr-=1
    return valor 
        
txt=input("Introduzca unos numeros en binario separados por , para comprobar si son divisibles por 5: ")
l=txt.split(",")
d=[]
for n in l:
    if binarioDecimal(n)%5==0:
        d.append(n)

for n in d:
    print(n)
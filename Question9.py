l=[]
contador=0
while True:
    s=input("Introduce una frase: ")
    if s:
        l.append(s.upper())
        contador+=1
    else:
        break

for i in range(contador):
    print(l[i])

for frase in l:
    print(frase)
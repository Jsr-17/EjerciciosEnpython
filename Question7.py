txt=input("Tamano del array separado por ,")
l=txt.split(",")
x=int(l[0])
y=int(l[1])
arraybi=[
    [ 7 for columna in range(y)]for fila in range(x)
]

for t in range(x):
    for z in range(y):
        arraybi[t][z]=t*z
arraybi.append("hola")
arraybi.insert(1,"Soy jose")
print(arraybi)
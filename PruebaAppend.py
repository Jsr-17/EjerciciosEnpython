#El Sentido de esta funcion es el poder incluir una serie de datos en una lista de manera ordenada 
def modificarAppend(n,l,datos):
    for i in range(n+1):
        l.append(datos[i])

l=["PrimerDato","Segundo Dato"]
datos=[12,32,4,123,76,45]
modificarAppend(5,l,datos)
l.append("Ultimo dato")
print(l)
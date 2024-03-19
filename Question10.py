txt=input("Introduce una frase separada por espacios ordenare las palabras alfabeticamente: ")
l=txt.split(" ")
l.sort()

for palabra in l:
    print(palabra, end=" ")
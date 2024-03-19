array=[]
count=0
for i in range(2000,3200):
    if i%7==0 and i%5!=0:
        print(i)
        array.insert(count,i)
        count+=1
print(array)
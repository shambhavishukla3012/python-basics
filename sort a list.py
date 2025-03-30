l=[25,45,78,59,88,45]
for i in range(0,6):
    for j in range(i+1,6):
        if l[i]>l[j]:
         temp=l[i]
         l[i]=l[j]
         l[j]=temp
print(l)

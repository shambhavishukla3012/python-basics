l=[25,45,78,59,88888,45]
sort=[]
for i in range(0,5):
    for j in range(i+1,5):
        if l[i]>l[j]:
         temp=l[i]
        else:
         temp=l[j]
         sort=[temp]
print(sort)

a=int(input())
c=0
if(a>=1):print(2)
for i in range(0,100*a):
    if(c<a-1):
        for j in range(2,i):
            if(i%j==0):
             break
            if(j==i-1):
                print(i)
                c=c+1

n=int(input())
s=0
while(n!=0):
    t=n%10
    s=s*10+t
    n=n//10
print("reverse of no. is ",s)

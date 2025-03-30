#sum of digits of a number
print("ENTER THE NUMBER")
n=int(input())
s=0
while(n>0):
    t=n%10
    s=s+t
    n=int(n/10)
print("SUM OF DIGITS IS",s) 

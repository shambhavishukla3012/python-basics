#product of digits of a number
print("ENTER THE NUMBER")
n=int(input())
s=1
while(n>0):
    t=n%10
    s=s*t
    n=int(n/10)
print("PRODUCT OF DIGITS IS",s)

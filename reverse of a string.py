# TO REVERSE A STRING
str=input()
l=len(str)
rev=""
while(l>0):
    rev=rev+str[l-1]
    l=l-1
print(rev)

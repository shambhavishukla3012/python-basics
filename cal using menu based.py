''' This program uses menu based calling '''
print("1. add")
print("2. subtract")
print("3. multiply")
print("4. division")
c=int(input())
a=int(input("first no. : "))
b=int(input("second no. : "))
if(c==3):
   mult=a*b
   print(mult)
elif(c==4):
   div=a/b
   print(div)
elif(c==1):
   add=a+b
   print(add)
elif(c==2):
   sub=a-b
   print(add)

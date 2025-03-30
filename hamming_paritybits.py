a = input('enter a eight digit bianry no. = ')

l = len(a)

z=[]
x=[]
c=[]
v=[]

s={}
p1=''
p2=''
p4=''
p8=''
s[0]=p1
s[1]=p2
s[3]=p4
s[7]=p8

s[2]=a[0]
s[4]=a[1]
s[5]=a[2]
s[6]=a[3]

j=8
for i in range(4,l-1):
    s[j]=a[i]
    j=j+1
    i=i+1

'''for p1'''
q=2
while q<l:
    z.append(a[q])
    q=q+2
print('First: ')
print(z.count('1'))

'''for second parity bit'''
w=6
x.append(a[2])
while w<l:
    x.append(a[w])
    x.append(a[w+1])
    w=w+3
print('Second: ')
print(x.count('1'))


'''for third parity bit'''
w=12
c.append(a[4])
c.append(a[5])
c.append(a[6])
while w<=l:
    c.append(a[w])
    c.append(a[w+1])
    c.append(a[w+2])
    c.append(a[w+3])
    c.append(a[w+4])

    w=w+4
print('Third: ')
print(c.count('1'))

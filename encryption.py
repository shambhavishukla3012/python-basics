''' ENTER A SENTENCE TO ENCRYPT -> IT WILL BE ENCRYPTED AND WILL BE SAVED TO A FILE NAME encrypt.txt'''
a=" "
a=(input("\nENTER THE SENTENCE : "))
l = len(a)
x=" "

file=open('encrypt.txt','w+')

''' ENCRYPTION'''
def encryption(x):
        n=0
        i=0
        y=" "
        d=" "

        for i in range(l):
            n=ord(a[i])              # ord(a): converting alphabet to ASCII code
            n=n+2
            d = d+chr(n)         # chr(n): converting ASCII code to corresponding alphabet
        print('encrypted form -',d)
        file.write(d)
        file.close()

def decryption():
        file=open('encrypt.txt','r+')
        z=file.read()
        j=1
        e=''

        for j in range(l+1):
            n=ord(z[j])
            n=n-2
            e=e+chr(n)
        print('after decryption - ',e)

#calling the function
encryption(a)
decryption()

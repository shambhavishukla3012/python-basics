m = int(input("\nmesage : "))
p=int(input("enter value of 'p': "))
q=int(input("enter the value of 'q': "))

N=p*q #public key
phiN=(p-1)*(q-1)
print("phiN = ",phiN)

1<e<phiN
e=17 #public key......it should be random but i have fixed its value

k=1
d=((k*phiN)+1)/e
#we repeat following if statement until value of 'd' becomes an integer
if(d%1!=0):
    # to make value of d an integer we every time increment value of k by 1............ it's in the formula
    while(d%1!=0):
        k=k+1
        d=((k*phiN)+1)/e

print("numeric msg",m)
print("public key are e=",e,"N=",N)

# c - cipher that is encoded text
c=(m**e)%N
print("encrypted msg is ",c)
print("private key is ",d)
dn=int(d) # it's just to convert data type of d to int....so i have declared new variable

M=(c**dn)%N
print("decrypted msg is ",M)


def ipalindrome(a):
    b=len(a)

    i=0
    c=0
    for i in range(int(b/2)):
           if a[i] == a[-1-i]:
             c=c+1
           else:
             print('NOT A')
             break

    if c == b/2 or  b/2-1:
     print('PALINDROME')


a=input("ENTER THE STRING :-")
ipalindrome(a)

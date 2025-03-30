i = input('ENTER THE WORD = ')
''' IT USES DATA FROM data.py FILE'''
from data import*

if i in word:
    print(word[i])
else:
    print('SORRY WORD NOT FOUND')

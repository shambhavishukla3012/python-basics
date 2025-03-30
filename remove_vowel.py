def disemvowel(string):
  vowel = ['a','e','i','o','u']
  for i in range(len(string)):
      for j in range(5):
          if string[i] in vowel[j]:
              string = string.replace(string[i]," ")
  print(string)

string = input("Enter the string : ")
disemvowel(string)

a=input()

li=['a','e','i','o','u']

if a.isalpha():
  if a in li:
    print("Vowel")
  else:
    print("Consonant")
elif a.isalpha()==False:
  print("invalid")

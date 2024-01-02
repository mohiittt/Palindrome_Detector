import os, time

def palindrome(word):
  if len(word)<=1:
    return True
  if word[0] != word[-1]:
    return False
  return palindrome(word[1:-1])

while True:
  word = input("Input a word : ")
  print()
  if palindrome(word) == True:
    print("Yes! It's a Palindrome.")
  else:
    print("It's not a Palindrome.")
  time.sleep(1)  
  os.system("clear")
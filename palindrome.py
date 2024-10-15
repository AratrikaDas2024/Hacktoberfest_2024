def check_palindrome(word):
     
     s = word[::-1]
     print(s)
     if s==word:
         return 1
     else:
         return 0

status=check_palindrome("malayalam")
if(status):
     print("word is palindrome")
else:
     print("word is not palindrome")

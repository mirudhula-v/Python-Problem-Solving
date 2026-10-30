#Length of a string
n=input()
print(len(n))
#Join the strings
n=input()
m=input()
print(n,m,end=" ")
#Compare the Strings
n=input()
m=input()
if n==m:
  print("true")
else:
  print("false")
#First character of a string
n=input()
print(n[0])
#Last character of a string
n=input()
print(n[-1])
#Join first & last characters of a string
n=input()
print(n[0],end="")
print(n[-1],end="")
#Alphanumeric strings
n=input()
alphacount=numcount=False
for m in n:
  if m.isalpha():
    alphacount=True
  elif m.isdigit():
    numcount=True
  if numcount and alphacount:
    break
if alphacount>0 and numcount>0:
  print("true")
else:
  print("false")
#Uppercase check
n=input()
if n.isupper():
  print("true")
else:
  print("false")
#Lowercase check
n=input()
if n.islower():
  print("true")
else:
  print("false")
#String lengths equal or not
n=input()
m=input()
if len(n)==len(m):
  print("true")
else:
  print("false")
#Reverse a string
n=input()
print(n[::-1])
#Split strings by comma
n=input()
m=n.split(",")
for col in m:
  print(col)
#Remove vowels
string = input()

vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
result = ""

for i in range(len(string)):
    if string[i] not in vowels:
        result = result + string[i]

print(result)
#Reverse the character case
n=input()
print(n.swapcase())
#Print ascii value
n=input()
print(ord(n))
#Remove occurrences of a char
n=input()
m=input()
print(n.replace(m,""))
#Search for a word
n=input()
m=input ()
print("true" if m in n else "false")
#Count vowels and consonants
n=input()
vow=0
con=0
for i in n:
  if i in "aeiouAEIOU":
    vow+=1
  else:
    con+=1
print(vow) 
print(con)
#Anagram check
n=input().lower().replace(" ","")
m=input().lower().replace(" ","")
if (len(n)!=len(m)):
  print("false")
elif sorted(n)==sorted(m):
  print("true")
else:
  print("false")
#Palindrome check
n=input()
if n==n[::-1]:
  print("true")
else:
  print("false")

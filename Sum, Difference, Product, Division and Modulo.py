a,b=map(int,input().split())
print(a+b)
print(a-b)
print(a*b)
print(int(a/b))
if a<0 or b<0:
  c=abs(a)%abs(b)
  print(-1*c)
else:
  print(a%b)

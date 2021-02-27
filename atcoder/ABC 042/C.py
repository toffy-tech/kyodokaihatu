n,k=map(int,input().split())
a=0

dd=list(map(int,input().split()))


for i in range(n,10000):
  t=0
  for j in range(k):
    if str(dd[j]) not in str(i):
      t+=1

  if t==k:
    a=i
    break

print(a)
n,l=map(int,input().split())
ss=[]

for i in range(n):
  ss.append(input())

ss.sort()

print("".join(ss))
a=[]
A=0
B=0
x=0

while True:
  e=input("数字を入力してください:")
  if e=="":
    break
  else:
    a.append(int(e))

a.sort()
a.reverse()

if len(a)%2==1:
  a.append(0)

while True:
  A+=a[x]
  x+=1
  B+=a[x]
  x+=1
  if x==len(a):
    break

print(str(A-B))
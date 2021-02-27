tt=[0]
xx=[0]
yy=[0]
a=0

n=int(input("N="))

for i in range(n):
  t,x,y=map(int,input().split())
  tt.append(t)
  xx.append(x)
  yy.append(y)

for i in range(n):
  x=abs(xx[i+1]-xx[i])
  y=abs(yy[i+1]-yy[i])
  total=x+y
  time=tt[i+1]-tt[i]
  if total<=time:
    if total%2==time%2:
      pass
    else:
      a=1
      break
  else:
    a=1
    break

if a==0:
  print("Yes")
else:
  print("No")
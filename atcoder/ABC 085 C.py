import time
n=int(input("N="))
y=int(input("Y="))
t1=time.time()
t=[-1,-1,-1]
z=0

for i in range(100):
  for j in range(200):
    k=n-i-j
    if 0<=k:
      x=i*10000+j*5000+k*1000
      if y==x:
        t[0]=i
        t[1]=j
        t[2]=k
        z=1
        break
  if z==1:
    break

t2=time.time()
print(t)
print(str(t2-t1))

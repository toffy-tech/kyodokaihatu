n=int(input("N="))
a=int(input("A="))
b=int(input("B="))
t=0

for i in range(1,n+1):
  z=i
  x=0
  for j in range(1,4):
    x=x+z%10**j
    z=z//10
    if z==0:
      if a<=x and x<=b:
        t=t+i
      break

print(t)
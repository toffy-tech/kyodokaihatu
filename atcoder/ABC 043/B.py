a=[]
b=[]

for i in range(10):
  s=str(input())
  if s=="0" or s=="1":
    a.append(s)
    b.append(s)
  elif s=="B":
    try:
      a.pop()
    except IndexError:
      pass
    b.append(s)
  elif s=="":
    break
  else:
    print("No")
  print("".join(a))

print("".join(b))
    
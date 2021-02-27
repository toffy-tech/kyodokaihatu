s=input("S=")
s=s[::-1]
aa=["dream", "dreamer", "eraser", "erase"]
i=0

while i!=len(aa):
  ab=aa[i]
  ab=ab[::-1]

  try:
    t=s.index(ab)
  except ValueError:
    i+=1
    continue

  if t==0:
    s=s[len(ab):]
    i=-1
  i+=1
  

print(len(s)==0)
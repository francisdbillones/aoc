t = open(0).read()
a,b=t.split('\n\n')
from collections import defaultdict
T = defaultdict(list)
for x in a.splitlines():
 A,B=x.split('|')
 T[int(B)].append(int(A))

s=0
for x in b.splitlines():
 x=eval(x)
 t=T.copy()
 g=set()
 for e in x:
  if e in g:
   break
  g.update(set(t[e]) - g)
 else:
  s+=x[len(x)//2]

print(s)

s=0
for x in b.splitlines():
 *x,=eval(x)
 t=T.copy()
 g=defaultdict(list)
 f=0
 for i, e in enumerate(x):
  if e in g:
   x.insert(min(map(x.index,g[e])), x.pop(i))
   f=1
  for p in t[e]:
   g[p] += e,
 s+=f*x[len(x)//2]

print(s)

a = int(raw_input())
b = int(raw_input())
c=list(str(a))
e=b
while e>0:
    e=e-1
    del(c[e])
print(''.join(c))

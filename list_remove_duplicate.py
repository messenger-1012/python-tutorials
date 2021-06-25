a=list(map(str,input().rstrip().split()))
b=[]
print(a)
for i  in a:
    count=0
    if i not in b:
        b.append(i)
print(b)        
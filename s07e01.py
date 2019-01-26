a=list(map(str,input().split()))
n=a[0]
k=int(a[1])
res=''
for i in range(0,k):
    res=res+n[i]
print(res)

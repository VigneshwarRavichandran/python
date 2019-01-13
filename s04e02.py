a=input()
n=len(a)
count=1
for i in range(0,n):
    b=ord(a[i])
    if(b==32):
        count=count+1
print(count)

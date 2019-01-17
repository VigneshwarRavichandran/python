n=int(input())
k=int(input())
count=0
a_ip=list(map(int,input().split()))
for i in range(0,len(a_ip)):
    if(a_ip[i]==k):
        count=count+1
if(count>0):
    print("yes")
else:
    print("no")

a=int(input())
count=0
for i in range(1,11):
    if(i==a):
        count=count+1
if(count==0):
    print("no")
else:
    print("yes")

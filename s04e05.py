a=input()
count=0
for i in range(0,len(a)):
    if a[i].isnumeric() :
        count=count+1
print(count)

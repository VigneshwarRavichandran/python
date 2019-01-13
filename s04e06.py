a=input()
count=0
for i in range(0,len(a)):
    if a[i].isnumeric()==False :
        if a[i].isalpha()==False :
            count=count+1
print(count)

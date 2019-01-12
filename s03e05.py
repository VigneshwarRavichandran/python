n=int(input())
arr = []
for j in range(0,n) :
    a=int(input())
    arr.append(a); 
arr.sort() 
temp=int((n+1)/2)
print(arr[temp])

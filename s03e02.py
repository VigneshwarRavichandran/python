n=int(input())
arr = []
for j in range(0,n) :
    a=int(input())
    arr.append(a); 
arr.sort() 
print(arr[n-1])

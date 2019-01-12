n=int(input())
arr = []
for j in range(0,n) :
    a=int(input())
    arr.append(a); 
arr.sort() 
for j in range(0,n) :
    print(arr[j])

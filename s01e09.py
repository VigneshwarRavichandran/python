import array
n=int(input())
k=int(input())
sum=0
arr = array.array('i', []) 
for j in range(0,n):
    a=int(input())
    arr.append(a);
for m in range(0,k):
    sum=int(sum+arr[m])
print(sum)
    

import array
a=int(input())
arr = array.array('i', []) 
for j in range(0,a):
    n=int(input())
    arr.append(n); 
for j in range(0,a):
    print(arr[j], end =" ") 
    print(j) 

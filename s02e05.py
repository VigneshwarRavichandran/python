a=int(input())
n=int(input())
value=a
for i in range(a+1,n):
    value=value+1
    if value%2==0 :
        print(value)

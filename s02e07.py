a=int(input())
check_val=a
b=len(str(a))
res=0
while a>=1 :
    temp_digit=a%10
    temp_val=temp_digit**b
    res=res+temp_val
    a=int(a/10)
if res==check_val :
    print("yes")
else :
    print("no")

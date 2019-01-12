m=int(input())
n=int(input())
for i in range(m+1,n) :
    res=0
    check_val=i
    b=len(str(i))
    while i>=1 :
      temp_digit=i%10
      temp_val=temp_digit**b
      res=res+temp_val
      i=int(i/10)
    if res==check_val :
      print(check_val)


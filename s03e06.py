n_input=int(input())
arr_sort = []
for j in range(0,n_input) :
    a=int(input())
    arr_sort.append(a); 
arr_sort.sort() 
for j in range(0,n_input) :
    print(arr_sort[j])

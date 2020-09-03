output_list=[]

binary_num=list(map(str,input().split(",")))

for i in binary_num:
    x=int(i,2)
    if not x%5:
        output_list.append(i)
print(output_list)

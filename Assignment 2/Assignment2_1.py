output_list=[]
for i  in range(1500,2701):
    if i%7==0 and i%5==0:
        output_list.append(i)
print(output_list)
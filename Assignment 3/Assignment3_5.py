input_str=['abc','xyz','aba','1221']
cnt=0

for i in input_str:
    if i[0]==i[-1]:
        cnt+=1
print(cnt)

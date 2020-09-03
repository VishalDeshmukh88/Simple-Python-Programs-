input_str=[]
digitcnt=0
lettercnt=0
input_str=input("")
for i in input_str:
    if i.isdigit():
        digitcnt+=1
    elif i.isalpha():
        lettercnt+=1

print("Letters ",lettercnt)
print("Digits ",digitcnt)     
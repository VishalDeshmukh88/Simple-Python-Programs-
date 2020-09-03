n=50
n1=0
n2=1
sum1=0
count=1

while count<=n:
    print(sum1,end=' ')
    count+=1
    n1=n2
    n2=sum1
    sum1=n1+n2
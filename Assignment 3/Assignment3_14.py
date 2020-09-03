num=[i for i in range(50)]

for i in num:
    if i%2==0:
        num.remove(i)

print(num)
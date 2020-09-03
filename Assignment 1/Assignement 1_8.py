def find_gcd(num1,num2):
    if(num2==0): 
        return num1
    else: 
        return find_gcd(num2,num1%num2) 
num1 = 60
num2= 48

print(find_gcd(num1,num2)) 
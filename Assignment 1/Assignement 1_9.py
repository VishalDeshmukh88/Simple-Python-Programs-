def find_gcd(num1,num2):
    if(num2==0): 
        return num1 
    else: 
        return find_gcd(num2,num1%num2) 
    
def find_lcm(num1,num2):
    lcm=num1*num2//find_gcd(num1,num2)
    print(lcm)
find_lcm(10,12)
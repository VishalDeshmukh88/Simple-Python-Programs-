def checkintersection(num1,num2):
    num1=set(num1)
    num2=set(num2)
    sunion=num1.intersection(num2)
    if len(sunion)>0:
        return True
    else:
        return False
num1=[1,2,35,6]
num2=[3,20,4]

checkintersection(num1,num2)

def celsius_farenheit(cel):
    print(cel,"C is",int(cel*(9/5)+32)," in Fahreheit")

def farenheit_celsius(fh):
    print(fh ,"F is ",int((fh-32)*(5/9))," in celsius ")
print(celsius_farenheit(60))
print(farenheit_celsius(45))
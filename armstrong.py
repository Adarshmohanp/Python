import math

n=int(input("Enter the number"))
b=n

m=int(math.log10(n))+1
result=0

while(n>0):
    a=n%10
    n=n//10
    result=result+a**m

if(result==b):
    print("The number is armstrong")
else:
    print("The number is not armstrong")





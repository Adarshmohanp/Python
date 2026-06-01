n=int(input("Enter the number to reverse: "))
result=0


while(n>0):
    remainder=n%10
    result=result*10+remainder
    n=n//10

print("the result is:",result)


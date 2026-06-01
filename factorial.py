def factorial(m):
    if(m==0 or m==1):
        return 1
    
    return m*factorial(m-1)


n=int(input("Enter the number"))

result=factorial(n)

print("The factorial is: ",result)


'''def factorial(m):
    if(m==0 or m==1):
        return 1
    
    return m*factorial(m-1)'''
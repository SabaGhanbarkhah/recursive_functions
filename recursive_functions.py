#some recursive functions

#factorial
def factorial():
    def fact(n):
        if n==1 or n==0:
            return 1
        else:
            s=n * fact(n-1)
            return s


#summation
def summation(n):
    if n==0:
        return 0
    if n==1:
        return 1
    sum=n+ summation(n-1)
    return sum

#exponentiation
def exponentiation(n,exponent):
    if n==0 or exponent==0:
        return 1
    if exponent==1:
        return n
    x=n* exponentiation(n,exponent-1)
    return x
    
#combination
def combination(n,m):
    if m==n or m==0:
        return 1
    comb=combination(n-1,m) + combination(n-1,m-1)
    return 

#divide
def divide(n,b):
    if n<b:
        return 0
    div=1+divide(n-b,b)
    return div

#fibonacci
def fibonacci(n):
    if n==0:
        return 0
    if n==1:
        return 1
    fib=fibonacci(n-1) + fibonacci(n-2)
    return fib

#choosing
option=int(input(' 1:summation \n 2:factorial \n 3:exponentiation \n 4:combination \n 5:divide \n 6:fibonacci \nenter your number to choose  the calculation : '))
n=int(input('entor your number to calculate: '))
if option==1:
    print(summation(n))
if option==2:
    print(factorial(n))
if option ==3:
    exponent=int(input('enter the exponent: '))
    print(exponentiation(n,exponent))
if option ==4:
    m=int(input('enter the m: '))
    print(combination(n-m,m))
if option ==5 :
    b=int(input('enter the devisor: '))
    print(divide(n,b))
if option ==6 :
    print(fibonacci(n))

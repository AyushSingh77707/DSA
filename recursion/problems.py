# Q1=> Print natural numbers from 1 to n using recursion

def printn(i,n):
    if i>n:
        return
    print(i)
    printn(i+1,n)

def func():
    n=int(input("Enter value of n: "))
    printn(1,n)

func()

# Q2=> find factorial of n using recursion

def fact(n):
    if n==0 or n==1:
        return n
    return n*fact(n-1)

def func():
    n=int(input("Enter value of n: "))
    print(f"the value of {n}! is {fact(n)}")

func()

# Q3=> Find value of nth term in fibbonaci series using recursion

def fib(n):
    if n==0 or n==1:
        return n
    return fib(n-1)+fib(n-2)

def func():
    n=int(input("Enter value of n: "))
    print(f"the value of {n}th fibbonaci is {fib(n)}")

func()






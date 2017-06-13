def factorial():
    n=input('Enter a number: ')
    n=int(n)
    factorial=1
    for i in range(1,n):
        factorial=factorial*n
        n=n-1
    print(factorial)

factorial()
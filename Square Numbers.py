def square_of_numbers():
    n=input('Enter a number: ')
    n=int(n)
    d=dict()
    for i in range(1,n+1):
        d[i]=i*i
    print(d)

square_of_numbers()
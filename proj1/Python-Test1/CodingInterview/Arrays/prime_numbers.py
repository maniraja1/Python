from math import sqrt, ceil, floor
def isprime(n):
    if n == 2 or n == 3:
        return True

    elif n == 4:
        return False

    for i in range (2,ceil(sqrt(n))+1):
        if n%i == 0:
            return False
    return True

def primes(n):
    z = [0,0]+[1]*(n-1)
    print(z)


    for x in range(2, n+1):
        y = isprime(x)
        if y is False:
            if len(z[x:len(z):x])>0:
                z[x:len(z):x]=[0]*len(z[x:len(z):x])
            z[x]=0

        print(x, z[x:])
        if z[x:] == [0]*len(z[x:]):
            print(f"Breaking out - {x}")
            break
    print(z)


'''
Below is the sieving technique that can be used to generate prime numbers
The counting  starts from 3, excludes even numbers and excludes multiples of i > i**2
Below is an explanation of the sieving technique
https://www.geeksforgeeks.org/sieve-of-eratosthenes/
'''
def primes2(n):
    if n <2:
        return []
    size = (n-3)//2+1
    print(size)
    primes = [2]
    is_prime = [True]*size
    print(f"is_prime: {is_prime}")
    for i in range(size):
        if is_prime[i]:
            p=i*2+3
            print(f"p: {p}, i: {i}")
            primes.append(p)
        for j in range(2*i**2+6*i+3,size,p):
            is_prime[j]=False
        print(f"is_prime: {is_prime}")
    print(primes)


primes(10)
print('#'*50)
primes2(50)
print(17//2+1)
print(18//2+1)




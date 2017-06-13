def sumofnnumbers():
    n=input('Enter a number:')
    n=[int(d) for d in str(n)]
    sum=0
    for i in range(len(n)):
        sum=sum+n[i]
    print(sum)


sumofnnumbers()
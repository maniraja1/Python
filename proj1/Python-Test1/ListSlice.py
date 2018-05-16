

def slice(a,n):
    if(len(a)>=n):
        print(a[n-1],a[n])
    else:
        print("List is not "+str(n)+" elements long")

daily_balances = [107.92, 108.67, 109.86, 110.15]

slice(daily_balances,5)
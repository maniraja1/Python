def median_function():
    n=input('enter a number: ')
    n=[int(d) for d in str(n)]
    m = sorted(n)
    j = int(len(m) / 2)
    median=m[j]
    print(median)

median_function()
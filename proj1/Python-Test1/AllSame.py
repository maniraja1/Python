def allsame(samples):

    ##print(type(samples))
    sets=[]
    if isinstance(samples,(list,tuple,dict)):
        ##print('iterable and not a generator')
        sets=samples
    else:
        ##print('not an iterable')
        for s in samples:
            ##print(s)
            sets.append(s)

    firstval=sets[0]

    for x in sets:
        if x != firstval:
            return False

    return True

def allsame2(samples):


    firstval=''

    for x in samples:
        if (firstval == ''):
            firstval = x

        if x != firstval:
            return False

    return True

x=allsame2([(1, 'a'), (1, 'a')])
print(x)

x=allsame2([[1, 'a'], [1, 'b']])
print(x)


numbers = [1, 4, 7, 10]
x=allsame2(n % 2 for n in numbers)
print(x)

numbers = [1, 4, 7, 10]
x=allsame2(n % 3 for n in numbers)
print(x)




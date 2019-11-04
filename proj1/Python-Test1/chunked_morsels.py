import types
def chunked(iterinput,n=0,debug=0,*,fill=0):
    if(isinstance(iterinput, types.GeneratorType)):
        iterinput=list(iterinput)
    outlist = []
    templist = []
    startpos=0
    endpos=n
    if(debug):
        print(f"Length:{len(iterinput)}")
    for i in iterinput:
        if (debug):
            print(f"StartPos{startpos}")
            print(f"EndPos{endpos}")
        templist = list(iterinput[startpos:endpos])
        while (len(templist) >0 and len(templist) < n):
            templist.append(fill)
        if(len(templist)>0):
            outlist.append(templist)
        startpos += n
        endpos += n
        if (debug):
            print(f"StartPos{startpos}")
            print(f"EndPos{endpos}")
    for i in outlist:
        yield i


for chunk in chunked([1, 2, 3, 4, 5],3,fill=-1):
    print(chunk)
for chunk in chunked(range(10), 4,fill=-1):
    print(tuple(chunk))
squares = (n**2 for n in range(6))
for chunk in chunked(squares, 3,fill=-1):
    print(*chunk)

squares = (n**2 for n in range(7))
chunks = chunked(squares, 3,fill=-1)
print(tuple(next(chunks)))
print(tuple(next(chunks)))
print(tuple(next(chunks)))

'''
When you want to return a generator use the following piece of code
    for i in list:
        yield i
If you want to calculate the length  or access a certain element on a generator, convert to a list
 if(isinstance(iterinput, types.GeneratorType)):
        iterinput=list(iterinput)


'''


'''

Look online to view pascals triange.
The concept is row[i][j = row[i-1][j]+row[i-1][j-1]

However you need to be careful about indices. The first and last element in each row should always be [1]
Note that the inner loop goes from 1 to i that way you will not update first and last element
The outer element starts from 0 to n but notice how we add 1 when building the list because the first element is 0
and if we multiple [1]*0 this will produce an empty list

'''

def pascaltriangle(n):
    out = []
    for i in range(0,n):
        out.append([1]*(i+1))
        for j in range(1,i):
            out[i][j]=out[i-1][j]+out[i-1][j-1]

    print(out)


pascaltriangle(10)

'''
different ways of dynamically generating lists
n=5
out=[[1]*(x+1) for x in range(n)]
print(out)

n=5
out=[1*(x+1) for x in range(n)]
print(out)

n=5
out=[]
for x in range(n):
    for j in [1]*(x+1):
        out.append(j)
print(out)

'''
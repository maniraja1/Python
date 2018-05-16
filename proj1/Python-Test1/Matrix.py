for i in range(1, 4):
    print(i)

iterator = (i for i in range(1, 4))
for i in iterator:
    print("I",i)
    for j in iterator:
        print("J",j)

iterator = (i for i in range(1, 4))
matrix = [[x * y for y in iterator] for x in iterator]

print(matrix)

iterator = [i for i in range(1, 4)]
matrix1 = [[x for x in iterator],[x*2 for x in iterator]]
print(matrix1)
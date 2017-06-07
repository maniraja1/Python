def minimum_function():
    list1=input('Enter a number:')
    list1=[int(d) for d in str(list1)]
    print(list1)
    min=list1[0]
    for i in range(len(list1)):
        if list1[i]<min:
            min=list1[i]
    print(min)

minimum_function()

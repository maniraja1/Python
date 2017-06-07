def Maximum_Function():
    list1=input('Enter a number: ')
    list1=[int(d) for d in str(list1)]
    max=list1[0]
    for i in range(len(list1)):
        if list1[i]>max:
            max=list1[i]
    print(max)


Maximum_Function()
list1=[[(1, 2), (3, 4),4], [(5, 6), (7, 8)]]
list2={(1, 2), (3, 4), (5, 6), (7, 8)}
list3=[['apple', 'pickle'], ['pear', 'avocado']]
list=[['apple', 'pickle'], ['pear', 'avocado']]
list5=([['apple', 'pickle'], ['pear', 'avocado']])
def deepflatten(items):
    finallist=[]

    def flatten(items):
        for l in items:
            try:
                if(iter(l)):
                    print(l)
                    print("Iterable")
                    flatten(l)
            except TypeError:
                print(l)
                finallist.append(l)
                print("not iterable")
    flatten(items)
    return finallist

def deepflatten1(items):
    finallist=[]

    def flatten1(items):
        print("***************************************************")
        print(items)
        print(type(items))
        for l in items:
            try:
                print(type(l))
                if isinstance(l, type(list)):
                    print("Iterable list")
                    print(l)
                    flatten1(l)
                elif isinstance(l, type(tuple)):
                    print("Iterable tuple")
                    flatten1(l)
                elif isinstance(l, type(set)):
                    print("Iterable set")
                    flatten1(l)
                else:
                    print(l)
                    finallist.append(l)
                    print("not iterable")
                    print
            except Exception as e:
                print("Error Ocurred" + str(e))

    flatten1(items)
    return finallist

def deepflatten2(items):
    flattened=[]
    def flattenx(items):
        for l in items:
            #print(l)
            #print(type(l))
            if(type(l) in [list,tuple]):
               #print("List")
               flattenx(l)
            else:
                #print("not a list")
                flattened.append(l)
    flattenx(items)
    return(flattened)

def deepflatten3(iterable):
    """Flatten an iterable of iterables."""
    flattened = []
    for item in iterable:
        #print(type(item))
        if type(item) in [list, tuple]:
            for x in deepflatten3(item):
                flattened.append(x)
        else:
            flattened.append(item)
    return flattened

def deepflatten5(items):
    finallist=[]

    def flatten(items):
        #print(items)
        #print(type(items))
        for l in items:
            try:
                #print(type(l))
                if isinstance(l, (list,tuple)):
                    #print("Iterable list")
                    #print(l)
                    flatten(l)
                else:
                    #print(l)
                    finallist.append(l)
                    #print("not iterable")
            except Exception as e:
                print("Error Ocurred" + str(e))

    flatten(items)
    return finallist

#deepflatten2(list)
X=deepflatten5(list)
print(X)

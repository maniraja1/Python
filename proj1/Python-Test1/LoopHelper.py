class info:

    def __init__(self , is_first,index):
        self.is_first=is_first
        self.index=index


def loop_helper(loop):
    items=[]
    index=0
    for l in loop:
        if index == 0:
            is_first=True
        else:
            is_first=False

        items.append((l,info(is_first,index)))
        index +=1
    print(items)
    return items

def loop_helper1(loop):
    items=[]
    index=0
    for item in loop:
        items.append((item,info(is_first=(index==0),index=index)))
        index += 1
    return(items)

def loop_helper2(loop):
    return[
        (item,info(is_first=(index==0),index=index))
           for index,item in enumerate(loop)]



colors = ["red", "blue", "green"]
for color, info in loop_helper2(colors):

    if info.is_first:
        print("This is the first color:{0}!".format(color))
    print("Color {0} is {1}".format(info.index,color))






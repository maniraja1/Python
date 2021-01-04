print('#'*75)
print("sort sub list")
class list_node:
    def __init__(self, val=0, next=None):
        self.data=val
        self.next = next

    def traverse(self):
        cur = self
        while cur is not None:
            xout = cur.data
            cur = cur.next
            yield xout


x8 = list_node(8)
x7 = list_node(7, x8)
x6 = list_node(6, x7)
x5 = list_node(5, x6)
x4 = list_node(4, x5)
x3 = list_node(3, x4)
x2 = list_node(2, x3)
x1 = list_node(1, x2)


def reverse_sublist(L, start, finish):
    dummy_head = sublist_head=list_node(0, L)

    for _ in range(1, start):
        sublist_head = sublist_head.next
        print(sublist_head.data)

    sublist_iter = sublist_head.next
    print(dummy_head.data, sublist_head.data, sublist_iter.data)

    print(sublist_iter.data)
    print('#' * 50)
    for _ in range(finish-start):
        temp = sublist_iter.next
        print(sublist_iter.data, temp.data, sublist_head.data)
        print(sublist_iter.next.data, temp.next.data, sublist_head.next.data)
        sublist_iter.next, temp.next, sublist_head.next = temp.next, sublist_head.next, temp
        print(sublist_iter.next.data, temp.next.data, sublist_head.next.data)
        print('#'*50)

    return dummy_head.next

y= reverse_sublist(x1, 3, 6)
print(list(y.traverse()))
'''
Even odd sort is sorting the list with all even elements first and then all the odd elements
1. Even, Odd, odd_head=list.head, list.head.next, list.head.next
2. even_next=odd.next
3. odd.next = event_next.next
4. even.next, odd.next=even_next, odd_next
5. even, odd= even_next, odd_next
6. If even.next is None or odd.next is None. you have reached he end. Just plug even.next
to odd_head



'''

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


class linked_list:

    def __init__(self, val=None):
        node = list_node(val)
        self.head = node
        self.tail = node

    def append(self, val):
        node = list_node(val)
        self.tail.next = node
        self.tail = node

    def append_items(self, vals):
        for x in vals:
            self.append(x)

    def traverse(self):
        return self.head.traverse()

    def updatenext(self, node, next):
        node.next = next

    def len(self):
        start = self.head
        l = 1
        while start.next is not None:
            l += 1
            start = start.next
        return l

    def delete(self,indx):

        if indx==1:
            self.head = self.head.next
        elif 1 < indx <= self.len():
            i=1
            pos = self.head
            while i < indx:
                prev=pos
                pos = pos.next
                i += 1
            prev.next=pos.next
        else:
            raise ValueError("Incorrect Index passed")

def oddevensort(l: linked_list)->None:
    even, odd, odd_head = l.head, l.head.next, l.head.next
    while even is not None and odd is not None:
        if odd.next:
            even_next = odd.next

        if odd.next is not None:
            odd_next = even_next.next


        even.next=even_next
        odd.next=odd_next

        even, odd = even_next, odd_next


        if even_next.next is None or odd_next.next is None:
            even.next=odd_head
            return


print('#'*75)
print("Original List")
x1=linked_list(1)
x1.append_items([2, 3, 4, 5])
print(f"x1: {list(x1.traverse())}")
oddevensort(x1)
print(f"x1: {list(x1.traverse())}")





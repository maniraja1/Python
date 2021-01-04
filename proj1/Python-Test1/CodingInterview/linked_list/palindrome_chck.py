'''
There are 3 parts to this problem
1. Implement function to find length of a list
2. implement function to reverse a sublist within a list
3. implement palindrome check
    1. split the list in two halfs
    2. reverse the second half using function to reverse a sublist within a list
    3. now have 2 pointers one that starts at the head and the other that starts at the head of the second half
    4. Iterate till you reach end of the list incrementing both pointers simultaneously
        start.data != second_half.data then it is not a palindrome
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

    def len(self):
        i=1
        start = self.head
        while start.next is not None:
            start = start.next
            i += 1
        return i


def reverse(l:linked_list, start:int, finish:int):
    start_node,prev_node = l.head.next,l.head
    i=2
    while i < start:
        start_node=start_node.next
        prev_node=prev_node.next
        i+= 1

    print(start_node.data, prev_node.data)
    while i < finish:
        temp = start_node.next

        start_node.next = temp.next
        temp.next=prev_node.next
        prev_node.next = temp

        print(prev_node.data, start_node.data,temp.data )
        if start_node.next is not None:
            print(prev_node.next.data, start_node.next.data, temp.next.data)
        i += 1
        print('#'*50)

def palindrome(l:linked_list):
    if l.len()%2==1:
        second_half_start = (l.len()//2)+2
        first_half_start= (l.len()//2)
    elif l.len()%2==0:
        second_half_start=(l.len()//2)+1
        first_half_start=(l.len()//2)

    reverse(l, second_half_start, l.len())
    print("Printing list after reverse")
    print(f"x1: {list(l.traverse())}")
    start_node, second_half_start_node=l.head, l.head
    i=1
    while i < second_half_start:
        second_half_start_node=second_half_start_node.next
        i += 1

    print(f"Start_Node:{start_node.data}, second_half_start_node: {second_half_start_node.data}")
    while second_half_start_node.next is not None:
        if start_node.data != second_half_start_node.data:
            return False
        start_node, second_half_start_node=start_node.next, second_half_start_node.next

    return True



print('#'*75)
print("Original List")
x1=linked_list(1)
x1.append_items([2,  3, 4, 5, 6, 7, 8, 9, 10])
print(f"x1: {list(x1.traverse())}")
#reverse(x1, 3, 10)
#print(f"x1: {list(x1.traverse())}")
print(x1.len())
print(palindrome(x1))
x2=linked_list('m')
x2.append('a')
x2.append('l')
x2.append('a')
x2.append('y')
x2.append('a')
x2.append('l')
x2.append('a')
x2.append('m')
print(f"x2: {list(x2.traverse())}")
print(palindrome(x2))

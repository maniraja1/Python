def scope_test():
    def do_local():
        spam = "local spam"
        print("After local assignment inside the function:", spam)
    def do_nonlocal():
        nonlocal spam
        spam = "nonlocal spam"
        print("After nonlocal assignment inside the function:", spam)
    def do_global():
        global spam
        spam = "global spam"
        print("After gloabal assignment inside the function:", spam)
    spam = "test spam"
    do_local()
    print("After local assignment:", spam)
    do_nonlocal()
    print("After nonlocal assignment:", spam)
    do_global()
    print("After global assignment:", spam)

scope_test()
print("In global scope:", spam)

my_list = [1, 2, 3]
my_list[1] = 5 # we can change just the first element of the list
print(my_list)
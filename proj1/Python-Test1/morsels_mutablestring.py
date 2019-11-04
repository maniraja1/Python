class MutableString():

    def __init__(self,data2):
        self.data = list(data2)

    def __add__(self, other):
        print("__Add")
        self.data.extend(list(other))
        ##return "".join(self.data)

    def __get__(self, instance, owner):
        print(f"__Get__{self.data}")
        return self.data

    def __getitem__(self, item):
        if type(item) == slice:
            return "".join(self.data[item])
        return self.data[item]

    def __set__(self, instance, value):
        print(f"__set__{self.data}")
        self.data.extend(list(value))

    def __setitem__(self, key, value):
        print("__setitem__")
        self.data[key]=value

    def __repr__(self):
        print("Repr")
        return "".join(self.data)

    def __len__(self):
        return len(self.data)


    def __delitem__(self, key):
        if type(key)==slice:
            del self.data[key]
            print(self.data)
        else:
            del self.data[key]
            print(self.data)






greeting = MutableString("Hello world!")
print((greeting))
print(len(greeting))
greeting + MutableString("!")
print(greeting)
print(len(greeting))
print(greeting[6:-1])
greeting[6:-1]="there"
print(greeting)
del greeting[:-3]
print(greeting)




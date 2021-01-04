
def coalesce(*input, sentinel=None):
    replacement = input[-1]
    names = input[:-1]
    out=sentinel
    print(input)
    print(sum(list(s1 in sentinel if s1 is not None and sentinel is not None else s1 is None for s1 in input)))
    if sum(list(s1 in sentinel if s1 is not None and sentinel is not None else s1 is None for s1 in input)) == len(input):
        raise ValueError(f"All given values were one of the sentinel values: {sentinel}")


    for name in names:
        if out != sentinel:
            return out
        if isinstance(sentinel, (list, tuple, set)):
            if name not in sentinel:
                out = name
        elif isinstance(sentinel, str):
            if name is not sentinel:
                out = name
        else:
            if name is not sentinel:
                out = name
    if out == sentinel:
        return replacement
    else:
        return out


print(coalesce("Trey", ""))

name = "Trey"
print(coalesce(name, "world", sentinel=""))

name = ""
print(coalesce(name, "world", sentinel=""))

name = None
print(coalesce(name, "world", sentinel=""))

name = "Trey"
print(coalesce(name, "world", sentinel=("", None)))
name = ""
print(coalesce(name, "world", sentinel=("", None)))
name = None
print(coalesce(name, "world", sentinel=("", None)))

(short_name, long_name) = ("Trey", "Trey Hunner")
print("Hi", coalesce(short_name, long_name, "you", sentinel=("", None)))

(short_name, long_name) = ("Trey", "")
print("Hi", coalesce(short_name, long_name, "you", sentinel=("", None)))

(short_name, long_name) = ("", "Trey Hunner")
print("Hi", coalesce(short_name, long_name, "you", sentinel=("", None)))

(short_name, long_name) = ("", "")
print("Hi", coalesce(short_name, long_name, "you", sentinel=("", None)))

#print(coalesce("", None, "", sentinel=("", None)))

s = ("test","")
t = ("test","",None)

print(True if sum(list(s1 in t for s1 in s)) > 0 else False)

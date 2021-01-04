
def validparantheses(string: str)->bool:
    open_list = ["[", "{", "("]
    close_list = ["]", "}", ")"]
    stacks = []
    previous = None
    # To keep track of opens. In a balanced string this should be 0
    opencounter = 0
    for x in s:
        if x in open_list:
            stacks.append(x)
            opencounter += 1
        if x in close_list:
            # If the first item is a closed parantheses then stack would be empty
            # checking to see if stack is empty if empty return false
            if stacks:
                previous = stacks.pop()
            else:
                return False
            # checking to see if open and close parantheses match
            if open_list.index(previous) != close_list.index(x):
                return False
            # Decrement the counter each time you find they match
            opencounter -= 1
    # In a balanced string this should be 0
    if opencounter > 0:
        return False
    else:
        return True


s = "()"
print(validparantheses(s))

s = "()[]{}"
print(validparantheses(s))

s="([)]"
print(validparantheses(s))

s="{[]}"
print(validparantheses(s))

s="{([)}"
print(validparantheses(s))
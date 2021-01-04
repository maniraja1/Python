
def openlock(deadends, target):
    queue = ["0000"]
    visited = {"0000"}
    level = 0
    while queue:
        #print(queue)
        print(len(queue))
        size = len(queue)
        while size >0:
            val = queue.pop(0)
            if val in deadends:
                size -= 1
                continue
            if val == target:
                return level

            for i,x in enumerate(val):
                newval1 = val[:i]+(str(int(val[i])+1) if int(val[i]) < 9 else '0')+val[i+1:]
                newval2 = val[:i] + (str(int(val[i]) - 1) if int(val[i]) > 0 else '9') + val[i + 1:]

                if newval1 == target:
                    return level+1

                if newval2 == target:
                    return level+1

                if newval1 not in deadends and newval1 not in visited:
                    queue.append(newval1)
                    visited.add(newval1)
                if newval2 not in deadends and newval2 not in visited:
                    queue.append(newval2)
                    visited.add(newval2)
            size -=1
        level += 1
    return -1

deadends = {"0201","0101","0102","1212","2002"}
target="0202"
print(openlock(deadends, target))
def selection_sort(input):
    i=0
    compcounter = 0
    movementcounter = 0
    print(f"original input: {input}")
    print("")
    while i<len(input)-1:
        compcounter += 1
        minval = min(input[i:])
        if input[i] > minval:
            input[input[i:].index(minval)+i], input[i] = input[i], minval
            movementcounter += 1
        i += 1
    print("")
    print(f"FinalOutput: {input}")
    print(f"compcounter: {compcounter}")
    print(f"MovementCounter: {movementcounter}")

selection_sort([4,3,8,6,2,1,8,1])


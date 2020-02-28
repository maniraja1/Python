def insertion_sort(input):
    i=1
    z=0
    compcounter = 0
    movementcounter = 0
    print(f"original input: {input}")
    print("")
    while i<len(input):
        j=i-1
        z=i
        while j >= 0:
            compcounter += 1
            if input[j] > input[z]:
                input[j], input[z] = input[z], input[j]
                movementcounter += 1
                z = j
            j -= 1
        print(input)
        i += 1
    print("")
    print(f"FinalOutput: {input}")
    print(f"compcounter: {compcounter}")
    print(f"MovementCounter: {movementcounter}")

insertion_sort([4, 3, 8, 6, 2, 1, 8, 1])


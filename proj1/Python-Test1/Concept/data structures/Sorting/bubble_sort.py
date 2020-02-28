def bubble_sort(input):
    issorted = True
    compcounter = 0
    movementcounter = 0
    print(f"original input: {input}")
    while issorted:
        print("")
        i=0
        issorted = False
        while i < len(input)-1:
            compcounter += 1
            if input[i] > input[i+1]:
                input[i], input[i+1] = input[i+1], input[i]
                issorted = True
                movementcounter += 1
            print(input)
            i += 1
    print("")
    print(f"FinalOutput: {input}")
    print(f"compcounter: {compcounter}")
    print(f"MovementCounter: {movementcounter}")

bubble_sort([4,3,8,6,2,1,8,1])


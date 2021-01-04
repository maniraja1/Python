import math
def numSquares2(n):
    if n <= 3:
        return n
    squares = { i * i for i in range(1, math.floor(math.sqrt(n)) + 1) }
    sums = squares
    print(sums)
    for i in range(1, n):
        print(f"I: {i}")
        if n in sums:
            return i
        sums = { a + b for a in squares for b in sums }
        print(sums)


print(numSquares2(30))
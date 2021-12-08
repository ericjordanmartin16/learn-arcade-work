def f(level):
    # Print the level we are at
    print("Recursion call, level",level)
    # If we haven't reached level ten...
    if level < 10:
        # Call this function again
        # and add one to the level
        f(level+1)


# This program calculates a factorial
# WITHOUT using recursion
def factorial_nonrecursive(n):
    answer = 1
    for i in range(2, n + 1):
        answer = answer * i
    return answer


# This program calculates a factorial
# WITH recursion
def factorial_recursive(n):
    if n == 1:
        return 1
    elif n > 1:
        return n * factorial_recursive(n - 1)


# Start the recursive calls at level 1
f(1)

# Mandelbrot set
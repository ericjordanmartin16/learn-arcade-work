# Write a function that takes three numbers
# and returns the average.

# Print the result of 10, 20, 30

def compute_average(x, y, z):
    sum_numbers = x + y + z
    average = sum_numbers / 3
    return average


my_result = compute_average(10, 20, 30)
print(my_result)

"""or:
n1 = 10
n2 = 20
n3 = 30
my_result = compute_average(n1, n2, n3)
"""

# If statement
# aka. Conditional logic

a = 3
b = 4
c = a == b

print(c)

if 1:
    print("1")
if "A":
    print("A")
if 21:
    print("21")
if 0:
    print("0")

"""temperature = int(input("What is the temperature in Fahrenheit? ")) # put a space here so that the user doesn't put one in.
print(f"You said the temperature was {temperature}.")


if temperature > 110:
    print("fry eggs on pavement.")
elif temperature > 90:
    print("It is hot outside.")
elif temperature < 30:
    print("It is cold outside.")
else:
    print("It is not hot outside.")"""

"""if a != b:
    print("A is not B")

if a < b and a < c:
    print("a is smaller than b and c")

if b >= a:
    print("b is smaller than or equal to a")

if b == a:
    print("b is smaller than or equal to a")"""

print("Done")

test = 3 < 4
print(test)

if "3" == "3":
    print("yes")
else:
    print("no")

if 3 == "3":
    print("yes")
else:
    print("no")

if "10" < "2":
    print("yes")
else:
    print("no")

name = "paul"
if name.lower() == "Paul":
    print("yes")
else:
    print("no")

name2 = "mary"
if name2.lower() == "bob" or "sam":
    print("yes")
else:
    print("no")
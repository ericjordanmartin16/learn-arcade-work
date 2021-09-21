# 'for loops' - know how many times to loop.
# 'while loops' - loop until a condition

# repetitions = int(input("How many times? "))


"""def print_about_gum(repetitions):
    for i in range(repetitions):
        print("I will not chew gum in class.")


print_about_gum(repetitions)


print("But I can drink water.")"""

for i in range(3):
    print("a")
    for j in range(3):
        print("b")

# Print a clock
for hour in range(1, 13):
    for minute in range(60):
        print(hour, minute)

# Running total
total = 0 # Outside the loop so it does not reset to 0
for i in range(1, 101):
    total += i

print("The total is", total)

for hello_loop in range(5):
    print("Hello")

print("there")

a = 0
for x in range(10):
    a += 1
    for y in range(10):
        a += 1
print(a)

# while loop
n = 10 # Sentinel variable
while n >= 0:
    print(n)
    n -= 1
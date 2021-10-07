"""x = 3
print("x =", x, "and is of type:", type(x))

x = 3.241
print("x =", x, "and is of type:", type(x))

x = "Hi there"
print("x =", x, "and is of type:", type(x))

x = True
print("x =", x, "and is of type:", type(x))

y = (2, 3, 4, 5)
print("y =", y, "and is of type:", type(y))
y = [2, 3, 4, 5]
print("y", type(y))"""


x = [3, 8, 7, 0, 5, 5, 2, 1]
print(x)
print(x[1])

x[2] = 22
print(x)

# replaces the ENTIRE list!
x = 18
print(x)

my_list = [3, 7, 3]
size = len(my_list)
print(size)

for item in my_list:
    print(item)

my_string_list = [2, 3, 6, 5, 8, 10]

print(my_string_list[2])

for item in my_string_list:
    print(item)

# Don't necessarily do this:
for i in range(len(my_string_list)):
    print("Item", i, "is", my_string_list[i])
    # Cannot do this with the first loop!

# Distinct to Python:
for index, value in enumerate(my_string_list):
    print("Item", index, "is", value)

print(my_string_list)
my_string_list.append(100)
print(my_string_list)

my_other_list = []

"""for i in range(5):
    user_input = int(input("Enter an integer: "))
    my_other_list.append(user_input)"""

print(my_other_list)

my_different_list = [0] * 100
print(my_different_list)

my_sum_list = [5, 76, 8, 5, 3, 3, 56, 5, 23]

for i in range(len(my_sum_list)):
    my_sum_list[i] *=2

print(my_sum_list)

sum(my_sum_list)

list_total = 0
for item in my_sum_list:
    list_total += item

print(list_total)


my_user_list = []
for i in range(5):
    user_input = int(input("Enter a number: "))
    my_user_list.append(user_input)

print(my_user_list)


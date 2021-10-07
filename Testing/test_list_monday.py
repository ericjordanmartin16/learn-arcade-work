x = "0123456789"

print("x=", x)
print("x[0]=", x[0])
print("x[1]=", x[1])
print("x[2]=", x[2])
print("x[4]=", x[4])
print("x[-1]=", x[-1])

print("x[:5]=", x[:5])
print("x[5:]=", x[5:])
print("x[5:8]=", x[5:8])

a = "Hi"
b = "There"
c = "!"

print(a + b)
print(a + b + c)
print(30 * a)
print((a * 2) + (b * 2))

for character in "This is a test.":
    print(character)

"""months = "JanFebMarAprMayJunJulAugSepOctNovDec"
n = int(input("Enter a month number: "))
month = months[(n - 1) * 3:(n - 1) * 3 + 3]
for n in months:
    print(months[(n - 1) * 3: (n - 1) * 3 + 4])
print(month)"""

plain_text = "This is a test. ABC abc"

for c in plain_text:
    x = ord(c) # converts letters to unicode numbers
    x += 1
    c2 = chr(x) # converts unicode numbers to letters
    print(c2, end="")

print()
encrypted_text = "U i j t ! j t ! b ! u f t u / ! B C D ! b c d "
for c in encrypted_text:
    x = ord(c)  # converts letters to unicode numbers
    x -= 1
    c2 = chr(x)  # converts unicode numbers to letters
    print(c2, end="")

print()

# Check for the biggest number.
my_list = [-4, -2, -56, -2, -30]
biggest_number = my_list[0]
for item in my_list:
    if item > biggest_number:
        biggest_number = item

print(biggest_number)

# Prints only positive numbers from my_list
my_list = [-4, -2, -56, 2, 30]
positive_list = []
for item in my_list:
    if item > 0:
        positive_list.append(item)

print(positive_list)

################################################################################################

print()
print()
print("################################################################")
print()
print()
for i in range(3):
    print("*")

print()
for i in range(3):
    print(i, end="")

print()
for i in range(3):
    print("*", end="")
for j in range(3):
    print("*", end="")

print()
for i in range(3):
    for j in range(3):
        print("*", end="")
        print()

print()

for i in range(3):
    for j in range(3):
        print("*", end="")
    print()

for i in range(3):
    for j in range(3):
        print(i, end="")
    print()

x = 1
while x < 64:
    print(x)
    x *= 2
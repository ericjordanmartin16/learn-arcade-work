import random

a = 0
for i in range(40):
    a += 1
for j in range(40):
    a += 1
print(a)

b = 0
for x in range(20):
    for y in range(20):
        b += 1
print(b)

q = random.random() * 10 + 10
print(q)

for z in range(2, 12, 2):
    print(z + 1)
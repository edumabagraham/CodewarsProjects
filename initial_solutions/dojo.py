print(list(range(1,100)))

total2 = 0
for i in range(1,100):
    if (i % 3) == 0 or (i % 5) == 0:
        total2 += i

print(total2)
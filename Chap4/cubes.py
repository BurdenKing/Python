list_of_cubes = []
for i in range(1, 11):
    list_of_cubes.append(i ** 3)
for num in list_of_cubes:
    print(f"{num}")

listc = [num ** 3 for num in range(1, 11)]
print(f"{listc}")

# 4 - 10 slices
for i in range(0, 3):
    print(f"{listc[i]}")
print(f"{listc[0:3]}")

for i in range(7, 10):
    print(f"{listc[i]}")
print(f"{listc[7:10]}")

for i in range(4, 7):
    print(f"{listc[i]}")
print(f"{listc[4:7]}")

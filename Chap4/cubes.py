list_of_cubes = []
for i in range(1, 11):
    list_of_cubes.append(i ** 3)
for num in list_of_cubes:
    print(f"{num}")

listc = [num ** 3 for num in range(1, 11)]
print(f"{listc}")

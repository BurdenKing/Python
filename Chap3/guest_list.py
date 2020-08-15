# 3.4
guests = ['Tom', 'Jerry', 'Cook']
msg = "Welcome to dinner!"

# 3.6
guests.insert(3, "Flower")

guests.insert(0, "hOhO")

print(f"{msg} {guests[0].title()}")

print(f"{msg} {guests[1].title()}")

print(f"{msg} {guests[2].title()}")

# 3.5
guests[0] = "Big Daddy"

print(f"{msg} {guests[0].title()}")

print(f"{msg} {guests[1].title()}")

print(f"{msg} {guests[2].title()}")

guests.append("Nobody")

# 3.7
guests.pop(0)

guests.pop(1)

guests.pop(2)

print(guests)

del guests[0]

del guests[0]

del guests[0]


print(guests)

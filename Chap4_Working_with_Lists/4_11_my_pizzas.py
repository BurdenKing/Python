pizzas = ['Pepperoni', 'Hawaiian', 'Cheeeese', 'D2L']
for pizza in pizzas:
    print(f"I like {pizza} pizza!")
print(f"I really love pizza")

friends_pizza = pizzas[:]

pizzas.append("XYZ")

friends_pizza.append("ABC")

print(f"My fav pizzas are:")

for pizza in pizzas:
    print(f"{pizza}")

print(f"My friend's fav pizzas are:")

for pizza in friends_pizza:
    print(f"{pizza}")

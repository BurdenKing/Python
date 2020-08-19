person1 = {
    'first_name': 'Lawrence',
    'last_name': 'Zheng',
    'age': 24,
    'city': 'Vancouver',
}

person2 = {
    'first_name': 'James',
    'last_name': 'Ye',
    'age': 30,
    'city': 'Toronto',
}

person3 = {
    'first_name': 'Seb',
    'last_name': 'Sun',
    'age': 17,
    'city': 'Winnipeg',
}

list_of_person = [person1, person2, person3]

for person in list_of_person:
    print(f"{person['first_name']}, {person['last_name']}"
          f" is {person['age']} years old who lives in {person['city']}")

# 6.8 is similar to 6.7 so omitted

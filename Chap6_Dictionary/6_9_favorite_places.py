favorite_places = {
    'Mike': ['Seattle', 'New York'],
    'Bob': ['Vancouver', 'Toronto'],
    'Jason': ['Beijing', 'Wuhan'],
}

for key, values in favorite_places.items():
    print(f"\n{key.title()}'s favorite places are:")
    for places in values:
        print(f"\t{places}")


rivers = {
    'Amazon': 'Peru',
    'Nile': 'Egypt',
    'Yangtze': 'China',
}

for key, value in rivers.items():
    print(f"{key} runs through {value}.")

print(f"\nRivers includes:")

for key in rivers:
    print(f"{key}")

print(f"\nCountries are:")

for value in rivers.values():
    print(f"{value}")

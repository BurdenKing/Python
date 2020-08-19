fav_nums = {
    'James': 23,
    'Kobe': 24,
    'KaKa': 10,
    'Messi': 10,
}

for pair in fav_nums:
    print(f"{pair}\'s favorite number is: {fav_nums.get(pair)}")

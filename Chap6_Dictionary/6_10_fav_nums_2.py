fav_nums = {
    'James': [23, 25, 28, 30],
    'Kobe': [24, 37, 41],
    'KaKa': [10, 9, 8, 67],
    'Messi': [10, 604, 69],
}

for k, v in fav_nums.items():
    print(f"\n{k}'s favorite numbers are:")
    for num in v:
        print(num)

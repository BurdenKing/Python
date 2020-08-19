# nested dictionary

cities = {
    'Vancouver': {
        'Population': 631_486,
        'Area (Km^2)': 2878.52,
        'Province': 'British Columbia',
        'Country': 'Canada',
    },

    'Toronto': {
        'Population': 2_731_571,
        'Area (Km^2)': 5905.71,
        'Province': 'Ontario',
        'Country': 'Canada',
    },

    'Wuhan': {
        'Population': 19_000_000,
        'Area (Km^2)': 8494.41,
        'Province': 'Hubei',
        'Country': 'China',
    },
}

for key, value in cities.items():
    print(f"\n{key}:")
    for k, v in value.items():
        print(f"{k}: {v}")

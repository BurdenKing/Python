favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}

peoples = ['jen', 'jenny', 'edward', 'phil', 'jake']

for key in peoples:
    if key in favorite_languages:
        print(f"Thank you {key} for taking the poll!")
    else:
        print(f"Please take the poll {key}!")

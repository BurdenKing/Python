glossary = {
    'import': 'Import modules into current namespace',
    'pass': 'A null statement. Placeholder for execution',
    'break': 'End the most inner loop it is in',
    'continue': 'End the current iteration, but not the whole loop',
    'except': 'Used for catch exceptions with try...except blocks',
}

for word in glossary:
    print(f"{word} : {glossary.get(word)}")  # Need to find a better way to loop thru dictionary


# 6.4
for key, value in glossary.items():
    print(f"{key} : {value}")

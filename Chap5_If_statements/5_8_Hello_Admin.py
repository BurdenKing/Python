usernames = ['admin', 'Bob', 'Kathy', 'Adam', 'Jaden']
usernames = []

if not usernames:
    print("We need more users!")
else:
    for name in usernames:
        if name == 'admin':
            print(f"Hello {name}, would you like to see a status report?")
        else:
            print(f"Hello {name}, thank you for logging again.")

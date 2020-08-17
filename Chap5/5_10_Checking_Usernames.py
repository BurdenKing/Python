current_users = ['admin', "Ade", "Adam", "Audry", "Aoi"]
new_users = ['admin', 'Ade', 'Bosco', "Boyd", "Becky"]

current_users_new = []
for user in current_users:
    current_users_new.append(user.lower())

for user in new_users:
    if user.lower() in current_users_new:
        print(f"{user} already exist!")
    else:
        print(f"{user} is an available username.")

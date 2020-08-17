# string equality

my_cat = "Brock"
friends_cat = "Peanut"
print(my_cat == friends_cat)

# lower()
my_cat_cap = "BROCK"
print(my_cat == my_cat_cap.lower())

# Numerical stuff, + and/or
num = 15
fav_num = 24
print(num <= fav_num and fav_num >= 19)
print(fav_num < num or fav_num % 2 == 0)

# Check if an item exist in a list
my_list = [1, 2, 3, 4, 5]
print(15 in my_list)
print(15 not in my_list)

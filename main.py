# Move an item in a List in Python

my_list = ['bobby', 'hadz', '.', 'com']

# ✅ Move an item in a list

item = 'hadz'

my_list.remove(item)

my_list.insert(0, item)
print(my_list)  # 👉️ ['hadz', 'bobby', '.', 'com']

# --------------------------------------------

# ✅ Insert a value into a list at a specific position

my_list = ['bobby', '.', 'com']

my_list.insert(1, 'hadz')

print(my_list)  # 👉️ ['bobby', 'hadz', '.', 'com']
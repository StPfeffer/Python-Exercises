list = [12, 24, 35, 70, 88, 120, 155]

new_list = [x for x in list if x % 5 != 0 and x % 7 != 0]
print(new_list)

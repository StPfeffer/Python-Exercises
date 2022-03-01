list = [12, 24, 35, 70, 88, 120, 155]

new_list = [v for (i, v) in enumerate(list) if i not in (0, 4, 5)]
print(new_list)

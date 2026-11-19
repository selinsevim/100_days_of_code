numbers = [1, 2, 3]
new_list = [number + 1 for number in numbers]
print(new_list)


name = "Noah"
new_list = [letter for letter in name]
print(new_list)

range_seq = range(1, 5)
new_range = [num * 2 for num in range_seq]
print(new_range)

names = ["Selin", "Noah", "Matthias", "Ataberk", "Osman", "Ebru"]
short_names = [name for name in names if len(name) <= 4]
upper_case_long_names = [name.upper() for name in names if len(name) > 5]
print(short_names)
print(upper_case_long_names)

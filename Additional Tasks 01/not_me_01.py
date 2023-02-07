my_list = [1.1, 1.2, 3.1, 5, 10.01]
frac_list = []
for i in my_list:
    if isinstance(i, float):
        frac_list.append(i % 1)

min_value = min(frac_list)
max_value = max(frac_list)
print(max_value-min_value)

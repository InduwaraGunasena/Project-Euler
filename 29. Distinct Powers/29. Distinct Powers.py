upper_limit = 2
lower_limit = 100

sequence_list = []
for i in range(upper_limit, lower_limit + 1):
    for j in range(upper_limit, lower_limit + 1):
        sequence_list.append(i ** j)

print(len(list(set(sequence_list))))
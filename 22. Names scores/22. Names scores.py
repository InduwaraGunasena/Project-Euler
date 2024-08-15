file = open("p022_names.txt", "r")
names = sorted(i.strip('"') for i in file.read().split(','))

values = 0
for i in range(len(names)):
    values += sum(ord(j) - 64 for j in names[i]) * (i + 1)

print(values)

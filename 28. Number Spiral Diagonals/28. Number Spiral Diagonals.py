size = 1001 # matrix size
sum = 1 # The sum of the diagonal numbers

num = 1  # this is used to get each diagonal numbers
l = [1]  # this stores all the diagonal numbers.(OPTIONAL)

for i in range(3, size + 1, 2):
    for j in range(4): # Every spiral has 4 corner diagonal values
        num += i-1
        sum += num
        l.append(num)

print(l)
print(sum)
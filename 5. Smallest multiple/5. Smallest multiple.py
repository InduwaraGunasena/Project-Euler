numbers_1 = [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
numbers_2 = [1]*len(numbers_1)
number = 1
x = 0
smallest_dividing_num = 2


def dividing_a_number(num):
    dividing_num = 2
    while num % dividing_num != 0:
        dividing_num += 1
    return dividing_num


while True:
    for i in range(len(numbers_1)):
        if x == 0 and numbers_1[i] != 1:
            smallest_dividing_num = dividing_a_number(numbers_1[i])
            numbers_1[i] = int(numbers_1[i] / smallest_dividing_num)
            x = 1
        else:
            if numbers_1[i] % smallest_dividing_num == 0:
                numbers_1[i] = int(numbers_1[i] / smallest_dividing_num)
        if numbers_1[i] == 1:
            continue

    number = number * smallest_dividing_num
    x = 0
    smallest_dividing_num = 2
    print(numbers_1)

    if numbers_1 == numbers_2:
        break

print(f"answer is {number}")

#i = 1
#for k in range(1, 21):
#    if i % k > 0:
#        for j in range(1, 21):
#            if (i*j) % k == 0:
#                i *= j
#                break
#print(i)

limit = 10000  # This is the limit that we evaluate the sum of amicable numbers under this variable.
digit = 1


def divisor(number):  # This function is used to find all the proper divisors and adding them together.
    div = 1
    l_1 = []  # I used a list to store all the proper divisors. So you can check whether code is right or wrong by looking divisors.
    while div < number / 2:
        if number % div == 0:
            l_1.append(div)
            div += 1
        else:
            div += 1

    if number % 2 == 0:
        l_1.append(number // 2)
    return sum(l_1)

list_2 = []
while digit <= limit:
    sum_1 = divisor(digit)
    sum_2 = divisor(sum_1)
    if sum_2 == digit and digit != sum_1:
        list_2.append(digit)
        list_2.append(sum_1)
        digit += 1
    else:
        digit += 1
    if digit in list_2:
        digit += 1


print(list_2)
print(sum(list_2))




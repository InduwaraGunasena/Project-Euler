import time
start = time.time()

sum_of_triangle_number = 1 # initial number of triangle number
number = 2 # this is the number to get a new triangle number from the past triangle number
no_of_divisors = 500
x = []

def find_divisors(num):
    divisors = []
    for i in range(1, num + 1):
        if num % i == 0:
            if i in divisors:
                break
            y = num // i
            # if a number can be divide without a remainder(if remainder = 0),then we have just found 2 divisors at once.
            # one number is the divisor and the other one is quotient.Here y is the quotient and i is the divisor.
            # e.g. :- 12/2 = 6 and the remainder is 0.so we have just found 2 factors that are 2 and 6 (6 is the quotint of 12/2).
            divisors.append(i)
            divisors.append(y)
    return divisors


while True:
    # I saw a special rule for a triangle number which has most divisors,they can be divided by 2.
    # So I decided to divide all the triangle numbers to whether they can be divide by 2 or not.
    if sum_of_triangle_number % 2 == 0:
        x = find_divisors(sum_of_triangle_number)
    if len(x) > no_of_divisors:
        break

    sum_of_triangle_number += number
    number += 1

print(f"first triangle number of over {no_of_divisors} divisors = {sum_of_triangle_number}")

finish = time.time()
print("you have used", finish - start, "s  to solve this")

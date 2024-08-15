import math

num_limit = 2 * pow(10, 6)
number = 2
sum = 0


def finding_whether_prime_or_not(num):
    if num == 2:  # include the first prime number 2.
        return True
    elif num % 2 == 0:  # exclude all the even numbers because all the prime numbers are odd except 2.
        return False
    # if any number 'N' has a prime factor within lower than sqrt(N),that N number will not be a prime number
    f = math.sqrt(num) + 1
    i = 3
    while i < f:
        if num % i == 0:
            return False
        i += 1
    # After done all these steps,if there is any number still remains,those number is a prime.
    return True


while True:
    if number > num_limit:
        break
    if finding_whether_prime_or_not(number) == True:
        sum += number
    number += 1

print("sum = %d" % sum)

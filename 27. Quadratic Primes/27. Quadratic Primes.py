import math

# a and b range(upper bound)
limit = 1000
def check_prime(num):
    if num == 2:
        return True
    elif num % 2 == 0:
        return False
    else:
        f = math.sqrt(num)+1
        i = 3
        while i < f:
            if num % i == 0:
                return False
            i += 1
        return True

# The function should give us any prime number for every consecutive integers from 0.
# This function calculates the last integer which gives any prime.
def check_prime_function(a, b):
    n = 0
    while True:
        val = n ** 2 + a * n + b
        # if function gives us negative values then that n number is the last number which gives primes.
        # Because negative numbers aren't prime.
        if val <= 0:
            return n
        if not check_prime(val):
            return n # this is last number which gives us prime numbers from 0 to consecutive integers.
        n += 1

# Take all the prime numbers less than the upper bound.
prime_list = [i for i in range(2, limit+1) if check_prime(i) == True]

max_prime_nums = 0
answer = 0

# Now we have to assign prime values for p and b.
# First take one value from prime_list for p and assign another value for b which is not equal to p but in prime_list
for p in prime_list:
    restList = [x for x in prime_list if x != p]
    for b in restList:
        a = p - b - 1
        e = check_prime_function(a, b)
        if e > max_prime_nums:
            max_prime_nums = e
            answer = a*b

print(answer)
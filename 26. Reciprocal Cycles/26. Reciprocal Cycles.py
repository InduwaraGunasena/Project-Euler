import math

def recurrence_length(num):
    l = 0
    remainder = 1
    ans = '0.' # used to ease the debug. this will represent the answer of 1/num.
    while True:
        ans = ans + str((remainder * 10) // num) # calculate the answer of 1/num. NOT NECESSARY FOR TO FIND THE SOLUTION.
        remainder = (remainder * 10) % num  # we know that, when we are dividing a number we add a zero to back of the remainder and do it until we get a zero remainder.
        l += 1
        if remainder == 1:  # if we're dividing the remainder again and again and meet again 1, that's the point recurrence occur.
            break
    return l


# numerator range(upper bound)
d_limit = 1000

def check_prime(num):
    if num == 2:
        return True
    elif num % 2 == 0:
        return False
    else:
        a = math.sqrt(num)+1
        i = 3
        while(i < a):
            if num % i == 0:
                return False
            i += 1
        return True

prime_list = [i for i in range(2, d_limit+1) if check_prime(i) == True]

# We know if numerator is multiple of 2 or 5(any power of both) or both then it has no recurring decimal part.
# In fact, if numerator is divisible of 3 then it has an infinite series of same number or numbers(usually few)
# Other prime numbers form a recurring part
prime_list = [x for x in prime_list if x % 2 != 0 and x % 3 != 0 and x % 5 != 0]

answer = 0
max_recurrence_length = 0

for j in prime_list:
    p = recurrence_length(j)
    if p > max_recurrence_length:
        max_recurrence_length = p
        answer = j

print(answer)
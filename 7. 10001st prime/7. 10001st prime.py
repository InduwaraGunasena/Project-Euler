import time, math
s = time.time()
prime_number = []
position = 10001
num = 3


def finding_whether_prime_or_not(number):
    if number == 2:  #include the first prime number 2.
        return True
    elif number % 2 ==0: #exclude all the even numbers because all the prime numbers are odd except 2.
        return False
    #if any number 'N' has a prime factor within lower than sqrt(N),that N number will not be a prime number
    f = math.sqrt(number) + 1
    i = 3
    while i < f:
        if number % i == 0:
            return False
        i += 1
    #After done all these steps,if there is any number still remains,those number is a prime.
    return True

"""
    dividers = 0
    for i in range(1, number + 1):
        if number % 2 == 0:
            break
        if number % i == 0:
            if i != number:
                dividers += 1
                if dividers == 2:
                    break
            elif i == number and dividers == 1:
                break

    if i == number and dividers == 1:
        return True
"""

while len(prime_number) < position - 1:
    if finding_whether_prime_or_not(num) == True:
        prime_number.append(num)
    num = num + 2
    print(len(prime_number))

print(f"{position}th prime number is {prime_number[position - 2]}")
print(time.time() - s)

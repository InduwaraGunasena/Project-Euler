import math
import time

start = time.time()
def is_prime(n):
    if n == 1:
        return False
    else:
        square = math.sqrt(n)
        i = 2
        while i <= square:
            if n % i == 0:
                return False
            i += 1
        return True

# if you explore some prime numbers, you realize that they will be ended up either 1,3,7 or 9. (only one number ended up 2 which is prime number '2')
# Therefore, to get another prime number by eliminating some digits, you have to remove all numbers which having 1 any of side.
# So you can start from 20 not from 10.
# e.g. :- 113 is a prime number. But 113 -> 11 (OK) -> 1 (is not prime)    ; by removing digits one by one from right side
#                                    113 -> 13 (OK) -> 1 (is not prime)    ; by removing digits one by one from left side
answers = []
i = 20
s = ['1', '4', '6', '8', '9']

while len(answers) != 11:
    a = str(i)
    if a[0] not in s and a[-1] not in s:
        if is_prime(i):
            is_truncatable = True
            for j in range(len(a)-1):
                right = int(a[:j+1])        # by removing digits one by one from right side
                left = int(a[len(a)-1-j:])  # by removing digits one by one from left side
                if not is_prime(right) or not is_prime(left):
                    is_truncatable = False
                    continue
            if is_truncatable == True:
                answers.append(i)
    i += 1

print(answers)
print("answer =", sum(answers), "\n")

end = time.time()
print(end - start)
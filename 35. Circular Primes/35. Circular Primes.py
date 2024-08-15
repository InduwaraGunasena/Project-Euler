import math
import time

start = time.time()

limit = 10**6

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

def num_circular(n):
    lis = []
    num = str(n)
    for i in range(len(num)):
        lis += [int(num[i:] + num[:i])]
    return list(set(lis))


answer = []
n = True

for x in range(2, limit):
    if not is_prime(x) or x in answer:
        continue
    else:
        a = num_circular(x)
        for i in a:
            if not is_prime(i):
                n = False
                break
        if n == True:
            answer += a
        n = True

print(len(answer))

end = time.time()
print(end - start)
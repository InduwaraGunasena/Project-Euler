# We know that the largest factorial from 0 to 9 is 9.
# So, the largest digit factorial can get only when all the digits having value 9.
# Therefore, let's try to find an upper bound for our problem space.
# 9! = 362880
# 9!*5 = 1814400  ( We know that 99999     < 1814400 )
# 9!*6 = 2177280  ( We know that 999999    < 2177280 )
# 9!*7 = 2540160  ( We know that 9999999   > 2540160 )
# 9!*8 = 2903040  ( We know that 99999999  > 2903040 )
# 9!*9 = 3265920  ( We know that 999999999 > 3265920 )
# Now you clearly see that the inequality sign inverts from 9!*7. That is, if the number having more than 7 digits, it cannot have same digit factorial with number.

import time

#time at the start of program execution
start = time.time()

factorials = [1, 1, 2, 6, 24, 120, 720, 5040, 40320, 362880]

def digit_factorial_sum(n):
    s = 0
    while n != 0:
        s += factorials[n%10]
        n = n // 10
    return s

answer = []
s = 0
for i in range(10, 1999999):
    # Though this condition is reduce the search space, it takes more time. Therefore, I commented that.
    #if int(str(i)[::-1]) <= i:
    #    continue
    if digit_factorial_sum(i) == i:
        answer.append(i)
        s += i
print(s)

end = time.time()
print(end - start)
# This question is more trivial if that number only multiplied by 1. Because then
# the largest 1 to 9 pandigital 9-digit number would be only 987654321. ( Since 987654321 * 1 = 987654321 <- including all digits)
# But the question is asked when n > 1. So it is not trivial now. But luckily, we know that the upper bound now.
# Which is none other than 987654321. But we have to find any number which is give all the digits from 1 to 9 by multiplying at least
# 2 or more numbers from 1.

digits = [str(a) for a in range(1, 10)]

i = 918273645 # Since we are finding the largest number, it is easier if going from upper bound rather than going from 1.
answer = 0

while i < 987654321:
    a = str(i)
    if 0 not in a:
        fo


print(answer)
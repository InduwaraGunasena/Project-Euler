"""
a + b + c = 1000 ---->1
a^2 + b^2 = c^2 ----->2
I solved the above simultaneous equations and written solutions using 'a'.
Now I iterate 'a' and find solutions to 'b' and 'c' until we get a integer value.
"""

import math

a = b = c = 0
B = C = ()
while True:
    a += 1
    b = (pow(10, 6) - 2000 * a) / (2000 - 2 * a)
    c = (a ** 2 - 1000 * a + 5 * pow(10, 5)) / (1000 - a)
    B = math.modf(b)
    C = math.modf(c)
    if B[0] == 0 and C[0] == 0:
        break
print("a = %d, b = %d, c =%d" % (a, b, c))
print("a*b*c = ", a * b * c)

num_list = [1,2,3,4,5,6,7,8,9]

# Now we calculate all the possible chances. We have only 9 numbers.
# First we choose a number for x. x can have multiple digits. So we consider the number of digits in x that make one possible chance.
# Then we select another number y. y can be also have multiple digits but the number of digits in x and y cannot be greater than 9.
# After chose x and y, we can select another number z which is made as x*y = z. The sum of all the number of digits in x,y and z is
# equal to nine because we consider num_list to construct numbers x and y.
# After explore this problem you will realize that we can come up this inequality.
# -1 <= n(z) - { n(x) + n(y) } <= 0 ;  <------- EXPRESSION 1
# where n(x) = no. of digits in x / n(y) = no. of digits in y / n(z) = no. of digits in z
# x * y = z and n(x) + n(y) + n(z) = 9 = no. of elements in the num_list

ways = []
length = len(num_list)

for x in range(1,length + 1):
    for y in range(1,length):
        if length - 2*x -2*y == -1 or length - 2*x -2*y == 0: # <------- EXPRESSION 1
            ways.append([x,y])

ways = ways[:len(ways)//2]

# =============================== SPECIAL ==============================
#  This function returns a list containing all the permutations of getting n numbers from a list.
#  input :- lis = list, containing different numbers
#            n  = no. of items you need to get from that lis
#            combination = is an empty list ( leave it as a '[]' is essential )
#            result = this is resultant list ( output )
#  output :- A list containing all the permutations
#
#  The output has nPr values. Where n is the no. of items in the group, r is the no. of items you want to select from that list.

import copy

def chooser(lis, n, combination, result):
    if n == 0:
        result.append(combination)
        return
    else:
        for i in lis:
            j = copy.copy(lis)
            j.remove(i)
            chooser(j, n - 1, combination + [i], result)

# ================================== END of the SPECIAL FUNCTION ===============================

# This function is used to convert a digit list to a number
# e.g. :- [1,2,3,4] >> 1234
def list_to_number(lis):
    num = ''
    for i in lis:
        num += str(i)
    return int(num)


# This function is used to check all the constraints in the problem.
def pandigital_checker(lis, x, y):
    if len(str(x)) + len(str(y)) + len(str(x*y)) != len(lis):
        return False

    x_digit_list = [int(digit) for digit in str(x)]
    y_digit_list = [int(digit) for digit in str(y)]
    z_digit_list = [int(digit) for digit in str(x*y)]

    a = (x_digit_list + y_digit_list + z_digit_list)
    a.sort()
    if a == lis:
        return True
    else:
        return False

answer = []

for i in ways:
    x = i[0]
    y = i[1]
    ways_for_x = []
    ways_for_y = []
    chooser(num_list, x, [], ways_for_x)
    chooser(num_list, y, [], ways_for_y)
    for j in ways_for_x:
        for k in ways_for_y:
            q = list_to_number(j)
            w = list_to_number(k)
            if pandigital_checker(num_list, q, w):
                answer.append([q,w,q*w])

print(answer)

# there are some products (x*y) are same. You can see 5346 is containing 2 time.(18*297 , 27*198).
# We have to eliminate that.
aa = [u[2] for u in answer]

print("required answer =", sum(list(set(aa))))


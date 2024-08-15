num_list = [0,1,2,3,4,5,6,7,8,9]

def checker(a, b):
    a_digitList = [int(digit) for digit in str(a)]
    b_digitList = [int(digit) for digit in str(b)]
    a_digitList.sort()
    b_digitList.sort()

    intersection = list(set([num for num in a_digitList if num in b_digitList]))
    # Eliminating there is no common element in both numerator and denominator scenario and
    # if common element is zero(Since we don't need TRIVIAL Scenarios)
    if len(intersection) == 0 or intersection == [0]:
        return False

    a_digitList.remove(intersection[0])
    b_digitList.remove(intersection[0])
    new_a = a_digitList[0]
    new_b = b_digitList[0]

    if a_digitList == b_digitList:
        return False
    elif new_b == 0:
        return False
    elif a/b == new_a/new_b:
        return True
    else:
        return False

answer = []
# Now we have to select a 2-digit number from num_list
for i in range(11, 99):
    for j in range(10, i):
        if checker(j, i):
            answer.append([j,i])

print(answer)

a = 1
b = 1
for i in answer:
    a *= i[0]
    b *= i[1]

print(a,b)

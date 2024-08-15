chain = []
number = 2
num = number
terms = 0

while True:
    if number > 10**6:
        break

    if num == 1:
        chain.insert(number - 2, terms)
        number += 1
        terms = 0
        num = number
    elif num % 2 == 0:
        num = num // 2
        terms += 1
        try:
            if chain[num - 2]:
                chain.insert(number, terms + chain[num - 2])
                number += 1
                terms = 0
                num = number
        except:
            pass
    else:
        num = 3 * num + 1
        terms += 1

    print(number)

print(chain)
print("%d has the longest chain" % ( chain.index(max(chain)) + 2 ))
print("It has %d terms" % (max(chain)+1))

numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
limit = 1000000

factorials = [1, 1, 2, 6, 24, 120, 720, 5040, 40320, 362880]  # All factorials from 1 to 9
a = len(numbers) - 1
x = 1
prev_v = 0
num = ''

while a >= 0:
    v = limit - (factorials[a] * x)
    if v <= 0:
        a -= 1
        num += numbers[x-1]
        numbers.pop(x-1)
        limit = prev_v
        x = 1
    else:
        x += 1
    prev_v = v

print(num)



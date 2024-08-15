number = 100
answer = number

for i in range(1, number):
    answer = answer * (number - i)

sum_digit = 0
string = str(answer)

for i in range(len(string)):
    sum_digit += int(string[i])

print(f"{number}! = {answer}")
print(f"the sum of the digits in {number}! = {sum_digit}")
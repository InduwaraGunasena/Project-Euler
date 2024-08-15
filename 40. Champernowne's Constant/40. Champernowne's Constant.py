import time
start = time.time()

expression = [1, 10, 100, 1000, 10000, 100000, 1000000]

# I am using a special technique to calculate this rather than finding what digits from 1 to 1000000.
# I saw a pattern when combining each integer.
# we have already known that there are 10 digits. (0,1,2,3,4,5,6,7,8,9)
# So 1 to 10 there are 9 digits. Because we didn't include zero in the decimal part. (0.123456789 10 11 ....)
# after 9, other numbers from 10 to 20, there are 10 numbers. But from 10 to 100, it has 2 digits for each number.
# Therefore, from 10 to 20, there are 20 digits (no. of  integers * no. of digits per integer = 10 * 2)
# Then from 10 to 100, there are 100-10=90 numbers and 90*2=180 digits.
# Like wise from 100 to 1000, there are 900 numbers(1000-100 = 900) and 900*3=2700 digits.
# So we can conlude this as below.
# 1 is in the 1st position.
# 10 is in the 10th position. ( 9 + 1 = 10 )
# 100 is in the 190th position. ( 180 + 10 = 190 )
# 1000 is in the 2890th position. ( 2700 + 190 = 2890 )
# But remember, these positions tell that the digit 1 position. That is, 10th position means 1 is 10th and 0 is 11th in position (...8 9 10 11 ...)
# Likewise, 2890th position means that 1 is in 2890, next 0 is in 2891, other 0 is in 2892 and last 0 is in 2893 in position.

position = [1]     # This list save all the positions of each integer which are power of 10. Remember, it saves only front digit's position.
a = 1
for i in range(1, len(expression)): # We have to find out at least required digit's position.
    a += (10**i - 10**(i-1))*i
    position.append(a)

# This fuction can calculate any positional digit by using these inputs.
# number = what position you want to get. (value of n in the question)
# ten_position = the nearest lowest 10th power position.
# no_of_digits = number of digits in that ten_position number. ( if 100 is in 190th position,then no_of_digits = 3)
def finder(number, ten_position, no_of_digits):
    # if 100 is in 190th position,then this list looks like [190,191,192]. (= 100)
    character_list = [k for k in range(ten_position, ten_position + no_of_digits)]
    num = 10**(no_of_digits-1)  # getting the first number of any no. of digit. That is, 100 is the first number which has 3 digits.
    while number not in character_list:
        for i in range(no_of_digits):
            character_list[i] += no_of_digits
        num += 1
    num = str(num)
    return int(num[character_list.index(number)])

answer = 1

# I am going each lists separately. That's why I used 2 parameters. But it looks like unnecessary.
p = 0
q = 0
while True:
    if len(expression) == q:  # We want this while loop until meets the end of the expression list.
        break
    if position[p] == expression[q]:
        answer *= 1  # We know that position list shows the first digit's position. But we know ant 10th power number's first digit is always 1.
        q += 1
    elif position[p] > expression[q]:
        answer *= finder(expression[q], position[p-1], p)
        q += 1
    p += 1

print("answer =", answer, "\n")

end = time.time()
print(end - start)
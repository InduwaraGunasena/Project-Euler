number_in_Fibonacci = 2
previous_num1_in_Fibonacci = 1
previous_num2_in_Fibonacci = 0

total = 0

while number_in_Fibonacci < 4000000:
    if number_in_Fibonacci % 2 == 0:
        total += number_in_Fibonacci

    #print(number_in_Fibonacci)
    previous_num2_in_Fibonacci = number_in_Fibonacci
    number_in_Fibonacci += previous_num1_in_Fibonacci
    previous_num1_in_Fibonacci = previous_num2_in_Fibonacci

print(total)
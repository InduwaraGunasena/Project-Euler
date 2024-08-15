first_number = 1
last_number = 100
sum_of_square_numbers = 0
sum_of_numbers_after_square = 0

for i in range(first_number, last_number + 1):
    sum_of_square_numbers = sum_of_square_numbers + i ** 2
    sum_of_numbers_after_square = sum_of_numbers_after_square + i

final_sum = sum_of_numbers_after_square ** 2 - sum_of_square_numbers
print(f"answer is {final_sum}")

"""

numbers = 100


def sum_of_square_numbers(number_of_terms):
    sum = (number_of_terms * (number_of_terms + 1) * (2 * number_of_terms + 1)) / 6
    return sum


def sum_of_numbers_after_square(number_of_terms):
    sum = (number_of_terms * (number_of_terms + 1)) / 2
    return sum ** 2


final_sum = int(sum_of_numbers_after_square(numbers) - sum_of_square_numbers(numbers))
print("answer is ", final_sum)

"""

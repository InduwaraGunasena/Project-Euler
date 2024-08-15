letters_in_a_digit_1_to_10 = [3, 3, 5, 4, 4, 3, 5, 5, 4, 3]
letters_in_a_digit_11_to_19 = [6, 6, 8, 8, 7, 7, 9, 8, 8]
letters_in_a_digit_20_to_90 = [6, 6, 5, 5, 5, 7, 6, 6]
and_word = 3
hundred_word = 7
thousand_word = 11
letters = 0

first_number = 1
last_number = 1000

for i in range(first_number, last_number + 1):
    if i == 1000:
        letters += thousand_word
    elif i <= 10:
        letters += letters_in_a_digit_1_to_10[i - 1]
    elif i > 10 and i < 20:
        letters += letters_in_a_digit_11_to_19[i - 11]
    elif i >= 20 and i < 100:
        number = str(i)
        if number[1] == "0":
            letters += letters_in_a_digit_20_to_90[int(number[0]) - 2]
        else:
            letters += letters_in_a_digit_20_to_90[int(number[0]) - 2] + letters_in_a_digit_1_to_10[int(number[1]) - 1]
    elif i >= 100:
        number = str(i)
        if number[1] == '0' and number[2] == '0':
            letters += letters_in_a_digit_1_to_10[int(number[0])-1] + hundred_word
        elif number[1] == '1' and number[2] == '0':
            letters += letters_in_a_digit_1_to_10[int(number[0]) - 1] + hundred_word + and_word + \
                       letters_in_a_digit_1_to_10[-1]
        elif number[1] == '1':
            letters += letters_in_a_digit_1_to_10[int(number[0]) - 1] + hundred_word + and_word + \
                       letters_in_a_digit_11_to_19[int(number[2]) - 1]
        elif number[1] == '0':
            letters += letters_in_a_digit_1_to_10[int(number[0]) - 1] + hundred_word + and_word + \
                       letters_in_a_digit_1_to_10[int(number[2]) - 1]
        elif number[2] == '0':
            letters += letters_in_a_digit_1_to_10[int(number[0]) - 1] + hundred_word + and_word + \
                       letters_in_a_digit_20_to_90[int(number[1]) - 2]
        else:
            letters += letters_in_a_digit_1_to_10[int(number[0]) - 1] + hundred_word + and_word + \
                       letters_in_a_digit_20_to_90[
                           int(number[1]) - 2] + letters_in_a_digit_1_to_10[int(number[2]) - 1]

print(letters)

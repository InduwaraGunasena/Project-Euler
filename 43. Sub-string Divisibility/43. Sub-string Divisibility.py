divisors = [2, 3, 5, 7, 11, 13, 17]
answer = 0

def is_divisible(num):
    for i in range(1, 8):
        sub_num = int(num[i:i + 3])
        if sub_num % divisors[i - 1] != 0:
            return False
    return True

def generate_permutations(num_str, index):
    global answer
    if index == len(num_str) - 1:
        if is_divisible(num_str):
            answer += int(num_str)
    else:
        for i in range(index, len(num_str)):
            num_list = list(num_str)
            num_list[i], num_list[index] = num_list[index], num_list[i]
            generate_permutations(''.join(num_list), index + 1)

num_string = '0123456789'
generate_permutations(num_string, 0)
print(answer)

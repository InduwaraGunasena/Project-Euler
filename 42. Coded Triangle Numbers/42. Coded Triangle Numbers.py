import math

with open("0042_words.txt", 'r') as word_file:
    words = word_file.read().split(',')

words = [word.strip().strip('"') for word in words]

def ascii_sum(word):
    total = 0
    for i in word:
        total += ord(i) - 64
    return total

def is_triangleNumber(n):
    a = math.sqrt(1 + 8 * n) % 1
    if a == 0:
        return True
    else:
        return False

answer = 0
for i in words:
    if is_triangleNumber(ascii_sum(i)) == True:
        answer += 1

print(answer)

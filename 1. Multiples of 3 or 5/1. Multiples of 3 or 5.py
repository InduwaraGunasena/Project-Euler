limit = 1000

answer = 0
for i in range(1, limit):
    if i % 3 == 0 or i % 5 == 0:
        answer += i

print(answer)


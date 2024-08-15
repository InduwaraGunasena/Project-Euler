import time
s = time.time()

Colin = [1, 2, 3, 4, 5, 6]
Peter = [1, 2, 3, 4]

Colins_oppotunities = []
Peters_opportunities = []

for i in Colin:
    for j in Colin:
        for k in Colin:
            for l in Colin:
                for m in Colin:
                    for n in Colin:
                        Colins_oppotunities.append(i + j + k + l + m + n)

for a in Peter:
    for b in Peter:
        for c in Peter:
            for d in Peter:
                for e in Peter:
                    for f in Peter:
                        for g in Peter:
                            for h in Peter:
                                for p in Peter:
                                    Peters_opportunities.append(a + b + c + d + e + f + g + h + p)
Peters_opportunities.sort()
Peters_opportunities.reverse()

Colins_oppotunities.sort()

total_opportunities = len(Peters_opportunities) * len(Colins_oppotunities)


def re_arrange_list(lis):
    m = n = l = 0
    x = []  # sum of numbers ---> [[sum, quantity],....[]]
    while True:
        m = lis[l]
        if m != n:
            x.append([m, lis.count(m)])
        n = m
        l += 1
        if l == len(lis):
            break

    return x


Peters_opportunities = re_arrange_list(Peters_opportunities)
Colins_oppotunities = re_arrange_list(Colins_oppotunities)

win_peter = 0
win_colin = 0
draw = 0

for i in Peters_opportunities:
    for j in Colins_oppotunities:
        if i[0] > j[0]:
            win_peter += i[1] * j[1]
        elif i[0] < j[0]:
            win_colin += i[1] * j[1]
        elif i[0] == j[0]:
            draw += 1

rate_of_defeat_Peter = win_peter / total_opportunities

print(f"answer is {round(rate_of_defeat_Peter, 7)}")
print("time spend -" ,time.time() -s)
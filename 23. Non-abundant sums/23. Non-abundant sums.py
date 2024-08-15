limit = 28123
divisors = []
lis = []
abundants = []

for i in range(1,limit+1):
    for j in range(1,i):
        if i%j == 0:
            lis.append(j)
    if sum(lis) > i:
        abundants.append(i)
    divisors.append(lis)
    lis = []
    print(i)

sum_abds=[]
for i in abundants:
    for j in abundants:
        a = i + j
        sum_abds.append(a)
        a = 0
sum_abds = list(set(sum_abds))
anw = []

for i in range(1,limit+1):
    if i not in sum_abds:
        anw.append(i)

print(sum(anw))


limit = 10**6 # Take a suitable limit to stop the loop

i = 10
l = []

while i < limit:
    a = str(i)
    s = 0
    for j in range(len(a)):
        s += int(a[j])**5
    if s == i:
        l.append(i)
    print(i, l)
    i += 1

print("answer =", sum(l))
year = 1901
days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
first_sundays = 0
first = 2  # date = MON-1,TUE-2,WED-3,THU-4,FRI-5,SAT-6,SUN-7

for i in range(year, year + 100):
    if year % 4 != 0:  days[1] = 28
    else:  days[1] = 29

    for i in range(12):
        last = (days[i] - 29) + first
        if last > 7:
            last = last - 7
        first = last + 1
        if first == 7:
            first_sundays += 1

print(first_sundays)

digits_you_want = 3
a = 10**(digits_you_want-1)
b = 10**(digits_you_want-1)
largest_paldrome = 0

def isPalindrome(n):
    product = str(n)
    if product == product[::-1]:
        return 1
    else:
        return 0

for a in range( 10**(digits_you_want-1), 10**digits_you_want):
    for b in range(10**(digits_you_want-1), 10**digits_you_want):
        if isPalindrome(a*b) == 1  and (a*b) > largest_paldrome:
            largest_paldrome = a*b

print(largest_paldrome)
import time

start = time.time()

limit = 10**6
def is_palindrome(n): # Checking whether the input number n is a palindrome or not
    num = str(n)
    length = len(num)
    for i in range(length // 2): # Check all digits in both sides until met middle digit or not
        if num[i] != num[length - i - 1]:
            return False
    return True

answer = []  # Save all the double base palindromes
for i in range(1, limit + 1):
    a = str(bin(i))
    if a[-1] == '0': # You will simply realize that if least significant bit is 0, it in not a palindrome in binary system.
        continue
    if is_palindrome(i) and is_palindrome(a[2:]): # In python binary numbers are formatted by prefixing "0b". So we have to remove them.
        answer.append(i)

print(answer)
print(sum(answer))

end = time.time()
print(end - start)
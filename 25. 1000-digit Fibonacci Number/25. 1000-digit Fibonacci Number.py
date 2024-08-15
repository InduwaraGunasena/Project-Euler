digits = 1000

f1 = 1
f2 = 1

f_n = 0
f_n1 = f1
f_n2 = f2

#print("1.", f1)
#print("2.", f2)
j = 3

while(len(str(f_n)) != digits):
    f_n = f_n1 + f_n2
    #print(f"{j}.", f_n)
    f_n2 = f_n1
    f_n1 = f_n
    j += 1

print("\nanswer =", j-1 )
print(f"\nThe {j-1}th term is the first term which contain {digits} digits")
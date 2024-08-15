number = 600851475143 
devidor = 2
dev = []

while True:
    if number % devidor == 0:
        dev.append(devidor)
        number = number // devidor
        devidor = 1
    elif number == devidor or number == 1:
        break
    devidor += 1

maximum_prime = max(dev)
print(maximum_prime)
print(dev)


import os
os.system('cls')

n = 2
is_prime = True
l = []
while n < 10:
    for i in range(2, n+1):
        divide = n % i
        if divide != 0:
            l.append(i)
    n += 1
print(l)
print ('taha sadeghi')


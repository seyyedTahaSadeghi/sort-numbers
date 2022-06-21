import os
os.system("cls")
# this program writted by me and MR.farmani in 29 / 3 / 1401
count = int(input('enter the count of numbers : '))
l = []
for q in range(0, count):
    num = int(input('enter your number : '))
    l.append(num)
for i in reversed(range(0, count)):
    for j in range(0, i):
        if l[j] > l[j+1]:
            tmp = l[j]
            l[j] = l[j+1]
            l[j+1] = tmp
            # print(tmp)
for i in range(0, count):
    print(l[i])

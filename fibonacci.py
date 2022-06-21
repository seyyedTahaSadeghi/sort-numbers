import os
os.system('cls')


def fib(a):
    l = [1]
    first_num = 0
    secend_num = 1
    while len(l) <= a:
        th_num = secend_num + first_num
        l.append(th_num)
        first_num = secend_num
        secend_num = th_num
    return l


print(fib(100))

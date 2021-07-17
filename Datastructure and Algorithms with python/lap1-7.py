def sumdigit(n):
    if n == 0:
        return 0
    else:
        return  n % 10 + sumdigit(int(n / 10))

print(sumdigit(678))
print(sumdigit(79))
def sum_series(n):
    if n < 1: 
        return 0
    else:
        return n + sum_series(n-2)

def hamonic_sum(n):
    if n < 2:
        return 1
    else:
        return 1 / n +  (hamonic_sum(n-1))

def geometric_sum(n):
    if n < 0:
        return 0
    else:
        return 1 / (pow(2,n)) +  (geometric_sum(n-1))
    #** pow(2,n) == 2**n

def power(a, b):
    if b == 0:
        return 1
    elif a == 0:
        return  0
    elif b == 1:
        return a
    else:
         return a*power(a, b-1)


def gcd(a, b):
    lo = min(a, b) #** = 6
    hi = max(a, b) #** = 39
    if lo == 0: 
        return hi
    elif lo == 1:
        return 1
    else: 
        return gcd(lo,hi%lo) #todo (6,39%6) = 3
print(gcd(6, 39))

def sum(d):
    s = 0
    for i in range(len(d)):
        s += d[i]
    return s
def max(d):
    m = d[0]
    for i in range(len(d)):
        if d[i] > m:
            m = d[i]
    return m
def imax(d):
    for i in range(len(d)):
        if d[i] == max(d):
            return i
def seqsearch(d,x):
    for k in range(len(d)):
        if d[k] == x:
            return k
        elif d[k] > x:
            return -1
def binsearch(d,x):
    l = 0 ;r = len(d)
    while l <= r:
        mid = (l+r) // 2
        if x == d[mid]:
            return mid
        if x < d[mid]:
            r = mid - 1
        else:
            l = mid + 1
    return -1
def sel_sort(d):
        for i in range(len(d)):
            min = i
        for j in range(i+1,len(d)):
            if d[min] > d[j]:
                min = j
                d[i],d[min] = d[min],d[i]
            return d

def sumcouple(d, x):
    for i in range(len(d)):
        j = d[i]
        ''' Ex 1'''
        for j in range(len(d)):
             if i != j and d[i] + d[j] == x:
                 return i,j
        '''Ex 2'''
        delta = x - d[i]
        j = binsearch(d, delta)
        if j != -1:
            return i,j
'''
algroithms จาก สูตร
'''
def sqrt(a):
    x = 1
    while x**2 != a:
        x = (x + a/x) /2
    return x
def gcd(a,b):
    while b > 0:
        t = a%b
        a = b
        b = t
    return a
def log2(n):
    c = 0
    while n > 0:
        n /= 2
        c += 1
    return c

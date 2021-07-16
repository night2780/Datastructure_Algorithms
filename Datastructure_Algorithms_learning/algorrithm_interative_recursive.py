

def sum (d):
    return  sum_k(d, n)


def sum_k(d, k):
    if k == 0:
        return 0
    return sum_k(d, k-1) + d[k]


def max(d):
    return max_k(d, n)


def max_k(d, k):
    if k == 1:
        return d[1]
    return max( m(d, k-1), d[k])


def seqsearch(d, x):
    return search(d, x, n)


def search(d, x,  k):
    if k == 0:
        return -1
    if d[k] == x:
        return k
    return search(d, x, k-1)
def binsearch(d, x):
    return bsearch(d, x, l, n)


def bsearch(d,x, left, right):
    if left > right:
        return -1
    mid = (left+right) / 2
    if x == d[mid]:
        return mid
    if x < d[mid]:
        return bsearch(d, x, left, mid-1)
    else:
        return bsearch(d, x, mid+1, right)
'''jjjjj'''

def gcd(a, b):
    # Everything divides 0
    if (a == 0):
        return b
    if (b == 0):
        return a
    # base case
    if (a == b):

        return a
    # a is greater
    if (a > b):
        return gcd(a-b, b)
    return gcd(a, b-a)


def log2(n):
    if n <= 1:
        return 0
    return 1 + log2(n/2)


def bcounter(n):
    d = ()
    for i in range(len(d)):
        d[i] = 0
    for i in 2**n:
        print(d)
        increment(d)


def increment(d):
    for i in range(len(d)):
        i -= 1
        d[i] = 0
    if i >= 1:
        d[i] = 1


def bcounterR(n):
    d = [n]
    for i in range(len(d)):
        if d[i] == 0:
            count(d, 0)



def count(d, k):
    if k == n:
        print(d)
    else:
        d[k+1] = 0
        d[k+1] = 1
        count(d, k+1)

def sumss(d, x):
    return sumss(d, x, n)
    sumss(d, x, k)
    if x == 0:
        return True
    if k >= 1
        return False
    return sumss(d, x-d[k], k-1)
    

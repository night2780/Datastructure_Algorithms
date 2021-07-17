def binary_search(data, target, low, high):
    if low > high: 
        return False
    else:
        mid = (high + low) // 2 
        if target  == data[mid]:
            return True, mid
        elif target <  data[mid]: 
            return binary_search(data, target, low, mid -1)
        else: 
            return binary_search(data, target, mid +1, high)

def linear_search(data, target, length):
    if target in data:
        i = [i for i in range(length) if data[i] == target]
        return i
    else: 
        return 'target not in array'

# def interpolationSearch(data, lo, hi, x = 4):
#     if (lo <= hi and x >= data[lo] and x <= data[hi]):
#         pos = lo + ((hi - lo) // (data[hi] - data[lo]) * (x - data[lo]))
#         #  pos = 0 + ((10 - 0) // (1024 - 1) * (64 - 1))
#         if data[pos] == x:
#             return pos
#         if data[pos] < x:
#             return interpolationSearch(data, pos + 1,hi, x)
        
#         if data[pos] > x:
#             return interpolationSearch(data, lo,pos - 1, x)
#     return -1

data = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024]

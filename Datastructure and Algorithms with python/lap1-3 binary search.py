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

data = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024]
print(binary_search(data, 64, 0, len(data)-1))
    #todo recursion list sum 
def recursive_list_sum(data):
    total = 0
    for i in data: 
        if type(i) == list:
            total = total + recorsive_list_sum(i)
        else: 
            total = total + i
    return total
    
print(recursive_list_sum([2, 4, [6, 8],[10, 12]]))

